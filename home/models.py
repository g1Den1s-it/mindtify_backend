import string
import random

from django.db import models
from user.models import User
# Create your models here.


def set_random_slug():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(24))
    return random_string


class Test(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    slug = models.CharField(max_length=25, default=set_random_slug())
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:10]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:10]


class TextAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_id')
    text = models.TextField()

    def __str__(self):
        return self.text[:10]


class ResponseTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)
    choice = models.ManyToManyField(Choice, blank=True)
    text_answer = models.ForeignKey(TextAnswer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.test.title
