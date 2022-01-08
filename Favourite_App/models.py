from django.contrib.auth.models import User
from django.db import models
from Movie_app.models import Movie
from Series_app.models import Series
from User_IP.models import IPAddress

class Favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie,on_delete=models.CASCADE,blank=True,null=True)
    series = models.ForeignKey(Series,on_delete=models.CASCADE,blank=True,null=True)
    ip_address = models.ForeignKey(IPAddress,on_delete=models.CASCADE,blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.movies is not None:
            return f'{self.movies} added to favourite by {self.user} at ({self.time_stamp.strftime("%D ==>%T")})'
        else:
            return f'{self.series} added to favourite by {self.user} at ({self.time_stamp.strftime("%D ==>%T")})'
