from django import forms
from .models import Contact
from .models import SUBJECT_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.ModelForm):
    SUBJECT_CHOICES = [
        ('product_inquiry', 'Product Inquiry'),
        ('order_status', 'Order Status'),
        ('return_exchange', 'Return/Exchange'),
        ('payment_issue', 'Payment Issue'),
        ('technical_support', 'Technical Support'),
        ('feedback', 'Feedback/Suggestions'),
        ('other', 'Other'),
    ]


subject = forms.ChoiceField(choices=SUBJECT_CHOICES)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'surname', 'subject', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
