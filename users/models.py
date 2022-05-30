from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()

    SCHOOL = (
        ("HUFS", "한국외국어대학교"),
    )

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='이름')
    nickname = models.CharField(max_length=30, null=True, blank=True, verbose_name='닉네임')
    email = models.EmailField(null=True, unique=True, verbose_name='이메일')
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    school = models.CharField(choices=SCHOOL, max_length=30, null=True, blank=True, verbose_name='학교')
    birthday = models.DateTimeField(null=True, blank=True, verbose_name='생년월일')
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name='생성일')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = '유저'
