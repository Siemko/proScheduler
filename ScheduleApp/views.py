from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.http import HttpRequest
from django.utils.datastructures import MultiValueDictKeyError
from .models import Days,DayTasks
from django.template import loader
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime
from django.contrib import messages

def index(request):
    dates = Days.objects.order_by('day_date')
    context = {
        'dates': dates,
    }
    return render(request,'ScheduleApp/index.html',context)




def daytasks(request, date_id):

    date = Days.objects.get(id = date_id)
    context = {
        'date': date,
    }
    return render(request,'ScheduleApp/daytasks.html',context)



def deletetask(request, task_id):

    task = DayTasks.objects.get(id = task_id)
    task.delete()

    return HttpResponseRedirect(reverse('ScheduleApp:daytasks', args = (task.day.id,)))


def addtask(request: HttpResponse, date_id):

    task = request.POST["Task"]
    date = Days.objects.get(id = date_id)
    new_task = DayTasks(day = date, task_text = task)
    new_task.save()
    return HttpResponseRedirect(reverse('ScheduleApp:daytasks', args = (date.id,)))


def newday(request):
    context = {
    'min_date': Days.min_date.strftime('%Y-%m-%d'),
    }
    return render(request,'ScheduleApp/newday.html',context)

def add_day(request):

    date = request.POST["DayDate"]
    today = datetime.date.today()
    if date >= today.strftime('%Y-%m-%d'):
        newday = Days(day_date = date)
        newday.save()
    else:
        messages.error(request, 'Date cannot be in the past')
    return HttpResponseRedirect(reverse('ScheduleApp:index'))

def deleteday(request,date_id):
    day_deleted = Days.objects.get(id = date_id)
    day_deleted.delete()
    return HttpResponseRedirect(reverse('ScheduleApp:index'))





