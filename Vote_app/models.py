from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum, Avg, Q
from django.db.models.signals import pre_save
from django.shortcuts import get_object_or_404
from Movie_app.models import Movie
from Series_app.models import Series
from User_IP.models import IPAddress


class RateManager(models.Manager):
    def get_rate_or_unsaved_blank_rate(self,movie=None,series=None,user=None):
        try:
            if movie:
                return Rate.objects.filter(movie=movie,user=user)
            else:
                return Rate.objects.filter(series=series,user=user)

        except Rate.DoesNotExist:
            if movie:
                return Rate(movie=movie,user=user).save()
            else:
                return Rate(series=series,user=user).save()


    def get_rate_avg(self,obj_id=None,obj_slug=None):
        rate_avg = self.get_queryset().filter(
            (Q(movie_id=obj_id) & Q(movie__slug=obj_slug)) |
            (Q(series_id=obj_id) & Q(series__series_slug=obj_slug))
        ).aggregate(avg=Avg('rate'))
        return rate_avg


class VoteManager(models.Manager):
    def get_vote_or_unsaved_blank_vote(self,movie=None,user=None,series=None):
        try:
            if movie:
                return Vote.objects.get(movie=movie,user=user)
            else:
                return Vote.objects.get(series=series,user=user)
        except Vote.DoesNotExist:
            if movie:
                return Vote(movie=movie,user=user)
            else:
                return Vote(series=series,user=user)



Up = 1
Down = -1
like = '\U0001F44D'
dislike = '\U0001F44E'

VALUE_CHOICES = (
    (Up,like,),
    (Down,dislike,),
)
RATE_CHOICES = (
    (1,1,),
    (2,2,),
    (3,3,),
    (4,4,),
    (5,5,),
)


class Vote(models.Model):
    value = models.SmallIntegerField(choices=VALUE_CHOICES)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,blank=True,null=True)
    series = models.ForeignKey(Series,on_delete=models.CASCADE,blank=True,null=True)
    ip_address = models.ForeignKey(IPAddress,on_delete=models.CASCADE,blank=True,null=True)
    voted_on = models.DateTimeField(auto_now=True)

    objects = VoteManager()

    def __str__(self):
        if self.movie:
            return f'{self.user}\'s vote is ({self.value}) on {self.movie} '
        else:
            return f'{self.user}\'s vote is ({self.value}) on {self.series} '

    class Meta:
        unique_together = ('user','movie','series')


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,blank=True,null=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE,blank=True,null=True)
    rate_on = models.DateTimeField(auto_now=True)
    rate = models.IntegerField(choices=RATE_CHOICES, default=0,
            validators=[MaxValueValidator(5), MinValueValidator(0)])

    objects = RateManager()

    class Meta:
        unique_together = ('user','movie','series')

    def __str__(self):
        if not self.movie:
            return f'{self.user}\'s rate is ({self.rate}) on {self.series} in : {self.rate_on.strftime("%d / %m / %Y")} '
        else:
            return f'{self.user}\'s rate is ({self.rate}) on {self.movie} in : {self.rate_on.strftime("%d / %m / %Y")} '

