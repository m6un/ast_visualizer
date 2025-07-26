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
    
    # traversing the trees 
    # 1. Pre-order traversal (Node -> Children)
    def pre_order_traversal(self, indent=0) -> None:
        # just a function to print child nodes and distinguish them based on intendations!
        print(" "*indent + self.value)
        for node in self.children :
            node.pre_order_traversal(indent + 1)
    
    def post_order_traversal(self, indent=0) -> None:
        for node in self.children :
            node.post_order_traversal(indent + 1)
        
        print(" "*indent + self.value)
        # my guess on how this would be printed in order of printing and descending order of indent : c > a > d > e > b
        
    def level_order_traversal(self) -> None:
        """ 
        we have to implement this using a queue, so the idea is : 
        1. Have a loop running untile the queue is empty, now in each run , push the node's children to the end of the queue and pop the current one. 
        2. Interesting, but the only thing I'm thinking about is, how to print this. Printing this would be still making use of intendation actually hmmm. 
        
        """
        
        queue = [self]
        while len(queue) != 0:
            popped_node = queue.pop(0)
            print(popped_node.value)
            for node in popped_node.children :
                queue.append(node)
                
    def bf_search(self, value):
        """
        We have to implement search now. Approach is going to be level-order-search, because that makes more sense, than going the entire depth and backtracking imo.
        So, the idea is to do level-order search for each level and return whenever we get the value matched , so on it. 
        """
        queue = [self]
        while len(queue) != 0:
            popped_node = queue.pop(0)
            if (popped_node.value == value):
                return popped_node
            for node in popped_node.children:
                queue.append(node)
        return None
    
    def df_search(self,value):
        """
        we have to do depth first search hmmm. Now what needs to be done ? We need to do recursion here. Hmmmmm..... How ? 
        """
        if ( self.value == value):
            return self
        for node in self.children:
            result = node.df_search(value)
            if result is not None:
                return result
        return None 
        
    
        
    

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
    
    # print(f"Root: {root_node}")
    # print(f"Root is leaf: {root_node.is_leaf()}")
    # print(f"C is leaf: {c_node.is_leaf()}")
    # print(f"Root has {len(root_node.children)} children")
    # print("Pre-order:")
    # root_node.pre_order_traversal()
    # print("\nPost-order:")
    # root_node.post_order_traversal()
    
    # root_node.level_order_traversal()
    print(root_node.df_search("D"))
        
        
        
    