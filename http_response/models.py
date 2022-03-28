from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class HttpResponseMimicker(models.Model):
    name = models.CharField(unique=True, max_length=200)
    status_code = models.IntegerField(default=200, validators=[MinValueValidator(100), MaxValueValidator(599)])
    json_response = models.JSONField()

    def __str__(self):
        return self.name
