s = "https://www.google.com/ and then there could be https://yahoo.com"
start = 0
while True:
    start = s.find("https://")
    if start == -1:
        break
    end = s.find(" ",start)
    if end == -1:
        