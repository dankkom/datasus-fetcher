"""Verifica a extensão nativa instalada: descomprime uma fixture e confere o resultado.

Uso (no CI, depois de instalar o wheel recém-compilado)::

    python -I tests/smoke_extension.py tests/fixtures/DOAC1996.dbc

Fica fora da coleta do pytest (o nome não começa com ``test_``): o objetivo é
rodar contra o wheel instalado, não contra o código-fonte.
"""

from __future__ import annotations

import hashlib
import sys
import tempfile
from pathlib import Path

# Saída esperada para tests/fixtures/DOAC1996.dbc, medida com a extensão
# compilada in-tree em 2026-10-14.
EXPECTED_BYTES = 662_109
EXPECTED_SHA256 = "c094c55a426f184b0d99069a1aeaba152105fa0f0991d6b1550e6c15d362419c"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"uso: {argv[0]} <arquivo.dbc>", file=sys.stderr)
        return 2

    from datasus_fetcher import _datasus_dbc

    src = Path(argv[1])
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "saida.dbf"
        written = _datasus_dbc.decompress(str(src), str(dest))
        data = dest.read_bytes()

    from_bytes = _datasus_dbc.decompress_bytes(src.read_bytes())

    print(f"python {sys.version.split()[0]}  extensão {_datasus_dbc.__file__}")
    checks = {
        "bytes gravados": written == EXPECTED_BYTES,
        "tamanho do arquivo": len(data) == EXPECTED_BYTES,
        "sha256": hashlib.sha256(data).hexdigest() == EXPECTED_SHA256,
        "decompress_bytes igual a decompress": from_bytes == data,
    }
    for name, ok in checks.items():
        print(f"  {'ok' if ok else 'FALHOU'}: {name}")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
