from django.forms import ModelForm, DateInput
from scheduling_app.models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = ['title',
        'description',
        'start_time',
        'address',
        'length_of_set',
        'gig_or_rehearsal',
        'rate_of_pay',
        'lodging',
        'venue_contact']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].required=False

# .input_formats = ('%Y-%m-%dT%H:%M',)