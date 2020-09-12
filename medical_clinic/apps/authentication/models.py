import uuid
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .models_choices import COUNTY_CHOICE, UserTypeChoice
from .models_validators import phone_no_validator


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class.
    """

    def create_user(self, phone_no, user_type, first_name, last_name, date_of_birth, county, locality, password=None):
        """
        Creates and saves a User.
        """
        if not phone_no:
            raise ValueError('Users must have a phone number')

        if not user_type:
            raise ValueError('Users must have a type')

        if not first_name:
            raise ValueError('Users must have a first name')

        if not last_name:
            raise ValueError('Users must have a last name')

        if not date_of_birth:
            raise ValueError('Users must have a date of birth')

        if not county:
            raise ValueError('Users must have a county in address')

        if not locality:
            raise ValueError('Users must have a locality in address')

        if password is None:
            raise TypeError('Users must have a password.')

        user = self.model(
            phone_no=phone_no,
            user_type=user_type,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            county=county,
            locality=locality
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_no, user_type, first_name, last_name, date_of_birth, county, locality,
                         password=None):
        """
        Creates and saves a superuser.
        """

        user = self.create_user(
            phone_no=phone_no,
            user_type=UserTypeChoice.ADMIN,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            county=county,
            locality=locality,
            password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # The phone number will be used to represent the 'User' in the UI and it will be used also for logging in
    phone_no = models.CharField(
        'phone number',
        max_length=20,
        unique=True,
        db_index=True,
        help_text='Required.',
        validators=[phone_no_validator],
        error_messages={
            'unique': "A user with that phone number already exists.",
        },
    )
    user_type = models.IntegerField(
        'user type',
        choices=UserTypeChoice.choices,
        blank=False,
        default=UserTypeChoice.PATIENT,
        help_text='Required.'
    )
    first_name = models.CharField(
        'first name',
        max_length=150,
        blank=False,
        validators=[MinLengthValidator(3)],
        help_text='Required.',
    )
    last_name = models.CharField(
        'last name',
        max_length=150,
        blank=False,
        validators=[MinLengthValidator(3)],
        help_text='Required.',
    )
    date_of_birth = models.DateField(
        'date of birth',
        blank=False,
        help_text='Required.'
    )
    county = models.IntegerField(
        'county',
        choices=COUNTY_CHOICE,
        blank=False,
        help_text='Required.'
    )
    locality = models.CharField(
        'locality',
        max_length=150,
        blank=False,
        help_text='Required.'
    )
    email = models.EmailField(
        'email address',
        blank=True
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as active. \
            Unselect this instead of deleting accounts.'
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    @property
    def is_staff(self):
        return (
                self.user_type == UserTypeChoice.ADMIN or
                self.user_type == UserTypeChoice.DOCTOR or
                self.user_type == UserTypeChoice.SECRETARY
        )

    objects = UserManager()

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = ['user_type', 'first_name', 'last_name', 'date_of_birth', 'county', 'locality']

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.phone_no

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # If a backend raises a PermissionDenied exception in has_perm() or has_module_perms(),
        # the authorization will immediately fail and Django won’t check the backends that follow.

        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # If a backend raises a PermissionDenied exception in has_perm() or has_module_perms(),
        # the authorization will immediately fail and Django won’t check the backends that follow.

        # Simplest possible answer: Yes, always
        return True

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class AuthorizationToken(models.Model):
    """
    Token used by user to identify itself when sending an authorization code,
    in order to be allowed to alter sensitive data.
    The user can send an Aut
    """
    token = models.UUIDField(db_index=True, unique=True, editable=False, default=uuid.uuid4)
    code = models.CharField(
        max_length=10,
        blank=False,
        help_text='Required. Code used by the user to authorize an operation.'
    )
    expiry = models.DateTimeField(blank=False)

    def __str__(self):
        return str(self.token)
