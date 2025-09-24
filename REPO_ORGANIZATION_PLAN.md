## Repository Reorganization Plan

Goal: Improve consistency, discoverability, and professionalism without breaking project histories. Changes will be staged and reviewed before execution.

### Guiding principles
- Preserve build/run parity for each course project.
- Avoid moving compiled artifacts; remove from version control when safe.
- Prefer additive changes (readmes, docs) before heavy refactors.

### Proposed actions
1. Standardize README naming and contents
   - Rename `Readme.md`/`readme.md` to `README.md` across courses.
   - Add a short overview, prerequisites, run instructions, and structure to any course missing a README (e.g., AIT‑104, CST‑150, CST‑180, CST‑239, CST‑345).

2. Normalize directory structure per course
   - Use `src/` (or `Code/`) for source, `docs/` (or `Documentation/`) for artifacts, and `Notes/` for lecture notes.
   - Move stray screenshots into `docs/screenshots/`.
   - Keep solution files near their project folders; add a top‑level `src/` index README when multiple solutions exist.

3. Clean binary noise and archives
   - Ensure `.gitignore` excludes `bin/`, `obj/`, `.vs/`, and build outputs in all .NET projects (already mostly present).
   - Remove committed `bin/`/`obj/` caches and IDE state from version control where accidentally checked in.
   - Move `.zip` archives into a dedicated `archives/` folder per course (or remove if redundant with source in repo).

4. Consistent naming
   - Fix misspellings (e.g., `algorithims` → `algorithms`) via directory aliases or README clarifications to avoid breaking links. If renaming, do it once and update internal links.
   - Use consistent casing for folders like `Screenshots` vs `screenshots`.

5. Documentation cross‑links
   - From the root `README.md`, link to each course `README.md` and key milestone folders.
   - Within each course, add a mini index linking activities, milestones, and docs.

6. Optional: Monorepo tooling
   - Add a root `docs/` with an index page (optional) and shared assets.
   - Consider a root `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md` (if external collaboration is expected).

### Execution plan (phased)
Phase 1 (safe, low‑risk)
- Add/standardize course READMEs and cross‑links.
- Move screenshots into `docs/screenshots/` (no code changes).
- Add/confirm `.gitignore` coverage; remove tracked build artifacts.

Phase 2 (light structure)
- Consolidate `Code/` vs `src/` naming per course; update solution references only if required.
- Create `archives/` and move `.zip` files.

Phase 3 (optional renames)
- Rename misspelled folders with care; update links in READMEs.

### Review checkpoints
- After Phase 1, confirm builds still succeed for representative projects (C#, Java, Node/Angular).
- Before any renames (Phase 3), review with owner to avoid breaking external references.


