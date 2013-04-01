from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=15)
    register_date = models.DateField()
    mail = models.CharField(max_length=60)


class Proposal(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=20)
    proposed_by = models.ForeignKey(User)
    closed = models.BooleanField()

class Comment(models.Model):
    body = models.CharField(max_length=500)
    author = models.ForeignKey(User)
    publication_date = models.DateField()


class Vote(models.Model):
    proposal_ID = models.ForeignKey(Proposal)
    user = models.ForeignKey(User)
    value = models.SmallIntegerField()
    date = models.DateField()


