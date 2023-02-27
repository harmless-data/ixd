from django.db import models

# Create your models here.
class StaticData(models.Model):
    ean = models.BigIntegerField()
    json = models.JSONField()

    class meta:
        app_label = "contenttypes"


