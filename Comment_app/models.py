from django.contrib.auth.models import User
from django.db import models
from Movie_app.models import Movie
from accounts.models import Profile
from Series_app.models import Series


class CommentModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,blank=True,null=True)
    series = models.ForeignKey(Series,on_delete=models.CASCADE,blank=True,null=True)
    comment_title = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        if self.movie:
            return f'{self.comment_title} from {self.user} for : {self.movie.title} movie, ({self.created_on})'
        else:
            return f'{self.comment_title} from {self.user} for : {self.series.title} series, ({self.created_on})'