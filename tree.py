class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Example of building a tree (you'll need to adapt this to your data)
def build_tree(data):
    root = TreeNode("Starbucks Stores")
    # Add logic to populate the tree based on city and zip code
    return root
