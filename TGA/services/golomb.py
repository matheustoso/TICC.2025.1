import math

prefix = "0"
stop_bit = "1"

def encode(input, alphabet) -> str:
    output = ""
    divisor = math.ceil(len(alphabet)/2)
    suffix_size = math.ceil(math.log2(divisor))
    
    for char in input:
        symbol = alphabet[char]
        
        remainder = symbol % divisor
        prefix_size = symbol // divisor
        
        suffix = f"{remainder:b}".zfill(suffix_size)
        
        codeword = prefix * prefix_size + stop_bit + suffix
        output += codeword
        
    return output

def decode(input, alphabet) -> str:
    alphabet = {v: k for k, v in alphabet.items()}
    
    output = ""
    divisor = math.ceil(len(alphabet)/2)
    suffix_size = math.ceil(math.log2(divisor))
    
    suffix = ""
    prefix_size = 0
    is_prefix = True
    
    for bit in input:
        
        if is_prefix:
            if bit == prefix:
                prefix_size += 1
            else:
                is_prefix = False
            
        else:
            suffix += bit
            
            if len(suffix) == suffix_size:
                symbol = prefix_size * divisor + int(suffix, 2)
                output += alphabet[symbol]
                
                suffix = ""
                prefix_size = 0
                is_prefix = True
                
        
    return output