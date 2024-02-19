wordfreq = {}
punctuation = ".!,?\n"
with open("Dracula.txt") as file:
    for line in file:
        print(line, end="")
        for p in punctuation:
            line = line.replace(p, "")
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if len(word) < 5:
                continue
        #    if word in wordfreq[word]:
        #        wordfreq[word] += 1
        #    else:
        #    wordfreq[word] = 1
        # we have all the lines in the file
            wordfreq[word] = wordfreq.get(word, 0) + 1

topfreq = list(wordfreq.values())
topfreq.sort(reverse=True)
topfreq = topfreq[:10]
print(topfreq)

for word, freq in wordfreq.items():
    if freq in topfreq:
        print(f"{word}: {freq}")

for topword in topfreq:
    for key in wordfreq:
        if wordfreq[key] == topword:
            print(f"{key}: {topword}")
            del wordfreq[key]
            break