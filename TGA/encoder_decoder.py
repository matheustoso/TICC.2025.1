from enum import StrEnum

from textual import events, on
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, VerticalScroll
from textual.css.query import NoMatches
from textual.reactive import var
from textual.widgets import Button, TextArea, Header, Footer, RadioButton, RadioSet, Input, Label, Pretty

#region Constants

ASCII255_REGEX = r"[\x00-ÿ]*"
BINARY_REGEX = r"[01]*"

APP_ID = "app"

TEXT_ID = "text"

INPUT_ID = "input"
INPUT_AREA_ID = "inputArea"
INPUT_AREA_ID_CODE = "#inputArea"
INPUT_TEXT_ID = "inputText"
INPUT_TEXT_ID_CODE = "#inputText"
INPUT_LABEL = "Input"
INPUT_PLACEHOLDER = "Text to encode/decode"

OUTPUT_ID = "output"
OUTPUT_TEXT_ID = "outputText"
OUTPUT_TEXT_ID_CODE = "#outputText"
OUTPUT_LABEL = "Output"

ALPHABET_ID = "alphabet"
ALPHABET_LABEL = "Alphabet"

OPTIONS_ID = "options"
OPTIONS_LABEL = "Options"

OPERATION_ID = "operation"
OPERATION_ID_CODE = "#operation"
OPERATION_LABEL = "Operation"

ALGORITHM_ID = "algorithm"
ALGORITHM_ID_CODE = "#algorithm"
ALGORITHM_LABEL = "algorithm"

EXECUTE_ID = "execute"
EXECUTE_ID_CODE = "#execute"
EXECUTE_LABEL = "Execute"

#endregion

#region Enums

class Operation(StrEnum):
    ENCODE = "Encode",
    DECODE = "Decode"
    
class Algorithm(StrEnum):
    GOLOMB = "Golomb",
    ELIASGAMMA = "Elias-Gamma",
    FIBONACCI = "Fibonacci/Zeckendorf",
    HUFFMAN = "Huffman"

#endregion

class EncoderDecoder(App):

    operation = Operation.ENCODE
    algorithm = Algorithm.GOLOMB
    alphabet = {}
    for i in range(256):
        alphabet[chr(i)] = i  
    input = ""
    output = ""

    #region GUI

    AUTO_FOCUS = "Input"

    CSS_PATH = "encoder_decoder.tcss"
    
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id=APP_ID):
            with Horizontal(id=TEXT_ID):
                with VerticalScroll(id=INPUT_ID):
                    yield Label(INPUT_LABEL)
                    yield Input(id=INPUT_AREA_ID, restrict=ASCII255_REGEX, placeholder=INPUT_PLACEHOLDER)
                    yield TextArea(id=INPUT_TEXT_ID, read_only=True)
                with VerticalScroll(id=OUTPUT_ID):
                    yield Label(OUTPUT_LABEL)
                    yield TextArea(id=OUTPUT_TEXT_ID, read_only=True)
                with VerticalScroll(id=ALPHABET_ID):
                    yield Label(ALPHABET_LABEL)
                    yield Pretty(self.alphabet) 
            yield Label(OPTIONS_LABEL)      
            with Horizontal(id=OPTIONS_ID):
                with RadioSet(id=OPERATION_ID):
                    yield Label(OPERATION_LABEL)
                    yield RadioButton(Operation.ENCODE.value, value=True)
                    yield RadioButton(Operation.DECODE.value)
                with RadioSet(id=ALGORITHM_ID):
                    yield Label(ALGORITHM_LABEL)
                    yield RadioButton(Algorithm.GOLOMB.value, value=True)
                    yield RadioButton(Algorithm.ELIASGAMMA.value)
                    yield RadioButton(Algorithm.FIBONACCI.value)
                    yield RadioButton(Algorithm.HUFFMAN.value)
                yield Button(id=EXECUTE_ID, label=EXECUTE_LABEL)
        yield Footer()

    @on(RadioSet.Changed, OPERATION_ID_CODE)
    def on_operation_changed(self, event: RadioSet.Changed) -> None:
        self.operation = Operation(event.pressed.label)
        match self.operation:
            case Operation.ENCODE:
                self.query_one(INPUT_AREA_ID_CODE).clear()
                self.query_one(INPUT_TEXT_ID_CODE).clear()
                self.query_one(OUTPUT_TEXT_ID_CODE).clear()
                self.query_one(INPUT_AREA_ID_CODE).restrict = ASCII255_REGEX
            case Operation.DECODE:
                self.query_one(INPUT_AREA_ID_CODE).clear()
                self.query_one(INPUT_TEXT_ID_CODE).clear()
                self.query_one(OUTPUT_TEXT_ID_CODE).clear()
                self.query_one(INPUT_AREA_ID_CODE).restrict = BINARY_REGEX
        
    @on(RadioSet.Changed, ALGORITHM_ID_CODE)
    def on_algorithm_changed(self, event: RadioSet.Changed) -> None:
        self.query_one(OUTPUT_TEXT_ID_CODE).clear()
        self.algorithm = Algorithm(event.pressed.label)
        
    @on(Input.Changed, INPUT_AREA_ID_CODE)
    def on_input_changed(self, event: Input.Changed) -> None:
        self.input = event.input.value
        self.query_one(INPUT_TEXT_ID_CODE).clear()
        self.query_one(INPUT_TEXT_ID_CODE).insert(self.input)
        
    @on(Input.Submitted, INPUT_AREA_ID_CODE)
    def on_input_submitted(self) -> None:
        self.execute()
        
    @on(Button.Pressed, EXECUTE_ID_CODE)
    def on_button_press(self) -> None:
        self.execute()
        
    #endregion
        
    def execute(self) -> None:
        self.query_one(OUTPUT_TEXT_ID_CODE).clear()
        self.query_one(OUTPUT_TEXT_ID_CODE).insert(self.input)

if __name__ == "__main__":
    EncoderDecoder().run(inline=True)