from collections import Counter
from operator import itemgetter

prefix = '1'
stop_bit = '0'

def encode(input) -> tuple:
    output = ''
    alphabet = Counter(input)
    
    frequencies = sorted(alphabet.items(), key = itemgetter(1))
    
    codewords = {}
    
    offset = 2
    alphabet_size = len(frequencies)
    for i, (char, _) in enumerate(frequencies):
        codeword = (alphabet_size - offset) * prefix
        
        if i == 0: 
            codeword += prefix
        else: 
            codeword += stop_bit
            offset += 1
            
        codewords[char] = codeword
    
    for char in input:
        output += codewords[char]
    
    dicts = [alphabet, codewords]
    user_alphabet = {k: [d[k] for d in dicts] for k in dicts[0]}
    user_alphabet = {k: v for k, v in sorted(user_alphabet.items(), key=lambda item: item[1][1])}
    
    return (output, alphabet, user_alphabet)

def decode(input, alphabet) -> str:
    output = ''
    
    frequencies = sorted(alphabet.items(), key = itemgetter(1))
    
    codewords = {}
    
    offset = 2
    alphabet_size = len(frequencies)
    for i, (char, _) in enumerate(frequencies):
        codeword = (alphabet_size - offset) * prefix
        
        if i == 0: 
            codeword += prefix
        else: 
            codeword += stop_bit
            offset += 1
            
        codewords[codeword] = char
    
    codeword = ''
    count = 1
    for bit in input:
        codeword += bit
        count += 1
        
        if count >= alphabet_size or bit is stop_bit:
            output += codewords[codeword]
            codeword = ''
            count = 1
    
    return output