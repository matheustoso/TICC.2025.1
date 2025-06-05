import math

#region LOCAL CONSTANTS
prefix = "0"
stop_bit = "1"
#endregion

#region ENCODE
def encode(input, alphabet) -> str:
    output = ""
    
    for char in input:
        symbol = alphabet[char]
        
        n = math.floor(math.log2(symbol))
        remainder = symbol - 2 ** n
        
        suffix = f"{remainder:b}".zfill(n)

        codeword = prefix * n + stop_bit + suffix
        output += codeword
    
    return output
#endregion

#region DECODE
def decode(input, alphabet) -> str:
    alphabet = {v: k for k, v in alphabet.items()}
    
    output = ""
    
    suffix = ""
    n = 0
    is_prefix = True
    
    for bit in input:
        
        if is_prefix:
            if bit == prefix:
                n += 1
            else:
                is_prefix = False
            
        else:
            suffix += bit
            
            if len(suffix) == n:
                symbol = 2 ** n + int(suffix, 2)
                output += alphabet[symbol]
                
                suffix = ""
                n = 0
                is_prefix = True
    
    return output
#endregion