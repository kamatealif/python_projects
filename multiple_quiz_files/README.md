# multiple_quiz_files

Simple quiz runner that reads quiz data from `data.json` and runs quizzes via `main.py`.

## Project structure
- `main.py` — entrypoint to run the quiz application.
- `data.json` — quiz data (questions, choices, answers).

## Requirements
- Python 3.8+

## Installation
1. Clone the repository or download the files.
2. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install any dependencies (if present). This project has no external requirements by default.

## Usage

Run the quiz application with:

```bash
python3 main.py
```

The program reads `data.json` in the project root. Example `data.json` item format:

```json
[
	{
		"question": "What is 2 + 2?",
		"choices": ["3", "4", "5"],
		"answer": 1
	}
]
```

- `question`: string question text
- `choices`: array of choice strings
- `answer`: zero-based index of the correct choice

## Contributing
## Skills Showcased

- **File handling:** demonstrates reading `data.json`, parsing JSON, and writing results or logs, showcasing basic file I/O operations in Python.
- **Data validation & CLI I/O:** shows simple input/output handling and validation when running the quiz via `main.py`.

Contributions are welcome — open an issue or submit a pull request.

## License
MIT
