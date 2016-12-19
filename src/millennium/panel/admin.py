from django.contrib import admin
from django.contrib.auth.models import Group
from millennium.panel.models import *
from suit import apps
from suit.sortables import SortableStackedInline
# Register your models here.

admin.site.site_title = 'Millennium Panel'
admin.site.site_header = 'Millennium Panel'
admin.site.index_title = 'Administration'

class NCCTermParmsAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('name', 'datapac_num', 'alt_datapac_num', 'cad_id', 'cpe_id')

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

class InstallParmsAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('name',)

    def get_queryset(self, request):
        return InstallParms.objects.filter(tenant=request.session['tenant'])

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(InstallParmsAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and obj.tenant != int(request.session['tenant']) and request.user.groups.filter(id=obj.tenant.id).exists() != True:
           return False
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.tenant = Group.objects.get(id=request.session['tenant'])
        obj.save()

class FconfigOptsAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('name',)

    def get_queryset(self, request):
        return FconfigOpts.objects.filter(tenant=request.session['tenant'])

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(FconfigOptsAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and obj.tenant != int(request.session['tenant']) and request.user.groups.filter(id=obj.tenant.id).exists() != True:
           return False
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.tenant = Group.objects.get(id=request.session['tenant'])
        obj.save()

class CoinValDefsInline(SortableStackedInline):
    model = CoinValDefs
    sortable = 'order'
    suit_classes = 'suit-tab suit-tab-cities'
    suit_form_inlines_hide_original = True
    min_num = 16
    max_num = 16

    def has_delete_permission(self, request, obj=None):
        return False

class CoinValTableAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('name',)
    inlines = (CoinValDefsInline,)

    def get_queryset(self, request):
        return CoinValTable.objects.filter(tenant=request.session['tenant'])

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(CoinValTableAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and obj.tenant != int(request.session['tenant']) and request.user.groups.filter(id=obj.tenant.id).exists() != True:
           return False
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.tenant = Group.objects.get(id=request.session['tenant'])
        obj.save()

class CardDefsInline(SortableStackedInline):
    model = CardDefs
    sortable = 'order'
    suit_classes = 'suit-tab suit-tab-cities'
    suit_form_inlines_hide_original = True
    max_num = 32

class CardTableAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('name',)
    inlines = (CardDefsInline,)

    def get_queryset(self, request):
        return CardTable.objects.filter(tenant=request.session['tenant'])

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(CardTableAdmin, self).has_change_permission(request, obj)
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
admin.site.register(InstallParms, InstallParmsAdmin)
admin.site.register(FconfigOpts, FconfigOptsAdmin)
admin.site.register(CoinValTable, CoinValTableAdmin)
admin.site.register(CardTable, CardTableAdmin)
