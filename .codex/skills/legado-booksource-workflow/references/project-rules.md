# Project Rules

## Naming Rule

These rules came from the initial repository instruction and apply to all future work in this repo.

- Source display name must be `站点名称(domain)`
- Format only. Do not add site-specific examples into skill content.

- Output filename must be `站点名称-formattedDomain.bookSource.json`
- Format only. Replace `formattedDomain` with the domain where dots are converted to hyphens.

## Source Metadata Rule

- `bookSourceComment` must use `[ModelName] latestUpdate: yyyy/MM/dd`
- In this repository, use the active agent/model label consistently
- `bookSourceGroup` must always be an empty string

## Validation Gate

- You must use the local `调试源` page before writing or updating a `.bookSource.json`
- `搜索页` must return a valid book list
- `详情页` must return correct metadata and the intended intro formatting
- `目录页` must return a valid chapter list
- `正文页` must return non-empty content
- Do not write the file until all three pass

For `详情页` intro formatting:

- Preserve an intentional first-line leading indent when the source design uses one
- Preserve intentional blank lines before labeled sections such as `🏷️ 标签` or `📍版权来源`

## Editor Workflow Rule

- New sources must be created and edited through the internal book source editor page, operated with Chrome DevTools
- Fill the editor through visible form fields only
- Do not use `编辑源` to paste or restore a finished JSON blob back into the editor
- Do not directly handcraft the final `.bookSource.json`
- Use the page's `生成源` capability to obtain the final JSON before saving
- In the editor page `其他` tab, `启用搜索` and `CookieJar` must be enabled

## Header Rule

- If a request can use the top-level `header`, prefer that
- Prefer ordinary requests with a small fixed top-level `header` over `webView` when the site works that way
- If a sub-request must define its own `headers`, redefine the complete header object there
- Request-level custom headers override the top-level `header` instead of merging with it

## JS Style Rule

- Anonymous functions must use arrow functions such as `()=>{}`
- Only named functions may use the `function` keyword

## Content Title Rule

- Prefer leaving the content `标题规则` empty so the chapter title defaults to the title obtained from the directory phase
- Only fill the content `标题规则` when the directory title is unreliable or needs correction from the chapter response

## Content Extraction Rule

- Prefer extracting the 正文主容器 first
- Do not add source-side cleanup unless it is required to make parsing work
- Leave normal post-processing to 阅读 APP when possible

## Debugger Input Rule

Use the debugger's dedicated input forms when isolating a phase:

- 搜索: keyword only
- 发现: `标题::URL`
- 详情页: direct detail URL
- 目录页: `++<目录页URL>`
- 正文页: `--<正文页URL>`

## Search Redirect Rule

- If an exact-title search triggers a 30x redirect to the detail page, you may rely on that behavior when 阅读 APP or the debugger can parse the redirected page as a detail result
- If you need to validate true search-list parsing, switch to a stable keyword that returns multiple results instead of redirecting

## Research Rule

- Internet resources may be used only as references for ideas or patterns
- Do not directly copy a ready-made source file into this repository
- The final source must be independently derived from local inspection and debugger verification
