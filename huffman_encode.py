class HuffmanTree:
    def __init__(self, left_node=None, right_node=None) -> None:
        self.left_node  = left_node
        self.right_node = right_node

    def children(self) -> tuple:
        return (self.left_node, self.right_node)

class HuffmanEncode:
    DEFAULT_ENCODE_STRING = 'Default encode string.'
    
    def __init__(self, file_name=None, string_to_encode=None) -> None:
        if string_to_encode == None: string_to_encode = self.DEFAULT_ENCODE_STRING

        frequency = self.get_char_frequency(string_to_encode)
        nodes = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        huffman_code = self.build_code(nodes)

        out_encode = ''
        for char in string_to_encode:
            out_encode += huffman_code[char]

        to_print = ''

        to_print += f'{len(nodes)} {len(out_encode)}\n'
        
        for (char, _) in nodes:
            to_print += f'\'{char}\': {huffman_code[char]}\n'

        to_print += out_encode

        print(to_print)
        if file_name != None: open(file_name, 'w+').write(to_print)

    def get_char_frequency(self, string):
        result = {}
        for char in string:
            if char in result: result[char] += 1
            else:              result[char] = 1
        return result

    def code_tree(self, node, binString=''):
        if type(node) is str: return {node: binString}

        left, right = node.children()
        out = {}
        out.update(self.code_tree(left, binString + '0'))
        out.update(self.code_tree(right, binString + '1'))
        return out

    def build_code(self, nodes):
        while len(nodes) > 1:
            key1, c1 = nodes[-1]
            key2, c2 = nodes[-2]
            nodes    = nodes[:-2]
            node     = HuffmanTree(key1, key2)
            nodes.append((node, c1 + c2))
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        return self.code_tree(nodes[0][0])


def huffman_encode(string):
    HuffmanEncode(string)

if __name__ == '__main__':
    from sys import argv
    file_name = None
    string_to_encode = None

    if '-h' in argv:
        print('''This program is used to encode string with Huffman algoritm by TheHexReader
        
    -h                    - Print out this message 
    -f <file_name>        - Specify file_name to export output (!!! IT WILL REWRITE EXISTING FILE !!!)
    -m <string_to_encode> - Specify string to encode''')
        exit()

    if '-f' in argv:
        try:
            file_name = argv[argv.index('-f') + 1]
        except IndexError:
            print('Bad usage of "-f"')
            exit()
    
    if '-m' in argv:
        try:
            string_to_encode = argv[argv.index('-m') + 1]
        except IndexError:
            print('Bad usage of "-m"')
            exit()

    HuffmanEncode(file_name, string_to_encode)
