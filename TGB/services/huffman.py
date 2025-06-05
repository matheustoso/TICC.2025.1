from collections import Counter
from operator import itemgetter

#region LOCAL CONSTANTS
prefix = "1"
stop_bit = "0"
#endregion

#region ENCODE
def encode(input) -> tuple:
    output = ""
    alphabet = Counter(input)
    
    frequencies = sorted(alphabet.items(), key = itemgetter(1))
    
    codewords = {}
    
    offset = 1
    alphabet_size = len(frequencies)
    for i, (char, _) in enumerate(frequencies):
        prefix_size = (alphabet_size - offset) 
        codeword = prefix_size * prefix
        
        if i != 0 or alphabet_size == 1:
            codeword += stop_bit
            
        codewords[char] = codeword
        offset += 1
    
    for char in input:
        output += codewords[char]
    
    dicts = [alphabet, codewords]
    user_alphabet = {k: [d[k] for d in dicts] for k in dicts[0]}
    user_alphabet = {k: v for k, v in sorted(user_alphabet.items(), key=lambda item: item[1][1])}
    
    return (output, alphabet, user_alphabet)
#endregion

#region DECODE
def decode(input, alphabet) -> str:
    output = ""
    if len(alphabet) == 0: return output
    
    frequencies = sorted(alphabet.items(), key = itemgetter(1))
    
    codewords = {}
    
    offset = 1
    alphabet_size = len(frequencies)
    
    for i, (char, _) in enumerate(frequencies):
        prefix_size = (alphabet_size - offset) 
        codeword = prefix_size * prefix
        
        if i != 0 or alphabet_size == 1: 
            codeword += stop_bit
            
        codewords[codeword] = char
        offset += 1
    
    codeword = ""
    count = 1
    
    for bit in input:
        codeword += bit
        count += 1
        
        if count >= alphabet_size or bit is stop_bit:
            output += codewords[codeword]
            codeword = ""
            count = 1
    
    return output
#endregion