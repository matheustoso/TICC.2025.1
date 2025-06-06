## Instalação

Basta baixar o arquivo .exe na release [TGA-1.0](https://github.com/matheustoso/TICC.2025.1/releases/tag/v1.0):

## Uso

Ao executar o arquivo baixado, será exibida uma interface gráfica no terminal, na qual você pode:

- Escolher entre codificação/encriptação (Encode/Encrypt) e decodificação/decriptação (Decode/Decrypt):
    
    - Na codificação, é permitida a entrada de todos os caracteres ASCII, conforme alfabeto exibido em tela;
    - Na decodificação é permitida a entrada de códigos binários.
    - Caso não esteja usando algoritmo de codificação, somente de criptografia, a entrada sempre será em ASCII
    
- Escolher entre os quatro algoritmos de codificação disponíveis, ou desativar a codificação:

    - Golomb;
    - Elias-Gamma;
    - Fibonacci/Zeckendorf
    - Huffmanm Estático

        - Como esse algoritmo gera o alfabeto na codificação, é necessário primeiro codificar uma mensagem para realizar qualquer decodificação. A decodificação sempre utilizará o alfabeto da última codificação.

- Escolher se deseja ativar a criptografia com cifra de César, há também um campo de texto para inserir a chave da cifra.

- Caso tenha alguma codificação ativa, é possível escolher um dos 3 algoritmos implementados de detecção de erro:

    - Repetição R3:
        - Esse algoritmo funciona para todos os tipos de codificação, e também realizará correção de erros de até 1bit por bloco de repetição.
    - Hamming (7, 4):
        - Essa implementação usa paridade par, e necessita de uma palavra de entrada múltipla de 4, portanto funciona melhor com codificação Golomb, também realizará correção de erros de até 1bit por bloco hamming.
    - CRC:
        - A implementação do CRC utiliza o polinômio 11100111 (0xe7), e não realiza tratamento de erros, somente detecção. Além disso funciona para todos os tipos de codificação, mas com a introdução de erros, a decodificação após a detecção de erros pode não funcionar, pois não há tratamento dos erros. Caso esteja debugando o código, é possível modificar o polinômio no arquivo crc.py no diretório services, permitindo qualquer tamanho de polinômio.

A detecção de erro, correção de erro, e falhas inesperadas na decodificação, irão gerar logs no bloco de logs. Para a detecção e correção de erros (R3 e H74) será exibida a posição (iniciando em 1) de cada bit que foi corrigido, já para a detecção CRC, será indicado que houve erro na transmissão, e será exibido o resto CRC resultante desse erro.
    

## Debug

Caso queira debugar o código será necessário clonar o repositório, instalar as dependências e executar o arquivo encoder_decoder.py.

### Dependências

- Python >= 3.12
- lib Textual: pip install textual
- lib python-lorem: pip install python-lorem