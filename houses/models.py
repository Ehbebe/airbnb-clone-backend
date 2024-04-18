from django.db import models


# Create your models here.
class House(models.Model):
    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Positive Numbers Only (양수만 가능!)"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True,
        help_text="Does this house allow pets?",
    )

    # ForeignKey는 데이터 타입인데, django 한테 방의 가격처럼 단순한 숫자가 아닌 데이터를 houses 테이브렝 저장한다고 알려줍니다.
    # ForeignKey는 Django에서 여기 있는 숫자가 다른 앱에 있는 테이블의 object의 ID 라는 것을 알려줍니다.
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE
    )  # 사용자가 계정을 지워도 house는 주인이 없는 상태로 남음

    def __str__(self):
        return self.name
