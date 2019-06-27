# ResInsight User Documentation

## Edit documentation
Edit documentation in the folder **content**

## Preview the documentation locally
Download Hugo and install locally from
https://github.com/gohugoio/hugo/releases

1. Clone the master branch
2. Open a command line, and make sure `hugo.exe` is available in path
3. Execute command `hugo.exe serve` This will start a local webserver and display the documentation

## Publish the documentation
- Execute command `hugo.exe` This will create the static site in the folder `public`
- Publish the generated site to the branch `gh-pages`
  - Either : Copy content of folder public into branch `gh-pages` and push changes to github manually
  - Or : Use a script for linux `publish_to_ghpages.sh`, will automatically publish content of public to gh-pages branch on GitHub

## See documentation online
https://opm.github.io/ResInsight-UserDocumentation/
