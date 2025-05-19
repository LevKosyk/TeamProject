from django.db import models

class Student(models.Model):
    name = models.TextField("name")
    age = models.IntegerField("age")
    grade = models.TextField("grade")


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Receipt(models.Model):
    title = models.TextField("Name")
    description = models.TextField("How to cook")
    time  = models.TimeField("Time to cook")


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'
