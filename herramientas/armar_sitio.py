#!/usr/bin/env python3
"""Arma el sitio publicable a partir de una carpeta de entrega AMP-KGR.

La entrega original es una copia de trabajo: el catálogo vive en 1-catalogo/ y
apunta con rutas ../ a carpetas hermanas (2-pdf, 3-ajustadas, 4-masters). En la
web no hay «carpeta de arriba»: la raíz del sitio es la raíz. Este script copia
lo que se publica y reescribe esas rutas.

Qué se publica y qué no:
  1-catalogo/  -> raíz del sitio   (index.html, data.js, img/)   ~264 MB
  2-pdf/       -> pdf/                                            ~472 MB
  LEEME.html   -> leeme.html
  3-ajustadas/ y 4-masters/  NO se publican (24,2 GB). Sus rutas quedan en
  data.js pero index.html nunca las dibuja: sólo lee los bloques desc con
  k == 'PDF'. No hay botón roto que ocultar.

Uso:
    python3 herramientas/armar_sitio.py /ruta/a/AMP-KGR_entrega_AAAA-MM-DD
    python3 herramientas/armar_sitio.py --sin-copiar    # sólo reescribe rutas
"""
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# (texto original, reemplazo, archivo donde vive)
REESCRITURAS = [
    ("../2-pdf/", "pdf/", "data.js"),
    ("../LEEME.html", "leeme.html", "index.html"),
]


def copiar(entrega: Path) -> None:
    cat = entrega / "1-catalogo"
    if not (cat / "index.html").exists():
        sys.exit(f"No encuentro {cat / 'index.html'}. ¿Es una carpeta de entrega?")

    print("Copiando el catálogo…")
    for nombre in ("index.html", "data.js"):
        shutil.copy2(cat / nombre, RAIZ / nombre)
    shutil.copytree(cat / "img", RAIZ / "img", dirs_exist_ok=True)

    print("Copiando los PDF…")
    shutil.copytree(entrega / "2-pdf", RAIZ / "pdf", dirs_exist_ok=True)

    shutil.copy2(entrega / "LEEME.html", RAIZ / "leeme.html")


def reescribir() -> None:
    for viejo, nuevo, archivo in REESCRITURAS:
        ruta = RAIZ / archivo
        texto = ruta.read_text(encoding="utf-8")
        n = texto.count(viejo)
        if n == 0:
            print(f"  {archivo}: ya estaba reescrito ({viejo} no aparece)")
            continue
        ruta.write_text(texto.replace(viejo, nuevo), encoding="utf-8")
        print(f"  {archivo}: {n} rutas {viejo} -> {nuevo}")

    # GitHub Pages pasa todo por Jekyll si no encuentra este archivo, y Jekyll
    # se saltea lo que empieza con guion bajo. Acá no hay nada así, pero el
    # archivo vacío también evita el paso de build y publica más rápido.
    (RAIZ / ".nojekyll").touch()


def verificar() -> None:
    """Falla ruidosamente si quedó alguna ruta que sale de la raíz del sitio."""
    problemas = []
    for archivo in ("index.html", "data.js"):
        for linea, texto in enumerate((RAIZ / archivo).read_text(encoding="utf-8").splitlines(), 1):
            for marca in ('"../2-pdf/', '"../LEEME.html'):
                if marca in texto:
                    problemas.append(f"{archivo}:{linea} {marca}")
    if problemas:
        sys.exit("Quedaron rutas sin reescribir:\n  " + "\n  ".join(problemas[:10]))
    print("Verificado: no quedan rutas ../ a lo que sí publicamos.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] != "--sin-copiar":
        copiar(Path(args[0]).expanduser())
    elif not args:
        sys.exit(__doc__)
    print("Reescribiendo rutas…")
    reescribir()
    verificar()
