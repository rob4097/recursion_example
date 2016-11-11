# Node class for holding information about a node in the tree
class node:
    visited = False         # visited is used to track the nodes we have already been to.
    name = "Unnamed"        
    neighbors = []          # neighbors is used to track the adjacent nodes

    def __init__(self, name):
        self.name = name

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor) # Append a neighbor to the neighbors list

# Class for recursing through a tree
class recursor:

    # This builds the tree/graph
    def build_tree(self):
        node1 = node("Node 1")
        node2 = node("Node 2")
        node3 = node("Node 3")
        node4 = node("Node 4")
        node5 = node("Node 5")
        node6 = node("Node 6")
        node7 = node("Node 7")

        node1.add_neighbor(node2)
        node1.add_neighbor(node3)
        
        node2.add_neighbor(node6)
        node2.add_neighbor(node7)

        node3.add_neighbor(node4)
        node3.add_neighbor(node5)

        return [node1, node2, node3, node4, node5, node6, node7]    # Build a list of nodes and return it

    def recurse(self, node):
        # Base case
        # This is what happens if we do not want to recurse any more
        if (node.visited == True):  # If we have visited all of our neighbors, we don't need to recurse through them
            print "Node " + node.name + " has already been visited!"
            return None # Return none for simplicity, but we can return anything
        # Recursive case
        # In this example, we want to recurse through any neighbors that we have not already visited
        else:
            # Do 'something' (TM)
            print node.name
            node.visited = True # Mark that we've visited the node
            # It's important that you do this _before_ you recurse or else when you look at neighbors, it will still be marked as unvisited

            # Recurse through all neighbors
            for child_node in node.neighbors:
                self.recurse(child_node)
            return None

if __name__ == "__main__":
    rc = recursor()         # Create a recursor object
    tree = rc.build_tree()  # Build the tree

    rc.recurse(tree[0])   # Go!
