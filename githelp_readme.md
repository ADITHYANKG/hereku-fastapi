# Git Help README

A simple and comprehensive guide to commonly used Git commands.

---

## 1. Initial Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Check config:
```bash
git config --list
```

---

## 2. Create / Clone Repository

Initialize a repo:
```bash
git init
```

Clone a repo:
```bash
git clone <repo_url>
```

---

## 3. Basic Workflow

Check status:
```bash
git status
```

Add files:
```bash
git add <file>
git add .
```

Commit changes:
```bash
git commit -m "message"
```

---

## 4. Branching

List branches:
```bash
git branch
```

Create branch:
```bash
git branch <branch_name>
```

Switch branch:
```bash
git checkout <branch_name>
```

Create + switch:
```bash
git checkout -b <branch_name>
```

Delete branch:
```bash
git branch -d <branch_name>
```

---

## 5. Remote Repositories

Add remote:
```bash
git remote add origin <repo_url>
```

View remotes:
```bash
git remote -v
```

Push to remote:
```bash
git push origin <branch>
```

Push first time:
```bash
git push -u origin <branch>
```

Pull from remote:
```bash
git pull origin <branch>
```

Fetch:
```bash
git fetch
```

---

## 6. Merging & Rebasing

Merge branch:
```bash
git merge <branch>
```

Rebase:
```bash
git rebase <branch>
```

Pull with rebase:
```bash
git pull --rebase origin <branch>
```

---

## 7. Undo Changes

Unstage file:
```bash
git restore --staged <file>
```

Discard changes:
```bash
git restore <file>
```

Reset commit (soft):
```bash
git reset --soft HEAD~1
```

Reset commit (hard):
```bash
git reset --hard HEAD~1
```

---

## 8. Logs & History

View commits:
```bash
git log
```

One-line log:
```bash
git log --oneline
```

Graph view:
```bash
git log --oneline --graph --all
```

---

## 9. Stashing

Save changes:
```bash
git stash
```

List stashes:
```bash
git stash list
```

Apply stash:
```bash
git stash apply
```

Drop stash:
```bash
git stash drop
```

---

## 10. Tags

Create tag:
```bash
git tag v1.0
```

Push tags:
```bash
git push origin --tags
```

---

## 11. Delete / Clean

Remove file:
```bash
git rm <file>
```

Clean untracked files:
```bash
git clean -f
```

---

## 12. Useful Shortcuts

Check differences:
```bash
git diff
```

Amend last commit:
```bash
git commit --amend
```

Rename branch:
```bash
git branch -m <new_name>
```

---

## 13. Common Workflow Example

```bash
git clone <repo>
cd <repo>

git checkout -b feature_x

git add .
git commit -m "add feature"

git push -u origin feature_x
```

---

## 14. Tips

- Commit often
- Use meaningful messages
- Pull before pushing
- Use branches for features

---

## 15. Emergency Fixes

Force push (use carefully):
```bash
git push --force
```

Abort merge:
```bash
git merge --abort
```

Abort rebase:
```bash
git rebase --abort
```

---

**End of Guide**

