from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.containers import Vertical, Horizontal, VerticalScroll
from textual.widgets import (
    Button,
    TextArea,
    Header,
    Footer,
    RadioButton,
    RadioSet,
    Input,
    Label,
    Pretty,
    Log,
)

from domain.constants import *
from domain.enums import *
from ui.style import *
from services import (
    golomb,
    eliasgamma,
    fibonacci,
    huffman,
    caesar_cypher,
    repetition,
    hamming,
    crc,
)

import rstr, string, random, lorem


class EncoderDecoder(App):
    # region ENCODING/DECODING SERVICE
    operation = Operation.ENCODE_ENCRYPT
    error_detection = ErrorDetection.NONE
    encryption = Encryption.NONE
    encoding = Encoding.NONE

    user_huffman_alphabet = {}
    huffman_alphabet = {}
    alphabet = {}
    for i in range(ASCII_LENGTH):
        alphabet[chr(i)] = i

    input = ""
    output = ""
    key = 0

    def execute(self) -> None:
        logger = self.query_one(LOG_ID_CODE)

        try:
            input_text = self.input

            match self.operation:
                case Operation.ENCODE_ENCRYPT:
                    if self.encryption is not Encryption.NONE:
                        input_text = self.encrypt(input_text)
                    if self.encoding is not Encoding.NONE:
                        input_text = self.encode(input_text)
                        if self.error_detection is not ErrorDetection.NONE:
                            input_text = self.error_encode(input_text)

                case Operation.DECODE_DECRYPT:
                    if self.encoding is not Encoding.NONE:
                        if self.error_detection is not ErrorDetection.NONE:
                            input_text, bit_errors = self.error_decode(input_text)
                            if len(bit_errors) > 0:
                                logger.write_line(
                                    LOG_NOISE.format(", ".join(bit_errors))
                                )
                        input_text = self.decode(input_text)
                    if self.encryption is not Encryption.NONE:
                        input_text = self.decrypt(input_text)

            self.output = input_text
            output_text = self.query_one(OUTPUT_TEXT_ID_CODE)
            output_text.clear()
            output_text.insert(self.output)

        except Exception as e:
            logger.write_line(
                LOG_MESSAGE.format(self.encoding.value, self.operation.value.lower())
            )
            logger.write_line(getattr(e, EXCEPTION_MESSAGE_ATTRIBUTE, repr(e)))

    def encrypt(self, input_text) -> str:
        match self.encryption:
            case Encryption.CAESAR_CYPHER:
                return caesar_cypher.encrypt(input_text, self.key)
            case Encryption.NONE:
                return input_text

    def decrypt(self, input_text) -> str:
        match self.encryption:
            case Encryption.CAESAR_CYPHER:
                return caesar_cypher.decrypt(input_text, self.key)
            case Encryption.NONE:
                return input_text

    def encode(self, input_text) -> str:
        match self.encoding:
            case Encoding.GOLOMB:
                return golomb.encode(input_text, self.alphabet)
            case Encoding.ELIASGAMMA:
                return eliasgamma.encode(input_text, self.alphabet)
            case Encoding.FIBONACCI:
                return fibonacci.encode(input_text, self.alphabet)
            case Encoding.HUFFMAN:
                input_text, self.huffman_alphabet, self.user_huffman_alphabet = (
                    huffman.encode(input_text)
                )
                self.query_one(ALPHABET_TEXT_ID_CODE).update(self.user_huffman_alphabet)
                return input_text
            case Encoding.NONE:
                return input_text

    def decode(self, input_text) -> str:
        match self.encoding:
            case Encoding.GOLOMB:
                return golomb.decode(input_text, self.alphabet)
            case Encoding.ELIASGAMMA:
                return eliasgamma.decode(input_text, self.alphabet)
            case Encoding.FIBONACCI:
                return fibonacci.decode(input_text, self.alphabet)
            case Encoding.HUFFMAN:
                return huffman.decode(input_text, self.huffman_alphabet)
            case Encoding.NONE:
                return input_text

    def error_encode(self, input_text) -> str:
        match self.error_detection:
            case ErrorDetection.REPETITION:
                return repetition.encode(input_text)
            case ErrorDetection.HAMMING:
                return hamming.encode(input_text)
            case ErrorDetection.CRC:
                return crc.encode(input_text)
            case ErrorDetection.NONE:
                return input_text

    def error_decode(self, input_text) -> tuple[str, list]:
        match self.error_detection:
            case ErrorDetection.REPETITION:
                return repetition.decode(input_text)
            case ErrorDetection.HAMMING:
                return hamming.decode(input_text)
            case ErrorDetection.CRC:
                return crc.decode(input_text)
            case ErrorDetection.NONE:
                return (input_text, [])

    # endregion

    # region UI
    CSS = STYLESHEET
    AUTO_FOCUS = INPUT_AREA_ID_CODE
    BINDINGS = KEYBINDINGS

    def compose(self) -> ComposeResult:
        self.theme = THEME
        yield Header()
        with Vertical(id=APP_ID):
            with VerticalScroll(id=TEXT_CONTAINER_ID):
                with Horizontal(id=TEXT_ID):
                    with VerticalScroll(id=INPUT_ID):
                        yield Label(INPUT_LABEL)
                        yield Input(
                            id=INPUT_AREA_ID,
                            restrict=ASCII_REGEX,
                            placeholder=INPUT_ENCODE_PLACEHOLDER,
                        )
                        yield TextArea(id=INPUT_TEXT_ID, read_only=True)

                    with VerticalScroll(id=OUTPUT_ID):
                        yield Label(OUTPUT_LABEL)
                        yield TextArea(id=OUTPUT_TEXT_ID, read_only=True)

                    with VerticalScroll(id=ALPHABET_ID):
                        yield Label(ALPHABET_LABEL)
                        yield Pretty(id=ALPHABET_TEXT_ID, object=self.alphabet)

            with VerticalScroll(id=OPTIONS_CONTAINER_ID):
                with Horizontal(id=OPTIONS_ID):
                    with RadioSet(id=OPERATION_ID):
                        yield Label(OPERATION_LABEL)
                        yield RadioButton(Operation.ENCODE_ENCRYPT.value, value=True)
                        yield RadioButton(Operation.DECODE_DECRYPT.value)

                    with RadioSet(id=ALGORITHM_ID):
                        yield Label(ALGORITHM_LABEL)
                        yield RadioButton(Encoding.NONE.value, value=True)
                        yield RadioButton(Encoding.GOLOMB.value)
                        yield RadioButton(Encoding.ELIASGAMMA.value)
                        yield RadioButton(Encoding.FIBONACCI.value)
                        yield RadioButton(Encoding.HUFFMAN.value)

                    with RadioSet(id=ENCRYPTION_ID):
                        yield Label(ENCRYPTION_LABEL)
                        yield RadioButton(Encryption.NONE.value, value=True)
                        yield RadioButton(Encryption.CAESAR_CYPHER.value)

                    with RadioSet(id=ERRORDETECTION_ID):
                        yield Label(ERRORDETECTION_LABEL)
                        yield RadioButton(ErrorDetection.NONE.value, value=True)
                        yield RadioButton(ErrorDetection.REPETITION.value)
                        yield RadioButton(ErrorDetection.HAMMING.value)
                        yield RadioButton(ErrorDetection.CRC.value)

                    with Vertical(id=BUTTON_AREA_ID):
                        yield Input(
                            id=KEY_AREA_ID,
                            restrict=CAESAR_KEY_REGEX,
                            placeholder=CAESAR_KEY_PLACEHOLDER,
                        )

                        with Horizontal():
                            yield Button(id=RANDOM_BUTTON_ID, label=RANDOM_BUTTON_LABEL)
                            yield Button(id=ERROR_BUTTON_ID, label=ERROR_BUTTON_LABEL)

                        yield Button(id=EXECUTE_ID, label=EXECUTE_LABEL)

            with VerticalScroll(id=LOG_CONTAINER_ID):
                yield Label(LOG_LABEL)
                yield Log(id=LOG_ID, max_lines=LOG_MAX_LINES)

        yield Footer()

    @on(RadioSet.Changed, OPERATION_ID_CODE)
    def on_operation_changed(self, event: RadioSet.Changed) -> None:
        self.operation = Operation(event.pressed.label)

        if self.operation is Operation.ENCODE_ENCRYPT:
            self.query_one(RANDOM_BUTTON_ID_CODE).disabled = False
            self.query_one(ERROR_BUTTON_ID_CODE).disabled = True
            self.query_one(INPUT_AREA_ID_CODE).restrict = ASCII_REGEX
            self.query_one(INPUT_AREA_ID_CODE).placeholder = INPUT_ENCODE_PLACEHOLDER

        if self.operation is Operation.DECODE_DECRYPT:
            self.query_one(RANDOM_BUTTON_ID_CODE).disabled = True
            self.query_one(ERROR_BUTTON_ID_CODE).disabled = False
            self.query_one(INPUT_AREA_ID_CODE).restrict = BINARY_REGEX
            self.query_one(INPUT_AREA_ID_CODE).placeholder = INPUT_DECODE_PLACEHOLDER

        self.query_one(INPUT_AREA_ID_CODE).clear()
        self.query_one(INPUT_AREA_ID_CODE).insert(self.output, 0)
        self.query_one(OUTPUT_TEXT_ID_CODE).clear()
        self.input = self.output
        self.output = ""

    @on(RadioSet.Changed, ERRORDETECTION_ID_CODE)
    def on_error_detection_changed(self, event: RadioSet.Changed) -> None:
        self.error_detection = ErrorDetection(event.pressed.label)

    @on(RadioSet.Changed, ENCRYPTION_ID_CODE)
    def on_encryption_changed(self, event: RadioSet.Changed) -> None:
        self.encryption = Encryption(event.pressed.label)

    @on(RadioSet.Changed, ALGORITHM_ID_CODE)
    def on_algorithm_changed(self, event: RadioSet.Changed) -> None:
        self.encoding = Encoding(event.pressed.label)

    @on(RadioSet.Changed)
    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        if self.encryption is Encryption.CAESAR_CYPHER:
            self.query_one(KEY_AREA_ID_CODE).disabled = False
        else:
            self.query_one(KEY_AREA_ID_CODE).disabled = True

        if self.encoding is Encoding.HUFFMAN:
            self.query_one(ALPHABET_TEXT_ID_CODE).update(self.user_huffman_alphabet)
            self.query_one(ERRORDETECTION_ID_CODE).disabled = False
        elif self.encoding is Encoding.NONE:
            self.query_one(INPUT_AREA_ID_CODE).restrict = ASCII_REGEX
            self.query_one(ALPHABET_TEXT_ID_CODE).update(list(string.ascii_letters))
            self.query_one(ERRORDETECTION_ID_CODE).disabled = True
        else:
            self.query_one(ALPHABET_TEXT_ID_CODE).update(self.alphabet)
            self.query_one(ERRORDETECTION_ID_CODE).disabled = False

    @on(Input.Changed, INPUT_AREA_ID_CODE)
    def on_input_changed(self, event: Input.Changed) -> None:
        self.input = event.input.value
        input_text = self.query_one(INPUT_TEXT_ID_CODE)
        input_text.clear()
        input_text.insert(self.input)

    @on(Input.Changed, KEY_AREA_ID_CODE)
    def on_key_changed(self, event: Input.Changed) -> None:
        self.key = 0 if not event.input.value else int(event.input.value)

    @on(Input.Submitted, INPUT_AREA_ID_CODE)
    def on_input_submitted(self) -> None:
        self.query_one(EXECUTE_ID_CODE).press()

    @on(Button.Pressed, EXECUTE_ID_CODE)
    def on_execute_press(self) -> None:
        self.execute()

    @on(Button.Pressed, RANDOM_BUTTON_ID_CODE)
    def on_random_press(self) -> None:
        if self.operation is Operation.ENCODE_ENCRYPT:
            message = lorem.get_sentence(count=1, comma=(0, 0), word_range=(2, 4))
            self.input = message
            input_area = self.query_one(INPUT_AREA_ID_CODE)
            input_area.clear()
            input_area.insert(message, 0)

    @on(Button.Pressed, ERROR_BUTTON_ID_CODE)
    def on_error_press(self) -> None:
        if self.operation is Operation.DECODE_DECRYPT:
            input_with_noise = list(self.input)
            input_size = len(input_with_noise)

            for i in range(0, input_size, 16):
                bit_to_flip = random.randint(i, i + 7)
                if bit_to_flip < input_size:
                    original_bit = input_with_noise[bit_to_flip]
                    input_with_noise[bit_to_flip] = "0" if original_bit == "1" else "1"

            self.input = "".join(input_with_noise)
            self.query_one(INPUT_AREA_ID_CODE).clear()
            self.query_one(INPUT_AREA_ID_CODE).insert(self.input, 0)

    def on_mount(self) -> None:
        self.query_one(KEY_AREA_ID_CODE).disabled = True
        self.query_one(ERRORDETECTION_ID_CODE).disabled = True
        self.query_one(ERROR_BUTTON_ID_CODE).disabled = True

    # endregion


# region __main__
if __name__ == "__main__":
    EncoderDecoder().run(inline=True)
# endregion
