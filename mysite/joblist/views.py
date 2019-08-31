import bs4 as bs
import datetime
import urllib.request
from django.views.generic import ListView
from .models import Job
from django.shortcuts import render, redirect


class JobList(ListView):
    model = Job
    ordering = ['-date']


def isNone(variable):
    if variable is not None:
        return variable.get_text()
    else:
        return 'Not applicable'


def jobCrawler(request):
    source = urllib.request.urlopen(
        'https://www.seek.co.nz/jobs-in-banking-financial-services?sortmode=ListedDate').read()
    soup = bs.BeautifulSoup(source, 'lxml')
    nextPage = soup.find('a', attrs={'data-automation': 'page-next'})
    while nextPage is not None:
        for jobIndex in soup.find_all('article'):
            jobID = jobIndex.get('data-job-id')
            
            # if no jobs on the list set id=0
            try:
                latest_jobID = Job.objects.raw(
                    'SELECT * FROM joblist_job LIMIT 1')[0].id
            except:
                latest_jobID = 0
            if int(jobID) < latest_jobID:
                continue
            jobTitle = jobIndex.get('aria-label')
            jobCompany = isNone(jobIndex.find(
                'a', {"data-automation": "jobCompany"}))
            jobLocation = isNone(jobIndex.find(
                'a', {"data-automation": "jobLocation"}))
            IDUrl = 'https://www.seek.co.nz/job/' + jobID

            source2 = urllib.request.urlopen(IDUrl)
            soup2 = bs.BeautifulSoup(source2, 'lxml')
            detailDate = soup2.find(
                'dd', attrs={'data-automation': 'job-detail-date'}).get_text()
            detailDate = datetime.datetime.strptime(
                detailDate, "%d %b %Y").date()
            job = Job(id=jobID, title=jobTitle,
                      company=jobCompany, location=jobLocation, date=detailDate)
            job.save()
        nextPageHref = nextPage.get('href')
        nextPageUrl = 'https://www.seek.co.nz/' + nextPageHref
        source = urllib.request.urlopen(nextPageUrl).read()
        soup = bs.BeautifulSoup(source, 'lxml')
        nextPage = soup.find('a', attrs={'data-automation': 'page-next'})
    return redirect('/joblist')


# last = Job.objects.raw('SELECT * FROM joblist_job LIMIT 1')[0]
# jobtime = last.date
# print(jobtime)
# time = datetime.date.today()
# print(time)
# print(last.date == time)
