## Instalação

Basta baixar o arquivo .exe na release [TGA-1.0](https://github.com/matheustoso/TICC.2025.1/releases/tag/v1.0):

## Uso

Ao executar o arquivo baixado, será exibida uma interface gráfica no terminal, na qual você pode:

- Escolher entre codificação (Encode) e decodificação (Decode):
    
    - Na codificação, é permitida a entrada de todos os caracteres ASCII, conforme alfabeto exibido em tela;
    - Na decodificação é permitida a entrada de códigos binários.
    
- Escolher entre os quatro algoritmos de codificação disponíveis:

    - Golomb;
    - Elias-Gamma;
    - Fibonacci/Zeckendorf
    - Huffmanm Estático

        - Como esse algoritmo gera o alfabeto na codificação, é necessário primeiro codificar uma mensagem para realizar qualquer decodificação. A decodificação sempre utilizará o alfabeto da última codificação.

## Debug

Caso queira debugar o código será necessário clonar o repositório, instalar as dependências e executar o arquivo encoder_decoder.py

### Dependências

- Python >= 3.12
- lib Textual: pip install textual
- lib rstr: pip install rstr
