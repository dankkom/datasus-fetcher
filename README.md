# datasus-fetcher

This package function is to download DATASUS raw data files (DBC) from its FTP server. It does not have reading functions.

## Installation

```sh
pip install datasus-fetcher
```

Or install via pipx:

```sh
pipx install datasus-fetcher
```

## Usage

Use the command line interface to download files:

```sh
datasus-fetcher data --data-dir /path/to/data-dir sih-rd --start 2020-01 --end 2023-12 --regions sp rj mg
```

This will download all files from the SIH-RD dataset from January 2020 to December 2023 for the states of São Paulo, Rio de Janeiro and Minas Gerais.

You can also omit the dataset name, the start and end dates and the regions to download all available datasets:

```sh
datasus-fetcher data --data-dir /path/to/data-dir
```

## List datasets

| Dataset                     |    Nº files  |  Total size  | Period range            |
| --------------------------- | -----------: | -----------: | ----------------------- |
| base-populacional-ibge-pop  |     33 files |     150.4 MB | from 1980    to 2012    |
| base-populacional-ibge-pops |     25 files |      81.3 MB | from 2000    to 2024    |
| base-populacional-ibge-popt |     32 files |       2.4 MB | from 1992    to 2024    |
| base-territorial            |     14 files |      20.9 MB | from ----    to ----    |
| base-territorial-conversao  |     28 files |      35.7 MB | from ----    to ----    |
| base-territorial-mapas      |     83 files |     122.2 MB | from 1991    to 2013    |
| cih-cr                      |    868 files |     157.5 MB | from 2008-01 to 2011-04 |
| ciha                        |   4201 files |    4354.5 MB | from 2011-01 to 2024-09 |
| cnes-dc                     |   6318 files |     115.4 MB | from 2005-08 to 2025-01 |
| cnes-ee                     |   3201 files |       4.3 MB | from 2007-03 to 2021-07 |
| cnes-ef                     |   5374 files |      10.0 MB | from 2007-03 to 2025-01 |
| cnes-ep                     |   5778 files |     498.8 MB | from 2007-04 to 2025-01 |
| cnes-eq                     |   6317 files |    1329.2 MB | from 2005-08 to 2025-01 |
| cnes-gm                     |   5459 files |      11.9 MB | from 2007-03 to 2025-01 |
| cnes-hb                     |   5805 files |     122.2 MB | from 2007-03 to 2025-01 |
| cnes-in                     |   5520 files |      36.4 MB | from 2007-10 to 2025-01 |
| cnes-lt                     |   6264 files |     131.3 MB | from 2005-10 to 2025-01 |
| cnes-pf                     |   6318 files |   38238.1 MB | from 2005-08 to 2025-01 |
| cnes-rc                     |   5744 files |      67.2 MB | from 2007-03 to 2025-01 |
| cnes-sr                     |   6316 files |    1389.8 MB | from 2005-08 to 2025-01 |
| cnes-st                     |   6310 files |    2805.5 MB | from 2005-08 to 2025-01 |
| pce                         |    409 files |      14.1 MB | from 1995    to 2021    |
| po                          |     12 files |     129.5 MB | from 2013    to 2024    |
| resp                        |    280 files |       3.4 MB | from 2015    to 2024    |
| sia-ab                      |    544 files |      13.9 MB | from 2008-01 to 2017-04 |
| sia-abo                     |   1352 files |      32.2 MB | from 2014-01 to 2024-12 |
| sia-acf                     |   3263 files |      26.7 MB | from 2014-08 to 2024-12 |
| sia-ad                      |   5506 files |    2683.1 MB | from 2008-01 to 2024-12 |
| sia-am                      |   5447 files |   14762.8 MB | from 2008-01 to 2024-12 |
| sia-an                      |   2145 files |     437.6 MB | from 2008-01 to 2014-10 |
| sia-aq                      |   5466 files |    4202.1 MB | from 2008-01 to 2024-12 |
| sia-ar                      |   4982 files |     318.9 MB | from 2008-01 to 2024-12 |
| sia-atd                     |   3371 files |     855.0 MB | from 2014-08 to 2024-12 |
| sia-pa                      |  10193 files |  163258.4 MB | from 1994-07 to 2024-12 |
| sia-ps                      |   3881 files |    2543.1 MB | from 2012-11 to 2024-12 |
| sia-sad                     |   1088 files |      51.0 MB | from 2012-04 to 2018-10 |
| sih-er                      |   4419 files |     270.4 MB | from 2011-01 to 2024-12 |
| sih-rd                      |  10673 files |   22639.1 MB | from 1992-01 to 2024-12 |
| sih-rj                      |   5348 files |     815.8 MB | from 2008-01 to 2024-12 |
| sih-sp                      |   8928 files |   48377.4 MB | from 1997-06 to 2024-12 |
| sim-do-cid09                |    466 files |     722.2 MB | from 1979    to 1995    |
| sim-do-cid10                |    784 files |    4307.5 MB | from 1996    to 2023    |
| sim-doext-cid09             |     17 files |      42.0 MB | from 1979    to 1995    |
| sim-doext-cid10             |     28 files |     260.2 MB | from 1996    to 2023    |
| sim-dofet-cid09             |     17 files |      23.0 MB | from 1979    to 1995    |
| sim-dofet-cid10             |     28 files |      60.9 MB | from 1996    to 2023    |
| sim-doinf-cid09             |     17 files |      58.0 MB | from 1979    to 1995    |
| sim-doinf-cid10             |     28 files |      92.0 MB | from 1996    to 2023    |
| sim-domat-cid10             |     28 files |       4.1 MB | from 1996    to 2023    |
| sim-dorext-cid10            |     11 files |       0.4 MB | from 2013    to 2023    |
| sinan-acbi                  |     19 files |      44.2 MB | from 2006    to 2024    |
| sinan-acgr                  |     19 files |     112.4 MB | from 2006    to 2024    |
| sinan-aida                  |     17 files |      17.1 MB | from 2007    to 2023    |
| sinan-aidc                  |     17 files |       0.3 MB | from 2007    to 2023    |
| sinan-anim                  |     17 files |     127.5 MB | from 2007    to 2023    |
| sinan-antr                  |     19 files |     432.7 MB | from 2006    to 2024    |
| sinan-botu                  |     18 files |       0.1 MB | from 2007    to 2024    |
| sinan-canc                  |     18 files |       0.3 MB | from 2007    to 2024    |
| sinan-chag                  |     24 files |       4.0 MB | from 2000    to 2023    |
| sinan-chik                  |     11 files |      70.7 MB | from 2015    to 2025    |
| sinan-cole                  |     18 files |       0.0 MB | from 2007    to 2024    |
| sinan-coqu                  |     19 files |       9.1 MB | from 2007    to 2025    |
| sinan-deng                  |     26 files |    1229.0 MB | from 2000    to 2025    |
| sinan-derm                  |     19 files |       0.5 MB | from 2006    to 2024    |
| sinan-dift                  |     16 files |       0.1 MB | from 2007    to 2022    |
| sinan-espo                  |     10 files |       0.4 MB | from 2013    to 2022    |
| sinan-esqu                  |     17 files |       7.6 MB | from 2007    to 2023    |
| sinan-exan                  |     18 files |      14.0 MB | from 2007    to 2024    |
| sinan-fmac                  |     17 files |       3.9 MB | from 2007    to 2023    |
| sinan-ftif                  |     18 files |       0.8 MB | from 2007    to 2024    |
| sinan-hans                  |     24 files |      53.6 MB | from 2001    to 2024    |
| sinan-hant                  |     25 files |       2.1 MB | from 1999    to 2023    |
| sinan-hepa                  |     17 files |      28.1 MB | from 2007    to 2023    |
| sinan-hiva                  |     17 files |      15.3 MB | from 2007    to 2023    |
| sinan-hivc                  |     17 files |       0.1 MB | from 2007    to 2023    |
| sinan-hive                  |      9 files |       1.0 MB | from 2015    to 2023    |
| sinan-hivg                  |     17 files |       3.4 MB | from 2007    to 2023    |
| sinan-iexo                  |     19 files |     150.3 MB | from 2006    to 2024    |
| sinan-leiv                  |     25 files |      12.1 MB | from 2000    to 2024    |
| sinan-lept                  |     18 files |      21.5 MB | from 2007    to 2024    |
| sinan-lerd                  |     19 files |       6.5 MB | from 2006    to 2024    |
| sinan-ltan                  |     25 files |      36.2 MB | from 2000    to 2024    |
| sinan-mala                  |     20 files |       2.5 MB | from 2004    to 2023    |
| sinan-meni                  |     18 files |      40.9 MB | from 2007    to 2024    |
| sinan-ment                  |     19 files |       1.2 MB | from 2006    to 2024    |
| sinan-ntra                  |     13 files |       0.6 MB | from 2010    to 2022    |
| sinan-pair                  |     19 files |       0.5 MB | from 2006    to 2024    |
| sinan-pest                  |     14 files |       0.0 MB | from 2007    to 2020    |
| sinan-pfan                  |     10 files |       0.5 MB | from 2012    to 2021    |
| sinan-pneu                  |     19 files |       0.3 MB | from 2006    to 2024    |
| sinan-raiv                  |     15 files |       0.1 MB | from 2007    to 2021    |
| sinan-rota                  |     16 files |       1.2 MB | from 2009    to 2024    |
| sinan-sdta                  |     14 files |       0.8 MB | from 2007    to 2021    |
| sinan-sifa                  |     15 files |      28.3 MB | from 2010    to 2024    |
| sinan-sifc                  |     18 files |      13.3 MB | from 2007    to 2024    |
| sinan-sifg                  |     17 files |      16.7 MB | from 2007    to 2023    |
| sinan-src                   |     16 files |       0.2 MB | from 2007    to 2022    |
| sinan-teta                  |     16 files |       0.6 MB | from 2007    to 2022    |
| sinan-tetn                  |      8 files |       0.0 MB | from 2014    to 2021    |
| sinan-toxc                  |      6 files |       0.8 MB | from 2019    to 2024    |
| sinan-toxg                  |      6 files |       2.3 MB | from 2019    to 2024    |
| sinan-trac                  |     14 files |       1.6 MB | from 2009    to 2022    |
| sinan-tube                  |     23 files |      97.8 MB | from 2001    to 2023    |
| sinan-varc                  |     17 files |      33.2 MB | from 2007    to 2023    |
| sinan-viol                  |     15 files |     242.4 MB | from 2009    to 2023    |
| sinan-zika                  |     10 files |       8.9 MB | from 2016    to 2025    |
| sinasc-dn                   |    838 files |    6114.7 MB | from 1994    to 2023    |
| sinasc-dnex                 |     10 files |       0.5 MB | from 2014    to 2023    |
| siscolo-cc                  |   2858 files |    2380.9 MB | from 2006-01 to 2015-10 |
| siscolo-hc                  |   2858 files |      38.9 MB | from 2006-01 to 2015-10 |
| sismama-cm                  |   1675 files |       4.8 MB | from 2009-01 to 2015-07 |
| sismama-hm                  |   1674 files |       5.7 MB | from 2009-01 to 2015-07 |
| sisprenatal-pn              |    944 files |     221.6 MB | from 2012-01 to 2014-12 |

