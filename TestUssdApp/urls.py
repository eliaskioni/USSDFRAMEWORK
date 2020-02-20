"""
add this your ussd urls here.
Don't forget to include them in your projects root urls.py file.
"""
from django.conf.urls import url
from TestUssdApp.views import TestussdappUssdGateWay

urlpatterns = [
    url(r'^TestUssdApp_ussd_gateway',
        TestussdappUssdGateWay.as_view(),
        name='TestUssdApp_ussd_gateway')
]
