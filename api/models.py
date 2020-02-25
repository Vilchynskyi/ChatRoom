from django.db import models
from django.utils import timezone
from django.urls import reverse


class Message(models.Model):
    author = models.CharField(max_length=55)
    email = models.EmailField(null=True)
    text = models.TextField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    @property
    def short_text(self):
        return self.text[:15] + '...' if len(self.text) > 20 else self.text

    def get_absolute_url(self):
        return reverse('api:single_message', kwargs={'pk': self.pk})
