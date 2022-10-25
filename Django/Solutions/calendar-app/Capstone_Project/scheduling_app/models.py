from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

event_choices =(
    ('gig', 'Gig'),
    ('rehearsal', 'Rehearsal')
)

class Event(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField(blank=True)
    
    address = models.CharField(max_length=200, blank=True)
    length_of_set = models.CharField(max_length=200,blank=True)
    gig_or_rehearsal = models.CharField(max_length=9, choices=event_choices, default='Gig', blank=True)
    rate_of_pay = models.IntegerField(blank=True)
    lodging = models.CharField(max_length=200, blank=True)
    venue_contact = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
