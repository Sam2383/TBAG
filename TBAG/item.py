class Item():
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description
        self.inventory = {}

    def item_description(self):
        print(self.description)