Total size: 320.7 GB

Total files: 170543 files

Statistics generated on 2025-02-18

## Data sources

Online queries: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/

Microdata: https://datasus.saude.gov.br/transferencia-de-arquivos/

## Available datasets

- Base Populacional - IBGE
  - BASE-POPULACIONAL-IBGE-POP: Censo e Estimativas
  - BASE-POPULACIONAL-IBGE-POPS: Estimativas por Sexo e Idade
  - BASE-POPULACIONAL-IBGE-POPT: Estimativas TCU
- Base Territorial - Mapas e conversões para tabulação
  - Base Territoriais
  - Mapas
  - Conversões
- CIH: Sistema de Comunicação de Informação Hospitalar
  - CIH-CR: Comunicação de Internação Hospitalar
- CIHA: Sistema de Comunicação de Informação Hospitalar e Ambulatorial
  - CIHA-CIHA: Sistema de Comunicação de Informação Hospitalar e Ambulatorial
- CNES: Cadastro Nacional de Estabelecimentos de Saúde
  - CNES-LT: Leitos
  - CNES-ST: Estabelecimentos
  - CNES-DC: Dados Complementares
  - CNES-EQ: Equipamentos
  - CNES-SR: Serviço Especializado
  - CNES-HB: Habilitação
  - CNES-PF: Profissional
  - CNES-EP: Equipes
  - CNES-RC: Regra Contratual
  - CNES-IN: Incentivos
  - CNES-EE: Estabelecimento de Ensino
  - CNES-EF: Estabelecimento Filantrópico
  - CNES-GM: Gestão e Metas
