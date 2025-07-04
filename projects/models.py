from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def average_score(self):
        scores = self.votes.all()
        return sum(v.score for v in scores) / len(scores) if scores else 0

    def __str__(self):
        return self.title

class Vote(models.Model):
    project = models.ForeignKey(Project, related_name='votes', on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    submitted_at = models.DateTimeField(auto_now_add=True)
