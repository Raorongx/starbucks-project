import json
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def build_tree(data):
    root = TreeNode("Starbucks Stores")
    return root

def load_data_from_cache():
    with open('cache.json', 'r') as file:
        return json.load(file)
