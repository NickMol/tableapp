from django.db import models

class Characteristics(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TableData(models.Model):
    name = models.CharField(max_length=200, unique=True)
    attendance = models.IntegerField(blank=True, null=True)
    stadium = models.CharField(max_length=200,blank=True, null=True)
    characteristics = models.ManyToManyField(Characteristics,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


