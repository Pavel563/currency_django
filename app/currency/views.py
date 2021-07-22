from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from currency.utils import generate_password as gp
from currency.models import Rate, Bank, ContactUs
from currency.forms import RateForm, BankForm, ContactForm
from annoying.functions import get_object_or_None
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


def hello(request):
    return HttpResponse("Hello World!")


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def index(request):
    return render(request, 'index.html')


# def rate_list(request):
#     queryset = Rate.objects.all()
#     context = {
#         'objects': queryset,
#     }
#     return render(request, 'rate_list.html', context=context)

class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


# def rate_details(request, pk):
#     # try:
#     #     rate = Rate.objects.get(pk=pk)
#     # except Rate.DoesMotExist:
#     #     rate = None
#
#     rate = get_object_or_404(Rate, pk=pk)
#
#     context = {
#         'object': rate,
#     }
#     return render(request, 'rate_details.html', context=context)

class RateDetailView(DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()


# def rate_create(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         form = RateForm(form_data)
#         if form.is_valid():
#             form.save()
#             return redirect('currency:rate-list')
#     elif request.method == 'GET':
#         form = RateForm()
#
#     context = {
#         'message': 'Rate Create',
#         'form': form,
#     }
#     return render(request, 'rate_create.html', context=context)

class RateCreateView(CreateView):
    model = Rate
    fields = (
        'type',
        'sale',
        'buy',
        'source',
    )
    success_url = reverse_lazy('currency:rate-list')


# def rate_update(request, pk):
#     instance = get_object_or_404(Rate, pk=pk)
#
#     if request.method == 'POST':
#         form_data = request.POST
#         form = RateForm(form_data, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect('currency:rate-list')
#     elif request.method == 'GET':
#         form = RateForm(instance=instance)
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_update.html', context=context)


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm


# def rate_delete(request, pk):
#     instance = get_object_or_None(Rate, pk=pk)
#     if instance is not None:
#         instance.delete()
#     return redirect('currency:rate-list')

class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')


########################################################################################################################


# def bank_create(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         form = BankForm(form_data)
#         if form.is_valid():
#             form.save()
#             return redirect('currency:bank-list')
#     elif request.method == 'GET':
#         form = BankForm()
#
#     context = {
#         'message': 'Bank Create',
#         'form': form,
#     }
#     return render(request, 'bank_create.html', context=context)


class BankCreateView(CreateView):
    model = Bank
    fields = (
        'name',
        'url'
    )
    success_url = reverse_lazy('currency:bank-list')


# def bank_update(request, pk):
#     instance = get_object_or_404(Bank, pk=pk)
#
#     if request.method == 'POST':
#         form_data = request.POST
#         form = BankForm(form_data, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect('currency:bank-list')
#     elif request.method == 'GET':
#         form = BankForm(instance=instance)
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'bank_update.html', context=context)


class BankUpdateView(UpdateView):
    queryset = Bank.objects.all()
    template_name = 'bank_update.html'
    success_url = reverse_lazy('currency:bank-list')
    form_class = BankForm


# def bank_delete(request, pk):
#     instance = get_object_or_None(Bank, pk=pk)
#     if instance is not None:
#         instance.delete()
#     return redirect('currency:bank-list')

class BankDeleteView(DeleteView):
    queryset = Bank.objects.all()
    success_url = reverse_lazy('currency:bank-list')


# def bank_list(request):
#     bank = Bank.objects.all()
#     context = {
#         'objects': bank,
#     }
#     return render(request, 'bank_list.html', context=context)


class BankListView(ListView):
    template_name = 'bank_list.html'
    queryset = Bank.objects.all()


# def bank_details(request, pk):
#     bank = get_object_or_404(Bank, pk=pk)
#
#     context = {
#         'object': bank,
#     }
#     return render(request, 'bank_details.html', context=context)

class BankDetailView(DetailView):
    template_name = 'bank_details.html'
    queryset = Bank.objects.all()


########################################################################################################################

class CreateContactUs(CreateView):
    model = ContactUs
    fields = (
        'email_from',
        'subject',
        'message',
    )
    # form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        data = form.cleaned_data
        body = f"""
        From: {data['email_from']}
        Topic: {data['subject']}
        
        Message:
        {data['message']}
        """

        send_mail(
            'Contact Us from Client',
            body,
            'zvemrme@gmail.com',
            ['pasha.shalimoff169@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)
# def contact_create(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         form = ContactForm(form_data)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/currency//list/')
#     elif request.method == 'GET':
#         form = BankForm()
#
#     context = {
#         'message': 'Bank Create',
#         'form': form,
#     }
#     return render(request, 'bank_create.html', context=context)
#

########################################################################################################################

def table_test(request):
    return render(request, 'table_test.html')

########################################################################################################################
