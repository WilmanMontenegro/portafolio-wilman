# AGENTS.md — Portafolio Wilman Montenegro

Agent instructions for this repository. Keep this file up to date when conventions change.

---

## Project Overview

Personal portfolio for Wilman Montenegro. Static site (SSG) built with Astro 6, TypeScript strict, Tailwind CSS v4, and pnpm. No backend, no SSR adapter, no React/Vue/Svelte — pure `.astro` components only.

---

## Build & Dev Commands

All commands use **pnpm**. Never use npm or yarn.

```bash
pnpm dev          # Start local dev server (default: http://localhost:4321)
pnpm build        # Production build → dist/
pnpm preview      # Preview production build locally
pnpm astro --help # Astro CLI
```

There is no test suite, no linter, and no formatter configured. There are no `lint`, `test`, or `format` scripts. Do not add them unless explicitly requested.

To verify a change works, run `pnpm build` — a successful zero-error build is the acceptance criterion.

---

## Stack

| Layer | Tool |
|---|---|
| Framework | Astro 6 (SSG, MPA) |
| Language | TypeScript (strict) |
| Styles | Tailwind CSS v4 via `@tailwindcss/vite` |
| Fonts | JetBrains Mono (mono), Inter (sans) — Google Fonts CDN |
| Icons | DevIcons via jsDelivr CDN |
| Tooltips | tippy.js |
| Package manager | pnpm |

---

## Project Structure

```
src/
  components/     ← One .astro file per section (Hero, Navbar, Projects, …)
  layouts/        ← Layout.astro (wraps all pages, SEO head, skip link)
  pages/          ← index.astro (single page, composes all components)
  styles/
    global.css    ← Design tokens (@theme {}), global utilities, font imports
public/           ← Static assets (images, favicon, cv.pdf)
astro.config.mjs  ← Astro + Vite config (Tailwind loaded here)
tsconfig.json     ← Extends astro/tsconfigs/strict
```

No `src/data/`, `src/lib/`, `src/utils/`, or `src/types/` directories exist. Keep the structure flat and simple.

---

## Code Style

### `.astro` File Anatomy

Every component has up to four sections in this order:

```astro
---
// 1. Frontmatter: TypeScript only. Imports, Props interface, inline data.
interface Props { title: string }
const { title } = Astro.props
const items = [{ id: 1, label: 'Foo' }]
---

<!-- 2. HTML template: Tailwind classes, Astro expressions -->
<section id="section-id">
  <h2 class="text-2xl font-bold grad-text">{title}</h2>
</section>

<script>
  // 3. Client-side TypeScript (optional). Vanilla DOM only.
</script>

<style>
  /* 4. Scoped CSS (optional, use sparingly). */
</style>
```

### Imports

- Import order: framework first (`astro`, then components), then assets.
- Component imports go in frontmatter. Never import inside the template.
- No barrel files or index re-exports.

```astro
---
import Layout from '../layouts/Layout.astro'
import Hero from '../components/Hero.astro'
---
```

### TypeScript

- Always extend `astro/tsconfigs/strict` — do not weaken it.
- Define `interface Props` locally at the top of frontmatter when a component accepts props.
- Cast DOM queries with `as HTMLElement | null`; use optional chaining (`?.`) before calling methods.
- Use `as` casts for DOM elements rather than type guards.
- Prefer `const` everywhere. Never use `var`.
- No `any`. No disabling strict checks.

```ts
// Good
const toggle = document.getElementById('nav-toggle') as HTMLElement | null
toggle?.addEventListener('click', () => { /* … */ })

// Bad
const toggle: any = document.getElementById('nav-toggle')
toggle.addEventListener('click', () => {})
```

### Naming Conventions

| Scope | Convention | Example |
|---|---|---|
| Component files | PascalCase | `Hero.astro`, `Navbar.astro` |
| Variables / data | camelCase | `const projectList = […]` |
| HTML `id` attributes | kebab-case | `id="contact-form"` |
| HTML `class` attributes | Tailwind utilities + global classes | `class="text-sm grad-text"` |
| CSS custom properties | `--color-name`, `--font-family-*` | `--color-cyan: #0CFFFF` |

### Styling

- **Tailwind v4 utilities first.** Add a Tailwind class before reaching for custom CSS.
- Design tokens live in the `@theme {}` block inside `global.css`. Do not create `tailwind.config.js`.
- CSS custom properties in `:root` mirror the `@theme` tokens for use in raw CSS.
- Responsive design uses Tailwind breakpoints (`md:`, `lg:`) and arbitrary variants (`max-[640px]:`).
- Use `clamp()` for fluid typography/spacing: `text-[clamp(1.5rem,2.5vw,2rem)]`.
- Avoid per-component `<style>` blocks unless the style cannot be expressed with Tailwind.
- Global utility classes (`.grad-text`, `.btn`, `.btn--primary`, `.btn--ghost`, `.nav-link`) are defined in `global.css` and are available project-wide.

### Design Tokens (do not change without explicit instruction)

| Token | Value | Usage |
|---|---|---|
| `--color-bg` | `#100425` | Page background |
| `--color-surface` | `#1b0840` | Card / section backgrounds |
| `--color-cyan` | `#0CFFFF` | Primary accent, glows |
| `--color-purple` | `#DC00D3` | Secondary accent |
| `--color-text` | `#e8e8f2` | Body text |
| `--color-muted` | `#9494b0` | Secondary / meta text |
| `--font-family-mono` | `'JetBrains Mono'` | Code, headings |
| `--font-family-sans` | `'Inter'` | Body text |

### Data

All content (projects, experience, education, references) is defined as **inline `const` arrays** of typed objects directly in each component's frontmatter. There is no CMS, no JSON files, no external data layer.

### Error Handling

- Use `try/catch/finally` for any `fetch` calls (see `Contact.astro`).
- Guard DOM queries: `if (el) { … }` or optional chaining `el?.method()`.
- Provide user-facing feedback (loading states, error messages) for async operations.
- No custom error classes. No re-throwing unless necessary.

### Accessibility

- Every interactive element needs an `aria-label` or visible label.
- Use `aria-expanded` + `aria-controls` on toggle buttons.
- Decorative images/icons: `aria-hidden="true"`.
- External links: always `target="_blank" rel="noopener noreferrer"`.
- Dynamic status regions: `role="alert"` + `aria-live="polite"`.
- The skip-to-content link in `Layout.astro` must remain intact.

### Client-side JavaScript

- Write in TypeScript inside `<script>` blocks — Astro compiles them.
- Vanilla DOM only. Do not introduce a JS framework.
- Avoid large inline scripts; keep them focused on a single concern per component.

---

## Commit & Workflow Rules

- **Language**: commit messages and code comments in **Spanish**.
- **Atomic commits**: one logical change per commit.
- **No obvious comments**: avoid docstrings or comments that restate the code.
- **No over-engineering**: the simplest working solution is preferred.
- **No new dependencies** without consulting the user first.
- For substantial changes, follow SDD (Spec-Driven Development) with `/sdd-new`.

---

## What Not to Do

- Do not add ESLint, Prettier, Jest, Vitest, or any new tooling unless asked.
- Do not introduce React, Vue, or Svelte integrations.
- Do not enable SSR or add a server adapter.
- Do not create `src/data/`, `src/lib/`, or `src/utils/` directories unless asked.
- Do not use `npm` or `yarn`.
- Do not weaken TypeScript strict mode.
- Do not change the visual identity (colors, fonts, dark theme) without explicit instruction.
