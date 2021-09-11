from django.contrib import admin
from .models import Category, Sub_Category, Item, AboutUs, Course, Contact
from django.contrib import messages


class TestAdminPermissions(admin.ModelAdmin):
    
    def has_delete_permission(self, request, obj=None):

        # if obj != None and request.POST.get('action') =='delete_selected':
        #     messages.add_message(request, messages.ERROR,(
        #         "I really hope you are sure about this!"
        #     ))
        if request.user.groups.filter(name='admin').exists():
            return True
        return obj

    def has_add_permission(self, request):
        if request.user.groups.filter(name='admin').exists():
            return True
        return False
        
    
    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='admin').exists():
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.groups.filter(name='customer').exists():
            return True
        return obj

admin.site.register(Category, TestAdminPermissions)
admin.site.register(Sub_Category, TestAdminPermissions)
admin.site.register(Item, TestAdminPermissions)
admin.site.register(AboutUs, TestAdminPermissions)
admin.site.register(Contact, TestAdminPermissions)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(Course, CourseAdmin)