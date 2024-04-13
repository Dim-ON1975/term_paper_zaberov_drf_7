from rest_framework.permissions import BasePermission


class IsCreator(BasePermission):
    """Права создателя (владельца)"""
    message = 'Доступ запрещен'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.creator:
            return True
        return False
