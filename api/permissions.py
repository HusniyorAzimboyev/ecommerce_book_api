from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to work with orders only for owners of those orders
    or just read it
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and obj.owner == request.user

class IsStaff(permissions.BasePermission):
    """
    custom permission to allow staff members to do CRUD with object
    """

    def has_permission(self, request, view):
        if request in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
