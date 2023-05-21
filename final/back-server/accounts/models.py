from django.db import models
from django.contrib.auth.models import  AbstractUser, User #AbstractBaseUser, BaseUserManager, PermissionsMixin,
from django.contrib.auth import get_user_model
from django.conf import settings


class User(AbstractUser):
    # following = models.ManyToManyField('self', through='UserFollowing', related_name='followers', symmetrical=False)

    def __str__(self) :
        return self.username
        

# class UserFollowing(models.Model):
#     user = models.ForeignKey(User, related_name='user_following', on_delete=models.CASCADE)
#     following_user = models.ForeignKey(User, related_name='user_followers', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True, db_index=True)

#     class Meta:
#         unique_together = (('user', 'following_user'),)



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

     
    



# class Follow(models.Model):
    # follower = models.ForeignKey(get_user_model(), related_name='following', on_delete=models.CASCADE)
    # followee = models.ForeignKey(get_user_model(), related_name='followers', on_delete=models.CASCADE)
