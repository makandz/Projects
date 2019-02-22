def show(msg, typ = 1):
    if typ == 1:
        print("[INFO]", msg)
    elif typ == 2:
        print("[WARN]", msg)
    elif typ == 3:
        print("[ERROR]", msg)

# Opening
show("Document Viewer, made by Makan")
show("------------------------------")
show("Reading data file..")
data = open("DATA.txt", "r", encoding="utf8")
lines = data.read().split("\n")

if not len(lines):
    show("Data file is not found or empty, exiting..", 3)
    exit()

show("Processing data..")

words = {}
word_count = 0
for line in lines:
    line = line.strip()
    for word in line.split():
        if word_count % 125 == 0 and word_count != 0:
            show("Processed " + str(word_count) + " words..")
        word = word.lower()
        while word and not word[0].isalnum():
            word = word[1:]
        while word and not word[-1].isalnum():
            word = word[:-1]
        if word:
            word_count += 1
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        else:
            show("Unable to use word: " + word, 2)

show("Word processing complete!")
show("Type in a word to get all occurrences.")
show("Type in exit to leave.")
show("-------------------------")
while 1:
    search = input("[INPUT]: ").lower()
    if search == "exit":
        break
    if len(search.split()) > 1:
        show("You can only search for one word at a time.", 2)
    elif search in words:
        show("The word \"" + search + "\" shows up " + str(words[search]) + " times.")
    else:
        show("I can't find that word in the file!", 2)