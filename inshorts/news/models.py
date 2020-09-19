from django.db import models

class News(models.Model):
    imageUrl = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # created_at = models.DateTimeField(auto_now_add=True,verbose_name='created_at')

    # class Meta:
    #     ordering = ['created_at']
