from enum import StrEnum

#region OPERATION
class Operation(StrEnum):
    ENCODE_ENCRYPT = "Encode/Encrypt",
    DECODE_DECRYPT = "Decode/Decrypt"
#endregion

#region ALGORITHM
class Algorithm(StrEnum):
    GOLOMB = "Golomb",
    ELIASGAMMA = "Elias-Gamma",
    FIBONACCI = "Fibonacci/Zeckendorf",
    HUFFMAN = "Huffman"
    CAESAR_CYPHER = "Caesar Cypher"
#endregion