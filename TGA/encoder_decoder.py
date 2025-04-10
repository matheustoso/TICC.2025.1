from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, VerticalScroll
from textual.widgets import Button, TextArea, Header, Footer, RadioButton, RadioSet, Input, Label, Pretty

from domain.constants import *
from domain.enums import *

from services import golomb, eliasgamma, fibonacci, huffman

import rstr

class EncoderDecoder(App):

    operation = Operation.ENCODE
    algorithm = Algorithm.GOLOMB
    
    user_alphabet = {}
    huffman_alphabet = {}
    alphabet = {}
    for i in range(256):
        alphabet[chr(i)] = i  
    
    input = ""
    output = ""
    
    def execute(self) -> None: 
        match self.algorithm:
            case Algorithm.GOLOMB:
                match self.operation:
                    case Operation.ENCODE:
                        self.output = golomb.encode(self.input, self.alphabet)
                    case Operation.DECODE:
                        self.output = golomb.decode(self.input, self.alphabet)
                                        
            case Algorithm.ELIASGAMMA:
                match self.operation:
                    case Operation.ENCODE:
                        self.output = eliasgamma.encode(self.input, self.alphabet)
                    case Operation.DECODE:
                        self.output = eliasgamma.decode(self.input, self.alphabet)
                                     
            case Algorithm.FIBONACCI:
                match self.operation:
                    case Operation.ENCODE:
                        self.output = fibonacci.encode(self.input, self.alphabet)
                    case Operation.DECODE:
                        self.output = fibonacci.decode(self.input, self.alphabet)
                              
            case Algorithm.HUFFMAN:   
                match self.operation:
                    case Operation.ENCODE:
                        self.output, self.huffman_alphabet, self.user_alphabet = huffman.encode(self.input)
                        self.query_one(ALPHABET_TEXT_ID_CODE).update(self.user_alphabet)   
                    case Operation.DECODE:
                        self.output = huffman.decode(self.input, self.huffman_alphabet)
                        
        self.query_one(OUTPUT_TEXT_ID_CODE).clear()
        self.query_one(OUTPUT_TEXT_ID_CODE).insert(self.output)
        
    #region GUI

    AUTO_FOCUS = "Input"
    
    CSS_PATH = "ui/style.tcss"
    
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id=APP_ID):
            with Horizontal(id=TEXT_ID):
                with VerticalScroll(id=INPUT_ID):
                    yield Label(INPUT_LABEL)
                    yield Input(id=INPUT_AREA_ID, restrict=ASCII255_REGEX, placeholder=INPUT_ENCODE_PLACEHOLDER)
                    yield TextArea(id=INPUT_TEXT_ID, read_only=True)
                with VerticalScroll(id=OUTPUT_ID):
                    yield Label(OUTPUT_LABEL)
                    yield TextArea(id=OUTPUT_TEXT_ID, read_only=True)
                with VerticalScroll(id=ALPHABET_ID):
                    yield Label(ALPHABET_LABEL)
                    yield Pretty(id=ALPHABET_TEXT_ID, object=self.alphabet) 
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
                with Vertical(id="buttons"):
                    yield Button(id=RANDOM_BUTTON_ID, label=RANDOM_BUTTON_LABEL)    
                    yield Button(id=EXECUTE_ID, label=EXECUTE_LABEL)
        yield Footer()

    @on(RadioSet.Changed, OPERATION_ID_CODE)
    def on_operation_changed(self, event: RadioSet.Changed) -> None:
        self.operation = Operation(event.pressed.label)
        match self.operation:
            case Operation.ENCODE:
                self.query_one(INPUT_AREA_ID_CODE).clear()
                self.query_one(INPUT_TEXT_ID_CODE).clear()
                self.query_one(INPUT_AREA_ID_CODE).restrict = ASCII255_REGEX
                self.query_one(INPUT_AREA_ID_CODE).placeholder = INPUT_ENCODE_PLACEHOLDER
            case Operation.DECODE:
                self.query_one(INPUT_AREA_ID_CODE).clear()
                self.query_one(INPUT_TEXT_ID_CODE).clear()
                self.query_one(INPUT_AREA_ID_CODE).restrict = BINARY_REGEX
                self.query_one(INPUT_AREA_ID_CODE).placeholder = INPUT_DECODE_PLACEHOLDER
        
    @on(RadioSet.Changed, ALGORITHM_ID_CODE)
    def on_algorithm_changed(self, event: RadioSet.Changed) -> None:
        self.query_one(OUTPUT_TEXT_ID_CODE).clear()
        self.algorithm = Algorithm(event.pressed.label)
        if self.algorithm is Algorithm.HUFFMAN:
            self.query_one(ALPHABET_TEXT_ID_CODE).update(self.user_alphabet)
        else:
            self.query_one(ALPHABET_TEXT_ID_CODE).update(self.alphabet)
        
    @on(Input.Changed, INPUT_AREA_ID_CODE)
    def on_input_changed(self, event: Input.Changed) -> None:
        self.input = event.input.value
        self.query_one(INPUT_TEXT_ID_CODE).clear()
        self.query_one(INPUT_TEXT_ID_CODE).insert(self.input)
        
    @on(Input.Submitted, INPUT_AREA_ID_CODE)
    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.query_one(EXECUTE_ID_CODE).press()
        
    @on(Button.Pressed, EXECUTE_ID_CODE)
    def on_execute_press(self, event: Button.Pressed) -> None:
        self.execute()
        
    @on(Button.Pressed, RANDOM_BUTTON_ID_CODE)
    def on_random_press(self) -> None:
        message = rstr.rstr(rstr.nonwhitespace()+rstr.punctuation(), 50)
        self.input = message
        self.query_one(INPUT_AREA_ID_CODE).clear()
        self.query_one(INPUT_AREA_ID_CODE).insert(message, 0)
        
    #endregion

if __name__ == "__main__":
    EncoderDecoder().run(inline=True)