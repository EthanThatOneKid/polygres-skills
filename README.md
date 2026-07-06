# polygres-skills

Nightly-mirrored Polygres docs plus a companion `polygres` agent skill.

## Install

```bash
npx skills add https://github.com/EthanThatOneKid/polygres-skills --skill polygres
```

## What lives here

- `skills/polygres/SKILL.md` - master skill entry point
- `references/upstream/pages/` - mirrored Polygres docs pages
- `references/upstream/manifest.json` - scrape manifest
- `scripts/sync_polygres_sources.py` - repeatable mirror job

## Sync

Run the mirror job with:

```bash
python3 scripts/sync_polygres_sources.py
```

The scraper starts from `https://docs.evokoa.com/polygres`, tries crawl-friendly discovery endpoints when present, and falls back to the rendered nav tree on the landing page.

## Skill

The `polygres` skill is now routed from the mirrored docs:

- `start` - product overview and onboarding
- `workspace` - organization, projects, data, and dashboard operations
- `sdk` - application integration and client setup
- `retrieve` - retrieval configuration and query patterns
- `reference` - guardrails, permissions, limits, and troubleshooting
