from django.shortcuts import render

from django.views.generic import UpdateView, CreateView, RedirectView
from accounts.models import User
from django.urls import reverse_lazy
from accounts.forms import SingUpForm
from django.core.checks import messages
from accounts.tokens import account_activation_token

class MyProfile(UpdateView):
    queryset = User.objects.all()
    template_name = 'my-profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(pk=self.request.user.pk)
    #     return queryset

    def get_object(self, queryset=None):
        return self.request.user


class SingUp(CreateView):
    model = User
    template_name = 'singup.html'
    success_url = reverse_lazy('index')
    form_class = SingUpForm


class ActivateAccount(RedirectView):
    pattern_name = 'index'

    """
    
    """
    def get_redirect_url(self, *args, **kwargs):
        activation_key = kwargs.pop('activation_key')
        user = get_object_or_None(User.objects.only('is_active'), username=activation_key)
        # User.objects.filter(username=activation_key).update(is_active=True)

        if user:
            if user.is_active:
                messages.warning(
                    self.request, 'Your account is already activated'
                )
            else:
                massages.info(self.request, 'Thanks for activating your account')
                user.is_active = True
                user.save()

        response = super().get_redirect_url(*args, **kwargs)
        return response

    def activate(request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'account_activation_invalid.html')

    def signup(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message)
                return redirect('account_activation_sent')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})