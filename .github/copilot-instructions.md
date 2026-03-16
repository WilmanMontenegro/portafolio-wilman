# Portafolio – Wilman Montenegro

## Proyecto
Portafolio personal de Wilman Montenegro. Stack: **Astro 6**, TypeScript, pnpm.

## Stack y convenciones
- Framework: Astro 6 (MPA, SSG por defecto)
- Gestor de paquetes: **pnpm** (no usar npm ni yarn)
- Estilos: diseño minimalista, mobile-first
- Lenguaje: TypeScript strict donde aplique
- No añadir dependencias sin consultarlo

## Estructura del proyecto
```
src/
  pages/       ← Páginas Astro (.astro)
public/        ← Assets estáticos (imágenes, favicon, etc.)
astro.config.mjs
```

## Preferencias de código
- Commits atómicos y descriptivos
- No agregar comentarios obvios ni docstrings innecesarios
- Español para mensajes de commit y comentarios de código
- Mantener el código simple: sin over-engineering

## Contexto de Gentle AI
Este proyecto usa Gentle AI con:
- SDD (Spec-Driven Development) para cambios sustanciales → usar `/sdd-new`
- Engram para memoria persistente entre sesiones
- Copilot como agente principal en VS Code
