from django.db import models


class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Django가 이 모델을 보더라도 DB에 저장하지 않음!
