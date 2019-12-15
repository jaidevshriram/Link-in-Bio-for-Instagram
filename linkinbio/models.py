from django.db import models

class PostModel(models.Model):
    link = models.URLField()
    img = models.ImageField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link
