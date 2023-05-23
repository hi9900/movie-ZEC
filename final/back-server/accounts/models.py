from django.db import models
from django.contrib.auth.models import  AbstractUser # User #AbstractBaseUser, BaseUserManager, PermissionsMixin,
from django.contrib.auth import get_user_model
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=10, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    blocked_users = models.ManyToManyField('self', symmetrical=False, related_name='blocked_by', blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self) :
        return self.username



# class UserManager(BaseUserManager):
#     def create_user(self, email, password, **kwargs):
#     	# """
#         # 주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
#     	# """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=email,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email=None, password=None, **extra_fields):
#     	# """
#         # 주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
#         # 단, 최상위 사용자이므로 권한을 부여
#         # """
#         superuser = self.create_user(
#             email=email,
#             password=password,
#         )
#         superuser.is_staff = True
#         superuser.is_superuser = True
#         superuser.is_active = True
#         superuser.save(using=self._db)
#         return superuser


# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)
#     follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
#     followee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30, default='')
#     last_name = models.CharField(max_length=30, default='')

# 	# 헬퍼 클래스 사용
#     objects = UserManager()

# 	# 사용자의 username field는 email으로 설정 (이메일로 로그인)
#     USERNAME_FIELD = 'email'

