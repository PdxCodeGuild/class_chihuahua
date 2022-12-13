from datetime import datetime, date, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe



from scheduling_app.forms import *
from .models import *
from .utils import Calendar
import calendar
from django.urls import reverse


class CalendarView(generic.ListView):
    model = Event
    template_name = 'pages/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month, self.request.user.id)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    events = Event.objects.filter(user=request.user)
    print(events)
    return render(request, 'pages/about.html', {"events":events})


def index(request):
    return HttpResponse('hello')



def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        form.save()
        return redirect('calendar')
    context = {'form': form,
    'event_id': event_id}
    return render(request, 'pages/event.html', context)

def delete(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect ('calendar')


