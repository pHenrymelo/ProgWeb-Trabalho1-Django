from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['event_title',
                  'event_type',
                  'event_time',
                  'event_start_date',
                  'event_end_date',
                  'event_location',
                  'event_location_city',
                  'event_is_free',
                  'event_voucher_price',
                  'event_is_limitless_vacancies',
                  'event_vacancies']
        widgets = {
            'event_start_date': forms.DateInput(attrs={'type': 'date'}),
            'event_end_date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'type': 'time'}),
        }