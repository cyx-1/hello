# GitPython Library Illustration

This example demonstrates how the **GitPython** library supports common git commands in Python. GitPython provides a Python-friendly interface to interact with Git repositories programmatically.

## Requirements

- **Python Version**: Python 3.8 or higher
- **Library**: gitpython >= 3.1.40
- **Installation**: Dependencies are managed automatically via inline script metadata

## Running the Example

Using `uv` (recommended):
```bash
cd python/gitpython
uv run main_gitpython.py
```

## What is GitPython?

GitPython is a Python library that provides:
- Object-oriented access to Git repositories
- Pythonic interfaces for common git operations
- Support for both high-level and low-level git commands
- Direct access to git command-line when needed

**Key capabilities:**
- Initialize and configure repositories
- Stage, commit, and track changes
- Branch and merge operations
- View history, diffs, and file annotations
- Tag management
- Remote repository operations

## Source Code and Output Walkthrough

### 1. Repository Initialization (Lines 35-38)

**Source Code:**
```python
35  # LINE 35: Initialize a new repository
36  print_section("1. git init - Initialize Repository")
37  repo = git.Repo.init(temp_dir)
38  print(f"Initialized empty Git repository in {repo.git_dir}")
```

**Output:**
```
======================================================================
  1. git init - Initialize Repository
======================================================================

Initialized empty Git repository in /tmp/gitpython_demo_r_5ek7dh/.git
```

**Explanation:** Line 37 initializes a new Git repository using `git.Repo.init()`, equivalent to running `git init` from the command line. The method returns a `Repo` object that we use for all subsequent operations.

---

### 2. Configuration (Lines 40-47)

**Source Code:**
```python
40  # LINE 40: Configure user
41  print_section("2. git config - Configure User")
42  with repo.config_writer() as config:
43      config.set_value("user", "name", "Demo User")
44      config.set_value("user", "email", "demo@example.com")
45  print("Configuration set:")
46  print(f"  user.name = {repo.config_reader().get_value('user', 'name')}")
47  print(f"  user.email = {repo.config_reader().get_value('user', 'email')}")
```

**Output:**
```
======================================================================
  2. git config - Configure User
======================================================================

Configuration set:
  user.name = Demo User
  user.email = demo@example.com
```

**Explanation:** Lines 42-44 demonstrate git configuration using a context manager. The `config_writer()` sets values (like `git config user.name`), while `config_reader()` on lines 46-47 retrieves them.

---

### 3. Staging Changes (Lines 50-58)

**Source Code:**
```python
50  # LINE 50: Create and add a file (git add)
51  print_section("3. git add - Stage Changes")
52  file_path = Path(temp_dir) / "README.md"
53  file_path.write_text("# GitPython Demo\n\nThis is a demo repository.\n")
54  print(f"Created file: {file_path.name}")
55
56  repo.index.add(["README.md"])
57  print("Staged file: README.md")
```

**Output:**
```
======================================================================
  3. git add - Stage Changes
======================================================================

Created file: README.md
Staged file: README.md
```

**Explanation:** Line 56 stages the file using `repo.index.add()`, which is equivalent to `git add README.md`. The `index` object represents the staging area.

---

### 4. Repository Status (Lines 60-67)

**Source Code:**
```python
60  # LINE 60: Check status
61  print_section("4. git status - Check Repository Status")
62  # Check for staged files (before first commit, we check index entries)
63  staged_files = [item[0] for item in repo.index.entries.keys()]
64  untracked_files = repo.untracked_files
65  print(f"Staged files: {staged_files}")
66  print(f"Untracked files: {untracked_files if untracked_files else 'none'}")
```

**Output:**
```
======================================================================
  4. git status - Check Repository Status
======================================================================

Staged files: ['README.md']
Untracked files: none
```

**Explanation:** Lines 63-64 show two ways to check repository status: `repo.index.entries` for staged files and `repo.untracked_files` for untracked files, similar to `git status`.

---

### 5. Creating Commits (Lines 69-74)

