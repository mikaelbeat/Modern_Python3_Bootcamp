
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return "man" + word
    elif "suffix" in kwargs:
        return word + "ish"
    else:
        return word
           
print(combine_words("Kissa", suffix="man"))  
    
     
    
# def combine_words(word,**kwargs):
#     if 'prefix' in kwargs:
#         return kwargs['prefix'] + word
#     elif 'suffix' in kwargs:
#         return word + kwargs['suffix']
#     return word