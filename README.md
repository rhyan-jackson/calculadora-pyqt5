# Calculadora com Interface Gráfica

Este projeto é uma calculadora com interface gráfica desenvolvida em Python usando a biblioteca PyQt5. A calculadora suporta operações matemáticas básicas e inclui suporte para parênteses e validação de entradas.

## Estrutura do Projeto

```plaintext
CALCULADORA-PYQT5
├── config/
│   └── config.py           Permite alterar a fonte e as cores da interface da calculadora.
├── tests/
│   └── test-cases.py       Contém testes unitários para verificar o funcionamento correto da calculadora.    
│
├── calculadora.py          Define a classe `Calculadora`.
├── main.py                 Inicializa e exibe a calculadora.
├── melhorias.txt           Local para anotar as futuras alterações ao programa.
└── README.md
```

## Funcionalidades

- **Operações básicas:** Adição, subtração, multiplicação e divisão.
- **Parênteses:** Suporte para expressões com parênteses de fecho automático.
- **Validação de entrada:** Previne entradas inválidas, como operadores consecutivos ou parênteses vazios.
- **Resultado inteligente:** Interpretação de entradas incompletas e retorno de resultados válidos sempre que possível.
- **Estilo personalizado:** Interface com cores, fontes e tamanhos personalizáveis em '/config/config.py'.

## Requisitos

- Python 3.8 ou superior.
- PyQt5.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/rhyan-jackson/calculadora-pyqt5.git
   ```
2. Instale as dependências:
   ```bash
   pip install PyQt5
   ```

### Uso

1. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```
2. A interface da calculadora será exibida.

## Testes

Para executar os testes, use o seguinte comando:
```bash
python tests/test-cases.py
```

Os testes cobrem cenários comuns e casos limite, garantindo o comportamento esperado da calculadora.

### Exemplos de Testes

- `2+2` resulta em `4`.
- `8x(2+3)` resulta em `40`.
- `(45+(8x(-6x((((` resulta em `-3`.
- Entradas inválidas como `10÷0` retomam `Conta inválida.`.
