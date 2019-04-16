playlist = {"title": "patagonia bus", 
            "author": "colt steele", 
            "songs": [
                {"title": "song1", "artist": ["blue"], "duration": 1},
                {"title": "song2", "artist": ["kitty", "djcat"], "duration": 2},
                {"title": "meowmeow", "artist": ["garfield"], "duration": 3}
                ]
            }

total_length = 0

for song in playlist["songs"]:
    total_length += song["duration"]
    
print(total_length)