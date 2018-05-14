from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, default="")
    age = models.IntegerField()
    birthday = models.DateField("Date of birth")
    angel = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
