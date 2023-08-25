from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from visualizationapp.models import Energy,EnergyProject

''' first try
@admin.register(Energy)
class EnergyAdmin(ImportExportModelAdmin):
     list_display = ("end_year","intensity","sector","topic","insight","url","region","start_year","impact","added",
                     "published","country","relevance","pestle","source","title","likelihood")
     pass
'''

''' second try
class EnergyResources(resources.ModelResource):
    class Meta:
        model=Energy

class EnergyAdmin(ImportExportModelAdmin):
    resource_class=EnergyResources

admin.site.register(Energy, EnergyAdmin)   '''  


from .models import Energy
    
class EnergyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
        
admin.site.register(Energy, EnergyAdmin)



from .models import EnergyProject
    
class EnergyProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
        
admin.site.register(EnergyProject, EnergyProjectAdmin)