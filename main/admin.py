from django.contrib import admin
from .models import UserFirst, UserReview


# Register your models here.
class ser(admin.ModelAdmin):
    list_display = ("name", "phone",)

admin.site.register(UserFirst, ser)


class usr(admin.ModelAdmin):

    list_display_user = ("name", "phone",)

admin.site.register(UserReview, usr)