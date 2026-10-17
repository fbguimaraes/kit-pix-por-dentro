"""Etapa 2 — o formato TLV (ID, tamanho, valor) do padrão EMV.

Todo campo do BR Code é escrito assim:  ID (2 dígitos) + TAMANHO (2 dígitos) + VALOR.
Exemplo: o país "BR" no campo 58 vira "5802BR".
Um valor pode conter outros TLVs dentro (o campo 26 contém os subcampos 00 e 01).
"""


def tlv(id_: str, valor: str) -> str:
    """Monta um campo TLV.

    Regras:
    - `id_` precisa ter exatamente 2 dígitos ("00" a "99"), senão ValueError.
    - `valor` precisa ter de 1 a 99 caracteres, senão ValueError (o tamanho tem só 2 dígitos).
    - o tamanho é escrito com zero à esquerda: 5 → "05".

    >>> tlv("58", "BR")
    '5802BR'
    """
    raise NotImplementedError("Etapa 2: implemente tlv")


def parse_tlv(payload: str) -> list[tuple[str, str]]:
    """Faz o caminho inverso: quebra uma sequência de TLVs em uma lista de (id, valor).

    Lê só o nível atual (não desce nos campos aninhados).
    Levanta ValueError se o texto terminar no meio de um campo.

    >>> parse_tlv("5802BR5913Fulano de Tal")
    [('58', 'BR'), ('59', 'Fulano de Tal')]
    """
    raise NotImplementedError("Etapa 2: implemente parse_tlv")
