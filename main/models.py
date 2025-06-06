from django.db import models

class Student(models.Model):
    name = models.TextField("name")
    photo = models.ImageField(upload_to='photos/', default='photos/default.jpg')
    age = models.IntegerField("age")
    grade = models.TextField("grade")

    def get_absolute_url(self):
        return f'/{self.pk}'

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Comment(models.Model):
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Comment")
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.created_at:%Y-%m-%d %H:%M})"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at'] 


class Receipt(models.Model):
    title = models.TextField("Name")
    description = models.TextField("How to cook")
    time  = models.TimeField("Time to cook")


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'

