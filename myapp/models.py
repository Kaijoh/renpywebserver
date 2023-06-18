from django.db import models


class Score(models.Model):
    player_name = models.CharField(max_length=50)
    player_score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.player_name}: {self.player_score}'
    
class Score2(models.Model):
    player_name = models.CharField(max_length=50)
    player_score2 = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.player_name}: {self.player_score2}'

class Score3(models.Model):
    player_name = models.CharField(max_length=50)
    player_score3 = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.player_name}: {self.player_score3}'
