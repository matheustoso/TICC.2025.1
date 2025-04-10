from enum import StrEnum

#region OPERATION
class Operation(StrEnum):
    ENCODE = "Encode",
    DECODE = "Decode"
#endregion

#region ALGORITHM
class Algorithm(StrEnum):
    GOLOMB = "Golomb",
    ELIASGAMMA = "Elias-Gamma",
    FIBONACCI = "Fibonacci/Zeckendorf",
    HUFFMAN = "Huffman"
#endregion