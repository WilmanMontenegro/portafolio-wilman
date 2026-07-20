# IA Estratégica para Emprendedores de Marketing Digital (2026)

> Exportado desde NotebookLM — bloque Wilman.
> Base para diapositivas. Orden pedagógico: LLM → token → contexto → cobro/modelo → riesgos → prompts → proveedores → productividad → decks.
> Creación imagen/video: bloque de la compañera (fuera de diapos Wilman).

## 1. ¿Qué es un LLM?

- **Definición:** Motor de IA (Large Language Model) diseñado para entender, generar y manipular lenguaje humano.
- **Función:** No es una base de datos, sino un sistema que **predice la siguiente palabra** basándose en patrones de miles de millones de ejemplos.
- **Uso en Marketing:** No solo texto. Mapa: **Texto** (copies, emails, guiones, ideas) · **Visual** (imágenes, video corto, decks) · **Datos** (análisis, reportes, SEO/AEO) · **Atención** (chatbots, personalización, automatizar).
- **Fuente:** [HubSpot State of Marketing 2026](https://blog.hubspot.com/marketing/hubspot-blog-marketing-industry-trends-report) — 86.4% de equipos usan IA; usos intensivos frecuentes: content creation 42.5%, media creation 37.2%, admin automation 35.6%. Video corto = formato con mayor ROI reportado. Herramientas de imagen/video las detalla el bloque de la compañera.

## 2. El Token: La Moneda de la IA

- **¿Qué es?** Unidad básica de información (palabras cortas, fragmentos o signos). El modelo predice el siguiente *token*; al público se explica primero como “palabra”.
- **Equivalencia (OpenAI, solo inglés):** 1 token ≈ 4 caracteres; 1.000 tokens ≈ 750 palabras. Fuente: [OpenAI Help — What are tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).
- **Español vs inglés:** El mismo mensaje en español suele gastar **~20–50% más tokens** que en inglés (tokenizer entrenado sobre todo en EN). ≈ 550–650 palabras / 1.000 tokens en ES según medidas con `tiktoken` (cl100k / o200k). Escritura en español **no** es más barata: suele costar más.

## 3. Contexto / ventana de contexto

- **Qué es:** Lo que la IA “ve” en este momento (se mide en tokens).
- **Qué entra:** Tu pregunta + historial del chat + archivos que subes.
- **Límite:** Cada modelo tiene un tope (ventana de contexto). Si te pasas, “olvida” lo de arriba.
- **Takeaway:** Más contexto útil ≠ mejor respuesta automática; hay que elegir qué meter.
- **Cobro (después de entender contexto):** Se cobra por tokens de **entrada** (llenan el contexto) y **salida** (respuesta). Salida suele ser **3× a 6×** más cara.
- **Modelo correcto (práctica):** misma app, varios modelos. Barato/rápido para volumen; fuerte/caro solo para decidir.
  - **ChatGPT:** Mini → clasificar comentarios / resumir reseñas · GPT/Thinking → plan de campaña o propuesta.
  - **Claude:** Haiku → leads y respuestas cortas · Sonnet → copy/briefs · Opus → estrategia difícil.
  - **Gemini:** Flash → resumir Docs/Sheets · Pro → auditoría con varios archivos.
  - Regla: empieza barato; sube solo si no alcanza.

## 4. Desafíos y Riesgos

- **Alucinaciones:** La IA puede inventar información que suena lógica pero es falsa; siempre requiere verificación humana.
- **Sesgos:** Los modelos pueden reproducir prejuicios culturales o estereotipos de sus datos de entrenamiento.
- **Seguridad:** Riesgos de inyección de prompts para robo de datos y cuidado con la privacidad en modelos que usan tus datos para entrenar.

## 5. Prompts prácticos (malo vs bueno)

- **Prompt** = la instrucción que le das a la IA.
- **Receta:** Rol + Tarea + Contexto + Formato.
- **Malo:** “Escribe un copy para Instagram.” → vago, respuesta genérica.
- **Bueno (ejemplo cafetería Barranquilla):** rol copywriter + 1 caption máx. 80 palabras + tono cercano costeño + beneficio + CTA suave + 3 hashtags locales + no inventar precios/premios.
- Práctica: copiar el bueno, adaptarlo al negocio y probar.

## 6. Comparativa de Gigantes (Superpoderes)

Fuentes: [OpenAI / ChatGPT Voice e Images](https://help.openai.com/), [Anthropic Claude](https://www.anthropic.com/claude), [Google Gemini](https://blog.google/products-and-platforms/products/gemini/), [Meta Llama](https://ai.meta.com/blog/Llama-4-multimodal-intelligence/) + docs en llama.com / ai.google.dev.

- **OpenAI (ChatGPT):** Multimodal en un solo chat — texto, voz en tiempo real e imágenes. Buen “todo terreno” para empezar.
- **Anthropic (Claude):** Fuerte en redacción clara, razonamiento paso a paso y seguir instrucciones complejas (trabajo de conocimiento / coding).
- **Google (Gemini):** Contexto muy grande (~1M tokens) y multimodal nativo (texto, audio, video, docs). Ideal para “pásame mucho material de una vez”.
- **Meta (Llama):** Pesos abiertos descargables; puedes correrlo en tu equipo o servidor → más control y privacidad (requiere algo de setup técnico).

## 7. Herramientas de Generación (Video e Imagen) — bloque compañera

> No va en las diapos de Wilman. Referencia para el curso completo:

- **Video:** InVideo AI, Creatify, Synthesia.
- **Imagen:** Midjourney, Leonardo AI, Adobe Firefly.

## 8. Presentaciones rápidas (marketing)

Fuentes: [NotebookLM Slide Decks — Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-labs/8-ways-to-make-the-most-out-of-slide-decks-in-notebooklm/), [notebooklm.google](https://notebooklm.google/), [Claude Design — Anthropic](https://www.anthropic.com/news/claude-design-anthropic-labs), [tutorial decks Claude Design](https://claude.com/resources/tutorials/using-claude-design-for-presentations-and-slide-decks), [Claude Design Help](https://support.claude.com/en/articles/14604416-get-started-with-claude-design). Extra: [Gamma](https://gamma.app).

- **NotebookLM (Google):** Subes PDFs/briefs/notas → Studio → **Slide Deck**. Ideal cuando quieres que el deck se base en *tus* fuentes (menos alucinaciones). Export PDF/PPTX; a veces el PPTX va poco editable (capas/imágenes) — revisar antes de cliente.
- **Claude Design (claude.ai/design):** Describes el deck → canvas con slides. Export PPTX, PDF, HTML o envío a Canva. Pensado para pitches y propuestas. Suele requerir plan Pro/Max+.
- **Gamma (extra):** Prompt → deck con look de pitch muy rápido; tú verificas datos.
- **Usos marketing:** resultados de campaña, pitch a cliente, capacitación interna.
- **Prompt plantilla (producto):** con `[corchetes]` para personalizar — marca, producto, público, objetivo, precio, CTA. Sirve en Claude Design / Gamma; en NotebookLM: subir fuentes primero + prompt corto “solo usa las fuentes”.
- **Regla:** IA arma borrador; tú revisas cifras, marca y mensaje.

## 9. Productividad diaria (emprendedor, no técnico)

- **ChatGPT / Claude:** ofertas, correos a clientes, captions, borradores de respuesta. Flujo: chat → copiar → pegar en WhatsApp / IG / email. Sin APIs.
- **Gemini:** si ya usa Google (Docs, Sheets, Gmail) — resumir tablas, listas, mejorar correos.
- **ManyChat** ([manychat.com](https://manychat.com/)): automatizar DMs de Instagram sin código (ej. comentan “precio” → info al DM). Oficial Meta partner; pensado para creadores y pequeños negocios.
- **Fuera de este bloque (más tech):** OpenRouter (útil a desarrolladores) y Botpress (más setup) — no priorizar para audiencia emprendedora principiante.
- Regla: empieza con un chat; automatiza redes cuando los mensajes te ahoguen.

## 10. Ahorro = modelo correcto (antes “ROI” aparte)

- No hay sección ROI separada en diapos: va junto a Mini/Pro.
- **Regla:** barato/rápido para lo diario; fuerte/caro solo si hace falta.
- **Retorno simple:** menos gasto en tokens + más tiempo libre.
- (Histórico NotebookLM: ahorros de tiempo reportados ~26–75% en tareas — no martillar el techo en clase.)
