import os
import notes_manager

TEST_FILE = "notes_test.txt"

def setup():
    notes_manager.NOTES_FILE = TEST_FILE
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def teardown():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_note():
    setup()
    note = notes_manager.add_note("Test Title", "Test content")
    assert note["title"] == "Test Title", "Title should match what we passed in"
    assert note["content"] == "Test content", "Content should match what we passed in"
    assert note["id"] == 1, "First note should get id 1"

    with open(TEST_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) == 2, "There should be exactly 2 lines"
    assert lines[0].strip() == "2", "Counter on line 1 should have advanced to 2"
    assert "1 | Test Title | Test content" in lines[1], "Note data is not formatted correctly"

    teardown()
    print("PASS: test_add_note")

def test_id_keep_increment():
    setup()
    notes_manager.add_note("Note A", "Content A")
    notes_manager.add_note("Note B", "Content B")
    notes_manager.delete_note(2)
    new_note = notes_manager.add_note("Note C", "Content C")

    assert new_note["id"] == 3, f"Expect id 3 but got {new_note["id"]}"

    teardown()
    print("PASS: test_id_keep_increment")

def test_delete_note():
    setup()
    result = notes_manager.delete_note(9999)
    assert result == False, "Deleting a non-existent note should return False"
    teardown()
    print("PASS: test_delete_note")

def test_get_note_not_found():
    setup()
    result = notes_manager.get_note_by_id(100)
    assert result is None, "Should return None when note is found"

    teardown()
    print("PASS: test_get_note_not_found")

if __name__ == "__main__":
    print("Running tests\n")
    test_add_note()
    test_id_keep_increment()
    test_delete_note()
    test_get_note_not_found()
    print("All tests passed")