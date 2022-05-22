from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("이메일을 입력해주세요.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 유저 생성시
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(email, password, **extra_fields)

    # super user 생성시
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser는 반드시 is_staff=True 이어야 합니다.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser는 반드시 is_superuser=True 이어야 합니다.")

        return self._create_user(email, password, **extra_fields)


# User table
class User(AbstractBaseUser, PermissionsMixin):

    """Custom User Model"""

    email = models.EmailField(
        unique=True, blank=False, null=False
    )  # Email 애트리뷰트, 중복데이터 비허용
    password = models.CharField(
        max_length=45, blank=False, null=False
    )  # Password 애트리뷰트
    name = models.CharField(max_length=15, blank=False, null=False)
    nickname = models.CharField(max_length=30, blank=False)  # 닉네임 애트리뷰트
    created_at = models.DateTimeField(blank=True, auto_now_add=True)  # 가입날짜 애트리뷰트
    updated_at = models.DateTimeField(auto_now=True)  # 최근 로그인날짜/시간 애트리뷰트
    # django 필수 필드
    is_staff = models.BooleanField(default=False)  # 스태프권한 애트리뷰트
    is_active = models.BooleanField(default=True)  # is_active 는 필수로 True 해야 로그인 가능
    is_superuser = models.BooleanField(default=False)  # django에서 필요한 애트리뷰트
    objects = UserManager()  # User table을 위해 필요한 코드

    USERNAME_FIELD = "email"  # Email이 식별자
    REQUIRED_FIELDS = ["nickname"]  # 필수입력값
    
    def __str__(self):
        return self.name
