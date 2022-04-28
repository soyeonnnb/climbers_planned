from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Travel)
class TravelAdmin(admin.ModelAdmin):

    """User Admin Definition"""

    fieldsets = (  # User 애트리뷰트들 분류
        (
            "기본 정보",  # 기본 정보
            {
                "fields": (
                    "name",
                    "user",
                    "start_date",
                    "end_date",
                    "color",
                )
            },
        ),
    )
    list_display = (  # 메인 화면에서 해당 애트리뷰트들 보이기
        "name",
        "user",
        "start_date",
        "end_date",
        "color",
    )
    ordering = ("user", "name", "start_date", "end_date", "color")  # 해당 애트리뷰트들로 순서


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):

    """User Admin Definition"""

    fieldsets = (  # User 애트리뷰트들 분류
        (
            "기본 정보",  # 기본 정보
            {
                "fields": (
                    "travel",
                    "name",
                    "day",
                    "order",
                )
            },
        ),
        (
            "위치 정보",  # 추가 정보
            {
                "fields": (
                    "latitude",
                    "longitude",
                ),
            },
        ),
    )
    list_display = (  # 메인 화면에서 해당 애트리뷰트들 보이기
        "travel",
        "name",
        "day",
        "order",
        "latitude",
        "longitude",
        "created_at",
        "updated_at",
    )
    ordering = (
        "travel",
        "day",
        "order",
        "name",
    )  # 해당 애트리뷰트들로 순서


@admin.register(models.Lodging)
class LodgingAdmin(admin.ModelAdmin):

    """User Admin Definition"""

    fieldsets = (  # User 애트리뷰트들 분류
        (
            "기본 정보",  # 기본 정보
            {
                "fields": (
                    "travel",
                    "name",
                )
            },
        ),
        (
            "위치 정보",  # 기본 정보
            {
                "fields": (
                    "latitude",
                    "longitude",
                )
            },
        ),
    )
    list_display = (  # 메인 화면에서 해당 애트리뷰트들 보이기
        "travel",
        "name",
        "latitude",
        "longitude",
        "created_at",
        "updated_at",
    )
    ordering = ("travel", "name")  # 해당 애트리뷰트들로 순서
