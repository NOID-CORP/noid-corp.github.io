# Sitio nuevo de NOID: plan de trabajo

Rama `sitio-nuevo` del repo `NOID-CORP/noid-corp.github.io`, carpeta `nuevo/`.
Empezado el 16-nov-2026 por pedido de DON. Coordina Claude; cada etapa la hacen agentes.

## 1. La meta

Que la mayor cantidad de visitas termine en un contrato, **solo con la página**.
El camino de una visita es: entiende qué hacemos → se ve reflejado en un ejemplo → confía →
da un primer paso fácil (el gancho) → conversación → contrato.

Medida principal: conversaciones iniciadas (WhatsApp o diagnóstico agendado) por cada 100 visitas.
Cada botón lleva un mensaje ya escrito distinto ("Hola, vi el ejemplo de restaurantes…") para saber
qué pantalla trajo a cada cliente.

## 2. Lo que manda (decisiones de DON, 16-nov)

1. **Solo el manual de marca** (`NOID-Marca/manual-noid.html`). El sitio actual y la película de 8
   escenas (`pelicula/`) no atan: se puede usar lo que sirva, pero se parte de cero.
2. **Una sola idea por pantalla.** Al bajar, cada pantalla que queda quieta explica UNA cosa.
   Nada de información por todos lados. Tope: un titular, una frase de apoyo (máx. ~20 palabras)
   y un botón o una imagen que lo pruebe.
3. **Dos partes separadas**:
   - **Lo que podemos hacer** (servicios): los de hoy + otros fáciles de construir con vibecoding.
   - **Lo que ya hicimos** (casos): por sector, **sin nombres de clientes**, con **datos ficticios**.
4. **Imágenes**: generadas con ChatGPT (en el Chrome de DON) o capturas de herramientas reales
   con datos ficticios. Que la imagen explique sola; el texto solo la acompaña.
5. **Portada para pymes de cualquier sector**, y desde ahí cada quien encuentra su negocio.
6. **Gancho** (el primer paso que le pedimos al visitante): lo decide la investigación. El favorito
   de DON es el **diagnóstico gratis**.
7. **Investigación con lo de hoy** (2025–2026). Nada de teoría vieja: un dato sin fecha o de antes
   de 2024 no se usa, salvo que siga vigente y se diga por qué.
8. **Lenguaje sencillo**, como se le explica a un dueño de negocio, con ejemplos prácticos.
   Futurista y tecnológico en lo visual, nunca en las palabras.

## 3. Etapas

| # | Etapa | Quién | Sale |
|---|---|---|---|
| 0 | Preparación: preguntas a DON, rama, este plan | Claude | `PLAN.md` |
| 1 | Investigación (3 agentes en paralelo) | 1A, 1B, 1C | `investigacion/*.md` |
| 2 | Estrategia y guion pantalla por pantalla | Claude | `ESTRATEGIA.md`, `GUION.md` |
| — | **DON revisa el guion** (una página para ver y comentar) | DON | aprobado / cambios |
| 3 | Producción (en paralelo) | 3A, 3B, 3C | `img/`, `capturas/`, `index.html` |
| 4 | Revisión (3 críticos en paralelo) | 4A, 4B, 4C | `revision/*.md` |
| 5 | Correcciones, entrega a DON, rama → revisión de Carlos → publicar | Claude | sitio en noidcorp.com |

### Etapa 1: investigación

**1A · Qué convierte hoy** (búsqueda web, fuentes 2025–2026)
- Páginas de servicios B2B y agencias de IA/automatización: qué estructura, qué gancho y qué
  pruebas convierten hoy (diagnóstico gratis, demo con tu negocio, prueba, precios "desde",
  garantía, calculadora de ahorro).
- Pymes en Colombia y Latinoamérica: WhatsApp como canal de contacto, móvil primero, qué les
  genera desconfianza con la IA y cómo se responde.
- Cómo mostrar casos sin nombres y aun así generar confianza.
- Formato "una idea por pantalla": cuándo ayuda y cuándo estorba (fatiga de scroll, móvil, velocidad).
- Cómo aparecer en las respuestas de ChatGPT/Google con IA (lo que hoy reemplaza parte del SEO).
- Resultado: recomendaciones concretas con su fuente y fecha, y una decisión sobre el gancho.

**1B · Referentes** (búsqueda web)
- 15–20 sitios actuales (2025–2026) de agencias y productos de IA, y sitios de producto que
  explican una cosa por pantalla. Qué copiar y qué evitar, en concreto.
- Estilo de imagen que hoy se ve futurista sin caer en lo genérico de "robot azul con cerebro".

**1C · Inventario** (solo archivos locales)
- **Casos**: todo lo que DON y Carlos ya construyeron, por sector, sin nombres, con el problema,
  lo que hicimos y el resultado medible, y qué captura o imagen lo mostraría (con datos ficticios).
- **Catálogo de servicios**: los de hoy + nuevos fáciles con vibecoding, cada uno con un ejemplo
  práctico de una línea, el "antes / ahora" y si ya tenemos algo parecido construido.

### Etapa 2: estrategia y guion (Claude)

- `ESTRATEGIA.md`: el gancho elegido y por qué, el mensaje central, el orden de las pantallas
  y cómo se mide.
