from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    def __repr__(self):
        return self.title