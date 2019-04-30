
def find_and_replace(file, old, new):
    with open(file, "r+") as file:
        text = file.read()
        new_text = text.replace(old, new)
        file.seek(0)
        file.write(new_text)
        file.truncate()
        
find_and_replace("Story.txt", "story", "cat")

