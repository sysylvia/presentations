# Healthy Future — speaker notes and timing

14 main slides, 720 planned seconds, including about one minute of the 2:18 demo. Four backups follow. No timed rehearsal performed.

## 1. Opening Healthy Future — 20 seconds

[20 seconds] Introduce Healthy Future and CareLoom. Today: the program, evidence, reusable infrastructure, and the next research phase. Background is a text-free derivative of the Healthy Future curriculum cover; original retained. Curriculum artwork: Healthy Future Program, Stanford University, CC BY-NC 4.0.

## 2. Healthy Future collaborators — 25 seconds

[25 seconds] Healthy Future is a collaboration across these institutions, local health systems and participating families. Credits combine contributors to the protocol and published Healthy Future studies, not just one paper. Institutional groupings follow the public project credits. Thank the implementation teams and families verbally.
Source: https://dhep.org/healthy-future/ (collaborators and linked publications; checked November 13, 2026).

## 3. Home visits: global reach, demanding delivery — 65 seconds

[65 seconds] CHWs are a large global workforce; the four-million figure is reporting from 93 countries, not a census of home visitors. The home-visit estimate is a historical pooled effect on neonatal mortality in programme-setting trials in South Asia and sub-Saharan Africa, not a prediction for every programme or for Healthy Future. WHO identifies training, supervision, quality and workload as implementation needs. The two highlighted content-allocation problems motivate our work: our stage-based system does not yet provide validated outcome-informed personalization. Do not describe all CHW programmes as uniformly one-size-fits-all or without data.
Sources: WHO EB156/15 (20 December 2024), §9; Kirkwood et al. 2013, doi:10.1016/S0140-6736(13)60095-1, pooled programme-setting estimate; WHO 2018 CHW guideline, selection/training, supportive supervision, workload and data recommendations.

## 4. The Problem: One Visit, Many Needs — 45 seconds

[45 seconds] This is the Belgium framing: a broad maternal and child health agenda competes for one visit. Responsive caregiving is part of the broader agenda, not a claim that the original Healthy Future trial tested a separate stimulation intervention. For Healthy Future, stage determines scheduled content; families at that stage still differ. Transition to the integrated programme.

## 5. The Healthy Future Program — 45 seconds

[45 seconds] The intervention combines content, people and software. It addresses maternal and child health through stage-matched home visits. The curriculum starts in month four of pregnancy; the full curriculum extends to 18 months after birth. The trial delivered the programme over a 12-month study period; those are different time spans.

## 6. Healthy Future home-visit demo — 70 seconds

[70 seconds, including approximately 60 seconds of video] Show the app guiding a home visit, presenting content and capturing responses. Use the direct link if network access or the embedded player fails. The video is an existing programme demonstration, not new trial evidence. Stop after about one minute to preserve timing.
Source: original Healthy Future Video shared in the Belgium talk. The existing public demo is embedded as a native video; the original Canva link remains available.

## 7. What CHWs deliver: a stage-based curriculum — 45 seconds

[45 seconds] Walk through how topics change over pregnancy and infancy. Mental-health and government-service content recur across stages. This is scheduled content coverage, not evidence that every component has a known causal effect for every family. In the trial, 82% of intervention families received at least one visit; participating families had a median 12 visits and median visit duration 32 minutes. The numerical implementation details are in notes to keep the timeline readable.
Sources: Healthy Future curriculum (English September 2025); Chen et al., medRxiv v2 and September 2026 manuscript, Table 2.

## 8. The Healthy Future Platform — 50 seconds

[50 seconds] This is CareLoom, the platform behind Healthy Future. Describe implemented functions without claiming demonstrated reductions in CHW workload or automatically learned recommendations. Initial login, synchronization and media preparation require connectivity; offline support is qualified accordingly. English and Chinese are supported; other languages and outcome-informed recommendations remain development work. Public screenshot contains no participant records.

## 9. Open Source and Extensible — 35 seconds

[35 seconds] Invite reuse while distinguishing software from curriculum licensing. CPC seed funding supported opening the infrastructure and English-language access. New implementation and documentation changes are under review in separate PRs; this deck links the existing public material. No installable packaged release is claimed.
Sources: CareLoom LICENSE; curriculum attribution page; Sean Sylvia CV, 2024–25 CPC award “Open Sourcing a Maternal and Child Health Home Visiting Platform Called Healthy Future”; https://dhep.org/healthy-future/.

## 10. The initial China randomized trial — 95 seconds

