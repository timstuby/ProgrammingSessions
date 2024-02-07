#with operation allows you not to have to specify the close
print("Hi :)")
searchVar = input("Enter what word you want to look for: ")

num_watch = 0
with open("x-files.txt","r") as f:
    # inside here the f file is open for reading
    # print(f.read())
    for line in f:
        num_watch += line.lower().count(searchVar)

print("the word",searchVar, "shows up", num_watch,"times in the file.")

#once I am out, the file is closed
#for on a file iterates line by lines
#second for loop goes to characters

