// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

import sitemap from '@astrojs/sitemap';

/** En `pnpm dev`, Vite no sirve index.html al pedir /carpeta/ — sí en GitHub Pages. */
function publicDirIndex() {
  return {
    name: 'public-dir-index',
    configureServer(server) {
      server.middlewares.use((req, _res, next) => {
        const raw = req.url ?? ''
        const [path, qs] = raw.split('?')
        if (path === '/curso-ia-marketing/diapos' || path === '/curso-ia-marketing/diapos/') {
          req.url = `/curso-ia-marketing/diapos/index.html${qs ? `?${qs}` : ''}`
        }
        next()
      })
    },
  }
}

// https://astro.build/config
export default defineConfig({
  site: 'https://wilman.dev',

  vite: {
    plugins: [tailwindcss(), publicDirIndex()],
  },

  integrations: [sitemap()],
});