- PCE: Programa de Controle da Esquistossomose
  - PCE-PCE: Programa de Controle da Esquistossomose
- PO: Painel de Oncologia
  - PO-PO: Painel de Oncologia
- RESP: Notificações de casos suspeitos de SCZ
  - RESP: Notificações de casos suspeitos de SCZ
- SIA: Sistema de Informações Ambulatoriais
  - SIA-AB: APAC de Acompanhamento a Cirurgia Bariátrica
  - SIA-ABO: APAC Acompanhamento Pós Cirurgia Bariátrica
  - SIA-ACF: APAC Confeção de Fístula Arteriovenosa
  - SIA-AD: APAC de Laudos Diversos
  - SIA-AM: APAC de Medicamentos
  - SIA-AN: APAC de Nefrologia
  - SIA-AQ: APAC de Quimioterapia
  - SIA-AR: APAC de Radioterapia
  - SIA-ATD: APAC de Tratamento Dialítico
  - SIA-PA: Produção Ambulatorial
  - SIA-PS: Psicossocial
  - SIA-SAD: Atenção Domiciliar
- SIH: Sistema de Informação Hospitalar (Descentralizado)
  - SIH-RD: AIH Reduzida
  - SIH-RJ: AIH Rejeitadas
  - SIH-SP: Serviços Profissionais
  - SIH-ER: AIH Rejeitadas com código de erro
