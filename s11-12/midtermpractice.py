# Mid term practice questions

def print_b_words(file_name):
    punctuation = ",.!?\n"
    with open(file_name, 'r') as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p, "")
            words = line.split(" ")
            for word in words:
                if word.startswith(('B')) and len(word) == 3:
                    print(word)

print(print_b_words("Yankee.txt"))