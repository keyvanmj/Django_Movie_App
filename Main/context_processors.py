
def next_parameter(request):
    return {
        'next_parameter':request.GET['next'] if 'next' in request.GET else None,
    }