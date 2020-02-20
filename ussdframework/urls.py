from django.conf.urls import url
from ussdframework.views import journey_visual,journey_visual_data

urlpatterns = [
    url(r'ussdframework-airflow/journey_visual$',journey_visual,name="journey_visual"),
    url(r'ussdframework-airflow/journey_visual_data$',journey_visual_data,name='journey_visual_data')
]
