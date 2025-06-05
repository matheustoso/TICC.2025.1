def encode(input_text) -> str:
    input_list = list(input_text)
    input_size = len(input_text)
    encoded_input = ""

    if input_size % 4 != 0:
        return input_text

    for i in range(0, input_size, 4):
        d1 = input_list[i]
        d2 = input_list[i + 1]
        d3 = input_list[i + 2]
        d4 = input_list[i + 3]
        p1 = str(str.count(f"{d1}{d2}{d4}", "1") % 2)
        p2 = str(str.count(f"{d1}{d3}{d4}", "1") % 2)
        p3 = str(str.count(f"{d2}{d3}{d4}", "1") % 2)
        encoded_input += f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"

    return encoded_input


def decode(input_text) -> tuple[str, list]:
    input_list = list(input_text)
    input_size = len(input_text)
    decoded_input = ""
    bit_errors = list()

    if input_size % 7 != 0:
        return input_text, bit_errors

    for i in range(0, input_size, 7):
        p1 = input_list[i]
        p2 = input_list[i + 1]
        d1 = input_list[i + 2]
        p3 = input_list[i + 3]
        d2 = input_list[i + 4]
        d3 = input_list[i + 5]
        d4 = input_list[i + 6]

        error_bit = -1
        retry = 0
        max_retry = 32

        while error_bit != 0 and retry < max_retry:
            match error_bit:
                case 1:
                    p1 = "0" if p1 == "1" else "1"
                case 2:
                    p2 = "0" if p2 == "1" else "1"
                case 3:
                    d1 = "0" if d1 == "1" else "1"
                case 4:
                    p3 = "0" if p3 == "1" else "1"
                case 5:
                    d2 = "0" if d2 == "1" else "1"
                case 6:
                    d3 = "0" if d3 == "1" else "1"
                case 7:
                    d4 = "0" if d4 == "1" else "1"

            g1 = str(str.count(f"{p1}{d1}{d2}{d4}", "1") % 2)
            g2 = str(str.count(f"{p2}{d1}{d3}{d4}", "1") % 2)
            g3 = str(str.count(f"{p3}{d2}{d3}{d4}", "1") % 2)

            error_bit = int(f"{g3}{g2}{g1}", 2)
            if error_bit != 0:
                bit_errors.append(str(i + error_bit))
            retry += 1

        decoded_input += f"{d1}{d2}{d3}{d4}"

    return decoded_input, bit_errors
