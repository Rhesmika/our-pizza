from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class NewBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ('author', 'status')
        fields = ('reference', 'booking_date', 'booking_time', 'party_of')

        widgets = {
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg. Dinner with Michael'}),
            'booking_date': DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'booking_time': TimeInput(attrs={'class': 'form-control'}),
            'party_of': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.status = 0
        self.object.save()
        return super().form_valid(form)
