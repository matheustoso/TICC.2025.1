from enum import StrEnum

class Operation(StrEnum):
    ENCODE = "Encode",
    DECODE = "Decode"
    
class Algorithm(StrEnum):
    GOLOMB = "Golomb",
    ELIASGAMMA = "Elias-Gamma",
    FIBONACCI = "Fibonacci/Zeckendorf",
    HUFFMAN = "Huffman"