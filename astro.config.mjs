// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://WilmanMontenegro.github.io',
  base: '/portafolio-wilman/',
  vite: {
    plugins: [tailwindcss()],
  },
});
