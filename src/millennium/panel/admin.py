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
    extra = 0
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

class RateDefsInline(SortableStackedInline):
    model = RateDefs
    sortable = 'order'
    suit_classes = 'suit-tab suit-tab-cities'
    suit_form_inlines_hide_original = True
    extra = 0
    max_num = 128

class RateTableAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('name',)
    inlines = (RateDefsInline,)

    def get_queryset(self, request):
        return RateTable.objects.filter(tenant=request.session['tenant'])

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(RateTableAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and obj.tenant != int(request.session['tenant']) and request.user.groups.filter(id=obj.tenant.id).exists() != True:
           return False
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.tenant = Group.objects.get(id=request.session['tenant'])
        obj.save()

class NPANXXTableAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('name',)

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['npa']
        }),
        ('200-209', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_200', 'npa_201', 'npa_202', 'npa_203', 'npa_204', 'npa_205', 'npa_206', 'npa_207', 'npa_208', 'npa_209'],
        }),
        ('210-219', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_210', 'npa_211', 'npa_212', 'npa_213', 'npa_214', 'npa_215', 'npa_216', 'npa_217', 'npa_218', 'npa_219'],
        }),
        ('220-229', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_220', 'npa_221', 'npa_222', 'npa_223', 'npa_224', 'npa_225', 'npa_226', 'npa_227', 'npa_228', 'npa_229'],
        }),
        ('230-239', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_230', 'npa_231', 'npa_232', 'npa_233', 'npa_234', 'npa_235', 'npa_236', 'npa_237', 'npa_238', 'npa_239'],
        }),
        ('240-249', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_240', 'npa_241', 'npa_242', 'npa_243', 'npa_244', 'npa_245', 'npa_246', 'npa_247', 'npa_248', 'npa_249'],
        }),
        ('250-259', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_250', 'npa_251', 'npa_252', 'npa_253', 'npa_254', 'npa_255', 'npa_256', 'npa_257', 'npa_258', 'npa_259'],
        }),
        ('260-269', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_260', 'npa_261', 'npa_262', 'npa_263', 'npa_264', 'npa_265', 'npa_266', 'npa_267', 'npa_268', 'npa_269'],
        }),
        ('270-279', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_270', 'npa_271', 'npa_272', 'npa_273', 'npa_274', 'npa_275', 'npa_276', 'npa_277', 'npa_278', 'npa_279'],
        }),
        ('280-289', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_280', 'npa_281', 'npa_282', 'npa_283', 'npa_284', 'npa_285', 'npa_286', 'npa_287', 'npa_288', 'npa_289'],
        }),
        ('290-299', {
            'classes': ('suit-tab suit-tab-200-299',),
            'fields': ['npa_290', 'npa_291', 'npa_292', 'npa_293', 'npa_294', 'npa_295', 'npa_296', 'npa_297', 'npa_298', 'npa_299'],
        }),
        ('300-309', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_300', 'npa_301', 'npa_302', 'npa_303', 'npa_304', 'npa_305', 'npa_306', 'npa_307', 'npa_308', 'npa_309'],
        }),
        ('310-319', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_310', 'npa_311', 'npa_312', 'npa_313', 'npa_314', 'npa_315', 'npa_316', 'npa_317', 'npa_318', 'npa_319'],
        }),
        ('320-329', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_320', 'npa_321', 'npa_322', 'npa_323', 'npa_324', 'npa_325', 'npa_326', 'npa_327', 'npa_328', 'npa_329'],
        }),
        ('330-339', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_330', 'npa_331', 'npa_332', 'npa_333', 'npa_334', 'npa_335', 'npa_336', 'npa_337', 'npa_338', 'npa_339'],
        }),
        ('340-349', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_340', 'npa_341', 'npa_342', 'npa_343', 'npa_344', 'npa_345', 'npa_346', 'npa_347', 'npa_348', 'npa_349'],
        }),
        ('350-359', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_350', 'npa_351', 'npa_352', 'npa_353', 'npa_354', 'npa_355', 'npa_356', 'npa_357', 'npa_358', 'npa_359'],
        }),
        ('360-369', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_360', 'npa_361', 'npa_362', 'npa_363', 'npa_364', 'npa_365', 'npa_366', 'npa_367', 'npa_368', 'npa_369'],
        }),
        ('370-379', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_370', 'npa_371', 'npa_372', 'npa_373', 'npa_374', 'npa_375', 'npa_376', 'npa_377', 'npa_378', 'npa_379'],
        }),
        ('380-389', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_380', 'npa_381', 'npa_382', 'npa_383', 'npa_384', 'npa_385', 'npa_386', 'npa_387', 'npa_388', 'npa_389'],
        }),
        ('390-399', {
            'classes': ('suit-tab suit-tab-300-399',),
            'fields': ['npa_390', 'npa_391', 'npa_392', 'npa_393', 'npa_394', 'npa_395', 'npa_396', 'npa_397', 'npa_398', 'npa_399'],
        }),
        ('400-409', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_400', 'npa_401', 'npa_402', 'npa_403', 'npa_404', 'npa_405', 'npa_406', 'npa_407', 'npa_408', 'npa_409'],
        }),
        ('410-419', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_410', 'npa_411', 'npa_412', 'npa_413', 'npa_414', 'npa_415', 'npa_416', 'npa_417', 'npa_418', 'npa_419'],
        }),
        ('420-429', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_420', 'npa_421', 'npa_422', 'npa_423', 'npa_424', 'npa_425', 'npa_426', 'npa_427', 'npa_428', 'npa_429'],
        }),
        ('430-439', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_430', 'npa_431', 'npa_432', 'npa_433', 'npa_434', 'npa_435', 'npa_436', 'npa_437', 'npa_438', 'npa_439'],
        }),
        ('440-449', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_440', 'npa_441', 'npa_442', 'npa_443', 'npa_444', 'npa_445', 'npa_446', 'npa_447', 'npa_448', 'npa_449'],
        }),
        ('450-459', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_450', 'npa_451', 'npa_452', 'npa_453', 'npa_454', 'npa_455', 'npa_456', 'npa_457', 'npa_458', 'npa_459'],
        }),
        ('460-469', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_460', 'npa_461', 'npa_462', 'npa_463', 'npa_464', 'npa_465', 'npa_466', 'npa_467', 'npa_468', 'npa_469'],
        }),
        ('470-479', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_470', 'npa_471', 'npa_472', 'npa_473', 'npa_474', 'npa_475', 'npa_476', 'npa_477', 'npa_478', 'npa_479'],
        }),
        ('480-489', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_480', 'npa_481', 'npa_482', 'npa_483', 'npa_484', 'npa_485', 'npa_486', 'npa_487', 'npa_488', 'npa_489'],
        }),
        ('490-499', {
            'classes': ('suit-tab suit-tab-400-499',),
            'fields': ['npa_490', 'npa_491', 'npa_492', 'npa_493', 'npa_494', 'npa_495', 'npa_496', 'npa_497', 'npa_498', 'npa_499'],
        }),
        ('500-509', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_500', 'npa_501', 'npa_502', 'npa_503', 'npa_504', 'npa_505', 'npa_506', 'npa_507', 'npa_508', 'npa_509'],
        }),
        ('510-519', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_510', 'npa_511', 'npa_512', 'npa_513', 'npa_514', 'npa_515', 'npa_516', 'npa_517', 'npa_518', 'npa_519'],
        }),
        ('520-529', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_520', 'npa_521', 'npa_522', 'npa_523', 'npa_524', 'npa_525', 'npa_526', 'npa_527', 'npa_528', 'npa_529'],
        }),
        ('530-539', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_530', 'npa_531', 'npa_532', 'npa_533', 'npa_534', 'npa_535', 'npa_536', 'npa_537', 'npa_538', 'npa_539'],
        }),
        ('540-549', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_540', 'npa_541', 'npa_542', 'npa_543', 'npa_544', 'npa_545', 'npa_546', 'npa_547', 'npa_548', 'npa_549'],
        }),
        ('550-559', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_550', 'npa_551', 'npa_552', 'npa_553', 'npa_554', 'npa_555', 'npa_556', 'npa_557', 'npa_558', 'npa_559'],
        }),
        ('560-569', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_560', 'npa_561', 'npa_562', 'npa_563', 'npa_564', 'npa_565', 'npa_566', 'npa_567', 'npa_568', 'npa_569'],
        }),
        ('570-579', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_570', 'npa_571', 'npa_572', 'npa_573', 'npa_574', 'npa_575', 'npa_576', 'npa_577', 'npa_578', 'npa_579'],
        }),
        ('580-589', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_580', 'npa_581', 'npa_582', 'npa_583', 'npa_584', 'npa_585', 'npa_586', 'npa_587', 'npa_588', 'npa_589'],
        }),
        ('590-599', {
            'classes': ('suit-tab suit-tab-500-599',),
            'fields': ['npa_590', 'npa_591', 'npa_592', 'npa_593', 'npa_594', 'npa_595', 'npa_596', 'npa_597', 'npa_598', 'npa_599'],
        }),
        ('600-609', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_600', 'npa_601', 'npa_602', 'npa_603', 'npa_604', 'npa_605', 'npa_606', 'npa_607', 'npa_608', 'npa_609'],
        }),
        ('610-619', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_610', 'npa_611', 'npa_612', 'npa_613', 'npa_614', 'npa_615', 'npa_616', 'npa_617', 'npa_618', 'npa_619'],
        }),
        ('620-629', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_620', 'npa_621', 'npa_622', 'npa_623', 'npa_624', 'npa_625', 'npa_626', 'npa_627', 'npa_628', 'npa_629'],
        }),
        ('630-639', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_630', 'npa_631', 'npa_632', 'npa_633', 'npa_634', 'npa_635', 'npa_636', 'npa_637', 'npa_638', 'npa_639'],
        }),
        ('640-649', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_640', 'npa_641', 'npa_642', 'npa_643', 'npa_644', 'npa_645', 'npa_646', 'npa_647', 'npa_648', 'npa_649'],
        }),
        ('650-659', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_650', 'npa_651', 'npa_652', 'npa_653', 'npa_654', 'npa_655', 'npa_656', 'npa_657', 'npa_658', 'npa_659'],
        }),
        ('660-669', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_660', 'npa_661', 'npa_662', 'npa_663', 'npa_664', 'npa_665', 'npa_666', 'npa_667', 'npa_668', 'npa_669'],
        }),
        ('670-679', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_670', 'npa_671', 'npa_672', 'npa_673', 'npa_674', 'npa_675', 'npa_676', 'npa_677', 'npa_678', 'npa_679'],
        }),
        ('680-689', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_680', 'npa_681', 'npa_682', 'npa_683', 'npa_684', 'npa_685', 'npa_686', 'npa_687', 'npa_688', 'npa_689'],
        }),
        ('690-699', {
            'classes': ('suit-tab suit-tab-600-699',),
            'fields': ['npa_690', 'npa_691', 'npa_692', 'npa_693', 'npa_694', 'npa_695', 'npa_696', 'npa_697', 'npa_698', 'npa_699'],
        }),
        ('700-709', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_700', 'npa_701', 'npa_702', 'npa_703', 'npa_704', 'npa_705', 'npa_706', 'npa_707', 'npa_708', 'npa_709'],
        }),
        ('710-719', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_710', 'npa_711', 'npa_712', 'npa_713', 'npa_714', 'npa_715', 'npa_716', 'npa_717', 'npa_718', 'npa_719'],
        }),
        ('720-729', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_720', 'npa_721', 'npa_722', 'npa_723', 'npa_724', 'npa_725', 'npa_726', 'npa_727', 'npa_728', 'npa_729'],
        }),
        ('730-739', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_730', 'npa_731', 'npa_732', 'npa_733', 'npa_734', 'npa_735', 'npa_736', 'npa_737', 'npa_738', 'npa_739'],
        }),
        ('740-749', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_740', 'npa_741', 'npa_742', 'npa_743', 'npa_744', 'npa_745', 'npa_746', 'npa_747', 'npa_748', 'npa_749'],
        }),
        ('750-759', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_750', 'npa_751', 'npa_752', 'npa_753', 'npa_754', 'npa_755', 'npa_756', 'npa_757', 'npa_758', 'npa_759'],
        }),
        ('760-769', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_760', 'npa_761', 'npa_762', 'npa_763', 'npa_764', 'npa_765', 'npa_766', 'npa_767', 'npa_768', 'npa_769'],
        }),
        ('770-779', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_770', 'npa_771', 'npa_772', 'npa_773', 'npa_774', 'npa_775', 'npa_776', 'npa_777', 'npa_778', 'npa_779'],
        }),
        ('780-789', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_780', 'npa_781', 'npa_782', 'npa_783', 'npa_784', 'npa_785', 'npa_786', 'npa_787', 'npa_788', 'npa_789'],
        }),
        ('790-799', {
            'classes': ('suit-tab suit-tab-700-799',),
            'fields': ['npa_790', 'npa_791', 'npa_792', 'npa_793', 'npa_794', 'npa_795', 'npa_796', 'npa_797', 'npa_798', 'npa_799'],
        }),
        ('800-809', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_800', 'npa_801', 'npa_802', 'npa_803', 'npa_804', 'npa_805', 'npa_806', 'npa_807', 'npa_808', 'npa_809'],
        }),
        ('810-819', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_810', 'npa_811', 'npa_812', 'npa_813', 'npa_814', 'npa_815', 'npa_816', 'npa_817', 'npa_818', 'npa_819'],
        }),
        ('820-829', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_820', 'npa_821', 'npa_822', 'npa_823', 'npa_824', 'npa_825', 'npa_826', 'npa_827', 'npa_828', 'npa_829'],
        }),
        ('830-839', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_830', 'npa_831', 'npa_832', 'npa_833', 'npa_834', 'npa_835', 'npa_836', 'npa_837', 'npa_838', 'npa_839'],
        }),
        ('840-849', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_840', 'npa_841', 'npa_842', 'npa_843', 'npa_844', 'npa_845', 'npa_846', 'npa_847', 'npa_848', 'npa_849'],
        }),
        ('850-859', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_850', 'npa_851', 'npa_852', 'npa_853', 'npa_854', 'npa_855', 'npa_856', 'npa_857', 'npa_858', 'npa_859'],
        }),
        ('860-869', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_860', 'npa_861', 'npa_862', 'npa_863', 'npa_864', 'npa_865', 'npa_866', 'npa_867', 'npa_868', 'npa_869'],
        }),
        ('870-879', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_870', 'npa_871', 'npa_872', 'npa_873', 'npa_874', 'npa_875', 'npa_876', 'npa_877', 'npa_878', 'npa_879'],
        }),
        ('880-889', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_880', 'npa_881', 'npa_882', 'npa_883', 'npa_884', 'npa_885', 'npa_886', 'npa_887', 'npa_888', 'npa_889'],
        }),
        ('890-899', {
            'classes': ('suit-tab suit-tab-800-899',),
            'fields': ['npa_890', 'npa_891', 'npa_892', 'npa_893', 'npa_894', 'npa_895', 'npa_896', 'npa_897', 'npa_898', 'npa_899'],
        }),
        ('900-909', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_900', 'npa_901', 'npa_902', 'npa_903', 'npa_904', 'npa_905', 'npa_906', 'npa_907', 'npa_908', 'npa_909'],
        }),
        ('910-919', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_910', 'npa_911', 'npa_912', 'npa_913', 'npa_914', 'npa_915', 'npa_916', 'npa_917', 'npa_918', 'npa_919'],
        }),
        ('920-929', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_920', 'npa_921', 'npa_922', 'npa_923', 'npa_924', 'npa_925', 'npa_926', 'npa_927', 'npa_928', 'npa_929'],
        }),
        ('930-939', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_930', 'npa_931', 'npa_932', 'npa_933', 'npa_934', 'npa_935', 'npa_936', 'npa_937', 'npa_938', 'npa_939'],
        }),
        ('940-949', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_940', 'npa_941', 'npa_942', 'npa_943', 'npa_944', 'npa_945', 'npa_946', 'npa_947', 'npa_948', 'npa_949'],
        }),
        ('950-959', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_950', 'npa_951', 'npa_952', 'npa_953', 'npa_954', 'npa_955', 'npa_956', 'npa_957', 'npa_958', 'npa_959'],
        }),
        ('960-969', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_960', 'npa_961', 'npa_962', 'npa_963', 'npa_964', 'npa_965', 'npa_966', 'npa_967', 'npa_968', 'npa_969'],
        }),
        ('970-979', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_970', 'npa_971', 'npa_972', 'npa_973', 'npa_974', 'npa_975', 'npa_976', 'npa_977', 'npa_978', 'npa_979'],
        }),
        ('980-989', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_980', 'npa_981', 'npa_982', 'npa_983', 'npa_984', 'npa_985', 'npa_986', 'npa_987', 'npa_988', 'npa_989'],
        }),
        ('990-999', {
            'classes': ('suit-tab suit-tab-900-999',),
            'fields': ['npa_990', 'npa_991', 'npa_992', 'npa_993', 'npa_994', 'npa_995', 'npa_996', 'npa_997', 'npa_998', 'npa_999'],
        }),
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('200-299', '200-299'),
        ('300-399', '300-399'),
        ('400-499', '400-499'),
        ('500-599', '500-599'),
        ('600-699', '600-699'),
        ('700-799', '700-799'),
        ('800-899', '800-899'),
        ('900-999', '900-999'),
    )

    def get_queryset(self, request):
        return NPANXXTable.objects.filter(tenant=request.session['tenant'])

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(NPANXXTableAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and obj.tenant != int(request.session['tenant']) and request.user.groups.filter(id=obj.tenant.id).exists() != True:
           return False
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.tenant = Group.objects.get(id=request.session['tenant'])
        obj.save()

class terminalAdmin(admin.ModelAdmin):
    exclude = ('tenant',)
    list_display = ('term_id', 'NCCTermParms', 'InstallParms', 'FconfigOpts', 'CoinValTable', 'CardTable', 'RateTable')

    def get_queryset(self, request):
        return terminal.objects.filter(tenant=request.session['tenant'])

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(terminalAdmin, self).has_change_permission(request, obj)
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
admin.site.register(RateTable, RateTableAdmin)
admin.site.register(NPANXXTable, NPANXXTableAdmin)
admin.site.register(terminal, terminalAdmin)
