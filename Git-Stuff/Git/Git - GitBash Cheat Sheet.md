# Git - GitBash Cheat Sheet

#### File and Directory Commands
| __Description__        | __Command__ |
|------------------------|------|
| View directory content | $ ls |
| View hidden files      | $ ls -a |
| Create file in console | $ touch filename     |
| Delete file in console | $ rm filename    |
| Create directory       | $ mkdir directoryname |
| Delete directory       | $ rmdir directory name |
| Delete directory with content | $ rm directoryname -rf |
| Rename file with GIT command | $ git mv old_file.txt new_file.txt |
| Remove file with GIT (git tracks deletion) | $ git rm demo.txt |


#### General Commands
| __Description__        | __Command__ |
|------------------------|------|
| Location of .gitconfig (VISTA and higher) | C:\ProgramData\Git |
| List all config values | $ git config --list |
| Set user name | $ git config --global user<span>.</span>name "MyName" |
| Set user email | $ git config --global user.email "my<span>Name</span>@somemail.com" |
| Get help | $ git help <span>"verbNoQuote</span>" |
| Create GIT alias (example, commit log) | $ git config --global alias.hist "log --oneline --graph --decorate --all" |


#### Repository / Repository File Commands
| __Description__        | __Command__ |
|------------------------|------|
| Update local repository with remote content | $ git pull or git pull origin master (or branch name) |
|  |   Same as: $ git fetch then git merge |
| Update remote with local repository content | $ git push or git push origin master (or branch name) |
| Add all files to staging | $ git add -A or git add . |
| Add specific files to staging | $ git add filename<span>.py</span> |
| Remove file from staging | $ git reset file<span>name.</span>py |
| Remove all files from staging | $ git reset HEAD |
| Discard file edit/change(s) | $ git checkout filename<span>.</span>py |
| Commit a file | $ git commit -m <span>"Commit message</span>" |
| Stage and commit a file | $ git commit -am <span>"Commit message</span>" |
| Edit last commit message | $ git commit --amend |
| Check files that GIT is tracking | $ git ls-files |
| Untrack a file | $ git rm --cached filename<span>.</span>py |
| Stashing file edits instead of add and commit | $ git stash |
| View stash (WIP) list | $ git stash list |
| Remove stash, apply changes | $ git stash pop |


#### Branch Commands
| __Description__        | __Command__ |
|------------------------|------|
| Create local branch | $ git checkout -b branchname |
| Merge branches (from branch you want to merge into) | $ git merge branchname |
| Pull a remote branch to local (and track with remote) | $ git fetch then git checkout branchname |
| Push a local branch to remote (tracked) | $ git push -u origin branchname |
| Create a branch off of a branch (local) | $ git checkout -b newbranchname offbranchname |
|  | $ Complete work then: git commit -am "Your message" |
|  | $ Now merge your changes: git checkout offbranchname then git merge --no-ff newbranchname |
|  | $ Now push changes to remote: git push origin offbranchname then git push origin newbranchname |
| Delete a branch (local) | $ git branch -d branchname |
| Remove dead branches (local) | $ git fetch -p (-p = prune) |
| Check branch differences | $ git diff branch_1 branch_2 |


#### Commit / Version Tagging Commands
| __Description__        | __Command__ |
|------------------------|------|
| Tag last commit as version (annotated) | $ git tag -a v1.0.0 -m "Version 1.0.0 release" |
| View annotated tag information | $ git show v1.0.0 |
| Create tag at specific place (commit) | $ git tag -a v0.3-beta -m "Release 0.3 (Beta)" 70edf22 |
| Push tag to remote (by default, not pushed) | $ git push origin name_of_tag |
| Push all tags to remote | $ git push --tags |