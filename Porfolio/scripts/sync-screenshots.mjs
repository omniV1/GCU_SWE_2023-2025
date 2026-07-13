import { cpSync, existsSync, mkdirSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";

const root = resolve(import.meta.dirname, "../..");
const source = join(root, "SiteScreenshots");
const target = join(root, "Porfolio/public/screenshots");

if (!existsSync(source)) {
  console.error(`Missing screenshot source folder: ${source}`);
  process.exit(1);
}

mkdirSync(target, { recursive: true });

const images = readdirSync(source).filter((name) => /\.(png|jpe?g|webp)$/i.test(name));
if (images.length === 0) {
  console.log("No images found in SiteScreenshots.");
  process.exit(0);
}

for (const name of images) {
  cpSync(join(source, name), join(target, name), { force: true });
}

console.log(`Synced ${images.length} screenshot(s) to Porfolio/public/screenshots`);
