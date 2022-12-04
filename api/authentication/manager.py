from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Permission


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Почта не была передана!')

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        if user.role == "organization":
            user.is_staff = True
            
            user.user_permissions.set(
                Permission.objects.filter(
                    content_type_id__in=(10, 16, 17, 18)
                ),
            )
    
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', "staff")

        return self.create_user(email, password, **extra_fields)
