from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Department(models.Model):
    department  = models.CharField(max_length=100)
    image=models.ImageField(upload_to='department')


 #   class Meta:
 #       ordering=('department',)
  #      verbose_name='department'
  #      verbose_name_plural='departments'

  #  def __str__(self):
  #      return '{}'.format(self.department)




