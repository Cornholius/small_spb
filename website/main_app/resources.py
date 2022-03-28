from import_export import resources
from .models import MeterReadings


class MeterReadingsResource(resources.ModelResource):

    class Meta:
        model = MeterReadings
