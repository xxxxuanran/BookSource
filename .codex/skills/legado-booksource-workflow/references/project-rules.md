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
- `目录页` must return a valid chapter list
- `正文页` must return non-empty content
- Do not write the file until all three pass

## Debugger Input Rule

Use the debugger's dedicated input forms when isolating a phase:

- 搜索: keyword only
- 发现: `标题::URL`
- 详情页: direct detail URL
- 目录页: `++<目录页URL>`
- 正文页: `--<正文页URL>`

## Research Rule

- Internet resources may be used only as references for ideas or patterns
- Do not directly copy a ready-made source file into this repository
- The final source must be independently derived from local inspection and debugger verification
