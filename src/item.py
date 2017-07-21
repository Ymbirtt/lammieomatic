class Item(object):
    """Describes a single item from the item book, has the following attributes:
        Old recipe code
        New recipe code
        Item code
        Name
        Effect
        Tier
        WP cost
        Research Cost
        Material Cost
        Maintenance duration
        Maintenance WP
        Maintenance materials
        """
    def __init__(self, old_recipe_code, new_recipe_code, item_code, name, effect, tier, wp_cost, research_cost, material_cost, maintenance_duration, maintenance_wp, maintenance_materials):
        self.old_recipe_code = old_recipe_code
        self.new_recipe_code = new_recipe_code
        self.item_code = item_code
        self.name = name
        self.effect = effect
        self.tier = tier
        self.wp_cost = wp_cost
        self.research_cost = research_cost
        self.material_cost = material_cost
        self.maintenance_duration = maintenance_duration
        self.maintenance_wp = maintenance_wp
        self.maintenance_materials = maintenance_materials

    def __str__(self):
        return "Item {0}: {1}".format(self.item_code, self.name)


