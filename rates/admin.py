from django.contrib import admin
from models import Area,Country,Currency,Operator,Rate,Target

class AreaAdmin(admin.ModelAdmin):
    save_on_top = True        
    list_display = ('area_country', 'area_code', 'area_name')
    list_display_links = ('area_country', 'area_code', 'area_name')
    list_filter = ('area_country',)
    search_fields = ('area_country__country_code', 'area_code', 'area_country__country_name', 'area_name')
    list_select_related = True
    save_as = False
        
        # FIXME: 
        # date_hierarchy = 'name'
        
    #     def display_area_code(self):
    #         if (self.area_code==''):
    #             str_format =  '%d%s %s %s'          
    #         else:
    #             str_format = '%d%s %s, %s'
                
    #         return str_format  % (self.area_country.country_code, self.area_code, 
    #                                          self.area_country.country_name, self.area_name)
    #     display_area_code.short_description = _('Area code')

    
class CountryAdmin(admin.ModelAdmin):
    save_on_top = True        
    #        fields = (
    #            (None, {'fields': ('country_code', 'country_name')}),
    #           )
    list_display = ('country_code', 'country_name')
    list_display_links = ('country_code', 'country_name')        
    #list_filter = ('code', 'name')
    search_fields = ('country_code', 'country_name')

    
class CurrencyAdmin(admin.ModelAdmin):
    save_on_top = True

class OperatorAdmin(admin.ModelAdmin):
    #list_filter = ('name',)
    search_fields = ('operator_name',)
 
    
class RateAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('rate_operator', 'display_rate_code', 'rate_price', 'rate_quality', 
                        'rate_start_date', 'rate_end_date', 'rate_currency')
    
    list_display_links = ('rate_operator', 'display_rate_code', 'rate_price', 'rate_quality', 
                                'rate_start_date', 'rate_end_date', 'rate_currency')
    
    list_filter = ('rate_operator', 'rate_quality','rate_start_date', 'rate_end_date')
    search_fields = ('^rate_code__area_country__country_code',
                            '^rate_code__area_code',
                            'rate_code__area_country__country_name',
                            'rate_code_name',
                            'rate_code__area_name')
    list_select_related = True
    save_as = False

    
class TargetAdmin(admin.ModelAdmin):
    save_on_top = True        
    list_display = ('target_operator',
                         'display_target_code',
                         'target_price',
                         'target_currency',
                         'target_volume')
    list_display_links = ('target_operator',
                               'display_target_code',
                               'target_price',
                               'target_currency',
                               'target_volume')
    list_filter = ('target_operator',)
    search_fields = ('^target_code__area_country__country_code', 
                          '^target_code__area_code',
                          'target_code__area_country__country_name',
                          'target_code__area_name')
        
    list_select_related = True
    save_as = False
    
admin.site.register(Area, AreaAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Target, TargetAdmin)



