from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=50)
    time = models.DecimalField(max_digits=50)
    image = models.ImageField(upload_to="servise", verbose_name="Xizmat turi  rasmini kiriting")