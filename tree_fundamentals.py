# have to implement a basic NODE class. 

# what should the constructor take as parameter ? 
# How will you store the list of children ? 
# How will you add a child to the node ? 
# How can you tell if a node is a laef (has no children) ?

class Node :
    def __init__(self, value) -> None:
        self.value = value
        self.children = []
        
    def add_child(self, child_node) -> None:
        self.children.append(child_node)
        
    def is_leaf(self) -> bool:
        # I have to check if it's a leaf. to check if it's a leaf I have to do what ? I have to see if it has any children
        return len(self.children) == 0
    
    def __str__(self) -> str:
        return f"Node({self.value})"
    
    def display_tree(self, indent=0) -> None:
        # just a function to print child nodes and distinguish them based on intendations!
        print(" "*indent + self.value)
        for node in self.children :
            node.display_tree(indent + 1)
        
    

if __name__ == "__main__":
    
    root_node = Node("Root")
    a_node = Node("A")
    b_node = Node("B")
    c_node = Node("C")
    d_node = Node("D")
    e_node = Node("E")
    
    root_node.add_child(a_node)
    root_node.add_child(b_node)
    a_node.add_child(c_node)
    b_node.add_child(d_node)
    b_node.add_child(e_node)
    
    print(f"Root: {root_node}")
    print(f"Root is leaf: {root_node.is_leaf()}")
    print(f"C is leaf: {c_node.is_leaf()}")
    print(f"Root has {len(root_node.children)} children")
    print(f"A has {len(a_node.children)} children")
    root_node.display_tree()
        
        
        
    