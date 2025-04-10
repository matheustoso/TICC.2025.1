ASCII_REGEX = r"[\x00-ÿ]*"
ASCII_LENGTH = 256
BINARY_REGEX = r"[01]*"

THEME = "gruvbox"

APP_ID = "app"

TEXT_CONTAINER_ID = "textContainer"
OPTIONS_CONTAINER_ID = "optionsContainer"


TEXT_ID = "text"

INPUT_ID = "input"
INPUT_AREA_ID = "inputArea"
INPUT_AREA_ID_CODE = "#inputArea"
INPUT_TEXT_ID = "inputText"
INPUT_TEXT_ID_CODE = "#inputText"
INPUT_LABEL = "Input"
INPUT_ENCODE_PLACEHOLDER = "Text to encode"
INPUT_DECODE_PLACEHOLDER = "Bits to decode"

OUTPUT_ID = "output"
OUTPUT_TEXT_ID = "outputText"
OUTPUT_TEXT_ID_CODE = "#outputText"
OUTPUT_LABEL = "Output"

ALPHABET_ID = "alphabet"
ALPHABET_TEXT_ID = "alphabetText"
ALPHABET_TEXT_ID_CODE = "#alphabetText"
ALPHABET_LABEL = "Alphabet"

OPTIONS_ID = "options"
OPTIONS_LABEL = "Options"

OPERATION_ID = "operation"
OPERATION_ID_CODE = "#operation"
OPERATION_LABEL = "Operation"

ALGORITHM_ID = "algorithm"
ALGORITHM_ID_CODE = "#algorithm"
ALGORITHM_LABEL = "Algorithm"

EXECUTE_ID = "execute"
EXECUTE_ID_CODE = "#execute"
EXECUTE_LABEL = "Execute"

BUTTON_AREA_ID = "buttons"
RANDOM_BUTTON_ID = "randomButton"
RANDOM_BUTTON_ID_CODE = "#randomButton"
RANDOM_BUTTON_LABEL = "Get random message"
RANDOM_MESSAGE_MAX_SIZE = 200

LOG_CONTAINER_ID = "logContainer"
LOG_ID = "log"
LOG_CONTAINER_ID_CODE = "#logContainer"
LOG_ID_CODE = "#log"

LOG_MESSAGE = "The {} algorithm encountered an unexpected error during the {} operation."
LOG_MAX_LINES = 3

KEYBINDINGS = [("q", "quit", "Quit"),]