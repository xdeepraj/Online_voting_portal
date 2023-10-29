from django.db import models
from users.models import CustomUser

class Position(models.Model):
    positions = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.positions
    
class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    mobile_no = models.CharField(null=False, blank=False, max_length=10)
    candidate_image = models.ImageField(null=False, blank=False, upload_to="candidate_images/")
    description = models.TextField(null=True, blank=True)
    votes = models.IntegerField(default = 0)
    positions = models.ForeignKey(Position, on_delete = models.CASCADE)

    def __str__(self):
        return self.first_name
    
class Vote(models.Model):
    class Meta:
        unique_together = (('position','user'),)

    user = models.ForeignKey(CustomUser, on_delete = models.PROTECT)
    selected_choice = models.ForeignKey(Candidate, on_delete = models.PROTECT)
    position = models.ForeignKey(Position, on_delete = models.PROTECT)



    
    