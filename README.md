# Command-Line To-Do List (Python)

A small terminal app to track daily tasks, written in pure Python with no
external libraries. Tasks are saved in a JSON file so nothing is lost when
you close the terminal.

## Usage

```bash
python todo.py add "Study for the ML exam"
python todo.py list
python todo.py done 2
python todo.py remove 1
```

Example:

```
1. [ ] Study for the ML exam
2. [x] Finish the C++ lab task
3. [ ] Read 10 pages
```

## Concepts used in this project

- Command-line arguments with `sys.argv`
- Reading and writing JSON files
- Basic CRUD operations (create, read, update, delete)

## Notes

A learning example prepared for me by my AI assistant to study and extend as
I learn Python at the Faculty of Computers and Artificial Intelligence, Minya
University.
