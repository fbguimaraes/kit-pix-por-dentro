"""Etapa 3 — montar o payload completo do Pix estático.

Ordem dos campos (Manual de Padrões para Iniciação do Pix, seção 2.6.3):

    00  Payload Format Indicator   "01"
    26  Merchant Account Info      00 = "br.gov.bcb.pix", 01 = chave, 02 = info adicional (opcional)
    52  Merchant Category Code     "0000"
    53  Transaction Currency       "986" (real)
    54  Transaction Amount         opcional, ex.: "25.90"
    58  Country Code               "BR"
    59  Merchant Name              1 a 25 caracteres
    60  Merchant City              1 a 15 caracteres
    62  Additional Data Field      05 = txid ("***" quando não usado)
    63  CRC16                      calculado sobre tudo antes, incluindo "6304"
"""

from decimal import Decimal

from pix.crc import crc16_ccitt  # noqa: F401  (você vai usar)
from pix.emv import tlv  # noqa: F401  (você vai usar)

GUI_PIX = "br.gov.bcb.pix"


def normalizar_texto(texto: str) -> str:
    """Remove acentos e espaços sobrando: "  São   Paulo " → "Sao Paulo".

    Por quê: o tamanho no TLV conta caracteres, mas "ã" vira 2 bytes em UTF-8.
    Ficar só com ASCII elimina essa ambiguidade e evita recusa em apps de banco.
    Dica: unicodedata.normalize("NFKD", ...) separa a letra do acento.
    """
    raise NotImplementedError("Etapa 3: implemente normalizar_texto")


def formatar_valor(valor: Decimal) -> str:
    """Formata o valor do campo 54 com exatamente 2 casas: Decimal("10") → "10.00".

    Regras:
    - só aceita Decimal; float levanta TypeError (dinheiro não usa ponto flutuante)
    - zero ou negativo → ValueError
    - mais de 2 casas decimais → ValueError (não arredonde dinheiro escondido)
    - resultado com mais de 13 caracteres → ValueError (limite do campo 54)
    """
    raise NotImplementedError("Etapa 3: implemente formatar_valor")


def build_static_payload(
    chave: str,
    nome: str,
    cidade: str,
    valor: Decimal | None = None,
    txid: str = "***",
    info_adicional: str | None = None,
) -> str:
    """Monta o Pix copia e cola estático, com o CRC no final.

    Regras:
    - chave vazia → ValueError
    - nome e cidade passam por normalizar_texto antes de validar o tamanho
    - nome: 1 a 25 caracteres; cidade: 1 a 15 caracteres → senão ValueError (não trunque)
    - txid: "***" ou de 1 a 25 caracteres de A-Z, a-z, 0-9 → senão ValueError
    - info_adicional também é normalizada; se o campo 26 passar de 99 caracteres, o tlv já
      levanta ValueError
    """
    raise NotImplementedError("Etapa 3: implemente build_static_payload")
