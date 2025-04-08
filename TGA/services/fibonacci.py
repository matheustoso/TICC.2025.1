import math 

#region Encode

def encode(input, alphabet) -> str:
    output = ""
    
    for char in input:
        symbol = alphabet[char]
        
        sequence = get_fibonacci_up_to(symbol)
        print(sequence)
        codeword = ""
        
        for fibonacci in reversed(sequence):
            if fibonacci <= symbol:
                codeword += "1"
                symbol -= fibonacci
            else: 
                codeword += "0"
        
        output += codeword[::-1] + "1"
    
    return output

def get_fibonacci_up_to(n) -> list:
    sequence = [1, 2]
    
    next_fibonacci = 0
    
    while (sequence[-1] + sequence[-2]) <= n:
        next_fibonacci = sequence[-1] + sequence[-2]
        sequence.append(next_fibonacci)
        
    return sequence

#endregion

#region Decode

def decode(input, alphabet) -> str:
    alphabet = {v: k for k, v in alphabet.items()}
    
    output = ""
    codeword = ''
    consecutive_ones = 0
    
    for bit in input:
        if bit is "1":
            consecutive_ones += 1
        else:
            consecutive_ones = 0
        
        if consecutive_ones == 2:
            sequence = get_fibonacci_sequence(len(codeword))
            
            symbol = 0
            for b, f in zip(codeword, sequence):
                if b is "1": 
                    symbol += f
            
            output += alphabet[symbol]
            
            codeword = ''
            consecutive_ones = 0
        else:
            codeword += bit    
    
    return output

def parse_fibonacci_codeword(codeword) -> int:
    return 0
    
def get_fibonacci_sequence(n) -> list:
    sequence = [1, 2]
    
    next_fibonacci = 0
    
    for _ in range(n-2):
        next_fibonacci = sequence[-1] + sequence[-2]
        sequence.append(next_fibonacci)
        
    return sequence
#endregion