**Source Code:**
```python
69  # LINE 67: Make first commit (git commit)
70  print_section("5. git commit - Create Commit")
71  commit1 = repo.index.commit("Initial commit")
72  print(f"Commit created: {commit1.hexsha[:8]}")
73  print(f"  Author: {commit1.author.name} <{commit1.author.email}>")
74  print(f"  Message: {commit1.message.strip()}")
75  print(f"  Date: {commit1.committed_datetime}")
```

**Output:**
```
======================================================================
  5. git commit - Create Commit
======================================================================

Commit created: 23d630a6
  Author: Demo User <demo@example.com>
  Message: Initial commit
  Date: 2025-11-11 22:15:48+00:00
```

**Explanation:** Line 71 creates a commit using `repo.index.commit()`, equivalent to `git commit -m "Initial commit"`. The returned `Commit` object provides access to metadata like SHA, author, message, and timestamp.

---

### 6. Branch Operations (Lines 76-88)

**Source Code:**
```python
76  # LINE 76: Create a new branch (git branch & git checkout)
77  print_section("6. git branch & git checkout - Branch Operations")
78  new_branch = repo.create_head("feature/demo")
79  print(f"Created branch: {new_branch.name}")
80
81  new_branch.checkout()
82  print(f"Checked out branch: {repo.active_branch.name}")
83
84  # LINE 85: List all branches (git branch -a)
85  print("\nAll branches:")
86  for branch in repo.heads:
87      marker = "*" if branch == repo.active_branch else " "
88      print(f"  {marker} {branch.name}")
```

**Output:**
```
======================================================================
  6. git branch & git checkout - Branch Operations
======================================================================

Created branch: feature/demo
Checked out branch: feature/demo

All branches:
  * feature/demo
    master
```

**Explanation:** Line 78 creates a branch with `repo.create_head()` (`git branch`), line 81 switches to it with `.checkout()` (`git checkout`), and lines 86-88 list all branches (`git branch -a`). The asterisk marks the active branch.

---

### 7. Modifying and Committing (Lines 91-98)

**Source Code:**
```python
91  # LINE 91: Make changes and commit on feature branch
92  print_section("7. Modify File and Commit")
93  file_path.write_text("# GitPython Demo\n\nThis is a demo repository.\n\n## Feature\nAdded new feature.\n")
94  print(f"Modified file: {file_path.name}")
95
96  repo.index.add(["README.md"])
97  commit2 = repo.index.commit("Add feature section")
98  print(f"Commit created: {commit2.hexsha[:8]}")
99  print(f"  Message: {commit2.message.strip()}")
```

**Output:**
```
======================================================================
  7. Modify File and Commit
======================================================================

Modified file: README.md
Commit created: a2f3ea9d
  Message: Add feature section
```

**Explanation:** This section demonstrates the standard Git workflow on a feature branch: modify file (line 93), stage changes (line 96), and commit (line 97).

---

### 8. Viewing Commit History (Lines 102-108)

**Source Code:**
```python
102  # LINE 102: Show commit log (git log)
103  print_section("8. git log - View Commit History")
104  for i, commit in enumerate(repo.iter_commits(), 1):
105      print(f"Commit {i}:")
106      print(f"  SHA: {commit.hexsha[:8]}")
107      print(f"  Author: {commit.author.name}")
108      print(f"  Date: {commit.committed_datetime}")
109      print(f"  Message: {commit.message.strip()}")
110      print()
```

**Output:**
```
======================================================================
  8. git log - View Commit History
======================================================================

Commit 1:
  SHA: a2f3ea9d
  Author: Demo User
  Date: 2025-11-11 22:15:48+00:00
  Message: Add feature section

Commit 2:
  SHA: 23d630a6
  Author: Demo User
  Date: 2025-11-11 22:15:48+00:00
  Message: Initial commit

```

**Explanation:** Line 104 uses `repo.iter_commits()` to iterate through the commit history (`git log`). Each commit object provides properties for SHA, author, date, and message.

---

### 9. Viewing Differences (Lines 113-119)

**Source Code:**
```python
113  # LINE 113: Show diff (git diff)
114  print_section("9. git diff - Show Differences")
115  master_branch = repo.heads.master
116  diff = master_branch.commit.diff(commit2)
117  print(f"Differences between {master_branch.name} and {repo.active_branch.name}:")
118  for diff_item in diff:
119      print(f"  Changed file: {diff_item.a_path}")
120      if diff_item.diff:
121          print(f"  Diff preview: {diff_item.diff.decode('utf-8')[:200]}...")
```

