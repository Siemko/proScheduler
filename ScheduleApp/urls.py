from django.conf.urls import url

from . import views

app_name = 'ScheduleApp'
urlpatterns = [
    # /ScheduleApp/
    url(r'^$', views.index, name='index'),
    # /ScheduleApp/5/
    url(r'^(?P<date_id>[0-9]+)/daytasks/$', views.daytasks, name='daytasks'),
    url(r'^deletetask/(?P<task_id>[0-9]+)/$', views.deletetask, name='deletetask'),
    url(r'^(?P<date_id>[0-9]+)/addtask/$', views.addtask, name='addtask'),
    url(r'^newday/$', views.newday, name='newday'),
    url(r'^add_day/$', views.add_day, name='add_day'),
    url(r'^(?P<date_id>[0-9]+)/deleteday/$', views.deleteday, name='deleteday')
]