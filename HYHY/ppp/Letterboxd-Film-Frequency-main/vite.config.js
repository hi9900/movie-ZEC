import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  build: {
    cssCodeSplit: false
  },
  optimizeDeps: {
    include: ['vue']
  },
  plugins: [vue()]
});