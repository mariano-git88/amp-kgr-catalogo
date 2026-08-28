# Conjunto documental Kostzer–García Ramírez · catálogo web

Catálogo de acceso del conjunto documental Kostzer–García Ramírez
(Instituto Torcuato Di Tella, Centro de Experimentación Audiovisual, 1964–1970).
Colección Mariano Pappalardo. Adquirido en Galería Azur, Buenos Aires.
Digitalización: Belén Leuzzi y Matías Butelman, 2026.

## Qué hay en este repo

| Ruta | Qué es | Peso |
|---|---|---|
| `index.html` | el sitio entero: estructura, estilo y comportamiento en un solo archivo | 77 KB |
| `data.js` | los 130 documentos con sus fichas, fuentes y listas de archivos | 858 KB |
| `img/` | 344 imágenes de acceso (`_acc.jpg`) + 344 miniaturas (`_min.jpg`) | 264 MB |
| `pdf/` | 128 PDF, uno por documento, con capa de texto buscable | 472 MB |
| `leeme.html` | la nota de entrega del paquete original | 2 KB |
| `herramientas/armar_sitio.py` | rearma el sitio desde una entrega nueva | |

## Lo que no está publicado

La entrega original pesa 25 GB. Acá viven los dos niveles que se leen en
pantalla y los PDF. Quedan afuera:

- `3-ajustadas/` — 18 GB de TIFF preparados para trabajo editorial
- `4-masters/` — 6,2 GB de originales de cámara (CR2)

Sus nombres, medidas y pesos **sí** están descritos en `data.js`, porque
documentan qué existe en el archivo. Pero `index.html` sólo dibuja los bloques
`desc` cuyo `k` es `PDF`, así que no aparecen como botones de descarga y no hay
ningún enlace roto.

## Cómo actualizar desde una entrega nueva

```bash
python3 herramientas/armar_sitio.py /ruta/a/AMP-KGR_entrega_AAAA-MM-DD
```

Copia el catálogo y los PDF, y reescribe las rutas `../2-pdf/` a `pdf/`
(la entrega usa rutas que salen de la carpeta; un sitio web no tiene
«carpeta de arriba»). Después: commit y push.

## Buscadores

`robots.txt` hoy le pide a los buscadores que no indexen el sitio, para poder
trabajarlo tranquilo. Cuando esté listo para ser público en Google, se borra
ese archivo.

## Dónde se publica

GitHub Pages, desde la rama `main`.
