from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField('Email почта', max_length=255)
    number_of_telephone = models.CharField('Number Phone', max_length=255)
    message = models.TextField('Message')
    sent_at = models.DateTimeField(auto_now_add=True)