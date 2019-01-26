from django.db import models

# Create your models here.
class Doctors(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_image = models.ImageField(blank=True)

    def __str__(self):
        return "{}  {}".format(self.first_name, self.last_name)
