# Flashcard GUI Application

This project is a simple GUI-based flashcard application developed in Python. It uses the `tkinter` library for creating the graphical user interface and `pandas` for data manipulation. The application is designed to help users learn English-Turkish vocabulary effectively.

## Features

- **Interactive Flashcards:** Displays English words on cards, allowing users to learn Turkish translations by flipping the cards.
- **CSV Integration:** Loads a CSV file containing English-Turkish word pairs.
- **Progress Tracking:** Allows users to mark words as learned, updating the list dynamically.
- **Random Word Display:** Words are shown in random order to enhance learning.
- **User-Friendly Interface:** Easy-to-use design suitable for learners of all levels.

## File Structure

```
project-directory/
├── main.py         # Main Python script
├── words.csv       # CSV file containing English-Turkish word pairs
├── images/         # Folder for storing card images (if applicable)
└── README.md       # Project documentation
```

## Requirements

- Python 3.7 or higher
- Required libraries: `tkinter`, `pandas`

You can install the required library with:

```bash
pip install pandas
```

## How to Use

1. Clone the repository or download the project files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Make sure the `words.csv` file is in the same directory as `main.py`. The file should have the following structure:

   ```csv
   English,Turkish
   hello,merhaba
   world,dünya
   ...
   ```

3. Run the application:

   ```bash
   python main.py
   ```

4. Use the graphical interface to:
   - View a word in English.
   - Flip the card to see the Turkish translation.
   - Mark words as learned.

## Example CSV File

```csv
English,Turkish
apple,elma
banana,muz
car,araba
```

## Screenshot

*(Include a screenshot of your application here to give users a visual overview.)*

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
