def reverseWords(sentence):
    words = sentence.split()
    revSent = ' '.join(reversed(words)) 
    return revSent

inp = "The Ganges is the longest river in India while The Nile in World"
out = reverseWords(inp)
print(out)
