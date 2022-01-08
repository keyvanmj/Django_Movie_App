from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse
from Movie_app.utils import unique_slug_generator


class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(default='all', blank=True)
    meta_keywords = models.CharField(
        'Meta Keywords', max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag',
        default='Movie website'
    )
    meta_description = models.CharField(
        'Meta Description', max_length=255, help_text='Content for description meta tag',
        default='we have everything you need'

    )
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children', default=None
    )

    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' --> '.join(full_path[::-1])

    def get_cat_list(self):
        k = self
        breadcrumb = ['dummy']
        while k is not None:
            breadcrumb.append(k.title)
            k = k.parent
        for i in range(len(breadcrumb) - 3):
            breadcrumb[i] = '/'.join(breadcrumb)
        return breadcrumb[-1:0:-1]

def movie_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(movie_slug_pre_save_receiver, sender=Genre)