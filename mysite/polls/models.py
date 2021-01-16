""" definitions of the db models"""

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """ Definition of the Question model with additional configuration for the admin panel. """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """ Check if the question was published less than a day ago. """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # additional configuration for the display of the question list in the admin panel
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    """ Definition of the Choice model with its attributes. """

    # setting Question Choice relationship 1:n; delete all choices if question is deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
