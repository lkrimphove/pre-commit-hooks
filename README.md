# pre-commit-hooks

A collection of useful hooks for pre-commit.

See also:
- https://github.com/pre-commit/pre-commit
- https://github.com/pre-commit/pre-commit-hooks

## Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/l.krimphove/pre-commit-hooks
    rev: v0.1.0  # Use the ref you want to point at
    hooks:
    -   id: parse-obsidian-links
    # -   id: ...
```

## Hooks available

### parse-obsidian-links
Parses Obsidian.md links to regular Markdown links:
```markdown
from:
[[link-name|test-file]]

to:
[link-name](../path/to/test-file)
```