"""Leitura de .dbf em pedaços: mesmo resultado, memória limitada."""

from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
pytest.importorskip("fastdbf")

from polars.testing import assert_frame_equal  # noqa: E402

from datasus_fetcher import reader  # noqa: E402

FIXTURE_DBC = Path(__file__).parent / "fixtures" / "DOAC1996.dbc"


@pytest.fixture
def dbf(tmp_path: Path) -> Path:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")
    return reader.decompress_dbc(FIXTURE_DBC, tmp_path / "doac.dbf")


def test_iter_dbf_chunks_gera_varios_arquivos_validos(dbf: Path, tmp_path: Path):
    destino = tmp_path / "pedacos"
    destino.mkdir()
    total = 0
    n = 0
    for pedaco in reader._iter_dbf_chunks(dbf, 4096, destino):  # noqa: SLF001
        n += 1
        total += reader._read_dbf_fastdbf(pedaco).height  # noqa: SLF001
    assert n > 1
    assert total == reader.read_dbf(dbf, chunk_bytes=None).height
    assert list(destino.iterdir()) == []  # cada pedaço é removido ao avançar


def test_read_dbf_em_pedacos_igual_ao_inteiro(dbf: Path):
    inteiro = reader.read_dbf(dbf, chunk_bytes=None)
    em_pedacos = reader.read_dbf(dbf, chunk_bytes=2048)  # força vários pedaços
    assert_frame_equal(inteiro, em_pedacos)


def test_read_dbc_em_pedacos_igual_ao_inteiro(dbf: Path):
    """Tipar cada pedaço antes de juntar dá o mesmo DataFrame que tipar tudo."""
    inteiro = reader.wrangle_datasus(reader.read_dbf(dbf, chunk_bytes=None))
    em_pedacos = reader.read_dbf(
        dbf, chunk_bytes=2048, transform=lambda f: reader.wrangle_datasus(f)
    )
    assert_frame_equal(inteiro, em_pedacos)


def test_erro_da_transformacao_nao_dispara_o_fallback(dbf: Path):
    def quebra(_frame):
        raise ZeroDivisionError("da transformação")

    with pytest.raises(ZeroDivisionError):
        reader.read_dbf(dbf, chunk_bytes=2048, transform=quebra)


def test_fallback_do_dbfread_vale_so_para_o_pedaco_que_falha(dbf: Path, monkeypatch):
    """Campo numérico malformado derruba o fastdbf; só o pedaço dele usa dbfread."""
    pytest.importorskip("dbfread")
    esperado = reader.read_dbf(dbf, chunk_bytes=None)

    original = reader._read_dbf_fastdbf  # noqa: SLF001
    chamadas = {"fastdbf": 0, "dbfread": 0}

    def fastdbf_que_falha_no_segundo(path):
        chamadas["fastdbf"] += 1
        if chamadas["fastdbf"] == 2:
            raise ValueError('invalid numeric payload: "2165198310000EP3170"')
        return original(path)

    original_dbfread = reader._read_dbf_dbfread  # noqa: SLF001

    def conta_dbfread(path, encoding):
        chamadas["dbfread"] += 1
        return original_dbfread(path, encoding)

    monkeypatch.setattr(reader, "_read_dbf_fastdbf", fastdbf_que_falha_no_segundo)
    monkeypatch.setattr(reader, "_read_dbf_dbfread", conta_dbfread)
    lido = reader.read_dbf(dbf, chunk_bytes=2048)

    assert chamadas["fastdbf"] > 2
    assert chamadas["dbfread"] == 1
    assert lido.height == esperado.height
    assert lido.columns == esperado.columns
