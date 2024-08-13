import pandas as pd
import re
import random
import tkinter as tk
from tkinter import filedialog, messagebox

# Tarot card names
TAROT_CARDS = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"
]

# Basic ASCII symbols for phone numbers and SSNs
BASIC_SYMBOLS = ['*', '#', '+', '^']

# Patterns for sensitive information
PATTERNS = {
    "email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    "phone": r'\b\d{10}\b|\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b',
    "credit_card": r'\b(?:\d[ -]*?){13,16}\b',
    "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
    "name": r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'  # Pattern for First Last names
}

def mask_with_tarot_pair(match):
    return f"{random.choice(TAROT_CARDS)} {random.choice(TAROT_CARDS)}"

def mask_with_tarot_email(match):
    username = random.choice(TAROT_CARDS)
    domain = random.choice(TAROT_CARDS)
    return f"{username}@{domain}.com"

def mask_with_basic_symbols(match):
    length = len(match.group())
    return ''.join(random.choice(BASIC_SYMBOLS) for _ in range(length))

def mask_ssn(match):
    parts = match.group().split('-')
    return f"{''.join(random.choice(BASIC_SYMBOLS) for _ in parts[0])}-{'*' * len(parts[1])}-" \
           f"{''.join(random.choice(BASIC_SYMBOLS) for _ in parts[2])}"

def sanitize_data(df, patterns):
    for column in df.columns:
        for pattern_name, pattern in patterns.items():
            if pattern_name == "name":
                df[column] = df[column].apply(lambda x: re.sub(pattern, mask_with_tarot_pair, str(x)))
            elif pattern_name == "email":
                df[column] = df[column].apply(lambda x: re.sub(pattern, mask_with_tarot_email, str(x)))
            elif pattern_name == "phone":
                df[column] = df[column].apply(lambda x: re.sub(pattern, mask_with_basic_symbols, str(x)))
            elif pattern_name == "ssn":
                df[column] = df[column].apply(lambda x: re.sub(pattern, mask_ssn, str(x)))
            else:
                df[column] = df[column].apply(lambda x: re.sub(r'\d', mask_with_basic_symbols, str(x)))
    return df

def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format!")

def save_data(df, output_path):
    if output_path.endswith('.csv'):
        df.to_csv(output_path, index=False)
    elif output_path.endswith('.xlsx'):
        df.to_excel(output_path, index=False)
    elif output_path.endswith('.json'):
        df.to_json(output_path, orient='records', lines=True)
    else:
        raise ValueError("Unsupported file format!")

def sanitize_and_save(input_file, output_file):
    try:
        df = load_data(input_file)
        sanitized_df = sanitize_data(df, PATTERNS)
        save_data(sanitized_df, output_file)
        messagebox.showinfo("Success", "Your data has been sanitized!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_input_file():
    file_path = filedialog.askopenfilename(
        title="Choose Your File of Secrets",
        filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("JSON files", "*.json")]
    )
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def browse_output_file():
    file_path = filedialog.asksaveasfilename(
        title="Where Shall the Magic Be Stored?",
        filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("JSON files", "*.json")],
        defaultextension=".csv"
    )
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def run_sanitizer():
    input_file = input_entry.get()
    output_file = output_entry.get()
    if input_file and output_file:
        sanitize_and_save(input_file, output_file)
    else:
        messagebox.showwarning("Warning", "Please choose both input and output files.")

# Create the GUI window
root = tk.Tk()
root.title("Tarot Data Sanitizer")
root.configure(bg="#2b2b52")

# Style configurations
style_config = {
    "font": ("Verdana", 12),
    "bg": "#2b2b52",
    "fg": "#f5f6fa",
    "highlightbackground": "#706fd3",
    "highlightcolor": "#706fd3"
}

input_label = tk.Label(root, text="Choose the File of Secrets:", **style_config)
input_label.grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50, **style_config)
input_entry.grid(row=0, column=1, padx=10, pady=10)
input_button = tk.Button(root, text="Browse", command=browse_input_file, bg="#706fd3", fg="#ffffff", font=("Verdana", 10))
input_button.grid(row=0, column=2, padx=10, pady=10)

output_label = tk.Label(root, text="Choose Where to Store the Magic:", **style_config)
output_label.grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50, **style_config)
output_entry.grid(row=1, column=1, padx=10, pady=10)
output_button = tk.Button(root, text="Browse", command=browse_output_file, bg="#706fd3", fg="#ffffff", font=("Verdana", 10))
output_button.grid(row=1, column=2, padx=10, pady=10)

run_button = tk.Button(root, text="Make Some Magic!", command=run_sanitizer, bg="#34ace0", fg="#ffffff", font=("Verdana", 12, "bold"))
run_button.grid(row=2, column=1, padx=10, pady=20)

# Start the GUI event loop
root.mainloop()
