## How to contribute to this repository

- Create a personal fork of the project on Github.
- Clone your forked repository

```
git clone git@github.com:<your-username>/CITM.git
```
- Create a new branch in your repo directory
```
git switch -c <your-new_branch>
```

- After editing, you commit and push changes to your forked repo with respective branch.

```
git push -u origin <your-new-branch>
```

- Remember to add the upstream repo for contribution.

```
git remote add upstream git@github.com:doclai/CTIM.git
```

- **BEFORE** making any new change to the repository, you need to sync your local version with upstream version.

```
git pull upstream main
```

- Go to your fork web interface, click __Compare & Pull request__. Create a pull request with title and content.

```
Title: <name-of-your-change>
Content:
- <why-the-change-is-need?>
- <what-changed?>
```
