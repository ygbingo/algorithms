from choice_activity import choice_activity
from hoffman_tree import HuffmanTree

def test_choice_activities():
    A = [[1,4],[0,6], [3,5],[5,7],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]]
    assert choice_activity(A) == 4

def test_huffman_tree():
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
    assert huffman_tree.huffman_code['a'] == '0000'