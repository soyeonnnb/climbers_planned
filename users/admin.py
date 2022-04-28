from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    """User Admin Definition"""

    fieldsets = (  # User 애트리뷰트들 분류
        (
            "기본 정보",  # 기본 정보
            {"fields": ("email", "name", "nickname")},
        ),
        (
            "기타",  # 추가 정보
            {
                "fields": ("is_staff", "is_active", "is_superuser"),
            },
        ),
    )
    list_display = (  # 메인 화면에서 해당 애트리뷰트들 보이기
        "email",
        "name",
        "nickname",
        "is_staff",
        "created_at",
    )
    ordering = ("email", "nickname", "name", "is_staff", "created_at")  # 해당 애트리뷰트들로 순서
    list_filter = ("is_staff",)  # 해당 애트리뷰트로 filtering 가능
