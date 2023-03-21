from rest_framework.permissions import BasePermission

class HasModulePermission(BasePermission):
    
    # def has_permission(self, request, view):
    #     module_name = view.module_name 
    #     user = request.user
    #     if user.is_authenticated and (user.is_superuser or (user.company and user.modules.filter(name=module_name).exists())):
    #         return True
    #     else:
    #         return False

    def has_permission(self, request, view):
        module_name = view.module_name 
        user = request.user
        if not user.is_authenticated:
            return False
        elif user.is_superuser:
            return True
        elif user.company and user.modules.filter(name=module_name).exists():
            return True
        else:
            return False