## How to contribute to this repository

For first time contribute, check the __New contributors__ section, else, check __Old contributors__.

### New contributors

1. Create a personal fork of the project on Github.
2. Clone your forked repository

```
git clone git@github.com:<your-username>/CITM.git
```

3. Create a new branch in your repo directory
```
git switch -c <your-new_branch>
```

4. After editing, you commit and push changes to your forked repo with the respective branch.
```
git push -u origin <your-new-branch>
```

5. Remember to add the upstream repo for contribution.
```
git remote add upstream git@github.com:doclai/CTIM.git
```

6. Go to your fork web interface, click __Compare & Pull request__. Create a pull request with title and content in the following format.
```
Title: <name-of-your-change>
Content:
- <why-the-change-is-need?>
- <what-changed?>
```

### Old contributors

1. Sync your local files with upstream main repository.
```
git pull upstream main
```

2. After editing, follow step 4, then step 6 of __New contributors__.
