---
name: legado-booksource-workflow
description: Adapt, debug, and save Legado 3.0 text book sources in this repository. Use when creating or fixing any .bookSource.json here, validating 搜索页/目录页/正文页 through the local 调试源 page, handling generic chapter-page anti-bot verification flows, or applying this repo's naming and file-output conventions.
---

# Legado Booksource Workflow

## Overview

Use this skill for all book source work in this repository.

Treat the local `调试源` result as the release gate. Do not keep or write a `.bookSource.json` unless `搜索页`、`目录页`、`正文页` all return valid non-empty results in the debugger.

## Workflow

1. Inspect the target site in Chrome DevTools.
2. Confirm how search, detail, toc, and chapter pages are actually built.
3. Build rules in the local Legado source editor.
4. Run `调试源` with a stable keyword and a real chapter.
5. Write the `.bookSource.json` only after all three checks pass.

## Debug Input Conventions

The local debugger accepts different input forms depending on what you want to test.

- 调试搜索: enter a keyword only
- 调试发现: enter `标题::URL`
- 调试详情页: enter a detail page URL directly
- 调试目录页: enter `++<目录页URL>`
- 调试正文页: enter `--<正文页URL>`

Use the raw detail, toc, or chapter URL forms when you want to isolate one phase without rerunning the whole chain.

## Debugging Checklist

### Search page

- Use a stable title keyword that is guaranteed to exist on the site.
- Confirm the debugger returns a non-empty list.
- Confirm the selected item has correct `书名`, `作者`, `详情页链接`.
- If full-chain debugging is noisy, re-run only the detail/toc/content phase with the dedicated debugger input forms.

### Directory page

- Confirm the toc source is HTML or an API.
- If the site has a chapter API, prefer the API over DOM expansion.
- Confirm the debugger returns a non-empty chapter list.
- Confirm the first real chapter URL is valid.
- Filter out non-chapter items such as volume rows or notices when needed.
- Use `++<目录页URL>` to test toc parsing directly when the search or detail phase already works.

### Content page

- Confirm the debugger returns non-empty body content, not only a title.
- If content is empty, inspect the raw chapter response and determine whether the site returned:
  - anti-bot verification HTML
  - a redirect
  - a short notice-only chapter
  - unexpected container structure
- Prefer validating content with a long normal chapter, not a preface or note chapter.
- Use `--<正文页URL>` to test chapter extraction directly against a known real chapter.

## Anti-Bot Heuristic

If the debugger reaches the chapter URL but returns verification HTML instead of the chapter body, parse the validation response first and request the real chapter again before extracting content.

Typical patterns:

- the first chapter request returns a verification HTML page instead of the chapter body
- the verification page embeds a token in inline JavaScript
- the browser is expected to retry the same path with an extra query parameter

In these cases, handle the verification inside `ruleContent` by:

1. checking whether `src` is a verification page
2. extracting the token or redirect input
3. requesting the chapter URL again with the required verification parameter
4. parsing the returned real chapter HTML

## Repository Rules

Read [project-rules.md](references/project-rules.md) before saving files.

When writing the final source JSON, keep `bookSourceGroup` empty and set `bookSourceComment` to the required repository format from `project-rules.md`.
