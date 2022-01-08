import os
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify
from Movie_Category.models import Genre
from Stats_app.models import HitModel
from User_IP.models import IPAddress
from .manager import MovieManager
from .utils import random_string_generator,unique_slug_generator
from uuid import uuid4
from embed_video.fields import EmbedVideoField

def movie_directory_path_with_uuid(instance,filename):
    name,ext = os.path.splitext(filename)

    return f'movies/{instance.movie.title}{instance.movie_id} {uuid4()}{ext}'


class MovieImage(models.Model):
    image = models.ImageField(upload_to=movie_directory_path_with_uuid)
    uploaded = models.DateTimeField(auto_created=True,null=True)
    movie = models.ForeignKey(to='Movie',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.movie} image'



class Movie(models.Model):
    title = models.CharField(max_length=140)
    plot = models.TextField()
    release_date = models.CharField(max_length=100,blank=True,null=True)
    movie_length = models.CharField(max_length=50,blank=True,null=True)
    imdb_rating = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    trailer = EmbedVideoField(blank=True,null=True)
    cast = models.ManyToManyField('Person_app.Person',blank=True,related_name='movies_cast')
    director = models.ManyToManyField('Person_app.Person',blank=True,related_name='movies_director')
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField(Genre, blank=True)
    background_image = models.ImageField(upload_to='movies/background',blank=True,null=True)
    types = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    movie_hits = models.ManyToManyField(IPAddress,blank=True,through=HitModel,related_name='movie_hits')
    imdb_link = models.URLField(max_length=300,blank=True,null=True)

    objects = MovieManager()

    def __str__(self):
        return f'{self.title}({self.release_date})'

    def get_absolute_url(self):
        return reverse('Movies:movie_detail', kwargs={'slug': self.slug, 'pk': self.pk})

    @property
    def get_obj_image(self):
        image = self.movieimage_set.all()
        items = []
        img = None
        if image:
            for i in image:
                items.append(i.image)
            img = items
            return img[-1]
        else:
            return img

    @property
    def get_obj_rate(self):
        movie_rate = self.rate_set.filter(movie_id=self.pk)
        rate_item = []
        rate = None
        for r in movie_rate:
            rate_item.append(r.rate)
        rate = rate_item
        return rate

    def get_obj_hits(self):
        movie_hits = self.movie_hits.all()
        return movie_hits

    def snippet(self):
        return self.plot[:500] + '...'

    @property
    def get_obj_model_name(self):
        return self.__module__.title()


    def get_vote_value(self,request):
        val = None
        user_vote = self.vote_set.filter(user_id=request.user.id,movie_id=self.pk)
        for val in user_vote:
            if val.value == 1:
                val = 'LIKE'
            else:
                val = 'DISLIKE'
        value = val
        return value

    @property
    def obj_created_time(self):
        return self.created

    @property
    def get_obj_imdb_rate(self):
        return self.imdb_rating

    def thumbnail_tag(self):
        return format_html(f'<img width="150" height="200" src="{self.get_obj_image.url}">')

    @property
    def get_object_avg_rate(self):
        from Vote_app.models import Rate
        rate = Rate.objects.get_rate_avg(obj_id=self.pk, obj_slug=self.slug)
        try:
            rate = round(rate['avg'],1)
            rate = '%g' % (Decimal(str(rate)))
        except:
            rate = 0
        return rate


def movie_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(movie_slug_pre_save_receiver, sender=Movie)