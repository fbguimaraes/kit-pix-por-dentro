"""Etapa 1 — CRC16 do BR Code.

O último campo de todo Pix copia e cola é o ID 63 (CRC16): 4 caracteres hexadecimais
que protegem o resto do texto contra erro de digitação ou de leitura.

Parâmetros (Manual do BR Code, nota 10, e Manual de Padrões para Iniciação do Pix, nota 28):
- polinômio 0x1021
- valor inicial 0xFFFF
- sem reflexão de bits, sem XOR final  →  variante conhecida como CRC-16/CCITT-FALSE

Armadilha clássica: a entrada do cálculo INCLUI o "6304" (ID e tamanho do próprio campo 63)
e exclui só os 4 caracteres do valor.
"""


def crc16_ccitt(dados: str) -> str:
    """Calcula o CRC-16/CCITT-FALSE de `dados` e devolve 4 dígitos hex em maiúsculas.

    Exemplos:
        >>> crc16_ccitt("123456789")
        '29B1'

    Dica de caminho (não é a solução): trabalhe byte a byte sobre dados.encode("utf-8"),
    com um registrador inteiro de 16 bits. Para cada bit, olhe o bit mais alto (0x8000).
    Não esqueça de manter o registrador em 16 bits depois de cada deslocamento.
    """
    raise NotImplementedError("Etapa 1: implemente o CRC16")
