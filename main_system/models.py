from django.db import models

PARTICIPANT_TYPES = [
    ('CONTESTANT', 'CONTESTANT'), 
    ('PRACTICE', 'PRACTICE'), 
    ('VIRTUAL', 'VIRTUAL'), 
    ('MANAGER', 'MANAGER'), 
    ('OUT_OF_COMPETITION', 'OUT_OF_COMPETITION'),
]

VERDICTS = [
    ('FAILED', 'FAILED'),
    ('OK', 'OK'),
    ('PARTIAL', 'PARTIAL'),
    ('COMPILATION_ERROR,', 'COMPILATION_ERROR,'),
    ('RUNTIME_ERROR', 'RUNTIME_ERROR'),
    ('WRONG_ANSWER', 'WRONG_ANSWER'),
    ('PRESENTATION_ERROR', 'PRESENTATION_ERROR'),
    ('TIME_LIMIT_EXCEEDED', 'TIME_LIMIT_EXCEEDED'),
    ('MEMORY_LIMIT_EXCEEDED', 'MEMORY_LIMIT_EXCEEDED'),
    ('IDLENESS_LIMIT_EXCEEDED', 'IDLENESS_LIMIT_EXCEEDED'),
    ('SECURITY_VIOLATED', 'SECURITY_VIOLATED'),
    ('CRASHED', 'CRASHED'),
    ('INPUT_PREPARATION_CRASHED', 'INPUT_PREPARATION_CRASHED'),
    ('CHALLENGED', 'CHALLENGED'),
    ('SKIPPED', 'SKIPPED'),
    ('TESTING', 'TESTING'),
    ('REJECTED', 'REJECTED'),
]

class CFUser(models.Model):
    handle = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    rating = models.IntegerField()

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


class CFProblem(models.Model):
    contest = models.ForeignKey(CFContest, on_delete=models.CASCADE)
    problemset_name = models.CharField(max_length=255)
    index = models.CharField(max_length=255) # np. A, B, C, D
    name = models.CharField(max_length=255)
    points = models.FloatField()
    rating = models.IntegerField()


class CFProblemAndTag(models.Model):
    problem = models.ForeignKey(CFProblem, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)


class CFSubmission(models.Model):
    cf_id = models.IntegerField()
    contest = models.ForeignKey(CFContest, on_delete=models.CASCADE, null=True, 
                                blank=True) 
    creation_time = models.IntegerField() # jakiś unix-format XD
    problem = models.ForeignKey(CFProblem, on_delete=models.CASCADE)
    user = models.ForeignKey(CFUser, on_delete=models.CASCADE)
    verdict  = models.CharField(max_length=255, choices=VERDICTS, null=True, blank=True)