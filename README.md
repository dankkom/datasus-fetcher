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

| Dataset                     |    Nº files |  Total size | Period range            |
| --------------------------- | ----------: | ----------: | ----------------------- |
| base-populacional-ibge-pop  |    33 files |    150.4 MB | from 1980    to 2012    |
| base-populacional-ibge-popt |    29 files |      2.3 MB | from 1992    to 2021    |
| base-territorial            |     1 files |      2.3 MB | from 1992    to 2021    |
| base-territorial-conversao  |    28 files |      2.1 MB | from 1992    to 2021    |
| base-territorial-mapas      |    83 files |    124.4 MB | from 1991    to 2013    |
| cih-cr                      |   868 files |    157.5 MB | from 2008-01 to 2011-04 |
| ciha                        |  3856 files |   3054.7 MB | from 2011-01 to 2023-07 |
| cnes-dc                     |  5994 files |    111.2 MB | from 2005-08 to 2024-01 |
| cnes-ee                     |  3201 files |      4.3 MB | from 2007-03 to 2021-07 |
| cnes-ef                     |  5074 files |      9.5 MB | from 2007-03 to 2024-01 |
| cnes-ep                     |  5454 files |    450.6 MB | from 2007-04 to 2024-01 |
| cnes-eq                     |  5993 files |   1216.0 MB | from 2005-08 to 2024-01 |
| cnes-gm                     |  5157 files |     11.2 MB | from 2007-03 to 2024-01 |
| cnes-hb                     |  5481 files |    113.3 MB | from 2007-03 to 2024-01 |
| cnes-in                     |  5196 files |     32.0 MB | from 2007-10 to 2024-01 |
| cnes-lt                     |  5940 files |    124.2 MB | from 2005-10 to 2024-01 |
| cnes-pf                     |  5994 files |  34762.5 MB | from 2005-08 to 2024-01 |
| cnes-rc                     |  5420 files |     61.0 MB | from 2007-03 to 2024-01 |
| cnes-sr                     |  5993 files |   1277.9 MB | from 2005-08 to 2024-01 |
| cnes-st                     |  5994 files |   2583.1 MB | from 2005-08 to 2024-01 |
| pce                         |   409 files |     14.1 MB | from 1995    to 2021    |
| po                          |    12 files |    142.1 MB | from 2013    to 2024    |
| resp                        |   252 files |      3.2 MB | from 2015    to 2023    |
| sia-ab                      |   544 files |     13.9 MB | from 2008-01 to 2017-04 |
| sia-abo                     |  1203 files |     29.9 MB | from 2014-01 to 2023-12 |
| sia-acf                     |  2945 files |     23.9 MB | from 2014-08 to 2023-12 |
| sia-ad                      |  5182 files |   2451.5 MB | from 2008-01 to 2023-12 |
| sia-am                      |  5130 files |  13103.8 MB | from 2008-01 to 2023-12 |
| sia-an                      |  2145 files |    437.6 MB | from 2008-01 to 2014-10 |
| sia-aq                      |  5143 files |   3820.0 MB | from 2008-01 to 2023-12 |
| sia-ar                      |  4683 files |    304.7 MB | from 2008-01 to 2023-12 |
| sia-atd                     |  3047 files |    760.7 MB | from 2014-08 to 2023-12 |
| sia-pa                      |  9821 files | 141418.9 MB | from 1994-07 to 2023-12 |
| sia-ps                      |  3557 files |   2238.7 MB | from 2012-11 to 2023-12 |
| sia-sad                     |  1088 files |     51.0 MB | from 2012-04 to 2018-10 |
| sih-er                      |  4095 files |    251.3 MB | from 2011-01 to 2023-12 |
| sih-rd                      | 10348 files |  21622.2 MB | from 1992-01 to 2023-12 |
| sih-rj                      |  5024 files |    770.1 MB | from 2008-01 to 2023-12 |
| sih-sp                      |  8603 files |  44745.7 MB | from 1997-06 to 2023-12 |
| sim-do-cid09                |   449 files |    361.0 MB | from 1979    to 1995    |
| sim-do-cid10                |   733 files |   2537.4 MB | from 1996    to 2022    |
| sim-do-cid10-preliminar     |     0 files |      0.0 MB | from ----    to ----    |
| sim-doext-cid09             |    17 files |     42.0 MB | from 1979    to 1995    |
| sim-doext-cid10             |    27 files |    246.8 MB | from 1996    to 2022    |
| sim-dofet-cid09             |    17 files |     23.0 MB | from 1979    to 1995    |
| sim-dofet-cid10             |    27 files |     58.4 MB | from 1996    to 2022    |
| sim-doinf-cid09             |    17 files |     58.0 MB | from 1979    to 1995    |
| sim-doinf-cid10             |    27 files |     88.6 MB | from 1996    to 2022    |
| sim-domat-cid10             |    27 files |      3.9 MB | from 1996    to 2022    |
| sim-dorext-cid10            |    10 files |      0.4 MB | from 2013    to 2022    |
| sinan-acbi                  |    14 files |     28.5 MB | from 2006    to 2019    |
| sinan-acbi-preliminar       |     4 files |     12.9 MB | from 2020    to 2023    |
| sinan-acgr                  |    14 files |     44.3 MB | from 2006    to 2019    |
| sinan-acgr-preliminar       |     4 files |     51.6 MB | from 2020    to 2023    |
| sinan-anim                  |    13 files |     88.7 MB | from 2007    to 2019    |
| sinan-anim-preliminar       |     3 files |     30.3 MB | from 2020    to 2022    |
| sinan-antr                  |    13 files |    345.8 MB | from 2006    to 2018    |
| sinan-antr-preliminar       |     4 files |    120.0 MB | from 2019    to 2022    |
| sinan-botu                  |    13 files |      0.1 MB | from 2007    to 2019    |
| sinan-botu-preliminar       |     4 files |      0.0 MB | from 2020    to 2023    |
| sinan-canc                  |    13 files |      0.1 MB | from 2007    to 2019    |
| sinan-canc-preliminar       |     4 files |      0.1 MB | from 2020    to 2023    |
| sinan-chag                  |    20 files |      2.6 MB | from 2000    to 2019    |
| sinan-chag-preliminar       |     2 files |      0.4 MB | from 2020    to 2021    |
| sinan-chik                  |     8 files |     46.9 MB | from 2015    to 2022    |
| sinan-chik-preliminar       |     2 files |     11.8 MB | from 2023    to 2024    |
| sinan-cole                  |    13 files |      0.0 MB | from 2007    to 2019    |
| sinan-cole-preliminar       |     2 files |      0.0 MB | from 2020    to 2021    |
| sinan-coqu                  |    14 files |      7.5 MB | from 2007    to 2020    |
| sinan-coqu-preliminar       |     2 files |      0.2 MB | from 2021    to 2022    |
| sinan-deng                  |    23 files |    866.8 MB | from 2000    to 2022    |
| sinan-deng-preliminar       |     2 files |    158.3 MB | from 2023    to 2024    |
| sinan-derm                  |    14 files |      0.4 MB | from 2006    to 2019    |
| sinan-derm-preliminar       |     4 files |      0.1 MB | from 2020    to 2023    |
| sinan-dift                  |    14 files |      0.1 MB | from 2007    to 2020    |
| sinan-dift-preliminar       |     2 files |      0.0 MB | from 2021    to 2022    |
| sinan-esqu                  |    13 files |      7.0 MB | from 2007    to 2019    |
| sinan-esqu-preliminar       |     4 files |      0.5 MB | from 2020    to 2023    |
| sinan-exan                  |     0 files |      0.0 MB | from ----    to ----    |
| sinan-exan-preliminar       |    16 files |     13.8 MB | from 2007    to 2022    |
| sinan-fmac                  |    15 files |      2.5 MB | from 2007    to 2021    |
| sinan-fmac-preliminar       |     1 files |      0.3 MB | from 2022    to 2022    |
| sinan-ftif                  |    13 files |      0.7 MB | from 2007    to 2019    |
| sinan-ftif-preliminar       |     4 files |      0.1 MB | from 2020    to 2023    |
| sinan-hans                  |    18 files |     44.3 MB | from 2001    to 2018    |
| sinan-hans-preliminar       |     5 files |      8.3 MB | from 2019    to 2023    |
| sinan-hant                  |    11 files |      1.5 MB | from 2007    to 2017    |
| sinan-hant-preliminar       |    13 files |      0.5 MB | from 1999    to 2022    |
| sinan-hepa                  |     0 files |      0.0 MB | from ----    to ----    |
| sinan-hepa-preliminar       |    14 files |     22.8 MB | from 2007    to 2020    |
| sinan-iexo                  |    14 files |     86.3 MB | from 2006    to 2019    |
| sinan-iexo-preliminar       |     4 files |     52.2 MB | from 2020    to 2023    |
| sinan-infl                  |     0 files |      0.0 MB | from ----    to ----    |
| sinan-infl-preliminar       |     0 files |      0.0 MB | from ----    to ----    |
| sinan-leiv                  |    23 files |     11.2 MB | from 2000    to 2022    |
| sinan-leiv-preliminar       |     0 files |      0.0 MB | from ----    to ----    |
| sinan-lept                  |     0 files |      0.0 MB | from ----    to ----    |
| sinan-lept-preliminar       |    16 files |     17.1 MB | from 2007    to 2022    |
| sinan-lerd                  |    14 files |      4.5 MB | from 2006    to 2019    |
| sinan-lerd-preliminar       |     4 files |      1.5 MB | from 2020    to 2023    |
| sinan-ltan                  |    23 files |     35.1 MB | from 2000    to 2022    |
| sinan-ltan-preliminar       |     0 files |      0.0 MB | from ----    to ----    |
| sinan-mala                  |    15 files |      2.0 MB | from 2004    to 2018    |
| sinan-mala-preliminar       |     4 files |      0.4 MB | from 2019    to 2022    |
| sinan-meni                  |    13 files |     33.5 MB | from 2007    to 2019    |
| sinan-meni-preliminar       |     4 files |      4.8 MB | from 2020    to 2023    |
| sinan-ment                  |    14 files |      0.6 MB | from 2006    to 2019    |
| sinan-ment-preliminar       |     4 files |      0.5 MB | from 2020    to 2023    |
| sinan-ntra                  |     9 files |      0.5 MB | from 2010    to 2018    |
| sinan-ntra-preliminar       |     4 files |      0.1 MB | from 2019    to 2022    |
| sinan-pair                  |    14 files |      0.4 MB | from 2006    to 2019    |
| sinan-pair-preliminar       |     4 files |      0.1 MB | from 2020    to 2023    |
| sinan-pest                  |    11 files |      0.0 MB | from 2007    to 2017    |
| sinan-pest-preliminar       |     3 files |      0.0 MB | from 2018    to 2020    |
| sinan-pfan                  |     8 files |      0.5 MB | from 2012    to 2019    |
| sinan-pfan-preliminar       |     2 files |      0.0 MB | from 2020    to 2021    |
| sinan-pneu                  |    14 files |      0.2 MB | from 2006    to 2019    |
| sinan-pneu-preliminar       |     4 files |      0.1 MB | from 2020    to 2023    |
| sinan-raiv                  |    15 files |      0.1 MB | from 2007    to 2021    |
| sinan-raiv-preliminar       |     0 files |      0.0 MB | from ----    to ----    |
| sinan-sdta                  |    11 files |      0.7 MB | from 2007    to 2018    |
| sinan-sdta-preliminar       |     3 files |      0.1 MB | from 2019    to 2021    |
| sinan-sifa                  |     0 files |      0.0 MB | from ----    to ----    |
| sinan-sifa-preliminar       |    14 files |     24.5 MB | from 2010    to 2023    |
| sinan-sifc                  |     0 files |      0.0 MB | from ----    to ----    |
| sinan-sifc-preliminar       |    17 files |     12.2 MB | from 2007    to 2023    |
| sinan-sifg                  |     0 files |      0.0 MB | from ----    to ----    |
| sinan-sifg-preliminar       |    17 files |     16.7 MB | from 2007    to 2023    |
| sinan-src                   |     0 files |      0.0 MB | from ----    to ----    |
| sinan-src-preliminar        |    16 files |      0.2 MB | from 2007    to 2022    |
| sinan-teta                  |    14 files |      0.5 MB | from 2007    to 2020    |
| sinan-teta-preliminar       |     2 files |      0.1 MB | from 2021    to 2022    |
| sinan-tetn                  |     6 files |      0.0 MB | from 2014    to 2019    |
| sinan-tetn-preliminar       |     2 files |      0.0 MB | from 2020    to 2021    |
| sinan-toxc                  |     2 files |      0.2 MB | from 2019    to 2020    |
| sinan-toxc-preliminar       |     3 files |      0.3 MB | from 2021    to 2023    |
| sinan-toxg                  |     2 files |      0.6 MB | from 2019    to 2020    |
| sinan-toxg-preliminar       |     3 files |      1.0 MB | from 2021    to 2023    |
| sinan-trac                  |    10 files |      1.5 MB | from 2009    to 2018    |
| sinan-trac-preliminar       |     4 files |      0.1 MB | from 2019    to 2022    |
| sinan-tube                  |    17 files |     74.9 MB | from 2001    to 2017    |
| sinan-tube-preliminar       |     5 files |     25.5 MB | from 2018    to 2022    |
| sinan-varc                  |     0 files |      0.0 MB | from ----    to ----    |
| sinan-varc-preliminar       |    17 files |     33.2 MB | from 2007    to 2023    |
| sinan-viol                  |    13 files |    179.7 MB | from 2009    to 2021    |
| sinan-viol-preliminar       |     1 files |     28.6 MB | from 2022    to 2022    |
| sinan-zika                  |     7 files |      7.4 MB | from 2016    to 2022    |
| sinan-zika-preliminar       |     2 files |      0.6 MB | from 2023    to 2024    |
| sinasc-dn                   |   787 files |   3672.3 MB | from 1994    to 2022    |
| sinasc-dn-preliminar        |     0 files |      0.0 MB | from ----    to ----    |
| sinasc-dnex                 |     8 files |      0.4 MB | from 2014    to 2021    |
| siscolo-cc                  |  2858 files |   2380.9 MB | from 2006-01 to 2015-10 |
| siscolo-hc                  |  2858 files |     38.9 MB | from 2006-01 to 2015-10 |
| sismama-cm                  |  1675 files |      4.8 MB | from 2009-01 to 2015-07 |
| sismama-hm                  |  1674 files |      5.7 MB | from 2009-01 to 2015-07 |
| sisprenatal-pn              |   944 files |    221.6 MB | from 2012-01 to 2014-12 |

Total size: 282.0 GB

Total files: 161955 files

Statistics generated on 2024-02-23

## Data sources

Online queries: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/

Microdata: https://datasus.saude.gov.br/transferencia-de-arquivos/

## Available datasets

- Base Populacional - IBGE
  - BASE-POPULACIONAL-IBGE-POP: Censo e Estimativas
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
