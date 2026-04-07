from django.db import models
import uuid

class APIKey(models.Model):
    key = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    @staticmethod
    def generate_key():
        return uuid.uuid4().hex