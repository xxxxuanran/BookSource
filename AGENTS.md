# Repository Guidelines

## Project Structure & Module Organization
Root-level `*.bookSource.json` files are the source of truth for individual Legado 3.0 sites, one file per domain, for example `笔趣阁-www-biquge-tw.bookSource.json`. The generated aggregate import file is [bookSource.json](bookSource.json); treat it as build output, not hand-authored content. Helper automation lives in [scripts/merge_booksources.py](scripts/merge_booksources.py), and scheduled regeneration is defined in [.github/workflows/merge-booksources.yml](.github/workflows/merge-booksources.yml). Repo-specific authoring notes also live under [.codex/skills](.codex/skills).

## Build, Test, and Development Commands
Run `uv run .\scripts\merge_booksources.py` from the repository root to rebuild `bookSource.json` from all source files. Use `git diff -- bookSource.json` to confirm the merged output only contains expected changes. There is no separate build system; contributor work is mainly source editing plus regeneration.

## Source Authoring Workflow
Create or update sources through the local Legado editor and export with `生成源`; do not handcraft the final JSON or paste a full source back through `编辑源`. Validate with the local `调试源` page before saving. `启用搜索` and `CookieJar` should remain enabled in the editor’s `其他` tab.

## Coding Style & Naming Conventions
Keep JSON in UTF-8 and preserve stable formatting. File names must follow `站点名称-formattedDomain.bookSource.json`, while `bookSourceName` should use `站点名称(domain)`. Keep `bookSourceGroup` as an empty string and format `bookSourceComment` as `[ModelName] latestUpdate: yyyy/MM/dd`. In embedded rule JavaScript, use arrow functions for anonymous functions and move reused helpers into `jsLib`. Prefer a small top-level `header`; add request-level `headers` only when a sub-request truly needs a full override.

## Testing Guidelines
Manual validation is the release gate. Before committing, confirm `搜索页`, `详情页`, `目录页`, and `正文页` all return correct, non-empty results. Useful debugger inputs are: keyword for search, direct detail URL for details, `++<目录页URL>` for TOC, and `--<正文页URL>` for content. Test with stable keywords and real chapter URLs, not notices or prefaces.

## Commit & Pull Request Guidelines
Follow the existing Conventional Commit pattern: `feat: add www.biquge.tw source`, `fix: improve QBReader detail parsing`, `chore: update bookSource.json`, `docs: ...`. Keep commits scoped to one source or one tooling change when practical. Pull requests should identify affected domains, note whether `bookSource.json` was regenerated, and include debugger evidence or screenshots when parsing behavior changes.
