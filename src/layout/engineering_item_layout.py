from pdf_form_layout import PdfFormLayout

class EngineeringItemLayout(PdfFormLayout):
    max_items = 5
    form_file = "data/Engineering Items.pdf"

    @classmethod
    def _item_to_attrs(cls, index, item):
        return {'Item Name {0}'.format(index+1): item.name,
                'Item Code {0}'.format(index+1): item.item_code,
                'Effect {0}'.format(index+1): item.effect,
                'WP Cost {0}'.format(index+1): int(item.wp_cost),
                'Maintenance Resources {0}'.format(index+1): item.maintenance_materials
                }