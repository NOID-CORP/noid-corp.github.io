# Arma la página de noidcorp.com (index.html de la raíz) desde nuevo/index.html.
# La fuente es nuevo/index.html: se edita ahí y se corre `python3 nuevo/armar_raiz.py` desde la raíz del repo.
# Cambia: rutas a nuevo/, los ../ de privacidad y términos, y quita el noindex (la raíz sí se indexa).
import re, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
s = (raiz / 'nuevo' / 'index.html').read_text(encoding='utf-8')

s = re.sub(r'(?<![\w/.-])(audio|capturas|fuentes|img|vendor)/', r'nuevo/\1/', s)
s = s.replace('"../', '"')
quitar = ['<!-- Borrador en /nuevo/: quitar esta línea al pasar la página a la raíz (y agregar canonical y og:url) -->\n',
          '<meta name="robots" content="noindex">\n',
          '<!-- Ruta provisional: cambiarla cuando la página pase a la raíz del sitio -->\n']
for q in quitar:
    assert q in s, q
    s = s.replace(q, '')
s = s.replace('<meta property="og:type" content="website">',
              '<link rel="canonical" href="https://noidcorp.com/">\n<meta property="og:url" content="https://noidcorp.com/">\n<meta property="og:type" content="website">', 1)
s = s.replace('<!doctype html>', '<!doctype html>\n<!-- Generado desde nuevo/index.html con nuevo/armar_raiz.py: no editar aquí -->', 1)
assert 'noindex' not in s and "'nuevo/vendor/three.min.js'" in s
(raiz / 'index.html').write_text(s, encoding='utf-8')
print('index.html de la raíz armado')
