class HuffmanDecode:
    def __init__(self, file_name, out_file_name) -> str:
        code = self.convert_to_dict(file_name)
        decoded = self.decode(code, file_name)
        print(decoded)
        if out_file_name != None: open(out_file_name, 'w+').write(decoded)

    def convert_to_dict(self, file_name) -> dict:
        file = open(file_name, 'r')
        modified_file = list(filter(lambda x: ':' in x, file.readlines()))
        file.close()
        out = {}
        for item in modified_file:
            item = item.split(':')
            out[item[0][1:-1]] = item[1][1:-1]
        return out

    def decode(self, code, file) -> str:
        file = open(file_name, 'r')
        encoded_string = file.readlines()[-1]
        file.close()
        decoded_string = ''
        while len(encoded_string) > 0:
            for key in code.keys():
                if len(code[key])-len(encoded_string) != 0:
                    cut = len(code[key])-len(encoded_string)
                else:
                    cut = None
                if encoded_string[:cut] == code[key]:
                    decoded_string += key
                    encoded_string = encoded_string[len(code[key]):]
        return decoded_string


def huffman_decode(file_name):
    HuffmanDecode(file_name)

if __name__ == '__main__':
    from sys import argv
    out_file_name = None

    if '-h' in argv:
        print('''This program is used to decode string with Huffman algoritm by TheHexReader
        
    -h                    - Print out this message
    -f <file_name>        - Specify file_name to read from
    -t <file_name>        - Specify file_name to export output (!!! IT WILL REWRITE EXISTING FILE !!!)''')
        exit()

    if '-f' in argv:
        try:
            file_name = argv[argv.index('-f') + 1]
        except IndexError:
            print('Bad usage of "-f"')
            exit()

    if '-t' in argv:
        try:
            out_file_name = argv[argv.index('-t') + 1]
        except IndexError:
            print('Bad usage of "-t"')
            exit()

    if not '-f' in argv:
        print('You need to use "-f" parameter')
        exit()

    HuffmanDecode(file_name, out_file_name)