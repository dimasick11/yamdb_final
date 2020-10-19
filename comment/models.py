from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from api.models import Title

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='review')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    text = models.TextField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)
