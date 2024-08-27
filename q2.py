def countLetter(sentence):

    letter_freq = {}
    
    letters = [char.upper() for char in sentence]
    
    for letter in letters:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1
    
    return letter_freq

def countWord(sentence):
    word_freq = {}
    word = [{sentence.split(' ')}]
    
    for w in word:
        if w in word_freq:
            word_freq[w] += 1
        else:
            word_freq[w] = 1
            
    return word_freq
    

inp = "TCS is the largest IT service company in India, headquartered in Mumbai, and also the largest employee base."
letterOccurrences = countLetter(inp)

print("\nLetter Occurrence:")
for data in letterOccurrences :
    print(data , letterOccurrences[data]) 
    
    
#wordOccur = countWord(inp)
#print("\n Word Occurrences:")
#for data in wordOccur:
#    print(data, wordOccur[data])
