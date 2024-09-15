from rest_framework import permissions

# This custom permission class restricts a user’s ability to modify data by implementing object-level permissions.
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile """
    def has_object_permission(self,request,view,obj):

        if request.method in permissions.SAFE_METHODS:
            """safe method allow you to retrive data not to destruct data here we allow all users to get or review not to delete or update"""
            return True
        """ here we check if the user is updating his own profile otherwise the permission will be denied """
        return obj.id == request.user.id

"""

def has_object_permission(self, request, view, obj):

This method is called to determine whether the requesting user has permission to interact with the object (obj) in question.
It takes in three arguments:
request: The HTTP request being made (e.g., a PATCH or PUT request).
view: The view that is handling the request.
obj: The object (in this case, a user profile) that the user is attempting to access or modify.

return obj.id == request.user.id:

For unsafe methods (like PUT, PATCH, or DELETE, which modify data), the permission logic ensures that the user can only modify their own profile.
It checks whether the id of the object (profile) matches the id of the authenticated user making the request (request.user.id).
If the two IDs match, permission is granted, allowing the user to modify their own profile.
If the IDs do not match (i.e., the user is trying to modify someone else’s profile), permission is denied (False).


"""

class PostOwnStatus(permissions.BasePermission):
    """ Allow users to update their own status """
    def has_object_permission(self, request, view, obj):
        """ Checks the user that are trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
        """ that's checking if the user profile id is the same as the id comming in the request to update the status"""


