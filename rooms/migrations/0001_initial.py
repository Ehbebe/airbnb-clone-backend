# Generated by Django 5.0.4 on 2024-04-21 07:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Amenity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="편의시설의 이름을 입력하세요.",
                        max_length=150,
                        verbose_name="편의시설 이름",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="편의시설에 대한 설명을 입력하세요. (선택 사항)",
                        max_length=150,
                        null=True,
                        verbose_name="편의시설 설명",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Amenities",
            },
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        default="",
                        help_text="숙소 이름을 입력하세요.",
                        max_length=150,
                        verbose_name="숙소 이름",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        default="한국",
                        help_text="숙소가 위치한 국가를 입력하세요.",
                        max_length=50,
                        verbose_name="국가",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="서울",
                        help_text="숙소가 위치한 도시를 입력하세요.",
                        max_length=80,
                        verbose_name="도시",
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        help_text="숙소의 1박 기준 가격을 입력하세요.",
                        verbose_name="가격",
                    ),
                ),
                (
                    "rooms",
                    models.PositiveIntegerField(
                        help_text="숙소의 방 개수를 입력하세요.", verbose_name="방 개수"
                    ),
                ),
                (
                    "toilets",
                    models.PositiveIntegerField(
                        help_text="숙소의 화장실 개수를 입력하세요.",
                        verbose_name="화장실 개수",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="숙소에 대한 상세한 설명을 입력하세요.",
                        verbose_name="숙소 설명",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        help_text="숙소의 상세 주소를 입력하세요.",
                        max_length=250,
                        verbose_name="상세 주소",
                    ),
                ),
                (
                    "pet_friendly",
                    models.BooleanField(
                        default=True,
                        help_text="반려동물 동반 가능 여부를 선택하세요.",
                        verbose_name="반려동물 동반 가능 여부",
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("entire_place", "Entire Place"),
                            ("private_room", "Private Room"),
                            ("shared_room", "Shared Room"),
                        ],
                        help_text="숙소의 종류를 선택하세요.",
                        max_length=20,
                        verbose_name="숙소 종류",
                    ),
                ),
                (
                    "amenities",
                    models.ManyToManyField(
                        help_text="숙소에 편의시설을 선택하세요.",
                        to="rooms.amenity",
                        verbose_name="편의시설",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        help_text="숙소의 주인을 선택하세요.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="숙소 주인",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
