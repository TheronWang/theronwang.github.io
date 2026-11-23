---
layout: page
title: Home Project Manager
description: An Obsidian plugin that turns plain Markdown notes into a home dashboard and project pages, with an update format coding agents can write to.
img: assets/img/projects/hpm_home.png
importance: 1
category: software
github: https://github.com/TheronWang/home-project-manager
---

[**GitHub repository**](https://github.com/TheronWang/home-project-manager) · [**Latest release**](https://github.com/TheronWang/home-project-manager/releases/latest) · MIT license · Obsidian 1.5.0+

Home Project Manager is an [Obsidian](https://obsidian.md) plugin for keeping track of many projects at once. It builds a home dashboard and a page for each project from ordinary Markdown notes, so there's no database and nothing hidden: uninstall it and every note is still plain, readable Markdown.

It's designed for projects whose progress is spread across meeting notes, TODO lists and work done by coding agents. Session notes carry open tasks forward from one meeting to the next, and agents such as Claude Code or Codex can log their progress into the vault with a small shell script.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/hpm_home.png" title="Home dashboard" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    The home dashboard: every project as a card with its health, due date and recent activity, plus one feed of what happened across the vault.
</div>

## Features

- **Home dashboard:** every project as a card with health, due dates and an 8-week activity sparkline. Projects that have gone quiet are flagged.
- **Project pages:** each project gets Activity, Meetings, Tasks and Notes tabs, plus stats such as open tasks and last activity.
- **Session notes that carry tasks forward:** a new meeting note lists, live, every task checked off since the last meeting and everything still open, so you never retype last week's TODO list.
- **Finished tasks count as activity:** checking off a task shows up in the feed and the charts.
- **Built for coding agents:** updates are small Markdown files in a documented format, so Claude Code, Codex or any script can log progress with the included `log-update.sh`.
- **Archive and restore:** close a project as done or stopped, and its folder moves to your archive without breaking links.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/hpm_project.png" title="Project page" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/hpm_meetings.png" title="Meetings tab" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Left: a project page with its stats and activity timeline, including updates from me, Claude and Codex. Right: the Meetings tab, grouping session notes and reports.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/hpm_session.png" title="Session note" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/hpm_log.png" title="Log dialog" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Left: a session note with live "Done since last time" and "Still open" lists. Right: the Log dialog for a quick update, a session note or a dated note.
</div>

## How it works

A project is a hub note with `type: project` in its frontmatter, in a folder named after the project. Updates are short notes in the project's `Updates/` folder, named `YYYY-MM-DD HHmm - <author>.md`, and session notes are named `YYYY-MM-DD - <Project>.md`. Everything the plugin shows comes from frontmatter and file names, so any of these notes can be written by hand, by the plugin, or by an agent.

## Try it

Install it with [BRAT](https://github.com/TfTHacker/obsidian42-brat) using `TheronWang/home-project-manager`, or download `main.js`, `manifest.json` and `styles.css` from the [latest release](https://github.com/TheronWang/home-project-manager/releases/latest) into `<your vault>/.obsidian/plugins/home-project-manager/`. The repository also includes a sample vault with seven fictional projects, which is the quickest way to see what the plugin does. All screenshots on this page come from that sample vault.
