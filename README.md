# Polyglot File Merger

An internal web application using Flask to merge three files (exe, png, rar/zip) into a single file that is browsed in binary order: EXE -> PNG -> RAR.

## Requirements

- Python 3.x

- pip

## Installation

1. Clone or download this source code.

2. Navigate to the project directory.

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

```bash
python app.py
```

The application will run at `http://127.0.0.1:5000`.

## Usage

1. Open your browser and access `http://127.0.0.1:5000`.

2. Select the .exe file, .png file, and .rar or .zip file.

3. Enter the output file name (e.g., `final_output.png`).

4. Click the "Merge Files" button.

5. The merged file will be automatically downloaded.

## Note

- The output file may be blocked by browsers or antivirus software because it contains hidden executable code.

- This application is for educational and internal testing purposes only.

## Folder Structure

```

├── app.py

├── requirements.txt

├── README.md

└── templates

└── index.html
```

## License

Este proyecto está bajo la Licencia MIT.




FOR EDUCATIONAL PURPOSE ONLY.
