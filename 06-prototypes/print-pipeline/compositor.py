#!/usr/bin/env python3
"""Compositor do capitulo impresso . Projeto 2047 / Arquivo Terra Viva.

Diagramacao PROVA A, escolhida por Felipe no papel em 03/08/2026.

O capitulo e um objeto continuo. Cabecalho e corpo dividem a mesma forma, sem
avanco de formulario entre eles. Um unico preambulo abre o payload e o unico
form feed acontece depois do colofao. A versao anterior isolava o cabecalho numa
forma propria e desperdicava dois tercos de folha por capitulo.

  CAPITULO NNNN em tipo nativo, altura e largura duplas
  linha de arquivo em condensed, filete
  QR do chao da agulha, modulo 2x1, passe duplo
  legenda de procedencia
  corpo em LQ pica 10cpi, 76 colunas, 6 lpi, correndo na mesma forma
  colofao com fonte real, timestamp e dominio

Numeracao de 4 digitos por decisao de projeto. A URL do QR fica com 27
caracteres e trava o codigo na versao 3 ate o capitulo 9999. Com 3 digitos o
codigo nasce na versao 2 e pularia para a 3 no capitulo 1000, no meio da
exposicao, quebrando a uniformidade que o arquivo promete.

Espacamento vertical fixo em 6 lpi. Condensed muda so a largura, entao o
cabecalho nao precisa trocar de entrelinha. qr_bands usa 24/216 durante o
bitmap e devolve 1/6 no fim.

Uso
  compositor.py corpo.txt --numero 0013 --qr https://heretica.xyz/f/0013 \
                --fonte "..." --out payload.bin
"""
import argparse, datetime, json, os, textwrap

import escp_common as ep
from escp_qr import matrix, qr_bands

ESC = ep.ESC
BODY_COLS = 76
FORM_LINES_6LPI = 33          # 140mm a 6 lpi. revisar quando o papel virar 280mm
NORM = {"‘": "'", "’": "'", "“": '"', "”": '"',
        "–": "-", "—": "-", "…": "...", " ": " ", "«": '"', "»": '"'}


def cp(s):
  for a, b in NORM.items():
    s = s.replace(a, b)
  return s.encode("cp850", "replace")


def preamble(page_lines=FORM_LINES_6LPI, left=4):
  """Unico reset do payload. Nada depois disto emite ESC @ no meio da forma."""
  p = ESC + b"@"
  p += ESC + b"x\x01"                              # LQ
  p += ESC + b"(t" + bytes([3, 0, 1, 3, 0])        # PC850 -> tabela 1
  p += ESC + b"t\x01"                              # seleciona tabela 1
  p += ESC + b"2"                                  # 6 lpi, vale para o payload inteiro
  p += ESC + b"C" + bytes([page_lines])
  p += ESC + b"l" + bytes([left])
  return p


BODY_INCHES = BODY_COLS / 10.0        # 76 colunas a 10 cpi
COND_COLS = int(BODY_INCHES * 17.1)   # a mesma largura medida em condensed


def cabecalho(numero, url, data_ficcional="2047"):
  """Cabecalho alinhado pela mesma direita do corpo.

  O QR encosta na margem direita do bloco de texto, e nao na margem esquerda da
  folha. O deslocamento sai da largura do proprio codigo, entao vale para
  qualquer versao sem numero magico.
  """
  p = ep.CONDENSED_OFF + ESC + b"P"
  p += b"  " + ESC + b"w\x01" + ESC + b"W\x01" + cp(f"CAPITULO {numero}")
  p += ESC + b"w\x00" + ESC + b"W\x00" + b"\r\n\r\n"   # a segunda quebra abre o corpo do tipo duplo
  p += ep.CONDENSED_ON
  p += cp(f"  ARQUIVO TERRA VIVA . {data_ficcional}") + b"\r\n"
  p += b"  " + b"\xc4" * (COND_COLS - 2) + b"\r\n"
  m, ver = matrix(url)
  largura_dots = len(m) * 2
  lead = max(0, int(BODY_INCHES * 120) - largura_dots)
  p += qr_bands(m, 2, 1, True, lead_dots=lead)          # devolve 1/6 no fim
  p += ep.CONDENSED_ON
  legenda = f"{url.replace('https://', '')} . procedencia da fonte no arquivo vivo"
  p += cp(legenda.rjust(COND_COLS)) + b"\r\n\r\n"
  return p, ver


def corpo(texto):
  p = ep.CONDENSED_OFF + ESC + b"P"
  linhas = []
  for par in texto.split("\n\n"):
    par = " ".join(par.split())
    if par:
      linhas += textwrap.wrap(par, BODY_COLS) + [""]
  return p + b"\r\n".join(cp(l) for l in linhas) + b"\r\n", len(linhas)


def colofao(fonte, numero, dominio):
  ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
  p = ep.CONDENSED_ON
  p += b"\xc4" * 110 + b"\r\n"
  p += cp(f"fonte real. {fonte[:105]}") + b"\r\n"
  p += cp(f"impresso pela maquina do arquivo em {ts} . capitulo {numero} . {dominio}") + b"\r\n"
  return p + b"\x0c" + ESC + b"@"                       # unico form feed do capitulo


def registrar(caminho, numero, url, a):
  """Uma linha por folha impressa. E o unico elo entre o QR do papel e a fonte.

  O destino do QR le este registro. Sem a linha, o codigo aponta para um 404.
  """
  linha = {
    "numero": numero,
    "qr": url,
    "fonte_titulo": a.fonte,
    "fonte_veiculo": a.fonte_veiculo or "",
    "fonte_data": a.fonte_data or "",
    "fonte_url": a.fonte_url or "",
    "packet_id": a.packet_id or "",
    "impresso_em": datetime.datetime.now().isoformat(timespec="seconds"),
  }
  os.makedirs(os.path.dirname(caminho), exist_ok=True)
  with open(caminho, "a", encoding="utf-8") as fh:
    fh.write(json.dumps(linha, ensure_ascii=False) + "\n")


def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("corpo_txt")
  ap.add_argument("--numero", required=True, help="4 digitos, ex. 0013")
  ap.add_argument("--qr")
  ap.add_argument("--fonte", required=True, help="titulo da fonte real, vai no colofao")
  ap.add_argument("--fonte-url", default="")
  ap.add_argument("--fonte-veiculo", default="")
  ap.add_argument("--fonte-data", default="")
  ap.add_argument("--packet-id", default="")
  ap.add_argument("--registro", default="", help="jsonl que o destino do QR le")
  ap.add_argument("--dominio", default="heretica.xyz")
  ap.add_argument("--data-ficcional", default="2047")
  ap.add_argument("--out", required=True)
  a = ap.parse_args()

  numero = a.numero.zfill(4)
  url = a.qr or f"https://{a.dominio}/f/{numero}"
  texto = open(a.corpo_txt, encoding="utf-8").read()

  head, ver = cabecalho(numero, url, a.data_ficcional)
  body, nlin = corpo(texto)
  p = preamble() + head + body + colofao(a.fonte, numero, a.dominio)
  open(a.out, "wb").write(p)

  if a.registro:
    registrar(a.registro, numero, url, a)

  linhas_cabecalho = 12
  formas = max(1, -(-(nlin + linhas_cabecalho) // FORM_LINES_6LPI))
  print(f"{len(p)} bytes . QR v{ver} ({len(url)} chars) . {nlin} linhas de corpo . ~{formas} formas -> {a.out}")


if __name__ == "__main__":
  main()
