def encode(input_text) -> str:
    encoded_input = ""
    
    for c in input_text:
        encoded_input += c*3

    return encoded_input

def decode(input_text) -> tuple[str, list]:
    list_input = list(input_text)
    input_size = len(list_input)
    decoded_input = ""
    bit_errors = list()
    
    for i in range(0, input_size, 3):
        r1 = int(list_input[i])
        r2 = int(list_input[i+1]) 
        r3 = int(list_input[i+2])
        sum = r1 + r2 + r3 
        decoded_input += "1" if sum >= 2 else "0"
        
        if sum == 1:
            if r1 == 1:
                bit_errors.append(str(i+1))
            if r2 == 1:
                bit_errors.append(str(i+2))
            if r3 == 1:
                bit_errors.append(str(i+3))                                
            
        if sum == 2:
            if r1 == 0:
                bit_errors.append(str(i+1))
            if r2 == 0:
                bit_errors.append(str(i+2))
            if r3 == 0:
                bit_errors.append(str(i+3))              
    
    return decoded_input, bit_errors