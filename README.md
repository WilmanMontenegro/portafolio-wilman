# Portafolio Wilman Montenegro

Dos capas en este repo:

| Carpeta | Qué es |
|---------|--------|
| `src/` + `public/` | Sitio web público (Astro) |
| `vida/` | Desarrollo profesional y vida: laburo, práctica, cursos (local) |

## Sitio web

```bash
pnpm install
pnpm dev      # http://localhost:4321
pnpm build    # → dist/
```

## Vida (no es la web)

```text
vida/
├── laboral/cun|sae   ← notas + contratos (PDFs ignorados por git)
├── practica/         ← live coding, algoritmos
└── cursos/           ← aprendizaje paralelo
```

Ver `vida/README.md`.

## Stack

Astro 6 · TypeScript strict · Tailwind v4 · pnpm
