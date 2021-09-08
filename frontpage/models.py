from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name




class Sub_Category(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " | " + self.category.name 