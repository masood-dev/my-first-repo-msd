# GitHub Workflow Guide

## Understanding Git and GitHub

Git is a version control system that helps you track changes to your code. GitHub is a platform that hosts Git repositories and adds collaboration features.

## Basic Workflow

### 1. Making Changes

When you want to make changes to your code:

1. **Create a branch**: Branches let you work on new features without affecting the main code
   ```bash
   git checkout -b my-new-feature
   ```

2. **Make your changes**: Edit files, add new code, etc.

3. **Check what changed**:
   ```bash
   git status
   git diff
   ```

4. **Stage your changes**:
   ```bash
   git add <filename>
   # or add all changes
   git add .
   ```

5. **Commit your changes**:
   ```bash
   git commit -m "Add feature: description of what you did"
   ```

6. **Push to GitHub**:
   ```bash
   git push origin my-new-feature
   ```

### 2. Collaborating with Others

- **Pull Requests**: Propose changes to the codebase
- **Issues**: Track bugs, features, and tasks
- **Reviews**: Get feedback on your code before merging

### 3. Keeping Your Repository Up to Date

```bash
# Switch to main branch
git checkout main

# Get latest changes
git pull origin main

# Update your feature branch
git checkout my-new-feature
git merge main
```

## Best Practices

1. **Write clear commit messages**: Describe what and why, not just what
2. **Commit often**: Small, focused commits are better than large ones
3. **Use branches**: Keep main branch stable
4. **Review before pushing**: Check your changes with `git diff`
5. **Pull before pushing**: Get latest changes to avoid conflicts

## Common Scenarios

### Undoing Changes

```bash
# Undo changes to a file (before staging)
git checkout -- <filename>

# Unstage a file
git reset HEAD <filename>

# Amend the last commit
git commit --amend
```

### Viewing History

```bash
# See commit history
git log

# See compact history
git log --oneline

# See changes in a commit
git show <commit-hash>
```

## Learning More

- Practice these commands in this repository
- Try creating branches and making commits
- Experiment with different workflows
- Don't worry about making mistakes - that's how we learn!
