# Opening Healthy Future — Demography Daze 2026

[View slides](https://talks.ssylvia.io/research/2026-11-demography-daze-hf/slides.html) · [PDF](slides-v7.pdf)

Quarto Reveal.js version of the completed v7 DHEPLab deck for November 13, 2026. Eleven main slides retain a 12-minute working target; six labeled backup slides follow the closing slide. The original PowerPoint and PDF are unchanged.

## Edit and render

Edit `slides.qmd` and run `quarto render` in this directory (verified with Quarto 1.6.43). This is a nested standalone project: rendering it does not render other presentations. Output is `_rendered/slides.html`. Fonts and media are embedded, so the HTML can also be opened offline.

Use arrow keys to navigate, `O` for overview, `F` for fullscreen and `S` for speaker view. The main route ends at slide 11; slides 12–17 are backup. Notes contain speaking cues, timing, evidence limits and public citations.

## Figures and sources

`evidence.json` contains only published aggregate estimates from Chen et al., medRxiv v2 (June 16, 2026), Tables 3–4. Binary probability differences are multiplied by 100 for percentage-point displays. There is no participant dataset or new analysis. Run `python3 render_figures.py` after editing the aggregate values or figure layout; it regenerates the editable inline SVG fragments in `figures/`.

Architecture and branching diagrams reflect CareLoom source inspected at revision `71468fae6ce0ca9cd434ebbf847f7eac30cee11e`. Configured branching is distinguished from proposed learned prioritization. Exploratory heterogeneity stays qualitative; inconsistent outcome labels in the prior Belgium material do not support exact numerical claims here. The historical 2024 deck does not override the current evidence.

The curriculum excerpt is from the September 2025 English PDF, printed p.151 / PDF p.153, © 2022 Stanford University, CC BY-NC 4.0. The CareLoom interface is the existing public project screenshot, with no participant records. DHEPLab artwork comes from the repository's original logo. Instrument Serif, Source Sans 3 and JetBrains Mono retain their included SIL OFL licenses.

## Publishing

This repository's established target is the existing `sylvia-talks` Netlify site at `talks.ssylvia.io` (see root `_publish.yml`). GitHub stores the editable source; GitHub Pages is not enabled by this addition. The public files for this talk are the self-contained HTML and the matching PDF, under `research/2026-11-demography-daze-hf/`.

When updating the existing site, retain its current published files and add or replace only this talk's directory. A deployment containing only the new talk would replace the rest of the site. Verify the live slide URL and retained older URLs after publishing. Local review logs and deployment receipts are kept outside this repository.
