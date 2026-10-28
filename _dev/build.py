"""Gera Calendario_PGs.html (arquivo único, offline) a partir de _dev/app_template.html.

Embute o logo, a fonte Outfit e o ícone da aba (cópias do projeto 2, não referências).
Uso: python _dev/build.py
"""
import base64
import pathlib
import sys

DEV = pathlib.Path(__file__).resolve().parent
SAIDA = DEV.parent / "Calendario_PGs.html"


def b64file(nome, mime):
    return f"data:{mime};base64," + base64.b64encode((DEV / nome).read_bytes()).decode("ascii")


def main():
    s = (DEV / "app_template.html").read_text(encoding="utf-8")
    trocas = {
        "__LOGO__": (DEV / "logo_andritz.txt").read_text(encoding="utf-8").strip(),
        "__FONT_LATIN__": b64file("outfit-latin.woff2", "font/woff2"),
        "__FONT_LATIN_EXT__": b64file("outfit-latin-ext.woff2", "font/woff2"),
        "__ANDRITZ_ICO__": b64file("andritz.ico", "image/x-icon"),
    }
    for k, v in trocas.items():
        if k not in s:
            sys.exit(f"Marcador {k} não encontrado no template.")
        s = s.replace(k, v)
    tmp = SAIDA.with_suffix(".tmp")
    tmp.write_text(s, encoding="utf-8")
    tmp.replace(SAIDA)
    print(f"OK: {SAIDA.name} ({SAIDA.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
