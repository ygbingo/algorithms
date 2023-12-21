"""
霍夫曼编码
"""
import heapq


class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = 0

    def __lt__(self, nxt):
        return self.freq < nxt.freq
    

class HuffmanTree:
    def __init__(self, character_freq_dict):
        self.character_freq_dict = character_freq_dict
        self.huffman_tree = []
        self.huffman_code = dict()
        self.build_huffman_tree()

    def print_huffman_tree(self):
        self.print_node(self.huffman_tree[0])

    def print_node(self, node, huffcode=''):
        huffcode = huffcode + str(node.huff)
        if node.left:
            self.print_node(node.left, huffcode)
        if node.right:
            self.print_node(node.right, huffcode)
        if not node.left and not node.right:
            self.huffman_code[node.symbol] = huffcode
            print(f"{node.symbol} -> {huffcode}")
        
    def build_huffman_tree(self):
        self.huffman_tree.clear()
        for symbol in self.character_freq_dict.keys():
            freq = self.character_freq_dict[symbol]
            heapq.heappush(self.huffman_tree, Node(symbol=symbol, freq=freq))
        
        while len(self.huffman_tree) > 1:
            left = heapq.heappop(self.huffman_tree)
            right = heapq.heappop(self.huffman_tree)
            left.huff = 0
            right.huff = 1

            node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
            heapq.heappush(self.huffman_tree, node)
    

character_freq = {
    'a': 5,
    'b': 7,
    'c': 15,
    'd': 8,
    'e': 12,
    'f': 14
}
huffman_tree = HuffmanTree(character_freq)
huffman_tree.print_huffman_tree()