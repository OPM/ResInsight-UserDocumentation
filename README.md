# ResInsight User Documentation

This repository contains both the source code for three documentation sites

    resinsight.org
    beta.resinsight.org
    api.resinsight.org

The Python API is documented in the `docs` folder.

Documentation for ResInsight User Interface is located in the `content` folder.

## Edit of the documentation for Python API
[Edit docs for Python API](docs/README.md)

## Edit documentation
Edit documentation in the folder **content**

## Preview the documentation locally
Download Hugo and install locally from
https://github.com/gohugoio/hugo/releases

It is also possible to install Hugo using package managers
    sudo apt install hugo

**Last known working version is **
https://github.com/gohugoio/hugo/releases/tag/v0.113.0

The **next-major-release** branch is intended to represent the new features not yet released. The content of this branch is automatically published to **gh-pages** of this repository. This website can be reached by https://beta.resinsight.org

The **master** branch is intended to represent the documentation for latest public release, and is used as source for resinsight.org

1. Clone the branch to work on
2. Open a command line prompt, and make sure `hugo.exe` is available in path
3. Execute command `hugo.exe serve`. This will start a local webserver and display the documentation

## See beta documentation online
https://beta.resinsight.org redirects to https://opm.github.io/ResInsight-UserDocumentation/

## Publish to resinsight.org
- Update master branch from **next-major-release**
- In `config.toml`, set `baseURL = "https://resinsight.org/"`
- Generate site by executing command `hugo.exe`
- Checkout gh-pages from https://github.com/OPM/ResInsight
- Make sure there is a file named CNAME with content resinsight.org
- Copy content from Hugo into gh-pages
- Publish to https://github.com/OPM/ResInsight/tree/gh-pages

## Tips and tricks
- If you want to publish a page, but avoid having an entry in the menu, add `hidden = true` to the header of the MD file. See about.md for an example.

- Use the following syntax to define a text region with fixed font size
```txt
row a   row b   rov c
1       2       2   
2       2       5
34      23      2
```
