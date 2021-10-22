from rest_framework import permissions

class isStaffOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # Read-only permissions are allowed for any request 
        if request.method in permissions.SAFE_METHODS:
             return True
        
        # Write permissions are only allowed to staff
        return request.user.is_staff