from django.db import models
from django.utils import timezone

PARTICIPANT_TYPES = [
    ('CONTESTANT', 'CONTESTANT'), 
    ('PRACTICE', 'PRACTICE'), 
    ('VIRTUAL', 'VIRTUAL'), 
    ('MANAGER', 'MANAGER'), 
    ('OUT_OF_COMPETITION', 'OUT_OF_COMPETITION'),
]

class CFUser(models.Model):
    handle = models.CharField(max_length=255, unique=True)
    rank = models.CharField(max_length=255)
    rating = models.IntegerField()

class CFProblem(models.Model):
    # contest = models.ForeignKey(CFContest, on_delete=models.CASCADE)
    problemset_name = models.CharField(max_length=255)
    index = models.CharField(max_length=255) # np. A, B, C, D
    name = models.CharField(max_length=255)
    points = models.FloatField(null=True, blank=True, default=None)
    rating = models.IntegerField(null=True, blank=True, default=None)


class CFProblemAndTag(models.Model):
    problem = models.ForeignKey(CFProblem, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)


class CFSubmission(models.Model):
    submit_time = models.DateTimeField()
    problem = models.ForeignKey(CFProblem, on_delete=models.CASCADE)
    user = models.ForeignKey(CFUser, on_delete=models.CASCADE)
    verdict  = models.BooleanField(default=False)
    accept_time = models.DateTimeField(null=True, blank=True)


class CFTag(models.Model):
    tag = models.CharField(max_length=255, unique=True)


class CFContest(models.Model):
    contest_id = models.IntegerField()
    duration = models.IntegerField() # w sekundach
    difficulty = models.IntegerField() # od 1 do 5 dziwne


class CFRatingChange(models.Model):
    contest = models.ForeignKey(CFContest, on_delete=models.CASCADE)
    user = models.ForeignKey(CFUser, on_delete=models.CASCADE)
    rank = models.IntegerField()
    old_rating = models.IntegerField()
    new_rating = models.IntegerField()


class CFUserAndContest(models.Model): # oparte na Party i Member
    user = CFUser(models.Model)
    contest = CFContest(models.Model)
    participant_type = models.CharField(max_length=255, choices=PARTICIPANT_TYPES)

