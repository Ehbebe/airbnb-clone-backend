from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    """숙소 모델 정의"""

    class RoomKindChoices(models.TextChoices):
        """숙소 종류에 대한 선택 옵션을 정의하는 내부 클래스"""

        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(
        max_length=150,
        default="",
        verbose_name="숙소 이름",
        help_text="숙소 이름을 입력하세요.",
    )

    country = models.CharField(
        max_length=50,
        default="한국",
        verbose_name="국가",
        help_text="숙소가 위치한 국가를 입력하세요.",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
        verbose_name="도시",
        help_text="숙소가 위치한 도시를 입력하세요.",
    )
    price = models.PositiveIntegerField(
        verbose_name="가격",
        help_text="숙소의 1박 기준 가격을 입력하세요.",
    )
    rooms = models.PositiveIntegerField(
        verbose_name="방 개수",
        help_text="숙소의 방 개수를 입력하세요.",
    )
    toilets = models.PositiveIntegerField(
        verbose_name="화장실 개수",
        help_text="숙소의 화장실 개수를 입력하세요.",
    )
    description = models.TextField(
        verbose_name="숙소 설명",
        help_text="숙소에 대한 상세한 설명을 입력하세요.",
    )
    address = models.CharField(
        max_length=250,
        verbose_name="상세 주소",
        help_text="숙소의 상세 주소를 입력하세요.",
    )
    pet_friendly = models.BooleanField(
        default=True,
        verbose_name="반려동물 동반 가능 여부",
        help_text="반려동물 동반 가능 여부를 선택하세요.",
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
        verbose_name="숙소 종류",
        help_text="숙소의 종류를 선택하세요.",
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
        verbose_name="숙소 주인",
        help_text="숙소의 주인을 선택하세요.",
    )

    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        """방이 가진 편의시설의 수를 반환"""
        return self.amenities.count()

    def rating(room):
        # 방에 대한 리뷰의 갯수를 세는 변수 count를 선언합니다.
        count = room.reviews.count()

        # 만약 리뷰가 하나도 없는 경우 (count가 0인 경우)
        if count == 0:
            # "No Reviews" 문자열을 반환합니다. 즉, 리뷰가 없다는 것을 나타냅니다.
            return "No Reviews"

        # 리뷰가 하나 이상 있는 경우
        else:
            # 총 평점을 저장할 변수 total_rating을 0으로 초기화합니다.
            total_rating = 0
            # 방의 모든 리뷰를 반복하여 각 리뷰의 평점을 total_rating에 더합니다.
            for review in room.reviews.all().values("rating"):
                total_rating += review["rating"]

            # 평균 평점을 계산합니다. 이 때, round 함수를 사용하여 소수점 둘째 자리까지 반올림합니다.
            # 총 평점을 리뷰 갯수로 나누어 평균을 구합니다.
            return round(total_rating / count, 2)


class Amenity(CommonModel):
    """숙소 편의시설 모델 정의"""

    name = models.CharField(
        max_length=150,
        verbose_name="편의시설 이름",
        help_text="편의시설의 이름을 입력하세요.",
    )
    description = models.CharField(
        max_length=150,
        null=True,
        verbose_name="편의시설 설명",
        help_text="편의시설에 대한 설명을 입력하세요. (선택 사항)",
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
