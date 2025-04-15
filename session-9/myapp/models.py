from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']

class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(choices=[(i,i) for i in range (1,6)])
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-level']

class About(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    profile_image = models.URLField(blank=True)
    resume = models.URLField(blank=True)
    def __str__(self):
        return self.name
