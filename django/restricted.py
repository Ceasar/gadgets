from django.contrib import admin


#Django's admin model doesn't user super, so this is a little hacky.

class Restricted(object):
    '''
    A mix-in to speed up admin authentication functions.

    To use, override the following fields:
    -declared_fieldsets should not be overriden.
    
    -parent should refer to the parent class.
    -cls_fieldsets should the fieldsets relevant to the class
    -cls_restricted should be fieldsets relevant to the class that should only
        be shown to superusers.

    (cls_fieldsets and cls_restricted should be formatted like Django fieldsets
        and parent should be a ModelAdmin.)
    '''

    declared_fieldsets = None

    parent = None
    cls_fieldsets = None
    cls_restricted = None

    @classmethod
    def inherit_fieldsets(cls):
        '''Get all inherited fieldsets.'''
        fieldsets = tuple()
        if cls.parent:
            fieldsets += cls.parent.inherit_fieldsets()
        if cls.cls_fieldsets:
            fieldsets += cls.cls_fieldsets
        return fieldsets

    @classmethod
    def inherit_restricted(cls):
        '''Get all inherited restricted fields.'''
        restricted = tuple()
        if cls.parent:
            restricted += cls.parent.inherit_restricted()
        if cls.cls_restricted:
            restricted += cls.cls_restricted
        return restricted
                
    def get_fieldsets(self, request, obj=None):
        '''Get the fieldsets to display based on the user.'''
        fieldsets = self.inherit_fieldsets()
        if request.user.is_superuser:
            fieldsets += self.inherit_restricted()
        return fieldsets

    def get_form(self, request, obj=None, **kwargs):
        self.declared_fieldsets = self.get_fieldsets(request, obj)
        return admin.ModelAdmin.get_form(self, request, obj)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser: 
            obj.merchant = request.user.get_profile().merchant
        obj.save()
