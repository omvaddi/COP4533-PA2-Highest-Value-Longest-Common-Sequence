import random
import string

def generate_file(filename):
    with open(filename, 'w') as f:
        letters = set()
        size = random.randint(3, 26)
        f.write(str(size) + "\n")
        for i in range(size):
            new_letter = random.choice(string.ascii_lowercase)
            while new_letter in letters:
                new_letter = random.choice(string.ascii_lowercase)
            letters.add(new_letter)
            f.write(new_letter + " "  + str(random.randint(1, 15)) + "\n")

        a_size, b_size = random.randint(25, 100), random.randint(25, 100)
        for i in range(a_size):
            f.write(random.choice(list(letters)))
        f.write("\n")
        for i in range(b_size):
            f.write(random.choice(list(letters)))
            
def main():
    for i in range (1, 11):
        generate_file("files/file" + str(i) + ".txt")
if __name__ == '__main__':
    main()