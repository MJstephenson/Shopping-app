from django.db import models


SUBJECT_CHOICES = [
    ('product_inquiry', 'Product Inquiry'),
    ('order_status', 'Order Status'),
    ('return_exchange', 'Return/Exchange'),
    ('payment_issue', 'Payment Issue'),
    ('technical_support', 'Technical Support'),
    ('feedback', 'Feedback/Suggestions'),
    ('other', 'Other'),
]


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.CharField(max_length=200, choices=SUBJECT_CHOICES)
    email = models.EmailField(max_length=60)
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.first_name} {self.surname} - "
            f"{self.subject} - {self.timestamp}"
        )

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Messages"
