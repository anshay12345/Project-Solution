from django.db import models
from django.contrib.auth.models import (PermissionsMixin,
                                        BaseUserManager,
                                        AbstractBaseUser)


# Create your models here.

class UserManager(BaseUserManager):
    # HELPS DJANGO WITH OUR CUSTOM USER MODEL
    use_in_migrations = True

    def _createuser_(self, email, username, password=None):
        # CREATING AND SAVING A NEW USER WITH THE GIVEN EMAIL AND PASS WORD

        if username is None:
            raise ValueError('User should have a username')
        if not email:
            raise ValueError('User should have an email')

        user = self.model(username=username, email=self.normalize_email(email))
        # CREATING USER
        user.set_password(password)
        # SETTING PASSWORD
        user.save()
        # SAVING THE USER
        return user

    def create_superuser(self, email, name, password):  # CREATING AND SAVING THE SUPERUSER
        # WITH THE GIVEN DETAILS

        user = self.create_user(email, name, password)

        user.is_superuser = True  # SUPERUSER STATUS
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):  # GIVE ACCESS TO OUR REGULAR USER FIELDS
    # Respents a "user profile" inside our system.

    email = models.EmailField(max_length=300, unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # ATTRIBUTE USER WILL BE USING TO LOG IN
    REQUIRED_FIELDS = ['username']
    objects = UserManager()  # INSTANTIATING THE MANAGER CLASS

    # TELL DJANGO HOW TO MANAGE OBJECT OF THIS TYPE "USER".

    def get_full_name(self):
        # USED TO USER'S FULLNAME

        return self.username

    def get_short_name(self):
        # USED TO GET A USER'S SHORT NAME

        return self.username

    def __str__(self):
        # DJANGO USES THIS WHEN IT NEEDED TO CONVERT OBJECT TO A STRING

        return self.email


class ProfileFeedItem(models.Model):
    # PROFILE STATUS UPDATE

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # RETURN THE MODEL AS A STRING

        return self.status_text
