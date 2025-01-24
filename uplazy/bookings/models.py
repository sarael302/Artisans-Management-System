from django.db import models
from account.models import Profile
import uuid

class Booking(models.Model):
    booker = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    artisan = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    subject = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(max_length=2000, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    is_confirmed = models.BooleanField(default=False, null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self) -> str:
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created']