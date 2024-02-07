# first we open()
# Open by specifying the file name: e.g. "text.txt"
# need to include the directory
# Modes are: r - read, w - write, e - exclusive creation (don't create if already created,
# a - append, b - binary, t - text, +- update (read+write)

f = open("x-files.txt", "w")
while True:
    line = input("Give me text to put into a file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# closes file
f.close()
