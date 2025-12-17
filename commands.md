# 📘 Essential Commands Reference

A beginner-friendly guide to the most important Windows and GitHub commands.

---

## 🖥️ Windows Commands (PowerShell/CMD)

### **File & Directory Navigation**

#### `cd`
Change directory - move between folders.

#### `cd ..`
Go up one folder level.

#### `pwd`
Print working directory - shows your current location.

#### `ls` or `dir`
List all files and folders in current directory.

#### `ls -Force`
Show all files including hidden ones.

---

### **File Management**

#### `mkdir foldername`
Make directory - create a new folder.

#### `New-Item filename.txt`
Create a new empty file.

#### `copy source.txt destination.txt`
Copy a file to another location.

#### `move file.txt newfolder\`
Move a file to another folder.

#### `del filename.txt`
Delete a file.

#### `rmdir foldername`
Remove an empty directory.

#### `rm -Recurse foldername`
Remove a directory and all its contents.

#### `cat filename.txt` or `type filename.txt`
Display file contents in terminal.

---

### **System & Utilities**

#### `cls` or `clear`
Clear the terminal screen.

#### `echo "text"`
Print text to the terminal.

#### `echo "text" > file.txt`
Write text to a file (overwrites existing content).

#### `echo "text" >> file.txt`
Append text to a file (adds to end).

#### `Get-Location`
Get current directory path.

#### `Get-ChildItem`
Get list of items in current directory (detailed).

#### `Get-Content filename.txt`
Read and display file contents.

---

## 🐙 GitHub Commands (Git)

### **Initial Setup**

#### `git config --global user.name "Your Name"`
Set your name for commits.

#### `git config --global user.email "you@example.com"`
Set your email for commits.

#### `git config --list`
View all your Git configurations.

---

### **Repository Basics**

#### `git init`
Initialize a new Git repository in current folder.

#### `git clone <url>`
Download a repository from GitHub to your computer.

#### `git status`
Check the status of your files (modified, staged, etc).

---

### **Basic Workflow**

#### `git add filename.txt`
Stage a specific file for commit.

#### `git add .`
Stage all changed files for commit.

#### `git commit -m "message"`
Commit staged changes with a descriptive message.

#### `git push`
Upload your commits to GitHub (remote repository).

#### `git pull`
Download latest changes from GitHub to your local repo.

---

### **Branching**

#### `git branch`
List all branches and show current branch.

#### `git branch branchname`
Create a new branch.

#### `git checkout branchname`
Switch to a different branch.

#### `git checkout -b branchname`
Create and switch to a new branch (shortcut).

#### `git merge branchname`
Merge another branch into your current branch.

---

### **Information & History**

#### `git log`
View commit history.

#### `git log --oneline`
View commit history in compact format.

#### `git diff`
Show changes in files that aren't staged yet.

#### `git diff --staged`
Show changes in files that are staged.

#### `git remote -v`
View remote repository URLs.

---

### **Undoing Changes**

#### `git restore filename.txt`
Discard changes in a file (revert to last commit).

#### `git restore --staged filename.txt`
Unstage a file (keep changes, just remove from staging).

#### `git reset HEAD~1`
Undo last commit but keep the changes.

#### `git reset --hard HEAD~1`
Undo last commit and discard all changes (⚠️ use carefully).

---

## 💡 Quick Tips

### **Common Workflow Pattern**
```bash
git status              # Check what changed
git add .               # Stage all changes
git commit -m "Update"  # Commit with message
git push                # Upload to GitHub
```

### **Starting a New Project**
```bash
mkdir myproject         # Create project folder
cd myproject           # Enter the folder
git init               # Initialize Git
New-Item README.md     # Create README file
git add .              # Stage files
git commit -m "Initial commit"  # First commit
```

### **Cloning and Working on Existing Project**
```bash
git clone <url>        # Download project
cd projectname         # Enter project folder
git pull               # Get latest changes
# Make your changes
git add .              # Stage changes
git commit -m "Fixed bug"  # Commit
git push               # Upload changes
```

---

## 📌 Important Notes

- Always use `git status` before committing to see what will be committed
- Write clear commit messages that describe what you changed
- Use `git pull` before starting work to avoid conflicts
- Create branches for new features: `git checkout -b feature-name`
- The `.` in `git add .` means "all files in current directory"

---

**Remember:** Practice makes perfect! Don't be afraid to experiment with these commands in a test folder. 🚀
