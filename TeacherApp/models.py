from django.db import models

# Create your models here.
class herotext(models.Model):
    toptext = models.CharField(max_length=30)
    hero_title = models.CharField(max_length=200)
    hero_description= models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.toptext


class contentcolumn(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='content/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='certifications/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description
class contentbody(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='contentbody/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class footer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='footer/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class comparison(models.Model):
    labels = models.CharField(max_length=200)
    teacher = models.TextField()
    others = models.TextField()
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.labels

class whyus(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ImageField(upload_to='whyus/')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title