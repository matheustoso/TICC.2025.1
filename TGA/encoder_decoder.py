from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.containers import Vertical, Horizontal, VerticalScroll
from textual.widgets import Button, TextArea, Header, Footer, RadioButton, RadioSet, Input, Label, Pretty, Log

from domain.constants import *
from domain.enums import *
from ui.style import *
from services import golomb, eliasgamma, fibonacci, huffman, caesar_cypher

import rstr, string

class EncoderDecoder(App):

#region ENCODING/DECODING SERVICE
    operation = Operation.ENCODE_ENCRYPT
    algorithm = Algorithm.GOLOMB
    
    user_huffman_alphabet = {}
    huffman_alphabet = {}
    alphabet = {}
    for i in range(ASCII_LENGTH):
        alphabet[chr(i)] = i  
    
    input = ""
    output = ""
    key = 0

    def execute(self) -> None: 
        try:
            match self.algorithm:
                case Algorithm.GOLOMB:
                    match self.operation:
                        case Operation.ENCODE_ENCRYPT:
                            self.output = golomb.encode(self.input, self.alphabet)
                            
                        case Operation.DECODE_DECRYPT:
                            self.output = golomb.decode(self.input, self.alphabet)

                case Algorithm.ELIASGAMMA:
                    match self.operation:
                        case Operation.ENCODE_ENCRYPT:
                            self.output = eliasgamma.encode(self.input, self.alphabet)
                            
                        case Operation.DECODE_DECRYPT:
                            self.output = eliasgamma.decode(self.input, self.alphabet)

                case Algorithm.FIBONACCI:
                    match self.operation:
                        case Operation.ENCODE_ENCRYPT:
                            self.output = fibonacci.encode(self.input, self.alphabet)
                            
                        case Operation.DECODE_DECRYPT:
                            self.output = fibonacci.decode(self.input, self.alphabet)

                case Algorithm.HUFFMAN:   
                    match self.operation:
                        case Operation.ENCODE_ENCRYPT:
                            self.output, self.huffman_alphabet, self.user_huffman_alphabet = huffman.encode(self.input)
                            self.query_one(ALPHABET_TEXT_ID_CODE).update(self.user_huffman_alphabet)   
                            
                        case Operation.DECODE_DECRYPT:
                            self.output = huffman.decode(self.input, self.huffman_alphabet)
                            
                case Algorithm.CAESAR_CYPHER:
                    match self.operation:
                        case Operation.ENCODE_ENCRYPT:
                            self.output = caesar_cypher.encrypt(self.input, self.key)
                            
                        case Operation.DECODE_DECRYPT:
                            self.output = caesar_cypher.decrypt(self.input, self.key)

            output_text = self.query_one(OUTPUT_TEXT_ID_CODE)
            output_text.clear()
            output_text.insert(self.output)
            self.query_one(LOG_ID_CODE).clear()
            
        except Exception as e: 
            logger = self.query_one(LOG_ID_CODE)
            logger.write_line(LOG_MESSAGE.format(self.algorithm.value, self.operation.value.lower()))
            logger.write_line(getattr(e, EXCEPTION_MESSAGE_ATTRIBUTE, repr(e)))
                
#endregion

