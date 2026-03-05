# ResInsight User Documentation

## Writing Documentation

Use the `docs-writer` agent when writing or editing any documentation page:

```
Agent tool → subagent_type: "docs-writer"
```

The agent knows the Hugo content structure, frontmatter format, cross-reference syntax, writing conventions, and trademark guidance for this project. Its instructions are in [`agents/docs-writer.md`](agents/docs-writer.md).

## Writing Python Examples

Use the `python-script-writer` agent when writing or editing `rips` Python example scripts under `docs/rips/PythonExamples/`:

```
Agent tool → subagent_type: "python-script-writer"
```

The agent knows the rips API conventions, script structure, error-handling patterns, polygon workflows, property read/write patterns, and how to reference the API at https://api.resinsight.org. Its instructions are in [`agents/python-script-writer.md`](agents/python-script-writer.md).
