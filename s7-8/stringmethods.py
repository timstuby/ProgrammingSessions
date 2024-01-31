text = "abcdefghijklmnopqrst"
print(dir(text))

print("anananananananan".count("ana"))
print("anananananananan".replace("ana","banana"))
print("ananananananan".find("ana",1))
print("ananananananan".split("a"))
print("this is a sentence and I want the words".split(" "))
sentence = "Hello, kind sir, how may I be of service today?"
punctuation = ".,;!?-"
# sanitize the sentence
for p in punctuation:
    sentence = sentence.replace(p, " ")  # replace the punctuation with nothing

print(sentence)
sentence = sentence.replace("  "," ")
# split the sentence into words
words = sentence.split(" ")
print(words)