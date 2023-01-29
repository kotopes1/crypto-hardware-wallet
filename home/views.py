"""
The render function in Django's shortcuts module is used
to render a template and return an HttpResponse object.
It takes request, template_name and a context as arguments.
The template specified in template_name is rendered with the
context data and the resulting output is returned as an HttpResponse object.
This function is a convenient shortcut for creating
a simple view that only needs to return a rendered template.
:param request: The current HttpRequest object.
:type request: HttpRequest
:param template_name: The name of the template to be rendered.
:type template_name: str
:param context: The context data to be passed to the template.
:type context: dict
:return: An HttpResponse object containing the rendered template.

"""
from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
