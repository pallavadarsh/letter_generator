import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { VitePWA } from "vite-plugin-pwa";

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host : '0.0.0.0',
    port : 8080,
  },
  plugins: [
    react(),
    VitePWA({
      devOptions: {
        enabled: false,
      },
    }),
  ],
});