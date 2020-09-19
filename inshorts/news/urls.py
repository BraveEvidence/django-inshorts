from django.urls import path
from inshorts.news.views import NewsList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    path('news/',NewsList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)