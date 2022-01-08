import os

from django.db import models


def screen_shot_upload_to(instance,filename):
    name, ext = os.path.splitext(filename)
    types = None
    slug = None
    if instance.movie:
        slug = instance.movie.slug
        types = instance.movie.types
    elif instance.series:
        slug = instance.series.series_slug
        types = instance.series.types


    return f'screenshot/{types}/{slug}{ext}'



class ScreenShot(models.Model):
    movie = models.ForeignKey('Movie_app.Movie',on_delete=models.CASCADE,blank=True,null=True)
    series = models.ForeignKey('Series_app.Series',on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(upload_to=screen_shot_upload_to)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.movie:
            return f'{self.movie}'
        else:
            return f'{self.series}'