- `GUION.md`: por pantalla, la idea única, el titular, la frase, la imagen (con su encargo para
  ChatGPT o la captura), el movimiento y para qué sirve, y el botón con su mensaje de WhatsApp.
- Se publica como página para que DON la revise antes de producir.

### Etapa 3: producción

- **3A · Imágenes de ChatGPT**: las genera Claude en el Chrome de DON, una por una, desde
  `IMAGENES.md`, y las revisa antes de usarlas (fondo transparente cuando aplique; nada de GIF de
  ChatGPT, que salen pequeños). Un solo navegador: esta parte no se reparte entre agentes.
- **3B · Capturas con datos ficticios**: maquetas de las herramientas reales (panel de pedidos,
  CRM de pacientes, factura leída por WhatsApp, tablero, alertas) con nombres y cifras inventadas,
  capturadas en alta resolución para escritorio y celular.
- **3C · Construcción**: una sola página, móvil primero, sin dependencias pesadas, con las fuentes
  y colores del manual. Respeta "reducir movimiento" y carga rápido en un celular de gama media.

### Etapa 4: revisión

- **4A · Cliente escéptico**: un dueño de pyme que no sabe de IA recorre la página: ¿entendió?,
  ¿confió?, ¿escribiría? ¿Dónde se aburrió o dudó?
- **4B · Técnica**: celular de 360 px, velocidad, accesibilidad, contraste, teclado, "reducir movimiento".
- **4C · Marca**: el manual punto por punto, incluida la sección "lo que no".

## 4. Hipótesis de pantallas (se confirma o cambia con la investigación)

1. **Portada**: qué hacemos en una frase + el gancho.
2. **El problema**: el tiempo que se va en contestar, copiar y revisar a mano.
3. **Lo que podemos hacer**: una pantalla por servicio fuerte, con su ejemplo en imagen.
4. **"Y también"**: los servicios rápidos de vibecoding, en una sola pantalla.
5. **Lo que ya hicimos**: una pantalla por sector (salud, transporte, restaurantes…), con cifra real
   y captura con datos ficticios.
6. **Cómo trabajamos**: tres pasos y cuánto tarda.
7. **Las dudas**: precio, datos, "¿y si falla?".
8. **Cierre**: el gancho otra vez + WhatsApp.

## 5. Reglas para todos los agentes

- **Todo en español**: lo que escriben, lo que razonan y sus informes.
- **Ningún cliente con nombre**: ni empresas, ni personas, ni ciudades
  que los delaten. Por sector ("empresa de salud domiciliaria"). Nada de datos de pacientes,
  conductores o clientes reales: todo lo que se muestre es ficticio y se dice.
- Solo se escribe en `nuevo/`. No tocar `index.html`, `pelicula/`, `privacidad/`, `terminos/`
  ni otros repos. Sin commits ni push: eso lo hace Claude.
- Cada dato de la investigación lleva fuente, fecha y enlace.

## 6. Ronda 3 (19-nov-2026, pedido de DON: "marca premium")

- **Negro** (`#0A0A0B`) entra a la paleta: portada, llamadas, seguimiento, carta 3D, encabezado, pie y botón fijo.
  El **plateado** existe solo dentro de los cromados 3D (el logo), nunca como color plano.
- **Logo cromado en 3D arriba a la izquierda**, en todos los tamaños: la misma pieza de
  `NOID-Marca/logo/cromado-3d/logo.py`, dibujada en vivo con three.js r128 (`vendor/three.min.js`, se carga después
  de la página). Flota, sigue el cursor, da una vuelta al abrir, al pasar por encima y cada 14 s; el estallido late
  (1,6 s) y gira (14 s). Mientras carga, o sin WebGL, se ve `img/logo-cromado.webp`. Se esconde en el cierre (firma 2D).
- **Fuera los recortes de carta anónima** ("quitan formalidad"). En su lugar, el **foco**: la palabra clave en el
  acento dentro de la mirilla, que se cierra sobre ella al entrar en pantalla.
- **Frase nueva**: portada "Deja de hacerlo a mano"; cierre "Tu tiempo vale más que copiar y pegar"
  (DON: "no tu negocio trabajando solo"). Falta rehacer `img/og.jpg`, que aún dice la frase vieja.
- **Pantalla 6 nueva, carta en 3D**: la demo real (`/demo-ar/muestra/carta.html?r=muestra-noid`) dentro de un
  teléfono; en escritorio se usa ahí y trae un QR; en celular un toque la abre completa (ahí funciona la cámara).
  Se carga solo cuando la pantalla se acerca. La ficha "Carta en 3D" de "Y también" salió.
- La muestra con el kit de NOID (colores, logo cromado, Switzer) está en la rama local `marca-noid-muestra` del repo
  `noid` (de Carlos): hasta que Carlos la revise y se publique con `npm run demo:publicar`, noidcorp.com muestra la
  carta naranja de antes. Vista local de todo junto: `servidor.py` del scratchpad de la sesión (sitio + demo).
- 19-nov, ajustes de DON: sin la línea bajo el encabezado; garantía = "si algo falla en el primer mes después de la
  entrega"; en celular la carta 3D muestra el plato escaneado y "Ponlo en tu mesa" abre la AR del teléfono ahí mismo
  (Quick Look / Scene Viewer / WebXR con model-viewer 4.4.0); si no hay AR, abre la carta completa. En escritorio,
  el teléfono con la carta, "Abrir la carta completa" y el QR.
