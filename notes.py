import sys
import notes_manager

def cmd_add(args):
    if len(args) < 2:
        print("Error: 'add' needs a title and content")
        return

    title = args[0]
    content = args[1]
    note = notes_manager.add_note(title, content)
    print(f"Note added with id {note['id']}: {note['title']}")

def cmd_list():
    notes = notes_manager.list_notes()
    if len(notes) == 0:
        print("No notes")
        return

    print(f"You have {len(notes)} notes\n")
    for note in notes:
        print(f"    [{note['id']}] {note['title']}")
    print()


def cmd_show(args):
    if len(args) < 1:
        print("Error: 'show' needs an id")
        return

    try:
        note_id = int(args[0])
    except ValueError:
        print(f"Error: '{args[0]}' is not a valid id")
        return

    note = notes_manager.get_note_by_id(note_id)
    if note is None:
        print(f"Note with id {note_id} not found")
        return

    print(f"\n   Note #{note['id']}   ")
    print(f"Title:   {note['title']}")
    print(f"Content: {note['content']}")
    print()

def cmd_delete(args):
    if len(args) < 1:
        print("Error: 'delete' needs an id")
        return

    try:
        note_id = int(args[0])
    except ValueError:
        print(f"Error: '{args[0]}' is not a valid id")
        return

    deleted = notes_manager.delete_note(note_id)

    if deleted:
        print(f"Note with id {note_id} was deleted")
    else:
        print(f"Note with id {note_id} was not found")

def print_help():
    print("How to use the program:")
    print(" python notes.py add <title> <content> - add a new note")
    print(" python notes.py list - list all notes")
    print(" python notes.py show <id> - show note with given id")
    print(" python notes.py delete <id> - delete note with given id")

def main():
    args = sys.argv[1:]
    if len(args) == 0 or args[0] == '--help':
        print_help()
        return

    command = args[0]
    rest = args[1:]

    if command == 'add':
        cmd_add(rest)
    elif command == 'list':
        cmd_list()
    elif command == 'show':
        cmd_show(rest)
    elif command == 'delete':
        cmd_delete(rest)
    else:
        print(f"Unknown command: {command}")
        print("Run 'python notes.py --help' to see available commands")

if __name__ == "__main__":
    main()