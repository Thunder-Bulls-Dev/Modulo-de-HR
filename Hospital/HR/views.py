from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import loader

from .models import Empleado


def index(request):
    latest_empleado_list = Empleado.objects.order_by('-curp')[:5]
    template = loader.get_template('HR/index.html')
    context = {
        'latest_empleado_list': latest_empleado_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, empleado_id):
    empleado_id = get_object_or_404(Empleado, pk=empleado_id_id)
    return render(request, 'HR/detail.html', {'empleado_id': empleado_id})


def results(request, empleado_id):
    response = "You're looking at the results of empleado %s."
    return HttpResponse(response % empleado_id)


def vote(request, empleado_id):
    return HttpResponse("You're voting on empleado %s." % empleado_id)


def detail(request, empleado_id):
    try:
        empleado = Empleado.objects.get(pk=empleado_id)
    except Empleado.DoesNotExist:
        raise Http404("Empleado does not exist")
    return render(request, 'HR/detail.html', { empleado: empleado})