**Output:**
```
======================================================================
  9. git diff - Show Differences
======================================================================

Differences between master and feature/demo:
  Changed file: README.md
```

**Explanation:** Line 116 uses the `.diff()` method to compare two commits (`git diff master feature/demo`). The resulting diff objects contain information about changed files and the actual diff content.

---

### 10. Merging Branches (Lines 123-133)

**Source Code:**
```python
123  # LINE 123: Checkout master and merge (git checkout & git merge)
124  print_section("10. git merge - Merge Branches")
125  master_branch.checkout()
126  print(f"Checked out branch: {repo.active_branch.name}")
127
128  base = repo.merge_base(master_branch, new_branch)
129  print(f"Merge base: {base[0].hexsha[:8]}")
130
131  # Perform merge using git command interface
132  # This is a fast-forward merge since feature branch is ahead
133  repo.git.merge(new_branch.name)
134  print(f"Merged {new_branch.name} into {master_branch.name}")
135  print(f"New HEAD: {repo.head.commit.hexsha[:8]}")
```

**Output:**
```
======================================================================
  10. git merge - Merge Branches
======================================================================

Checked out branch: master
Merge base: 23d630a6
Merged feature/demo into master
New HEAD: a2f3ea9d
```

**Explanation:** Line 128 finds the merge base between branches using `repo.merge_base()`. Line 133 performs the actual merge using `repo.git.merge()` (`git merge feature/demo`), which does a fast-forward merge in this case.

---

### 11. Creating Tags (Lines 137-147)

**Source Code:**
```python
137  # LINE 139: Create a tag (git tag)
138  print_section("11. git tag - Create Tags")
139  tag = repo.create_tag("v1.0.0", message="Version 1.0.0 release")
140  print(f"Created tag: {tag.name}")
141  if tag.tag:
142      print(f"  Message: {tag.tag.message}")
143  print(f"  Commit: {tag.commit.hexsha[:8]}")
144
145  # LINE 148: List tags (git tag -l)
146  print("\nAll tags:")
147  for t in repo.tags:
148      print(f"  {t.name} -> {t.commit.hexsha[:8]}")
```

**Output:**
```
======================================================================
  11. git tag - Create Tags
======================================================================

Created tag: v1.0.0
  Message: Version 1.0.0 release
  Commit: a2f3ea9d

All tags:
  v1.0.0 -> a2f3ea9d
```

**Explanation:** Line 139 creates an annotated tag using `repo.create_tag()` (`git tag -a v1.0.0 -m "..."`). Lines 147-148 list all tags (`git tag -l`).

---

### 12. Remote Operations (Lines 153-160)

**Source Code:**
```python
153  # LINE 153: Show remote operations (git remote)
154  print_section("12. git remote - Remote Operations")
155  print("Current remotes:")
156  if repo.remotes:
157      for remote in repo.remotes:
158          print(f"  {remote.name}: {remote.url}")
159  else:
160      print("  No remotes configured")
161
162  # Example of how to add a remote (commented out as it's just for demonstration)
163  print("\nTo add a remote, you would use:")
164  print("  repo.create_remote('origin', 'https://github.com/user/repo.git')")
```

**Output:**
```
======================================================================
  12. git remote - Remote Operations
======================================================================

Current remotes:
  No remotes configured

To add a remote, you would use:
  repo.create_remote('origin', 'https://github.com/user/repo.git')
```

**Explanation:** Lines 156-160 check for configured remotes using `repo.remotes` (`git remote -v`). The example shows how to add a remote with `repo.create_remote()` (`git remote add origin <url>`).

---

### 13. File Annotations (Lines 167-168)

**Source Code:**
```python
167  # LINE 167: Show git blame equivalent
168  print_section("13. git blame - Show File Annotations")
169  blame = repo.blame("HEAD", "README.md")
170  print("File annotations (last 5 lines):")
171  for commit, lines in blame[-5:]:
172      for line in lines:
173          print(f"  {commit.hexsha[:8]} ({commit.author.name}): {line.strip()}")
```

