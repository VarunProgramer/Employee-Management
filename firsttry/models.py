from django.db import models

# Create your models here.

class empdetails(models.Model):
    CodeNo = models.IntegerField()
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Salary = models.IntegerField()
    Address = models.CharField(max_length=150)
    Work = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
