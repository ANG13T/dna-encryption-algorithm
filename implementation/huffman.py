"""
Huffman Coding for DNA Frequencies

Procedure:
1. Sort frequencies in ascending order 
2. Initiate a binary tree
3. Take the lowest two frequency nucleotide bases and add them = l1 + l2 = l (l1 < l2)
3. Root = l
4. Make Left Child of Root = l1
5. Make Right Child of Root = l2

        l
      /   \
    l1      l2

6. Keep repeating steps 3 - 5 until a tree is constructed out of all nucleotide bases
7. For each node in the tree, label the left child as 0 and right as 1
8. Get binary representation for each base by following path
"""

class Node:
    def __init__(self, data, label = ""):
        self.left = None
        self.right = None
        self.data = data
        self.label = label

    def insert(self, node):
        if self.data:
            if self.right == None:
                self.right = node
            elif self.left == None:
                self.left = node
            else:
                if node.label != "" and node.data > self.left.data:
                    self.right = node
                else:
                    self.left = node
        else:
            self.data = node.data

    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()


def retrieve_binary_output(node, value, track):
    tracker = track

    if (node == None):
        return None

    if(node.label == value):
        return tracker

    # check right first 
    res1 = retrieve_binary_output(node.right, value, tracker)

    if res1 != None:
        tracker.append(1)
        return tracker

    
    res2 = retrieve_binary_output(node.left, value, tracker)

    if res2 == None:
        tracker.append(0)
    
    return res2 

# Given Freq Dict -> Return Huffman Coding Table
def huffman_coding(frequencies):
    print(frequencies)
    labels = list(frequencies.keys())
    frequencies = list(frequencies.values())

    # init base node
    selected_node = None
    fre = frequencies[3]
    fre_2 = frequencies[2]
    print(fre_2, labels[2])
    print(fre, labels[3])
    total = fre + fre_2
    total_node = Node(total)
    total_node.insert(Node(fre, labels[3]))
    total_node.insert(Node(fre_2, labels[2]))
    selected_node = total_node

    # construct the tree
    for i in range(3,5):
       combo = selected_node.data + frequencies[4 - i]
       new_node = Node(combo)
       new_node.insert(Node(frequencies[4 - i], labels[4 - i]))
       new_node.insert(selected_node)
       selected_node = new_node

    huffman_codings = {
            "A": bin_array_to_string(retrieve_binary_output(selected_node, "A", [])),
            "T": bin_array_to_string(retrieve_binary_output(selected_node, "T", [])), 
            "G": bin_array_to_string(retrieve_binary_output(selected_node, "G", [])), 
            "C": bin_array_to_string(retrieve_binary_output(selected_node, "C", []))
    }
    
    return huffman_codings


def bin_array_to_string(bin):
    return "".join(map(str, bin))
