# Tarot Data Sanitizer

Tarot Data Sanitizer is a Python-based GUI application designed to sanitize sensitive data in files such as CSV, Excel, and JSON. The script replaces names, emails, phone numbers, and social security numbers with tarot card names and basic ASCII symbols, making it a fun and secure way to anonymize data.

## Features

- **Name Sanitization**: Replaces names like "John Doe" with tarot card names, e.g., "Strength Justice".
- **Email Sanitization**: Converts email addresses like "john.doe@example.com" into something like "Hierophant@TheMoon.com".
- **Phone Number Sanitization**: Replaces phone numbers like "18004444444" with symbols like "######^^^^".
- **SSN Sanitization**: Converts Social Security Numbers like "123-12-1234" into symbols like "###-++-^^^^".
## Installation

To run the Tarot Data Sanitizer, follow these steps:

### Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Pandas**: The script uses the Pandas library for data manipulation. Install it using pip if you don't have it already:

  ```bash
  pip install pandas
  ```

### Running the Script
1. Download the script: Save the 'tarot-sani.py' script to your local machine
2. Run the script: Open a terminal or command prompt, navigate to the directory where the script is saved, and run
   ```bash
   python tarot-sani.py
   ```
3. Using the GUI:
- Input File: Click the "Browse" button next to "Input File" to select the file you want to sanitize (CSV, Excel, or JSON).
- Output File: Click the "Browse" button next to "Output File" to specify where the sanitized file should be saved.
- Run Sanitizer: Click "Run Sanitizer" to begin the sanitization process. A success message will appear when the process is complete.

4. Sparkle sparkle
