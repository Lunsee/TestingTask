from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=100, blank=True, null=True)
    named_url = models.CharField(max_length=100, blank=True,null=True)