**Output:**
```
======================================================================
  13. git blame - Show File Annotations
======================================================================

File annotations (last 5 lines):
  23d630a6 (Demo User): # GitPython Demo
  23d630a6 (Demo User):
  23d630a6 (Demo User): This is a demo repository.
  a2f3ea9d (Demo User):
  a2f3ea9d (Demo User): ## Feature
  a2f3ea9d (Demo User): Added new feature.
```

**Explanation:** Line 169 uses `repo.blame()` to get line-by-line commit information (`git blame`). This shows which commit last modified each line and who authored it.

---

### 14. Working with HEAD and References (Lines 176-174)

**Source Code:**
```python
176  # LINE 176: Show stash-like operations
177  print_section("14. Working with HEAD and References")
178  print(f"HEAD commit: {repo.head.commit.hexsha[:8]}")
179  print(f"HEAD reference: {repo.head.reference}")
180  print(f"Active branch: {repo.active_branch.name}")
```

**Output:**
```
======================================================================
  14. Working with HEAD and References
======================================================================

HEAD commit: a2f3ea9d
HEAD reference: master
Active branch: master
```

**Explanation:** Lines 178-180 demonstrate accessing HEAD and references. `repo.head.commit` gets the current commit, `repo.head.reference` shows what HEAD points to, and `repo.active_branch` shows the current branch.

---

### 15. Repository Information (Lines 182-183)

**Source Code:**
```python
182  # LINE 182: Show repo information
183  print_section("15. Repository Information")
184  print(f"Repository path: {repo.working_dir}")
185  print(f"Git directory: {repo.git_dir}")
186  print(f"Is bare repository: {repo.bare}")
187  print(f"Total commits: {sum(1 for _ in repo.iter_commits())}")
188  print(f"Total branches: {len(repo.heads)}")
189  print(f"Total tags: {len(repo.tags)}")
```

**Output:**
```
======================================================================
  15. Repository Information
======================================================================

Repository path: /tmp/gitpython_demo_r_5ek7dh
Git directory: /tmp/gitpython_demo_r_5ek7dh/.git
Is bare repository: False
Total commits: 2
Total branches: 2
Total tags: 1
```

**Explanation:** Lines 184-189 demonstrate accessing repository metadata like working directory, git directory, bare status, and counting various git objects.

---

### 16. Direct Git Commands (Lines 191-190)

**Source Code:**
```python
191  # LINE 191: Direct git command execution
192  print_section("16. Direct Git Commands via repo.git")
193  print("GitPython also allows direct git command execution:")
194  git_status = repo.git.status()
195  print("Output of repo.git.status():")
196  print(git_status)
```

**Output:**
```
======================================================================
  16. Direct Git Commands via repo.git
======================================================================

GitPython also allows direct git command execution:
Output of repo.git.status():
On branch master
nothing to commit, working tree clean
```

**Explanation:** Line 194 demonstrates that GitPython allows direct execution of any git command via `repo.git.<command>()`. This returns the raw command output as a string, useful when you need git's exact output format.

---

## Summary

This example demonstrates GitPython's comprehensive support for git operations:

✓ **Repository initialization** (`git init`)
✓ **Configuration** (`git config`)
✓ **Staging changes** (`git add`)
✓ **Repository status** (`git status`)
✓ **Creating commits** (`git commit`)
✓ **Branch operations** (`git branch`, `git checkout`)
✓ **Viewing history** (`git log`)
✓ **Showing differences** (`git diff`)
✓ **Merging branches** (`git merge`)
✓ **Creating tags** (`git tag`)
✓ **Remote operations** (`git remote`)
✓ **File annotations** (`git blame`)
✓ **HEAD and references**
✓ **Direct git command execution**

## Key Takeaways

1. **Object-Oriented Interface**: GitPython provides Python objects (Repo, Commit, Branch, etc.) that represent git concepts
2. **Multiple Approaches**: You can use high-level Python methods or fall back to direct git commands via `repo.git`
3. **Full Git Coverage**: Nearly all git operations are supported through the library
4. **Type Safety**: All operations return proper Python objects with attributes and methods

## References

- [GitPython Documentation](https://gitpython.readthedocs.io/)
- [GitPython GitHub Repository](https://github.com/gitpython-developers/GitPython)
