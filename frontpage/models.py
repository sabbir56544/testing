from django.db import models

from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name




class Sub_Category(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name + " | " + self.title 

   

class Item(models.Model):
    name = models.CharField(max_length=200)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    disc = models.TextField()
    image = models.ImageField(upload_to='media/photos', blank=True, null=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    disc = models.TextField()
    image = models.ImageField(upload_to='media/photos')

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/photos')
    disc = models.TextField()
    about_course = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    messages = models.TextField()

    def __str__(self):
        return self.name
