from django.db import models

# Create your models here.
class Stock (models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length = 20)
    ticker = models.CharField (max_length = 10)
    decsc = models.CharField (max_length = 100)
    remark = models.CharField (max_length = 200)
    date= models.DateTimeField (auto_now_add=True)

    