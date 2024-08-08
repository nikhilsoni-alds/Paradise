 

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from import_export.admin import ImportExportModelAdmin


from .models import User
from .resources import UserResource


class UserAdmin(ImportExportModelAdmin,BaseUserAdmin):
    resource_class = UserResource
    list_display = ('email', 'phone', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'phone', 'username', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'username')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active','groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    def get_readonly_fields(self, request,perm, obj=None):
        readonly_fields = super(UserAdmin, self).get_readonly_fields(request, obj)
        # print(request.user.has_perm('core.can_view_phone'))
        if not request.user.has_perm('core.can_edit_phone'):
            readonly_fields += ('phone',)
        if not request.user.has_perm('core.can_edit_email'):
            readonly_fields += ('email',)
        return readonly_fields

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
        print(request.user.has_perm('core.can_view_phone'))
        if not request.user.has_perm('core.can_view_phone'):
            for fieldset in fieldsets:
                if 'phone' in fieldset[1]['fields']:
                    fieldset[1]['fields'] = tuple(f for f in fieldset[1]['fields'] if f != 'phone')
        if not request.user.has_perm('core.can_view_email'):
            for fieldset in fieldsets:
                if 'email' in fieldset[1]['fields']:
                    fieldset[1]['fields'] = tuple(f for f in fieldset[1]['fields'] if f != 'email')
        return fieldsets

    def has_permission(self, request): 
        return request.user.is_active and request.user.is_staff
    
    def has_import_permission(self, request):
        return request.user.has_perm('core.can_import_users')

    def has_export_permission(self, request):
        return request.user.has_perm('core.can_export_users')


class RoleAdmin(ImportExportModelAdmin):
    list_display=['title','slug']
    prepopulated_fields={'slug':['title']}

admin.site.register(User, UserAdmin)

# admin.site.unregister(Group)
