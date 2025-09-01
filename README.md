This is a Python-based GUI application built with Tkinter that helps users find job opportunities matching their skills, experience, location, and salary preferences. The system compares user inputs with predefined job profiles and displays suitable matches in a clean, interactive interface.

🚀 Features

User-friendly Tkinter GUI with modern fonts and background image.

Input form for:

Skills (comma-separated)

Years of experience

Preferred location

Preferred salary range

Job matching algorithm that checks:

Skills (at least 50% match)

Experience requirement

Location match

Salary range match

Results displayed in a new window with:

Job title

Company name

Location

Salary range

Description

Job type

Qualifications

Alerts the user if no matching jobs are found.

🛠️ Tech Stack

Python 3.x

Tkinter (for GUI)

Pillow (PIL) (for background image support)

📂 Project Structure
Project/
│── Project job profile matching1.py   # Main Python script
│── bg man.jpg                         # Background image (update path in code)
│── README.md                          # Documentation

▶️ How to Run

Install dependencies:

pip install pillow


Update the background image path inside the script:

background_image = Image.open("C:\\Users\\YourPath\\bg man.jpg")


Run the application:

python Project\ job\ profile\ matching1.py
