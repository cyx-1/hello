#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "gitpython>=3.1.40",
# ]
# ///
"""
GitPython Library Illustration

This script demonstrates how GitPython library supports common git commands.
It creates a temporary repository and showcases various git operations.
"""

import shutil
import tempfile
from pathlib import Path

import git


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def main() -> None:
    """Demonstrate common git commands using GitPython."""

    # Create a temporary directory for our demo repository
    temp_dir = tempfile.mkdtemp(prefix="gitpython_demo_")
    print(f"Working in temporary directory: {temp_dir}")

    try:
        # LINE 35: Initialize a new repository
        print_section("1. git init - Initialize Repository")
        repo = git.Repo.init(temp_dir)
        print(f"Initialized empty Git repository in {repo.git_dir}")

        # LINE 40: Configure user
        print_section("2. git config - Configure User")
        with repo.config_writer() as config:
            config.set_value("user", "name", "Demo User")
            config.set_value("user", "email", "demo@example.com")
        print("Configuration set:")
        print(f"  user.name = {repo.config_reader().get_value('user', 'name')}")
        print(f"  user.email = {repo.config_reader().get_value('user', 'email')}")

        # LINE 50: Create and add a file (git add)
        print_section("3. git add - Stage Changes")
        file_path = Path(temp_dir) / "README.md"
        file_path.write_text("# GitPython Demo\n\nThis is a demo repository.\n")
        print(f"Created file: {file_path.name}")

        repo.index.add(["README.md"])
        print("Staged file: README.md")

        # LINE 60: Check status
        print_section("4. git status - Check Repository Status")
        # Check for staged files (before first commit, we check index entries)
        staged_files = [item[0] for item in repo.index.entries.keys()]
        untracked_files = repo.untracked_files
        print(f"Staged files: {staged_files}")
        print(f"Untracked files: {untracked_files if untracked_files else 'none'}")

        # LINE 67: Make first commit (git commit)
        print_section("5. git commit - Create Commit")
        commit1 = repo.index.commit("Initial commit")
        print(f"Commit created: {commit1.hexsha[:8]}")
        print(f"  Author: {commit1.author.name} <{commit1.author.email}>")
        print(f"  Message: {commit1.message.strip()}")
        print(f"  Date: {commit1.committed_datetime}")

        # LINE 76: Create a new branch (git branch & git checkout)
        print_section("6. git branch & git checkout - Branch Operations")
        new_branch = repo.create_head("feature/demo")
        print(f"Created branch: {new_branch.name}")

        new_branch.checkout()
        print(f"Checked out branch: {repo.active_branch.name}")

        # LINE 85: List all branches (git branch -a)
        print("\nAll branches:")
        for branch in repo.heads:
            marker = "*" if branch == repo.active_branch else " "
            print(f"  {marker} {branch.name}")

        # LINE 91: Make changes and commit on feature branch
        print_section("7. Modify File and Commit")
        file_path.write_text("# GitPython Demo\n\nThis is a demo repository.\n\n## Feature\nAdded new feature.\n")
        print(f"Modified file: {file_path.name}")

        repo.index.add(["README.md"])
        commit2 = repo.index.commit("Add feature section")
        print(f"Commit created: {commit2.hexsha[:8]}")
        print(f"  Message: {commit2.message.strip()}")

        # LINE 102: Show commit log (git log)
        print_section("8. git log - View Commit History")
        for i, commit in enumerate(repo.iter_commits(), 1):
            print(f"Commit {i}:")
            print(f"  SHA: {commit.hexsha[:8]}")
            print(f"  Author: {commit.author.name}")
            print(f"  Date: {commit.committed_datetime}")
            print(f"  Message: {commit.message.strip()}")
            print()

        # LINE 113: Show diff (git diff)
        print_section("9. git diff - Show Differences")
        master_branch = repo.heads.master
        diff = master_branch.commit.diff(commit2)
        print(f"Differences between {master_branch.name} and {repo.active_branch.name}:")
        for diff_item in diff:
            print(f"  Changed file: {diff_item.a_path}")
            if diff_item.diff:
                print(f"  Diff preview: {diff_item.diff.decode('utf-8')[:200]}...")

        # LINE 123: Checkout master and merge (git checkout & git merge)
        print_section("10. git merge - Merge Branches")
        master_branch.checkout()
        print(f"Checked out branch: {repo.active_branch.name}")

        base = repo.merge_base(master_branch, new_branch)
        print(f"Merge base: {base[0].hexsha[:8]}")

        # Perform merge using git command interface
        # This is a fast-forward merge since feature branch is ahead
        repo.git.merge(new_branch.name)
        print(f"Merged {new_branch.name} into {master_branch.name}")
        print(f"New HEAD: {repo.head.commit.hexsha[:8]}")

        # LINE 139: Create a tag (git tag)
        print_section("11. git tag - Create Tags")
        tag = repo.create_tag("v1.0.0", message="Version 1.0.0 release")
        print(f"Created tag: {tag.name}")
        if tag.tag:
            print(f"  Message: {tag.tag.message}")
        print(f"  Commit: {tag.commit.hexsha[:8]}")

        # LINE 148: List tags (git tag -l)
        print("\nAll tags:")
        for t in repo.tags:
            print(f"  {t.name} -> {t.commit.hexsha[:8]}")

        # LINE 153: Show remote operations (git remote)
        print_section("12. git remote - Remote Operations")
        print("Current remotes:")
        if repo.remotes:
            for remote in repo.remotes:
                print(f"  {remote.name}: {remote.url}")
        else:
            print("  No remotes configured")

        # Example of how to add a remote (commented out as it's just for demonstration)
        print("\nTo add a remote, you would use:")
        print("  repo.create_remote('origin', 'https://github.com/user/repo.git')")

        # LINE 167: Show git blame equivalent
        print_section("13. git blame - Show File Annotations")
        blame = repo.blame("HEAD", "README.md")
        print("File annotations (last 5 lines):")
        for commit, lines in blame[-5:]:
            for line in lines:
                print(f"  {commit.hexsha[:8]} ({commit.author.name}): {line.strip()}")

        # LINE 176: Show stash-like operations
        print_section("14. Working with HEAD and References")
        print(f"HEAD commit: {repo.head.commit.hexsha[:8]}")
        print(f"HEAD reference: {repo.head.reference}")
        print(f"Active branch: {repo.active_branch.name}")

        # LINE 182: Show repo information
        print_section("15. Repository Information")
        print(f"Repository path: {repo.working_dir}")
        print(f"Git directory: {repo.git_dir}")
        print(f"Is bare repository: {repo.bare}")
        print(f"Total commits: {sum(1 for _ in repo.iter_commits())}")
        print(f"Total branches: {len(repo.heads)}")
        print(f"Total tags: {len(repo.tags)}")

        # LINE 191: Direct git command execution
        print_section("16. Direct Git Commands via repo.git")
        print("GitPython also allows direct git command execution:")
        git_status = repo.git.status()
        print("Output of repo.git.status():")
        print(git_status)

        print_section("Summary")
        print("This demonstration covered:")
        print("  ✓ Repository initialization (git init)")
        print("  ✓ Configuration (git config)")
        print("  ✓ Staging changes (git add)")
        print("  ✓ Repository status (git status)")
        print("  ✓ Creating commits (git commit)")
        print("  ✓ Branch operations (git branch, git checkout)")
        print("  ✓ Viewing history (git log)")
        print("  ✓ Showing differences (git diff)")
        print("  ✓ Merging branches (git merge)")
        print("  ✓ Creating tags (git tag)")
        print("  ✓ Remote operations (git remote)")
        print("  ✓ File annotations (git blame)")
        print("  ✓ HEAD and references")
        print("  ✓ Direct git command execution")

    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)
        print(f"\nCleaned up temporary directory: {temp_dir}")


if __name__ == "__main__":
    main()
