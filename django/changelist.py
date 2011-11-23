
#Django's admin model doesn't user super, so this is a little hacky.

class ChangeList(object):
    '''
    A mix-in to speed up some common admin changelist functions.

    To use, override the following fields:
    -parent should refer to the parent class.
    -cls_display refers to new list_display fields relevant to the class.
    -cls_editable refers to new list_editable fields relevant to the class.

    (cls_display and cls_editable should be tuples like their corresponding
        Django parts and parent should be a ModelAdmin.)
    '''

    parent = None
    cls_display = None
    cls_editable = None

    #Ought to be a better way to write the next two methods...
    @classmethod
    def inherit_display(cls):
        '''Get all inherited list_display fields.'''
        display = tuple()
        if cls.parent:
            display = cls.parent.inherit_display()
        if cls.cls_display:
            display += cls.cls_display
        return display

    @classmethod
    def inherit_editable(cls):
        '''Get all inherited list_editable fields.'''
        editable = tuple()
        if cls.parent:
            editable += cls.parent.inherit_editable()
        if cls.cls_editable:
            editable += cls.cls_editable
        return editable

    def changelist_view(self, request, extra_context=None):
        self.list_display = self.inherit_display()
        self.list_editable = self.inherit_editable()
        return super(ChangeList, self).changelist_view(request, extra_context)
