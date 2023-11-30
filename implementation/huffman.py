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

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()

# Given Freq Dict -> Return Huffman Coding Table
def huffman_coding(frequencies):
    freq_1 = frequencies[-1]
    freq_2 = frequencies[-2]
    freq_count = freq_1 + freq_2

    # creating binary tree
    root = Node(freq_count)
    root.insert(freq_1)
    root.insert(freq_2)

    root.display()

    
