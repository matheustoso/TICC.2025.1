polynomial = "11100111"

def encode(input_text) -> str:
    return input_text + crc(f"{input_text}{'0' * (len(polynomial) - 1)}")


def decode(input_text) -> tuple[str, list]:
    remainder = crc(input_text)
    decoded_input = input_text[:-3]
    bit_errors = []

    if "1" in remainder:
        for c in remainder:
            bit_errors.append(c)

    return decoded_input, bit_errors


def xor(x, y) -> str:
    result = ""

    y_size = len(y)

    for i in range(1, y_size):
        result += "0" if x[i] == y[i] else "1"

    return result


def crc(input_text) -> str:

    input_text_size = len(input_text)
    polynomial_size = len(polynomial)

    remainder = input_text[0:polynomial_size]

    for i in range(polynomial_size, input_text_size):
        if remainder[0] == "1":
            remainder = f"{xor(polynomial, remainder)}{input_text[i]}"
        else:
            remainder = f"{xor('0' * i, remainder)}{input_text[i]}"

    if remainder[0] == "1":
        remainder = xor(polynomial, remainder)
    else:
        remainder = xor("0" * i, remainder)

    return remainder
