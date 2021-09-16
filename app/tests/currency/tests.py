from currency import choices
from currency.models import Bank, Rate


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert [t.name for t in response.templates] == [
        'index.html',
        'base.html',
        'includes/navbar.html',
    ]


def test_rate_list(client):
    response = client.get('/currency/rate/list/')
    assert response.status_code == 200


def test_create_rate_get_form(client):
    response = client.get('/currency/rate/create/')
    assert response.status_code == 200


def test_create_rate_empty_form_data(client):
    response = client.post('/currency/rate/create/')
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'type': ['This field is required.'],
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'bank': ['This field is required.'],
    }


def test_create_rate_invalid_form_data(client, fake):
    rates_initial_count = Rate.objects.count()
    form_data = {
        'type': choices.RATE_TYPE_USD,
        'sale': 20,
        'buy': 30,
        'bank': 999999,
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'bank': ['Select a valid choice. That choice is not one of the available choices.'],
    }
    assert Rate.objects.count() == rates_initial_count


def test_create_rate_success(client):
    rates_initial_count = Rate.objects.count()
    bank = Bank.objects.last()
    form_data = {
        'type': choices.RATE_TYPE_USD,
        'sale': 20,
        'buy': 30,
        'bank': bank.id,
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 302
    assert response.url == '/currency/rate/list/'
    assert Rate.objects.count() == rates_initial_count + 1


def test_create_contact_us(client, mailoutbox, settings, fake):
    email_from = fake.email()
    form_data = {
        'email_from': email_from,  # TODO
        'subject': 'subject',
        'message': 'Message',
    }
    response = client.post('/currency/contact-us/create/', data=form_data)
    assert response.status_code == 302
    assert response.url == '/'
    assert len(mailoutbox) == 1
    mail = mailoutbox[0]
    assert mail.to == ['pasha.shalimoff169@gmail.com']
    assert mail.cc == []
    assert mail.bcc == []
    assert mail.reply_to == []
    # assert mail.from_email == settings.EMAIL_HOST_USER
