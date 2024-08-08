from import_export import resources
from .models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')
        export_order = ('id', 'email', 'phone', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')
