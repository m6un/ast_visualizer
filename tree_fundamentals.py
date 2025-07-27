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
    
    # Now we calculate tree height 
    # Think about what the height of a leaf node will be - height of a leaf node would be the sum of height of it's parent node + 1 
    # Logically this gives correct answer only, just that it's top-down. Meaning the top node is telling the child node that you are 1 level below me. That's all. 
    def get_height_firsttry(self,height=0): 
        max_height = height 
        if (len(self.children) == 0): #will never get triggered because we are setting max_height as height just above. 
            return max_height 
        for node in self.children:
            result = node.get_height_firsttry(height + 1) # apparently I'm ignoring the return value here. , I need to capture the return value of recursive calls hmmmm. 
            max_height = max(max_height, result)
        
        return max_height
    
    # THis is another way of solving it. THis is more of a bottom-up approach where the child tells it's parent what height it has and final output from parent would be child's height + 1 
    def get_height(self):
        if len(self.children) == 0:  # Leaf node
            return 0

        max_child_height = 0
        for child in self.children:
            child_height = child.get_height()  # Get child's height
            max_child_height = max(max_child_height, child_height)

        return 1 + max_child_height  # My height = 1 + tallest child
    
    
    def get_size(self):
        """
        Okay so we have to implement get size. for leaf node that would be 1 , size meaning total number of nodes in the subtree to the node. 
        questions would be : 
        1. What is the base case for a leaf ? no children
        2. How do you combine children's sizes with your own ? - + 1
        3. Which recursive pattenr ? - accumulate all of children's sizes hmmm. 
        """
                
        total_nodes_number = 0
        if self.is_leaf() :
            return 1
        
        for child in self.children :
            nodes_in_child = child.get_size()
            total_nodes_number += nodes_in_child
        
        return total_nodes_number + 1
    
    def find_parent_firsttry(self, target_value):
        """
        This is tricky, because there is no parent reference for a child. Only a parent has child reference. Then, how do you find parent for a given node ? Hmmm interestingo,
        SO the intuition should be to think  that if I'm the parent node to the given value how would I output that. And start from root_node and check in which subtree the parent lies, recursively. Hmmmmmm...  
        """
        parent_node = None
        if (self.value == target_value):
            return parent_node # we maintain immediate parent_node for children and return it if any children has the target value. 
        
        while len(parent_node.children) != 0:
            for node in parent_node.children :
                parent_node = node
        
        return parent_node 
        # THe above approach is wrong because we initialize parent_node as None in the beginning and are checking for it's children. This would have worked if a child node had reference to it's parent node. But doesn't work here because child node doesn't have reference. 
        
    def find_parent_secondtry(self, target_value):
        """
        Each node has to check 2 things : 
        1. Am I the direct parent ? 
        2. Is the parent somewhere in my subtree ? 
        
        The recursive qn each node should ask : 
        1. Is the target on of MY Children ? - ( direct ask )
        2. Is the target's parent somewhere below me ? - ( recursive ask)
        """
        
        for node in self.children:
            if node.value == target_value:
                return self
        
        while len(self.children) != 0:
            for node in self.children:
                result_node = node.find_parent_secondtry(target_value)
                if result_node != None:
                    return result_node
            
        return None
    
    def find_parent_thirdtry(self, target_value):
        """
        The mistake we made above is that first we were returning whatever value the recursive call returns. And if it's None, we return none. But there are other subtrees to chck we don't check that. Now, with the current implementation, we return result_node if it's not None. Then we are not handling the none case. SO then that made it an ifinite loop. Apparently while is not the correct control structure we need there. Hmmm. 
        """
        
        for node in self.children:
            if node.value == target_value: return self
        
        # The control structure here should execute ATMOST ONCE only. Hmmm. then it's an IF statement. not a loop that runs endlessly. 
        if len(self.children) !=0:
            for node in self.children:
                result_node = node.find_parent_thirdtry(target_value)
                if result_node is not None:
                    return result_node
                
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
    # print(root_node.df_search("D"))
    # print(root_node.get_height())
    print(root_node.find_parent_thirdtry("D"))
        
        
        
    