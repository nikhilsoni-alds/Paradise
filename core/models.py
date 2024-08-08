from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.contrib.auth.models import BaseUserManager
# Create your models here.
 

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)



class User(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255,unique=True)
    username = models.CharField(max_length=255,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    # role=models.ForeignKey(Role,on_delete=models.SET_NULL,related_name="users",db_index=True,null=True,blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Use a custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Use a custom related_name
        blank=True
    )

    objects = UserManager()
    

    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username','first_name','last_name']

    class Meta:
        permissions = (
            ("can_import_users", "Can import users"),
            ("can_export_users", "Can export users")
        )

    def natural_key(self):
        return (self.email,)
    
    def has_perm(self, perm, obj=None):
        print("has_perm",self.user_permissions.all())
        # If the user is a superuser, they have all permissions
        if self.is_superuser:
            return True
        
        # Check if the user has the specified permission directly
        if self.user_permissions.filter(codename=perm.split('.')[-1]).exists():
            return True
        
        # Check if the user has the specified permission through a group
        for group in self.groups.all():
            if group.permissions.filter(codename=perm.split('.')[-1]).exists():
                return True
        
        return False

    def has_module_perms(self, app_label):
        # If the user is a superuser, they have all permissions
        if self.is_superuser:
            return True
        
        # Check if the user has any permissions in the given app_label directly
        if self.user_permissions.filter(content_type__app_label=app_label).exists():
            return True
        
        # Check if the user has any permissions in the given app_label through a group
        for group in self.groups.all():
            if group.permissions.filter(content_type__app_label=app_label).exists():
                return True
        
        return False


