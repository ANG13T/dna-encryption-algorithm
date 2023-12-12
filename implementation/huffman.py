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
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, node):
        if self.data:
            if node.data < self.data:
                if self.left == None:
                    self.left = node
                else:
                    self.left.insert(node)
            elif node.data > self.data:
                if self.right == None:
                    self.right = Node(node)
                else:
                    self.right.insert(node)
        else:
            self.data = node.data

    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()

# Given Freq Dict -> Return Huffman Coding Table
def huffman_coding(frequencies):
    print(frequencies)
    frequencies = list(frequencies.values())

    # init base node
    selected_node = None
    fre = frequencies[3]
    fre_2 = frequencies[2]
    total = fre + fre_2
    total_node = Node(total)
    selected_node = total_node

    for i in range(3,5):
       combo = selected_node.data + frequencies[4 - i]
       new_node = Node(combo)
       new_node.insert(selected_node)
       new_node.insert(Node(frequencies[4 - i]))
       selected_node = new_node

    print(selected_node.data)
    
    return

    # construct binary tree
    fre = frequencies[0] + frequencies[1]
    print()

    return
    # TODO: repeat for each frequency
    freq_1 = frequencies[-1]
    freq_2 = frequencies[-2]
    freq_count = freq_1 + freq_2

    # creating binary tree
    root = Node(freq_count)
    root.insert(freq_1)
    root.insert(freq_2)

    root.display()
    print(freq_1, freq_2, freq_count)
    print(root.data)

    
