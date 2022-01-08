from django.http import Http404


class CommentMixin:

    def get_success_url(self):
        # redirect to detail page
        get_absolute_url = self.request.META['HTTP_REFERER']
        return get_absolute_url

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return super().get(request, *args, **kwargs)
        else:
            raise Http404()