from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=True)
    name = models.CharField(max_length=30, default='')
    message = models.TextField(default='')
    email = models.EmailField(max_length=50, unique=True)

    class Meta:
        db_table = 'user'
        ordering = ['name']