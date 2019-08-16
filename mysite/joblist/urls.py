from django.urls import path
from . import views


app_name = 'joblist'
urlpatterns = [
    path('', views.JobList.as_view(), name="home"),
    path('update/', views.jobCrawler, name="crawler"),

]
