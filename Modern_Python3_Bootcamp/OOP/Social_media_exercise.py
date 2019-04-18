class Comment:
    
    def __init__(self, username, text,likes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self._msg = "This is private"
        
c = Comment("Davey", "lol", 3)

print(c.username)
print(c.text)
print(c.likes)
