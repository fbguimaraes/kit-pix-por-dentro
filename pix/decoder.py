"""Etapa 5 (bônus) — ler um Pix copia e cola de verdade.

É aqui que o post fica bom: cole o copia e cola de um Pix que você pagou e veja os campos.
"""


def decodificar(payload: str) -> dict:
    """Valida o CRC e extrai os campos principais.

    Passos:
    1. strip() no texto; se não terminar com "6304" + 4 caracteres → ValueError
    2. confira o CRC (compare em maiúsculas); se não bater → ValueError("CRC inválido")
    3. parse_tlv na raiz; procure nos IDs 26 a 51 o template cujo subcampo 00 seja
       "br.gov.bcb.pix" (sem diferenciar maiúsculas); se não achar → ValueError
    4. devolva um dict com as chaves:
       chave, info_adicional, url (subcampo 25, Pix dinâmico), valor (Decimal ou None),
       nome, cidade, txid (subcampo 05 do campo 62), uso_unico (campo 01 == "12")
       Campos ausentes viram None.
    """
    raise NotImplementedError("Etapa 5 (bônus): implemente decodificar")
