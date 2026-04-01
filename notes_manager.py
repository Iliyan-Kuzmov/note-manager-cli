import os

NOTES_FILE = "notes.txt"
SEPARATOR = " | "

def load_data():
    if not os.path.exists(NOTES_FILE):
        return {"next_id": 1, "notes": []}
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        return {"next_id": 1, "notes": []}

    try:
        next_id = int(lines[0].strip())
    except ValueError:
        next_id = 1

    notes = []
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split(SEPARATOR)
        if len(parts) >= 3:
            content = SEPARATOR.join(parts[2:])
            notes.append({
                "id": int(parts[0]),
                "title": parts[1],
                "content": content,
            }
            )
    return {"next_id": next_id, "notes": notes}

def save_data(data):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        f.write(f"{data['next_id']}\n")

        for note in data["notes"]:
            clean_title = str(note["title"].replace(SEPARATOR, " "))
            clean_content = str(note["content"].replace(SEPARATOR, " "))

            f.write(f"{note['id']}{SEPARATOR}{clean_title}{SEPARATOR}{clean_content}\n")

def load_notes():
    data = load_data()
    return data["notes"]

def save_notes(notes):
    data = load_data()
    data["notes"] = notes
    save_data(data)

def add_note(title, content):
    data = load_data()
    new_note = {
        "id": data["next_id"],
        "title": title,
        "content": content,
    }

    data["notes"].append(new_note)
    data["next_id"] += 1
    save_data(data)
    return new_note

def list_notes():
    data = load_data()
    return data["notes"]

def get_note_by_id(note_id):
    data = load_data()
    for note in data["notes"]:
        if note["id"] == note_id:
            return note
    return None

def delete_note(note_id):
    data = load_data()
    notes_list = data["notes"]
    original_count = len(notes_list)

    data["notes"] = [note for note in notes_list if note['id'] != note_id]
    if len(data["notes"]) == original_count:
        return False
    save_data(data)
    return True


