from django.db import models

# Create your models here.
class Candidates(models.Model):
    candidate_first_name = models.CharField(max_length=12)
    candidate_middle_name = models.CharField(max_length=12)
    candidate_last_name = models.CharField(max_length=12)
    candidate_id = models.IntegerField(default=0)

    def __str__(self):
        return self.candidate_first_name


class Votes(models.Model):
    voter_first_name = models.CharField(max_length=12)
    voter_last_name = models.CharField(max_length=12)
    voter_id = models.IntegerField(default=0)
    voter_choice = models.CharField(max_length=30)
    # vote_submit_time = models.DateTimeField("date submitted")

    def __str__(self):
        return self.voter_choice