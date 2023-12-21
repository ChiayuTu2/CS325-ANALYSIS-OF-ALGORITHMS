import heapq # Hint: use Python's priority queue class, heapq.

class Node:
    def __init__(self, count, children):
        self.count    = count
        self.children = children
        
    def is_leaf(self):
        return False
        
    def __lt__(self, other):
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count
        
class LeafNode(Node):
    def __init__(self, symbol, count):
        super().__init__(count, [])
        self.symbol = symbol
        
    def is_leaf(self):
        return True

class HuffmanCode:
    def __init__(self, F):
        self.C = dict()
        self.T = None
        self.cost = 0
        self.average_cost = 0
        # TODO: Construct the Huffman Code and set C, T, cost, and average_cost properly!
        
        # Construct Huffman tree
        heap = []
        for symbol, freq in F.items():
            node = LeafNode(symbol, freq)
            heap.append(node)

        heapq.heapify(heap)
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            combined_node = Node(left.count + right.count, [left, right])
            heapq.heappush(heap, combined_node)
        self.T = heap[0]

        # Build code map C
        def dfs(node, code):
            if node.is_leaf():
                self.C[node.symbol] = code
                return
            index = 0
            for child in node.children:
                dfs(child, code + str(index))
                index += 1
        dfs(self.T, "")

    def compute_costs(self):
        """Computes the cost and average cost of the Huffman code."""
        self.cost = 0
        total_symbols = sum(F.values())
        for symbol, freq in F.items():
            self.cost += len(self.C[symbol]) * freq
        self.average_cost = self.cost / total_symbols

    def encode(self, m):
        """
        Uses self.C to encode a binary message.
.    
        Parameters:
            m: A plaintext message.
        
        Returns:
            The binary encoding of the plaintext message obtained using self.C.
        """
        encoded_message = ""
        for char in m:
            encoded_message += self.C[char]
        return encoded_message
        # TODO: Implement this method!
        #return None
        
    def decode(self, c):
        """
        Uses self.T to decode a binary message c = encode(m).
   
        Parameters:
            c: A message encoded in binary using self.encode.
        
        Returns:
            The original plaintext message m decoded using self.T.
        """
        node = self.T
        decoded_message = ""
        for bit in c:
            if bit == '0':
                node = node.children[0]
            else:
                node = node.children[1]
                
            if node.is_leaf():
                decoded_message += node.symbol
                node = self.T
        return decoded_message
        # TODO: Implement this method!
        # return None
        
    def get_cost(self):
        """
        Returns the cost of the Huffman code as defined in CLRS Equation 16.4.
        
        Returns:
            Returns the cost of the Huffman code.
        """ 
        self.compute_costs()
        return self.cost        
        #return self.cost
        
    def get_average_cost(self):
        """
        Returns the average cost of the Huffman code.
        
        Returns:
            Returns the average cost of the Huffman code.
        """ 
        self.compute_costs()
        return self.average_cost        
        #return self.average_cost
        
def get_frequencies(s):
    """
    Computes a frequency table for the input string "s".
    
    Parameters:
        s: A string.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in s).
    """

    F = dict()
    
    for char in s:
        if not(char in F):
            F[char] = 1
        else:
            F[char] += 1
            
    return F
    
def get_frequencies_from_file(file_name):
    """
    Computes a frequency table from the text in file_name.
    
    Parameters:
        file_name: The name of a text file.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in the contents of <file_name>).
    """

    f = open(file_name, "r")
    s = f.read()
    f.close()

    return get_frequencies(s)


#Test my code
F = get_frequencies_from_file("cs325-f23-homework3-gettysburg-address.txt")
huffman = HuffmanCode(F)
print("Cost of Huffman code:", huffman.get_cost())
print("Average cost of Huffman code:", huffman.get_average_cost())