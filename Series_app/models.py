import os
from decimal import Decimal
from uuid import uuid4
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.html import format_html
from Movie_Category.models import Genre
from Movie_app.utils import unique_slug_generator
from Series_app.manager import SeriesManager
from Stats_app.models import HitModel
from User_IP.models import IPAddress
from embed_video.fields import EmbedVideoField



class Series(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='series',blank=True,null=True)
    series_background_image = models.ImageField(upload_to='series/background',blank=True,null=True)
    series_slug = models.SlugField(max_length=100, blank=True)
    series_length = models.CharField(max_length=50)
    release_date = models.CharField(max_length=100,blank=True,null=True)
    trailer = EmbedVideoField(blank=True,null=True)
    series_rate = models.CharField(max_length=100,blank=True,null=True)
    imdb_rate = models.CharField(max_length=100,blank=True,null=True)
    cast = models.ManyToManyField('Person_app.Person',blank=True,related_name='series_cast')
    creator = models.ManyToManyField('Person_app.Person',blank=True,related_name='series_creator')
    genre = models.ManyToManyField(Genre, blank=True)
    types = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    series_hits = models.ManyToManyField(IPAddress,blank=True,through=HitModel,related_name='series_hits')
    imdb_link = models.URLField(max_length=300,blank=True,null=True)

    objects = SeriesManager()


    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return f'{self.title} (release : {self.release_date})'

    def snippet(self):
        return self.description[:500] + '...'

    def get_absolute_url(self):
        return reverse('Series:series_detail_view',kwargs={'slug':self.series_slug,'pk':self.pk})

    @property
    def get_obj_rate(self):
        series_rate = self.rate_set.filter(series_id=self.pk)
        rate_item = []
        rate = None
        for r in series_rate:
            rate_item.append(r.rate)
        rate = rate_item
        return rate

    @property
    def get_obj_image(self):
        image = self.image
        img = None
        if image:
            img = image
            return img
        else:
            return img

    @property
    def get_obj_model_name(self):
        return self.__module__.title()


    def get_vote_value(self,request):
        val = None
        user_vote = self.vote_set.filter(user_id=request.user.id,series_id=self.pk)
        for val in user_vote:
            if val.value == 1:
                val = 'LIKE'
            else:
                val = 'DISLIKE'
        value = val
        return value

    @property
    def obj_created_time(self):
        return self.date

    @property
    def get_obj_imdb_rate(self):
        return self.imdb_rate

    def thumbnail_tag(self):
        return format_html(f'<img width="150" height="200" src="{self.get_obj_image.url}">')

    @property
    def get_object_avg_rate(self):
        from Vote_app.models import Rate
        rate = Rate.objects.get_rate_avg(obj_id=self.pk, obj_slug=self.series_slug)
        try:
            rate = round(rate['avg'], 1)
            rate = '%g' % (Decimal(str(rate)))
        except:
            rate = 0
        return rate

def series_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.series_slug:
        instance.series_slug = unique_slug_generator(instance)
pre_save.connect(series_slug_pre_save_receiver, sender=Series)




def season_directory_path_with_uuid(instance,filename):
    name,ext = os.path.splitext(filename)
    return f'series/{instance.series.title}/season{instance.season}/{instance.series_slug}{instance.pk} {uuid4()}{ext}'
