"""Captura las maquetas de capturas/src/ como PNG (2x) y WebP (calidad 85) en capturas/.

Uso (con cualquier Python que tenga Playwright y su Chromium):
    python capturar.py              # todas
    python capturar.py citas-plan   # solo una

Necesita `cwebp` (Homebrew: brew install webp) para la versión .webp.
"""
import asyncio
import shutil
import subprocess
import sys
from pathlib import Path

from playwright.async_api import async_playwright

SRC = Path(__file__).resolve().parent
SALIDA = SRC.parent

# nombre -> (ancho, alto) en px CSS; se captura con densidad 2
MAQUETAS = {
    "citas-plan": (1440, 900),
    "hallazgos": (1440, 900),
    "factura-hoja": (1440, 900),
    "factura-chat": (390, 844),
}


async def capturar(nombres):
    async with async_playwright() as p:
        nav = await p.chromium.launch()
        for nombre in nombres:
            ancho, alto = MAQUETAS[nombre]
            ctx = await nav.new_context(viewport={"width": ancho, "height": alto}, device_scale_factor=2)
            pag = await ctx.new_page()
            await pag.goto((SRC / f"{nombre}.html").as_uri())
            await pag.evaluate("document.fonts.ready")
            fuentes = await pag.evaluate(
                "[...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight)"
            )
            desborde = await pag.evaluate(
                "({w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight})"
            )
            png = SALIDA / f"{nombre}.png"
            await pag.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": ancho, "height": alto})
            await ctx.close()
            print(f"{nombre}: {png.name} · fuentes cargadas {sorted(set(fuentes))} · contenido {desborde}")
            if shutil.which("cwebp"):
                webp = SALIDA / f"{nombre}.webp"
                subprocess.run(["cwebp", "-quiet", "-q", "85", "-m", "6", str(png), "-o", str(webp)], check=True)
        await nav.close()


if __name__ == "__main__":
    elegidas = sys.argv[1:] or list(MAQUETAS)
    asyncio.run(capturar(elegidas))
