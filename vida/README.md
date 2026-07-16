# Vida — desarrollo profesional y personal

Espacio **local** (no es el sitio web). Aquí va lo de laburo, práctica y cursos.
El sitio público vive en `src/` + `public/`.

## Empezar aquí

**[`yo.md`](yo.md)** — perfil maestro (HV + historial + skills + situación laboral + cómo conocerme).  
Actualizar ese archivo cuando cambie algo. Los agentes deben leerlo primero.

```text
vida/
├── yo.md             ← QUIÉN SOY (fuente de verdad)
├── laboral/          ← contratos, notas de procesos (PDFs no van a git)
│   ├── cun/
│   └── sae/
├── practica/         ← live coding, algoritmos, drills
│   └── live-coding/
└── cursos/           ← aprendizaje paralelo (no publicado en la web)
```

**Regla:** PDFs y datos sensibles solo en `laboral/`. Están en `.gitignore`.
