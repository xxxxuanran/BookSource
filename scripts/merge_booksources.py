from __future__ import annotations

import json
from pathlib import Path


def prune_empty_values(value: object) -> object:
    if isinstance(value, dict):
        cleaned: dict[str, object] = {}
        for key, item in value.items():
            pruned = prune_empty_values(item)
            if pruned in ("", None):
                continue
            if isinstance(pruned, (dict, list)) and not pruned:
                continue
            cleaned[key] = pruned
        return cleaned

    if isinstance(value, list):
        cleaned_list: list[object] = []
        for item in value:
            pruned = prune_empty_values(item)
            if pruned in ("", None):
                continue
            if isinstance(pruned, (dict, list)) and not pruned:
                continue
            cleaned_list.append(pruned)
        return cleaned_list

    return value


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    output_path = repo_root / "bookSource.json"

    source_files = sorted(repo_root.glob("*.bookSource.json"), key=lambda p: p.name)
    if not source_files:
        output_path.write_text("[]\n", encoding="utf-8")
        print(f"No source files found. Wrote empty array to {output_path}")
        return

    items = [
        prune_empty_values(json.loads(path.read_text(encoding="utf-8")))
        for path in source_files
    ]

    output_path.write_text(
        json.dumps(items, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"Merged {len(source_files)} file(s) into {output_path}")


if __name__ == "__main__":
    main()
