from django.contrib import admin
from django.contrib.auth.models import Group
from millennium.panel.models import NCCTermParms
# Register your models here.

admin.site.site_title = 'Millennium Panel'
admin.site.site_header = 'Millennium Panel'
admin.site.index_title = 'Administration'

class NCCTermParmsAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('name', 'primaryNCCnumber', 'alternateNCCnumber', 'CADId', 'CPEId')

    def get_queryset(self, request):
        return NCCTermParms.objects.filter(tenant=request.session['tenant'])

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(NCCTermParmsAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and obj.tenant != int(request.session['tenant']) and request.user.groups.filter(id=obj.tenant.id).exists() != True:
           return False
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.tenant = Group.objects.get(id=request.session['tenant'])
        obj.save()

admin.site.register(NCCTermParms, NCCTermParmsAdmin)
