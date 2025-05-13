from django.db import models

class Receipt(models.Model):
    title = models.TextField("Name")
    description = models.TextField("How to cook")
    time  = models.TimeField("Time to cook")


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'
