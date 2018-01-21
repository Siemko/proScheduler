from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Days, DayTasks
from django.contrib import messages
from django.core.urlresolvers import reverse

class DaysTest(TestCase):

    def test_plans_inpast(self):
        date = datetime.date.today() - datetime.timedelta(days = 30)
        day = Days(day_date = date)
        self.assertEqual(day.plans_inpast(), False)

    def test_print(self):
           day1 = Days(day_date = datetime.date.today() + datetime.timedelta(days = 2))
           day1.save()
           day2 = Days(day_date = datetime.date.today() + datetime.timedelta(days = 3))
           day2.save()
           day3 = Days(day_date = datetime.date.today() + datetime.timedelta(days = 4))
           day3.save()
           day4 = Days(day_date = datetime.date.today() + datetime.timedelta(days = 10))
           day4.save()
           day5 = Days(day_date = datetime.date.today() + datetime.timedelta(days = 20))
           day5.save()
           day6 = Days(day_date = datetime.date.today() + datetime.timedelta(days = 60))
           day6.save()
           num_of_tasks_created = [];
           num_of_tasks_created.extend([2,1,3,2,2,0])
           task11 = DayTasks(day = day1, task_text = 'test 11' )
           task11.save()
           task12 = DayTasks(day = day1, task_text = 'test 12' )
           task12.save()
           task21 = DayTasks(day = day2, task_text = 'test 21' )
           task21.save()
           task31 = DayTasks(day = day3, task_text = 'test 31' )
           task31.save()
           task32 = DayTasks(day = day3, task_text = 'test 32' )
           task32.save()
           task33 = DayTasks(day = day3, task_text = 'test 33' )
           task33.save()
           task41 = DayTasks(day = day4, task_text = 'test 41' )
           task41.save()
           task42 = DayTasks(day = day4, task_text = 'test 42' )
           task42.save()
           task51 = DayTasks(day = day5, task_text = 'test 51' )
           task51.save()
           task52 = DayTasks(day = day5, task_text = 'test 52' )
           task52.save()
           days_list = [];
           days_list.extend((day1,day2,day3,day4,day5,day6))
           num_of_tasks = [];
           for day in days_list:
                print('Date:' + day.day_date.strftime('%m/%d/%Y') + ', Number of the tasks:' + str(day.tasks.count()))
                num_of_tasks.append(day.tasks.count())
           if num_of_tasks_created == num_of_tasks:
               print('Tasks successfully added and printed')




