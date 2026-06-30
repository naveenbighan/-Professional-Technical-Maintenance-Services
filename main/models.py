from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    """Model to store contact form submissions from website visitors."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.name} - {self.subject}'


class Service(models.Model):
    """Model representing the services offered by Bustan Altoor Technical Services."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    detailed_description = models.TextField()
    icon = models.CharField(max_length=100, help_text='Font Awesome icon class')
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
