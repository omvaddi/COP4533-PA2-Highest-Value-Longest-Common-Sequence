def read_file(filename):

    char_vals = {}
    with open(filename, 'r') as f:
        num_characters = int(f.readline().strip())
        
        for _ in range(num_characters):
            char, val = f.readline().strip().split()
            char_vals[char] = val

        a = f.readline().strip()
        b = f.readline().strip()

    return char_vals, a, b


def main():
    char_vals, a, b = read_file('tests/test1.txt')
    print(char_vals)
    print(a)
    print(b)

if __name__ == '__main__':
    main()
