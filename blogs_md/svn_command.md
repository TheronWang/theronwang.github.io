# SVN Command
---
date: 02/17/2024
---

[TOC]

## SVN Introduction

SVN, short for Subversion, is a version control system. Like CVS, SVN is a cross-platform software that supports most common operating systems. As an open-source version control system, Subversion manages data that changes over time. This data is stored in a central repository, which is similar to a standard file server, except that it remembers every change made to the files. This allows you to revert files back to older versions or browse the history of changes. Subversion is a versatile system that can manage any type of file, including program source code.

## SVN Installation

Install in Linux Server

## SVN Commands

### Checkout Files to Local

```bash
svn checkout [svn_path] [local_path]
// For example:
svn checkout svn://192.168.1.131/45dian/brand ./brand/
// Abbrivation
svn co
```

### Display file or directory status

```bash
svn status PATH
// normal status will display nothing
// ? not in the svn control
// M content is modified
// C conflict
// A intent to be added into repository
// K locked
svn status -v PATH
svn status
svn status -v
svn st
```

### Update Version

Before modifying any files, you must first update the repository, then modify the files, and finally commit them. If you are prompted that the submission is outdated at the time of committing, it is due to a conflict. You need to first update, modify the files, then clear the conflict with svn resolved, and lastly commit again.

```bash
svn update -r m PATH
// Update to the latest version
svn updata
// Recover to version 200
svn -r 200 main.py
// Update a specific file to latest version
svn update main.py
```

### Add files

```bash
svn add [file]
// Add all files of a type in current directory
svn add *.tex
// Add a directory
svn add static
```

### Delete files

```bash
svn delete PATH -m "commentary"
// For example:
svn delete test.php
svn ci -m 'commit deleting files'
// Abbrevation
svn del,remove,rm
```

### Commit changes to repository

```bash
svn commit -m "commentary" [--no-unlock] PATH
// For example, add file, add directory:
svn ci -m "add new file" output.log
svn ci -m "add new directory" static
```

### Lock & Unlock

```bash
svn lock -m "commentary" [--force] PATH
// For example:
svn lock -m "lock file" config.yaml
// Unlock file:
svn unlock PATH
```

### Check log
```bash
svn log PATH
// display the changes history and the version number
// For example:
svn log
svn log main.py
```

### Check details about files

```bash
svn info PATH
svn info
svn info main.py
```

### Compare local files and directory files

```bash
svn diff PATH
svn diff main.py
// Compare between versions
svn diff -r m:n PATH
svn diff -r 200:201 main.py
```

### Merge into current files

```bash
svn merge -r m:n PATH
svn merge -r 200:201 main.py
// Normally, it will produce a conflict which we need to resolve
```

### Other Commands

```bash
svn help
svn help ci
svn mkdir PATH
mkdir work
svn add work -m "add a new folder"
svn switch [PATH]
svn switch -relocate FROM TO [PATH..]
```