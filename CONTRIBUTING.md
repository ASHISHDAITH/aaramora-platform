# Contributing

## Before changing the interface
1. Read `docs/DESIGN_RESEARCH_AND_DIRECTION.md` and `docs/DESIGN_SYSTEM.md`.
2. Preserve the user's choice to skip, leave or find human support without account creation.
3. Keep safety/help information independent of third-party APIs and JavaScript-dependent features.
4. Avoid engagement mechanics, forced disclosure, autoplay, surprise motion, fake testimonials and AI-companion behaviour.

## Health-content changes
- Do not publish clinical content without a named qualified reviewer, source list, review date and next review/expiry date.
- Do not turn general information into diagnosis, individual treatment, medication/dose or supplement instructions.
- Preserve uncertainty. Observational associations must not be rewritten as causal claims.
- Keep PMOS (formerly PCOS) terminology and PCOS search synonyms during the naming transition.
- Check translations with native speakers and clinical reviewers.

## Pull requests
- Keep changes focused and describe the evidence or user need behind them.
- Include responsive, keyboard and reduced-motion checks for UI changes.
- Update the relevant documentation and QA checklist.
- Never include real personal mental-health data or credentials in tests, issues, screenshots or fixtures.

## Kiro IDE workflow

The primary development IDE for ongoing work is Kiro. Before editing, follow [the Kiro handoff guide](docs/KIRO_IDE_HANDOFF.md) and read `brain.md`, `SAFETY.md`, and the relevant feature specification. Work in the existing static HTML/CSS/JavaScript project; do not scaffold a replacement or remove existing pages, content, assets, data or tests. Preserve all current support-route and privacy constraints. Use small additive changes, run focused and full tests, validate catalogue records, inspect the complete Git diff, and update project memory and relevant docs. GitHub remains the source of truth. Vercel deployment is a separate, deliberate step and must be verified against the exact deployed commit.
