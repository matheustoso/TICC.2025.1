from enum import StrEnum

#region OPERATION
class Operation(StrEnum):
    ENCODE_ENCRYPT = "Encode/Encrypt",
    DECODE_DECRYPT = "Decode/Decrypt",
#endregion

#region ALGORITHM
class Encoding(StrEnum):
    NONE = "None",
    GOLOMB = "Golomb",
    ELIASGAMMA = "Elias-Gamma",
    FIBONACCI = "Fibonacci/Zeckendorf",
    HUFFMAN = "Huffman"
#endregion

#region ENCRYPTION
class Encryption(StrEnum):
    NONE = "None",
    CAESAR_CYPHER = "Caesar Cypher"
#endregion

#region ERROR_DETECTION
class ErrorDetection(StrEnum):
    NONE = "None",
    REPETITION = "Repetition R3 - With correction",
    HAMMING = "Hamming (7,4) - With correction",
    CRC = "CRC - Only detection"
#endregion