import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({base:"/universe/", plugins:[react()], build:{outDir:"dist/client"}});