- SIM: Sistema de Informação de Mortalidade
  - SIM-DO: Declarações de Óbito
  - SIM-DOEXT: Declarações de Óbitos por causas externas
  - SIM-DOFET: Declarações de Óbitos fetais
  - SIM-DOINF: Declarações de Óbitos infantis
  - SIM-DOMAT: Declarações de Óbitos maternos
  - SIM-DOREXT: Mortalidade de residentes no exterior
- SINAN: Sistema de agravos de notificação compulsória
  - SINAN-ACBI: Acidente de trabalho com material biológico
  - SINAN-ACGR: Acidente de trabalho
  - SINAN-AIDA: AIDS em adultos
  - SINAN-AIDC: AIDS em crianças
  - SINAN-ANIM: Acidente por Animais Peçonhentos
  - SINAN-ANTR: Atendimento Antirrabico
  - SINAN-BOTU: Botulismo
  - SINAN-CANC: Cancêr relacionado ao trabalho
  - SINAN-CHAG: Doença de Chagas Aguda
  - SINAN-CHIK: Febre de Chikungunya
  - SINAN-COLE: Cólera
  - SINAN-COQU: Coqueluche
  - SINAN-DENG: Dengue
  - SINAN-DERM: Dermatoses ocupacionais
  - SINAN-DIFT: Difteria
  - SINAN-ESPO: Esporotricose (Epizootia)
  - SINAN-ESQU: Esquistossomose
  - SINAN-EXAN: Doenças exantemáticas
  - SINAN-FMAC: Febre Maculosa
  - SINAN-FTIF: Febre Tifóide
  - SINAN-HANS: Hanseníase
  - SINAN-HANT: Hantavirose
  - SINAN-HEPA: Hepatites Virais
  - SINAN-HIVA: HIV em adultos
  - SINAN-HIVC: HIV em crianças
  - SINAN-HIVE: HIV em crianças expostas
  - SINAN-HIVG: HIV em gestante
  - SINAN-IEXO: Intoxicação Exógena
  - SINAN-LEIV: Leishmaniose Visceral
  - SINAN-LEPT: Leptospirose
  - SINAN-LERD: LER/Dort
  - SINAN-LTAN: Leishmaniose Tegumentar Americana
  - SINAN-MALA: Malária
  - SINAN-MENI: Meningite
  - SINAN-MENT: Transtornos mentais relacionados ao trabalho
  - SINAN-NTRA: Notificação de Tracoma
  - SINAN-PAIR: Perda auditiva por ruído relacionado ao trabalho
  - SINAN-PEST: Peste
  - SINAN-PFAN: Paralisia Flácida Aguda
  - SINAN-PNEU: Pneumoconioses relacionadas ao trabalho
  - SINAN-RAIV: Raiva
  - SINAN-ROTA: Rotavírus
  - SINAN-SDTA: Surto Doenças Transmitidas por Alimentos
  - SINAN-SIFA: Sífilis Adquirida
  - SINAN-SIFC: Sífilis Congênita
  - SINAN-SIFG: Sífilis em Gestante
  - SINAN-SRC: Síndrome da Rubéola Congênia
  - SINAN-TETA: Tétano Acidental
  - SINAN-TETN: Tétano Neonatal
  - SINAN-TOXC: Toxoplasmose Congênita
  - SINAN-TOXG: Toxoplasmose Gestacional
  - SINAN-TRAC: Inquérito de Tracoma
  - SINAN-TUBE: Tuberculose
  - SINAN-VARC: Varicela
  - SINAN-VIOL: Violência doméstica, sexual e/ou outras violências
  - SINAN-ZIKA: Zika Vírus
- SINASC: Sistema de Informação de Nascidos Vivos
  - SINASC-DN: Declarações de nascidos vivos 1994 a 2020
  - SINASC-DNEX: Declarações de nascidos vivos no exterior 2014 a 2020
- SISCOLO: Sistema de Informações de Cânceres de Colo de Útero
  - SISCOLO-CC: Citopatológico de Colo de Útero
  - SISCOLO-HC: Histopatológico de Colo de Útero
- SISMAMA: Sistema de Informações de Cânceres de Mama
  - SISMAMA-CM: Citopatológico de Mama
  - SISMAMA-HC: Histopatológico de Mama
- SISPRENATAL: Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puepério e Criança
  - SISPRENATAL-PN: Pré-Natal

## Development

Install development version from Github running this command:

```sh
pip install -e git+https://github.com/dankkom/datasus-fetcher.git
```

Run unit tests with:

```sh
python -m unittest discover
```

### Build and publish package

Build package with:

```sh
python -m build
```

Publish package to PyPI with:

```sh
python -m twine upload dist/*
```

See [Python Packaging User Guide: The Packaging Workflow](https://packaging.python.org/en/latest/flow/) for more information.
