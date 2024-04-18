from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 이름과 성을 수정하지 못하도록 설정
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    # 한국식으로 이름을 작성할 수 있도록 설정
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
