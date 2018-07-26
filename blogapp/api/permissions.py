from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
        message = "U must be owner of this field"

        def has_object_permission(self, request, view, obj):
            my_safe_method = ['PUT']
            if request.method in self.my_safe_method:
                return True
            return obj.user == request.user


