# Note Manager CLI
A command line note-taking app. Notes are saved locally in a .txt file - no internet reuqired.
## How to install and run
1. Clone or download this repository
2. Open a terminal and go into the project folder
```bash
cd note manager
```
3. You are ready. Run the command
```bash
python notes.py --help
```
## Supported Commands
Add a note
```bash
python notes.py add "Meeting with client" "Discuss Q3  budget"
```
List all notes
```bash
python notes.py list
```
Show a specific note
```bash
python notes.py show <id>
```
Example
```bash
python notes.py show 3
```
Delete a note
```bash
python notes.py delete <id>
```
Example
```bash
python notes.py delete 3
```
Show help
```bash
python notes.py --help
```
Running the tests
```bash
python test_notes.py