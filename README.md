# ResInsight User Documentation

## Edit documentation
Edit documentation in the folder **content**

## Preview the documentation locally
Download Hugo and install locally from
https://github.com/gohugoio/hugo/releases

The **master** branch is intended to represent the documentation source for current published website at **gh-pages**. The **next-major-release** branch is intended to be used to document new features not yet released. When a new release is published, **next-major-release
** is merged into **master**

1. Clone the branch to work on
2. Open a command line prompt, and make sure `hugo.exe` is available in path
3. Execute command `hugo.exe serve`. This will start a local webserver and display the documentation

## Publish the documentation
- Execute command `hugo.exe` This will create the static site in the folder `public`
- Publish the generated site to the branch `gh-pages`
  - Either : Copy content of folder public into branch `gh-pages` and push changes to github manually
  - Or : Use a script for linux `publish_to_ghpages.sh`, will automatically publish content of public to gh-pages branch on GitHub

## See beta documentation online
https://opm.github.io/ResInsight-UserDocumentation/

## Publish to resinsight.org
- In `config.toml`, set `baseURL = "https://resinsight.org/"`
- Generate site by executing command `hugo.exe`
- Make sure there is a file named CNAME with content resinsight.org
- Publish to https://github.com/OPM/ResInsight/tree/gh-pages

## Tips and trics
- If you want to publish a page, but avoid having an entry in the menu, add `hidden = true` to the header of the MD file. See about.md for an example.