[95 seconds] Township randomization was stratified by county. Two intervention variants, 20 townships each, are pooled here versus 79 controls. The analysis cohort is 1,306; outcome-specific samples differ. The intervention lasted 12 months. The primary dietary-diversity estimate is modest and positive; hemoglobin and exclusive breastfeeding intervals include zero. Selected secondary outcomes show lower reported child illness and caregiver symptoms. These are selected secondary results with multiplicity-adjusted p-values in the backup, not an exhaustive list. Each primary row has its own labeled unit/scale; secondary effects are percentage points. Lines show 95% confidence intervals. Results are a preprint; the later recovered manuscript agrees on these values. Do not infer component-specific effects or validated personalization gains.
Sources: trial protocol doi:10.1136/bmjopen-2022-065403; Chen et al., medRxiv v2, Tables 3–4.

## 11. The backend separates content from delivery — 55 seconds

[55 seconds] Emphasize app versus curriculum: Healthy Future is one curriculum running on a more general delivery platform. Lessons describe stage/age windows and reference topic modules; modules contain scripts, media and structured components. The app renders that configuration. Another curriculum must be structured in the supported model; there is no automatic arbitrary-PDF importer. Explain branching verbally: a configured question can send a family through different content paths. Those authored branches are distinct from learned outcome prioritization.
Sources: CareLoom entities Curriculum, Lesson, Module, Component and LessonService; inspected public revision 71468fae6ce0ca9cd434ebbf847f7eac30cee11e; https://github.com/DHEPLab/careloom.

## 12. Next phase of research — 55 seconds

[55 seconds] Name the Cyrus Tang Foundation, as listed on the public project page. The funded next phase aims to develop predictive models to prioritize the content expected to help an individual family with specified outcomes. Predictive association alone does not establish a causal gain from reallocating modules. The model and allocation rule require prospective evaluation. Do not announce trial recruitment or imply the award scope includes every proposed evaluation. No award amount or dates are added.
Source: public Healthy Future funder listing and HF 2.0 overview; model-development focus specified by Sean for this talk.

## 13. Testing which content to prioritize — 70 seconds

[70 seconds] The planned comparison changes the rule for allocating content while keeping delivery infrastructure and curriculum shared. Compare the stage-based benchmark with family choice and algorithmic prioritization. Prespecify outcomes, eligibility, fidelity and workload measures. The previous whole-program trial does not tell us which module to allocate to which family. This is the proposed future trial, not completed results or a commitment on recruitment date, sample size or finalized protocol.
Source: Belgium talk, Healthy Future 2.0 planning and Sean's requested next-phase comparison.

## 14. Reuse, adapt and contribute — 45 seconds

[45 seconds] Close with one place to start: the existing project website. The compact table summarizes recurring content, not an exhaustive session-by-session schedule. The PDF and software have different licenses. Both source and guides are public; new PRs remain under review and no packaged release is announced. Invite researchers, implementers and developers to contact Sean or the lab. Offer participation in adaptation and evaluation rather than promising implementation support.
Sources: https://dhep.org/healthy-future/; https://dhep.org/contact/; CareLoom LICENSE, guides and contributing instructions; Healthy Future curriculum, September 2025.

## 15. Backup: selected secondary outcomes — 0 seconds

[Backup] Selected secondary outcomes from Table 4 do not replace the primary outcomes. The four shown retain FDR-adjusted p-values below .05 within their domains. Mental-health measures are symptoms or screening classifications, not clinical diagnoses. Effects concern the integrated intervention, not the software alone.

Source: [preprint v2](https://www.medrxiv.org/content/10.64898/2026.03.27.26349570v2.full.pdf), Table 4. Binary estimates and intervals are displayed in percentage points.

## 16. Backup: primary-outcome estimates — 0 seconds

[Backup] Main-slide breastfeeding results convert probability units to percentage points. Hemoglobin IPW sensitivity: −0.346 g/L, 95% CI −1.919 to 1.228. No new participant-level analysis was performed.

Source: [preprint v2](https://www.medrxiv.org/content/10.64898/2026.03.27.26349570v2.full.pdf), Table 3.

## 17. Backup: interpretation and design limits — 0 seconds

[Backup] The intervention variants were randomized, but the main analysis pools them. COVID disrupted follow-up and age-specific availability. Domain indices were post hoc. Prediction and entry timing do not establish mediation or a validated surrogate. Results in rural Sichuan do not establish transferability.

Sources: [preprint v2](https://www.medrxiv.org/content/10.64898/2026.03.27.26349570v2.full.pdf); [protocol](https://doi.org/10.1136/bmjopen-2022-065403).

## 18. Backup: the CareLoom interface — 0 seconds

[Backup] This public interface example illustrates program administration, CHW visits and supervision. It is not a live deployment or evidence of current production readiness. Android app, web administration and API responsibilities are distinct.

Sources: [CareLoom](https://github.com/DHEPLab/careloom); [public screenshot](https://dhep.org/images/healthy-future-chw-app-screenshot.webp).
