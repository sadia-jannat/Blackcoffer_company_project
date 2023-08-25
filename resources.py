from import_export import resources
from visualizationapp.models import Energy,EnergyProject
 
class EnergyResource(resources.ModelResource):
    class Meta:
        model = Energy  

class EnergyProjectResource(resources.ModelResource):
    class Meta:
        model = EnergyProject             