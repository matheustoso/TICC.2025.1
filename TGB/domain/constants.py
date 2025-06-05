ASCII_REGEX = r"[\x00-ÿ]*"
ASCII_LENGTH = 256
BINARY_REGEX = r"[01]*"
CAESAR_KEY_REGEX = r"^[0-9]|^1[0-9]|^2[0-5]|^$"

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
INPUT_ENCODE_PLACEHOLDER = "Bits/Text to encode/encrypt"
INPUT_DECODE_PLACEHOLDER = "Bits/Text to decode/decrypt"
CAESAR_KEY_PLACEHOLDER = "Caesar Cypher key (0-25)"

KEY_AREA_ID = "keyArea"
KEY_AREA_ID_CODE = "#keyArea"

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

ENCRYPTION_ID = "encryption"
ENCRYPTION_ID_CODE = "#encryption"
ENCRYPTION_LABEL = "Encryption"

ALGORITHM_ID = "algorithm"
ALGORITHM_ID_CODE = "#algorithm"
ALGORITHM_LABEL = "Encoding"

ERRORDETECTION_ID = "errorDetection"
ERRORDETECTION_ID_CODE = "#errorDetection"
ERRORDETECTION_LABEL = "Error Detection"

EXECUTE_ID = "execute"
EXECUTE_ID_CODE = "#execute"
EXECUTE_LABEL = "Execute"

ERROR_BUTTON_ID = "errorButton"
ERROR_BUTTON_ID_CODE = "#errorButton"
ERROR_BUTTON_LABEL = "Add bit errors"

BUTTON_AREA_ID = "buttons"
RANDOM_BUTTON_ID = "randomButton"
RANDOM_BUTTON_ID_CODE = "#randomButton"
RANDOM_BUTTON_LABEL = "Get random message"
RANDOM_MESSAGE_MAX_SIZE = 32

LOG_CONTAINER_ID = "logContainer"
LOG_ID = "log"
LOG_CONTAINER_ID_CODE = "#logContainer"
LOG_ID_CODE = "#log"
LOG_LABEL = "Logs"

LOG_MESSAGE = "The {} algorithm encountered an unexpected error during the {} operation:"
LOG_NOISE = "Noise was detected and corrected for the bits in the following positions: {}"
LOG_MAX_LINES = 100

EXCEPTION_MESSAGE_ATTRIBUTE = "message"

KEYBINDINGS = [("q", "quit", "Quit"),]