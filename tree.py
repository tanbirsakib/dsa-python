class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode('Electronics')
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Dell'))

    cell_phone = TreeNode('Cell Phone')
    cell_phone.add_child(TreeNode('iPhone'))
    cell_phone.add_child(TreeNode('Samsung'))
    cell_phone.add_child(TreeNode('Redmi'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Sony'))
    tv.add_child(TreeNode('Philips'))
    tv.add_child(TreeNode('Nippon'))
    
    

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(tv)

    root.print_tree()
if __name__=='__main__':
    build_product_tree()    
