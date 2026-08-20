#!/usr/bin/env python3

from importlib.metadata import PackageNotFoundError, version

from gencedula.gencedula import (
    calculate_digito_verificador,
    format_cedula,
    generate_cedula,
    verify_cedula,
)

try:
    __version__ = version("gencedula")
except PackageNotFoundError:  # not installed, e.g. running from a checkout
    __version__ = "0+unknown"

__all__ = [
    "calculate_digito_verificador",
    "format_cedula",
    "generate_cedula",
    "verify_cedula",
]
