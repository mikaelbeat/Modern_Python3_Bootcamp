
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return "man" + word
    elif "suffix" in kwargs:
        return word + "ish"
    else:
        return word
        
    
    
    
print(combine_words("Kissa", prefix="man"))  
    
    
    
    
    
    
    
    
    
    
    
    
# def special_greeting(**kwargs):
#     if "David" in kwargs and kwargs ["David"] == "special":
#         return "You get a special greeting!"
#     elif "David" in kwargs:
#         return f"{kwargs['David']} David! "
#     return "Not sure wh this is!"