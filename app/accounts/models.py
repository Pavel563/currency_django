import uuid
from django.db import models
from django.templatetags.static import static
from django.contrib.auth.models import AbstractUser
from accounts.validators import validate_is_digits


def user_directory_path(instance, filename):
    return 'uploads/avatars/{0}/{1}'.format(instance.id, filename)

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    avatar = models.FileField(
        null=True, blank=True, default=None, upload_to=user_directory_path)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    # FS AWS S3, DO spaces

    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        default=None,
        # validators=(validate_is_digits, ),
    )

    # username = models.CharField(
    #     'username',
    #     max_length=150,
    #     unique=True,
    #     default=default_username,
    #     help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
    #     error_messages={
    #         'unique': "A user with that username already exists.",
    #     },
    # )

    email = models.EmailField(
        'email address', blank=False, null=False, unique=True,
    )

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('img/default-avatar.png')

    def save(self, *args, **kwargs):
        print('Before Save')
        if not self.username:  # if object was created
            self.username = str(uuid.uuid4())
        if self.phone:
            self.phone = ''.join(char for char in self.phone if char.isdigit())
        if self.email:
            self.email = str(self.email).lower()

        super().save(*args, **kwargs)
        print('after Save')
