from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=10)
    time = models.DecimalField(max_digits=50, decimal_places=10)
    image = models.ImageField(upload_to="servise", verbose_name="Xizmat turi  rasmini kiriting")
        

class Review(models.Model):
    name = models.CharField(max_length=255 )
    comment = models.TextField()
    stars = models.PositiveIntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

class About(models.Model):
    image = models.ImageField(upload_to='about/')
    text = models.TextField()

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    date_upload = models.DateTimeField(auto_now_add=True)

class Barber(models.Model):
    name = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='barbers/')
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    