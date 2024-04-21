from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",  # 만약 작성한 모델의 str 메서드를 보여주길 원한다면 이렇게 작성해주면 됩니다.
        "payload",
    )
    list_filter = ("rating",)
