from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=32)
    img = models.ImageField(upload_to='test/')

    def __str__(self):
        return self.title
