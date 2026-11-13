# Opening Healthy Future — Demography Daze 2026

[View slides](https://talks.ssylvia.io/research/2026-11-demography-daze-hf/slides.html) · [Current PDF](slides-v8.pdf) · [Original v7 PDF](slides-v7.pdf)

Version 8 applies Sean’s November 13 walkthrough. Fourteen main slides have a 12-minute planned route; four labeled backups follow the final resources/contact slide. The demo is 2:18 in full; notes allocate about one minute of playback. Original v7 artifacts and earlier source commit are retained.

## Edit and render

Edit `slides.qmd`, then run `quarto render slides.qmd` here (Quarto 1.6.43 verified). This is a nested standalone project. Output: `_rendered/slides.html`. The PDF uses the verified slide renders, clickable resource links and a static demo thumbnail. The editable charts remain in the HTML/source. Slide fonts and images are embedded. The native video and its poster are sibling files in `_rendered/assets/`; keep that folder beside the HTML for offline playback. The original Canva link is also available. The video is the existing public demo, optimized for web delivery without cutting its content. `data-external="1"` keeps the video out of the HTML data bundle; `_quarto.yml` copies it to the output assets folder.

Arrow keys navigate; O opens overview; F enters fullscreen; S opens speaker view. Main talk ends at slide 14. `Speaker_notes.md` contains the timing and public source notes.

The typography follows the rendered Belgium reference: Instrument Serif headings, Times body text, Source Sans 3 subheadings and JetBrains Mono markers. The Times system font is used rather than redistributed. The title background is a text-free derivative of the curriculum cover; the original is retained. Official institutional logo assets retain their proportions.

## Figures and evidence

`evidence.json` contains published aggregate estimates from Chen et al., medRxiv v2 (June 16, 2026), Tables 3–4. Binary effects and their confidence bounds are multiplied by 100 for percentage points. No participant dataset or new analysis is included. `python3 render_trial_summary.py` regenerates the editable main forest plots; `python3 render_figures.py` regenerates the detailed backup figures and backend diagram. Tables remain editable HTML.

Architecture follows inspected CareLoom source revision 71468fae6ce0ca9cd434ebbf847f7eac30cee11e. Authored curriculum branching is separated from proposed learned prioritization. The standalone family-targeting and curriculum-paths slides were removed as requested. Trial uncertainty and the distinction between integrated-program and software effects remain explicit.

The global slide uses WHO EB156/15 (December 2024), §9 (approximately four million CHWs reported from 93 countries), and Kirkwood et al., Lancet 2013 (pooled programme-setting home-visit trials: 12% lower neonatal mortality, 95% CI 5–18%). These are different populations and evidence types, not a universal Healthy Future effect.

## Reuse and provenance

CareLoom: Apache-2.0. Healthy Future curriculum: © 2022 Stanford University, CC BY-NC 4.0; English PDF September 2025. Curriculum diagram/cover derive from the Belgium presentation and curriculum. The clean cover was produced by image editing to remove the embedded program title while retaining the artwork. Public interface screenshot contains no participant records. Instrument Serif, Source Sans 3 and JetBrains Mono retain SIL OFL licenses. Institutional logos are their respective institutions’ marks, used to credit research collaborators.

Logo sources: UNC official University Signature package (identity.unc.edu, August 2026); Stanford official full wordmark (identity.stanford.edu, June 2020); Sichuan University official website header wordmark (scu.edu.cn/images/logo.png, displayed on navy); UNR mark from the existing lab website partner assets.

## Publishing

This repository uses the existing `sylvia-talks` Netlify site at `talks.ssylvia.io` (root `_publish.yml`). GitHub stores editable source. Retain the currently published site and add/replace only the current talk’s HTML and v8 PDF. Do not remove older talk assets or the original v7 PDF. Current website/CareLoom implementation PRs remain separate; source availability is not a packaged public release.
