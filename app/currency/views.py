from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from currency.utils import generate_password as gp
from currency.models import Rate, Source


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
