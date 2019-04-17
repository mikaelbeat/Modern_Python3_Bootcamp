
def yell(text):
    return text.upper() + "!"

print(yell("Hello"))


def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count
    
print(count_dollar_signs("$uper $ize"))