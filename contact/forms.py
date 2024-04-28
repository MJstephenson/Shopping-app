from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


SUBJECT_CHOICES = [
    ('product_inquiry', 'Product Inquiry'),
    ('order_status', 'Order Status'),
    ('return_exchange', 'Return/Exchange'),
    ('payment_issue', 'Payment Issue'),
    ('technical_support', 'Technical Support'),
    ('feedback', 'Feedback/Suggestions'),
    ('other', 'Other'),
]

class ContactForm(forms.ModelForm):
  
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)

    class Meta:
        model = Contact
        fields = ['first_name', 'surname', 'subject', 'email', 'message']  

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'  
        self.helper.add_input(Submit('submit', 'Submit'))  
