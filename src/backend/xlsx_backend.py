from base_backend import BaseBackend
from openpyxl import load_workbook
from src.item import Item

class XlsxBackend(BaseBackend):
    def __init__(self, path):
        self.path = path

    def load(self):
        ws = load_workbook(self.path)['Engineering']
        values =  ws.values
        headers = tuple(self.__column_name_to_item_field(header) for header in next(values))
        dicts = [dict(zip(headers, row)) for row in values]
        for attrs in dicts:
            del attrs[None]
        return [Item(**attrs) for attrs in dicts if attrs['name']]

    @property
    def __item_mapping(self):
        return {'Name': 'name',
                'Old Blueprint Code': 'old_recipe_code',
                'New Blueprint Code': 'new_recipe_code',
                'Item Code': 'item_code',
                'List': 'tier',
                'Effect': 'effect',
                'EWP': 'wp_cost',
                'Research Cost': 'research_cost',
                'Compiled Materials': 'material_cost',
                'Maintenance': 'maintenance_duration',
                'Maintenance EWP': 'maintenance_wp',
                'Maintenance Components': 'maintenance_materials',
                }

    def __column_name_to_item_field(self, column_name):
        return self.__item_mapping.get(column_name, None)
