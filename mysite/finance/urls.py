from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from finance.views import company_article_list, ChartData, dash, dash_ajax

app_name = 'finance'
urlpatterns = [
    path('companies/', company_article_list, name='companies'),
    path('api/chart/data/', ChartData.as_view(), name='api-chart-data'),
    path('dash/', dash),
    path('_dash', dash_ajax),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
