# EnTrFlashCard

This repository contains a simple flashcard application developed using Python. It utilizes the `tkinter` library for the graphical user interface and `pandas` for handling CSV data. The project is aimed at helping users learn English-Turkish vocabulary efficiently.

## Features

- **Flashcard-Based Learning:** Display English words and view their Turkish translations by flipping the cards.
- **Randomized Cards:** Words are shown in random order to enhance memorization.
- **Progress Tracking:** Users can mark words as learned, dynamically updating the dataset.
- **Easy Data Management:** Supports importing and exporting the vocabulary list in CSV format.

## File Structure

```
EnTrFlashCard/
├── data/
│   └── words.csv        # Default CSV file containing English-Turkish word pairs
├── images/
│   ├── card_front.png   # Front side of the flashcard
│   └── card_back.png    # Back side of the flashcard
├── main.py              # Main application script
├── README.md            # Project documentation
└── requirements.txt     # Dependencies list
```

## Requirements

- Python 3.7 or higher
- Libraries: `pandas`

Install the required library using:

```bash
pip install -r requirements.txt
```

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/trkbey/EnTrFlashCard.git
   cd EnTrFlashCard
   ```

2. Ensure the `data/words.csv` file is present. The file should have two columns:

   ```csv
   English,Turkish
   apple,elma
   car,araba
   ...
   ```

3. Run the application:

   ```bash
   python main.py
   ```

4. Use the interface to:
   - View English words.
   - Flip cards to reveal the Turkish meaning.
   - Mark cards as learned.

## Example CSV File

```csv
English,Turkish
hello,merhaba
world,dünya
book,kitap
```

## Screenshots

![image](https://github.com/user-attachments/assets/5924a802-89d7-43dd-b0fb-0851a5fa742f)

![image](https://github.com/user-attachments/assets/9694abae-6c9e-4579-be5d-8fc99c975077)

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements.
