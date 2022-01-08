from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def user_rate(context,*args,**kwargs):
    from Vote_app.models import Rate
    request = context['request']
    objects = context['object']

    try:
        rate = Rate.objects.get_user_rate(request=request,object_id=objects.pk,object_slug=objects.slug)
    except:
        rate = Rate.objects.get_user_rate(request=request,object_id=objects.pk,object_slug=objects.series_slug)

    return rate

@register.simple_tag(takes_context=True)
def range_tag(context,value):
    numbers = range(value)
    return numbers