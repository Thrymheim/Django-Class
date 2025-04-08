from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.laptop.name} by {self.user.username}"
