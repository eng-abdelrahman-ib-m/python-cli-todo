"""Command-line to-do list.

A small terminal app to track tasks. Tasks are stored in a JSON file
so they survive between runs.

Usage:
    python todo.py add "Study for the ML exam"
    python todo.py list
    python todo.py done 2
    python todo.py remove 1
"""

import json
import os
import sys

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def list_tasks(tasks):
    if not tasks:
        print("No tasks. Add one with: python todo.py add \"your task\"")
        return
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")


def main():
    tasks = load_tasks()
    args = sys.argv[1:]

    if not args or args[0] == "list":
        list_tasks(tasks)
    elif args[0] == "add" and len(args) >= 2:
        tasks.append({"title": " ".join(args[1:]), "done": False})
        save_tasks(tasks)
        print(f"Added: {' '.join(args[1:])}")
    elif args[0] == "done" and len(args) == 2 and args[1].isdigit():
        idx = int(args[1]) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print(f"Done: {tasks[idx]['title']}")
        else:
            print("No task with that number.")
    elif args[0] == "remove" and len(args) == 2 and args[1].isdigit():
        idx = int(args[1]) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Removed: {removed['title']}")
        else:
            print("No task with that number.")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
