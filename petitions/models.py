from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    movie_name = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='petitions')
    created_at = models.DateTimeField(auto_now_add=True)
    yes_votes = models.IntegerField(default=0)
    no_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Petition for {self.movie_name}"

    class Meta:
        ordering = ['-created_at']

class Vote(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('petition', 'user')

    def __str__(self):
        return f"{self.user.username} voted {self.vote_type} on {self.petition.movie_name}"
