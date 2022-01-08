from django.db import models
from django.db.models.signals import pre_save

from Movie_app.utils import unique_slug_generator


class PersonManager(models.Manager):
    def all_with_prefetch_movies(self):
        qs = self.get_queryset()
        return qs.prefetch_related('directed','writing_credits','role_set__movie')


class Person(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    objects = PersonManager()

    class Meta:
        ordering = (
            'title',
        )

    def __str__(self):
        return f'{self.title}'

def person_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(person_slug_pre_save_receiver, sender=Person)
