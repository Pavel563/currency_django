from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from currency.utils import generate_password as gp
from currency.models import Rate, Source
from currency.forms import RateForm
from annoying.functions import get_object_or_None


def hello(request):
    return HttpResponse("Hello World!")


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def rate_list(request):
    queryset = Rate.objects.all()
    context = {
        'objects': queryset,
    }
    return render(request, 'rate_list.html', context=context)


def rate_details(request, pk):
    # try:
    #     rate = Rate.objects.get(pk=pk)
    # except Rate.DoesMotExist:
    #     rate = None

    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'object': rate,
    }
    return render(request, 'source_details.html', context=context)


############################# Занятие 9 ################################################################################


def rate_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'message': 'Rate Create',
        'form': form,
    }
    return render(request, 'rate_create.html', context=context)


def rate_update(request, pk):
    instance = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=instance)

    context = {
        'form': form,
    }
    return render(request, 'rate_update.html', context=context)


def rate_delete(request, pk):
    instance = get_object_or_None(Rate, pk=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/rate/list/')


########################################################################################################################


################################ Домашняя работа 7 #####################################################################
def source_list(request):
    queryset = Source.objects.all()
    context = {
        'objects': queryset,
    }
    return render(request, 'source_list.html', context=context)


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)

    context = {
        'object': source,
    }
    return render(request, 'source_details.html', context=context)


def table_test(request):
    return render(request, 'table_test.html')

########################################################################################################################
