# Updating Documentation from ResInsight Changes

How to keep this repository in sync with changes in [OPM/ResInsight](https://github.com/OPM/ResInsight). Applies to the `next-major-release` branch, which is published to [beta.resinsight.org](https://beta.resinsight.org).

Two kinds of updates flow from ResInsight into this repo:

| What | Location | How it is updated |
|------|----------|-------------------|
| Python API (`rips` package, `.proto` files) | `docs/` | Automated pull request |
| User interface documentation | `content/`, `assets/images/` | Manual, per feature |

---

## 1. Python API (automated)

The workflow `.github/workflows/update-from-latest.yml` runs daily. It downloads the `dev-latest` build of ResInsight and `rips` from [CeetronSolutions/resinsight-builds](https://github.com/CeetronSolutions/resinsight-builds/releases/tag/dev-latest), copies the package into `docs/rips/`, fetches `.proto` files from `GrpcInterface/GrpcProtos` on the ResInsight `dev` branch into `docs/proto/`, and opens a pull request titled **Automated updates from ResInsight repository**.

To process it:

1. Review the diff of `docs/rips/` and `docs/proto/`. Look for removed or renamed methods that pages in `content/scripting/` refer to.
2. Merge the pull request. Close stale duplicates, since each run uses a new branch name.
3. Nothing else to regenerate. `ProtobufStructures.rst`, the class and enum index, and the Python example pages are generated at Sphinx build time by `docs/source/conf.py`.

To check the API docs locally, follow [`docs/README.md`](../docs/README.md).

---

## 2. User interface documentation (manual)

### Find what changed

ResInsight marks fixed issues with the **PendingRelease** label until the next release. This is the primary list of candidates:

```sh
gh issue list -R OPM/ResInsight --label PendingRelease --state closed --limit 300 \
  --json number,title,labels,closedAt \
  --jq 'sort_by(.closedAt) | .[] | "\(.number)\t\(.closedAt[:10])\t\([.labels[].name] | join(","))\t\(.title)"'
```

To list only changes since the last documentation update:

```sh
git log -1 --format=%cs -- content/          # date of last content change
gh pr list -R OPM/ResInsight --base dev --state merged \
  --search "merged:>=YYYY-MM-DD" --limit 200
```

Read the issue and the linked pull request before writing. The pull request diff shows the actual UI labels, menu paths and default values.

### Decide whether a change needs documentation

| Change | Action |
|--------|--------|
| New feature, plot type, import/export format | New or extended page, plus release note entry |
| Changed menu, renamed command, new property in an editor | Update every page that mentions the old wording |
| Removed feature or toolbar | Remove or rewrite references; check `relref` links to deleted pages |
| User-visible bug fix | Release note entry under **Additional Fixes and Improvements**, if notable |
| Internal refactoring, build, tests | Nothing |

To find pages affected by a renamed or removed UI element, search for the old wording:

```sh
grep -rn "Old Menu Name" content/
```

### Map the change to a section

| ResInsight area | Content folder |
|-----------------|----------------|
| 3D views, cell results, filters, contour maps | `content/3d-main-window/` |
| Plots (summary, RFT, well log, histogram, ...) | `content/plot-window/` |
| File import, ensembles | `content/import/` |
| Export (COMPDAT, MSW, sector models, ...) | `content/export/` |
| Well paths, completions, fractures, MSW | `content/Wells-and-Completions/` |
| Calculator, statistics, derived results | `content/calculated-data/` |
| OPM Flow runs | `content/opm-flow-integration/` |
| Python, command file, command line | `content/scripting/` |

Images go in the matching `assets/images/<section>/` folder.

### Collect screenshots from the issue

Screenshots for the documentation are attached to the ResInsight issue, so they can be fetched automatically. When a feature is done, the developer adds the **Documentation** label and posts one comment starting with `### Documentation`:

```markdown
### Documentation

Page: plot-window/SummaryPlots.md

<img width="1278" alt="plot-window/SummaryPlotCommonLegend.png" src="https://github.com/user-attachments/assets/..." />
Common legend shown once for all subplots.
```

- **Alt text is the target path** below `assets/images/`: an existing section folder, PascalCase name, lowercase `.png` or `.jpg`. GitHub sets `alt="Image"` on paste; replace it with the path.
- **Reusing an existing name replaces that image**, so pages that link to it stay valid.
- **The first paragraph below an image** is its caption. **`Page:`** (optional) names the page to update.
- **Use a comment, not the issue description.** The description shows the problem; the comment shows the finished state. The newest `### Documentation` comment wins.
- **Images with other alt text are ignored**, so discussion screenshots are never picked up.

Fetch the images:

```powershell
$env:GITHUB_TOKEN = gh auth token
python scripts/fetch_issue_images.py --dry-run        # all issues labelled Documentation + PendingRelease
python scripts/fetch_issue_images.py 14891 14878      # specific issues
```

The script saves images to `assets/images/`, compresses PNG files when `pngquant` or `oxipng` is on `PATH`, and writes `issue-images.json` (ignored by git) listing issue, path, caption, page and whether the image is new or a replacement. Give the manifest to the `docs-writer` agent as input. Invalid paths are reported and skipped.

### Write the update

Use the `docs-writer` agent (see [`docs-writer.md`](docs-writer.md)) for all page edits. It holds the frontmatter, cross-reference, image and terminology rules.

- Take new screenshots from a current `dev` build. Replace an outdated image in place rather than adding a new file, so existing references keep working.
- Keep one ResInsight feature per commit. Reference the upstream issues in the commit body, for example `(OPM/ResInsight#14878, #14880)`.

### Verify

```powershell
& 'f:\tools\hugo\hugo_0.167.0\hugo.exe' --minify
```

The build must succeed without warnings about missing `relref` targets. Use `hugo serve` to inspect changed pages. Codespell runs on pull requests against `content/`; add legitimate domain terms to `.codespell-ignore`.

---

## 3. At release time

1. Create `content/releases/release-notes/releasenotes_YYYY_MM.md` from the **PendingRelease** list. Group by feature and link each section to the page documenting it.
2. Move `aliases = ["/releases/release-notes/latest/"]` from the previous release note to the new one.
3. Merge `next-major-release` into `master` to publish to [resinsight.org](https://resinsight.org). See the publish steps in [`README.md`](../README.md).
4. Clear the label in ResInsight:

   ```powershell
   $env:GITHUB_TOKEN = gh auth token
   python scripts/remove_pending_release_label.py --dry-run
   python scripts/remove_pending_release_label.py
   ```
