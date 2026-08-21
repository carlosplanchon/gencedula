#!/usr/bin/env python3

from random import randrange

COEFICIENTES = (2, 9, 8, 7, 6, 3, 4)


def calculate_digito_verificador(cedula: int) -> int:
    """
    Get verifier digit of uruguayan identification document.
    Each of the 7 digits (padded with leading zeros) is multiplied
    by its coefficient in (2, 9, 8, 7, 6, 3, 4); the verifier digit
    is the negated sum of those products, modulo 10.
    https://es.wikipedia.org/wiki/C%C3%A9dula_de_Identidad_de_Uruguay
    (spanish article).

    :param cedula: int: Identification number without verifier digit,
        between 0 and 9_999_999.

    """
    if not 0 <= cedula <= 9_999_999:
        raise ValueError("Cedula values have to be between 0 and 9 999 999.")

    cedula_string = str(cedula).zfill(7)
    total = sum(
        int(digito) * coeficiente
        for digito, coeficiente in zip(cedula_string, COEFICIENTES)
    )
    return -total % 10


def verify_cedula(cedula: int) -> bool:
    """
    Verify that a full uruguayan identity document number is valid,
    i.e. that its last digit matches the verifier digit computed
    from the preceding digits.

    :param cedula: int: Full identification number, including
        the verifier digit as its last digit.

    """
    if not 0 <= cedula <= 99_999_999:
        return False
    return calculate_digito_verificador(cedula // 10) == cedula % 10


def format_cedula(cedula: int) -> str:
    """
    Format a full uruguayan identity document number in its usual
    written form, grouping the digits with dots and separating the
    verifier digit with a hyphen, e.g. 46308006 -> "4.630.800-6".

    :param cedula: int: Full identification number, including
        the verifier digit as its last digit.

    """
    if not 0 <= cedula <= 99_999_999:
        raise ValueError("Cedula values have to be between 0 and 99 999 999.")

    numero, digito_verificador = divmod(cedula, 10)
    numero_formateado = f"{numero:,}".replace(",", ".")
    return f"{numero_formateado}-{digito_verificador}"


def generate_cedula(
    start: int = 0,
    stop: int = 10_000_000,
    step: int = 1
        ) -> int:
    """
    Get a random uruguayan identity document.
    The result is checksum-valid but not necessarily an issued
    document.
    :param start: int: Start number. (Default value = 0)
    :param stop: int: Stop number, exclusive. (Default value = 10_000_000)
    :param step: int: Step. (Default value = 1)

    """
    if start < 0 or stop > 10_000_000:
        raise ValueError("Cedula values have to be between 0 and 10 000 000.")

    cedula = randrange(start=start, stop=stop, step=step)
    return cedula * 10 + calculate_digito_verificador(cedula)
