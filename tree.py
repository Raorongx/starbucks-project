import json
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.zip_code = None  

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

class StoreNode(TreeNode):  
    def __init__(self, name, zip_code):
        super().__init__(name)
        self.zip_code = zip_code

def build_tree(data):
    root = TreeNode("Starbucks Stores")
    for store_info in data:
        city_name = store_info['city']
        store_name = store_info['name']
        zip_code = store_info.get('zip_code', 'Unknown') 
        city_node = root.find_child(city_name)
        if not city_node:
            city_node = TreeNode(city_name)
            root.add_child(city_node)

        store_node = StoreNode(store_name, zip_code)
        city_node.add_child(store_node)

    return root


def load_data_from_cache():
    with open('starbucks_locations.json', 'r') as file:
        return json.load(file)
