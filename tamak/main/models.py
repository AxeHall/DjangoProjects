from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    feedback_text = models.TextField(verbose_name="Оставьте Отзыв")
    date_of_review = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.feedback_text

    def get_absolute_url(self):
        return reverse("feedback_list")

class Comment(models.Model):
    creater = models.ForeignKey(User, on_delete=CASCADE, verbose_name="Автор комметариев")
    feedback = models.ForeignKey(Feedback, on_delete=CASCADE)
    comment_body = models.TextField(max_length=256)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.comment_body

class UserProfile(models.Model):
    django_user = models.OneToOneField(User,
    related_name="user_profile",
     on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to="user_profiles", default="user_profiles/default.png")

    def str(self) -> str:
        return self.django_user.username