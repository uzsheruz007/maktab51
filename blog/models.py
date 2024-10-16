from django.db import models

# Create your models here.

class Yangiliklar(models.Model):
    Rasm = models.ImageField(upload_to ='Rasm/%y')
    teacher = models.CharField(max_length=225, verbose_name="Mavzu")
    messages = models.TextField(max_length=10000, verbose_name="Xabar matni", null=True)
    # date = models.DateField()

    def __str__(self):
        return self.teacher