from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from typing import List

from user.models import User
# Register your models here.

class CommonActionsAndList(ImportExportModelAdmin):
    list_display: List[str] = ["created_at"]
    list_filter = [
        "created_at",
        "updated_at",
        "is_active",
    ]

@admin.register(User)
class UserAdmin(CommonActionsAndList):
    list_display=['id', 'name', 'type', 'phone', 'email', 'password', 'gender']