#region UI
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
                        yield Input(id=INPUT_AREA_ID, restrict=ASCII_REGEX, placeholder=INPUT_ENCODE_PLACEHOLDER)
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
                        yield RadioButton(Algorithm.GOLOMB.value, value=True)
                        yield RadioButton(Algorithm.ELIASGAMMA.value)
                        yield RadioButton(Algorithm.FIBONACCI.value)
                        yield RadioButton(Algorithm.HUFFMAN.value)
                        yield RadioButton(Algorithm.CAESAR_CYPHER.value)
                        
                    with Vertical(id=BUTTON_AREA_ID):
                        yield Input(id=KEY_AREA_ID, restrict=CAESAR_KEY_REGEX, placeholder=CAESAR_KEY_PLACEHOLDER)
                        yield Button(id=RANDOM_BUTTON_ID, label=RANDOM_BUTTON_LABEL)    
                        yield Button(id=EXECUTE_ID, label=EXECUTE_LABEL)
                        
            with VerticalScroll(id=LOG_CONTAINER_ID):
                yield Label(LOG_LABEL)
                yield Log(id=LOG_ID, max_lines=LOG_MAX_LINES)
                    
        yield Footer()

    @on(RadioSet.Changed, OPERATION_ID_CODE)
    def on_operation_changed(self, event: RadioSet.Changed) -> None:
        self.operation = Operation(event.pressed.label)
        input_area = self.query_one(INPUT_AREA_ID_CODE)
        input_area.clear()

        if self.algorithm is Algorithm.CAESAR_CYPHER:
            self.query_one(RANDOM_BUTTON_ID_CODE).disabled = True
            input_area.restrict = ASCII_REGEX
            match self.operation:
                case Operation.ENCODE_ENCRYPT:
                    input_area.placeholder = INPUT_ENCRYPT_PLACEHOLDER
                case Operation.DECODE_DECRYPT:
                    input_area.placeholder = INPUT_DECRYPT_PLACEHOLDER

        else: 
            match self.operation:
                case Operation.ENCODE_ENCRYPT:
                    self.query_one(RANDOM_BUTTON_ID_CODE).disabled = False
                    input_area.restrict = ASCII_REGEX
                    input_area.placeholder = INPUT_ENCODE_PLACEHOLDER

                case Operation.DECODE_DECRYPT:
                    self.query_one(RANDOM_BUTTON_ID_CODE).disabled = True
                    input_area.restrict = BINARY_REGEX
                    input_area.placeholder = INPUT_DECODE_PLACEHOLDER
        
        input_area.insert(self.output, 0)
        self.query_one(OUTPUT_TEXT_ID_CODE).clear()

        
    @on(RadioSet.Changed, ALGORITHM_ID_CODE)
    def on_algorithm_changed(self, event: RadioSet.Changed) -> None:
        self.query_one(OUTPUT_TEXT_ID_CODE).clear()
        self.algorithm = Algorithm(event.pressed.label)
        if self.algorithm is Algorithm.HUFFMAN:
            self.query_one(INPUT_AREA_ID_CODE).placeholder = INPUT_ENCODE_PLACEHOLDER if self.operation is Operation.ENCODE_ENCRYPT else INPUT_DECODE_PLACEHOLDER
            self.query_one(ALPHABET_TEXT_ID_CODE).update(self.user_huffman_alphabet)
            self.query_one(RANDOM_BUTTON_ID_CODE).disabled = False
            self.query_one(KEY_AREA_ID_CODE).disabled = True
        if self.algorithm is Algorithm.CAESAR_CYPHER:
            self.query_one(INPUT_AREA_ID_CODE).placeholder = INPUT_ENCRYPT_PLACEHOLDER if self.operation is Operation.ENCODE_ENCRYPT else INPUT_DECRYPT_PLACEHOLDER
            self.query_one(INPUT_AREA_ID_CODE).restrict = ASCII_REGEX
            self.query_one(ALPHABET_TEXT_ID_CODE).update(list(string.ascii_letters))
            self.query_one(RANDOM_BUTTON_ID_CODE).disabled = True
            self.query_one(KEY_AREA_ID_CODE).disabled = False
        else:
            self.query_one(INPUT_AREA_ID_CODE).placeholder = INPUT_ENCODE_PLACEHOLDER if self.operation is Operation.ENCODE_ENCRYPT else INPUT_DECODE_PLACEHOLDER
            self.query_one(ALPHABET_TEXT_ID_CODE).update(self.alphabet)
            self.query_one(RANDOM_BUTTON_ID_CODE).disabled = False
            self.query_one(KEY_AREA_ID_CODE).disabled = True
            
        
        
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
        if self.operation is Operation.ENCODE_ENCRYPT and self.algorithm is not Algorithm.CAESAR_CYPHER:
            message = rstr.rstr(rstr.nonwhitespace() + rstr.punctuation(), RANDOM_MESSAGE_MAX_SIZE)
            self.input = message
            input_area = self.query_one(INPUT_AREA_ID_CODE)
            input_area.clear()
            input_area.insert(message, 0)
            
    def on_mount(self) -> None:
        self.query_one(KEY_AREA_ID_CODE).disabled = True
#endregion

#region __main__
if __name__ == "__main__":
    EncoderDecoder().run(inline=True)
#endregion