import tkinter as tk
from tkinter import filedialog, messagebox
import re
from difflib import SequenceMatcher

# ---------------- LOGIC ---------------- #

def preprocess(code):
    code = re.sub(r'#.*', '', code)
    code = re.sub(r"'''[\s\S]*?'''", '', code)
    code = re.sub(r'"""[\s\S]*?"""', '', code)
    code = re.sub(r'\s+', ' ', code).strip()
    return code

def similarity(a, b):
    return round(SequenceMatcher(None, a, b).ratio() * 100, 2)

def common_lines(c1, c2):
    l1 = set([line.strip() for line in c1.split('\n') if line.strip()])
    l2 = set([line.strip() for line in c2.split('\n') if line.strip()])
    return list(l1.intersection(l2))

def browse(entry):
    path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    entry.delete(0, tk.END)
    entry.insert(0, path)

def check():
    p1 = entry1.get()
    p2 = entry2.get()

    if not p1 or not p2:
        messagebox.showerror("Error", "Please select both Python files")
        return

    try:
        with open(p1, 'r', encoding='utf-8') as f:
            c1 = f.read()
        with open(p2, 'r', encoding='utf-8') as f:
            c2 = f.read()
    except:
        messagebox.showerror("Error", "File reading error")
        return

    clean1 = preprocess(c1)
    clean2 = preprocess(c2)

    score = similarity(clean1, clean2)
    common = common_lines(c1, c2)

    result.delete(1.0, tk.END)

    result.insert(tk.END, f"Similarity Score: {score}%\n\n", "score")
    result.insert(tk.END, "Common Lines:\n\n", "heading")

    for line in common:
        result.insert(tk.END, "• " + line + "\n", "line")

# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Python Plagiarism Detector")
root.geometry("750x550")
root.configure(bg="#0f172a")  # dark navy

# Title
title = tk.Label(root, text="🐍 Python Plagiarism Detector",
                 font=("Segoe UI", 20, "bold"),
                 bg="#0f172a", fg="#38bdf8")
title.pack(pady=20)

# Card Frame
card = tk.Frame(root, bg="#1e293b", bd=0)
card.pack(pady=10, padx=20, fill="x")

# File 1
entry1 = tk.Entry(card, width=50, font=("Segoe UI", 10))
entry1.grid(row=0, column=0, padx=10, pady=10)

btn1 = tk.Button(card, text="Browse",
                 bg="#38bdf8", fg="black",
                 font=("Segoe UI", 9, "bold"),
                 command=lambda: browse(entry1))
btn1.grid(row=0, column=1, padx=5)

# File 2
entry2 = tk.Entry(card, width=50, font=("Segoe UI", 10))
entry2.grid(row=1, column=0, padx=10, pady=10)

btn2 = tk.Button(card, text="Browse",
                 bg="#38bdf8", fg="black",
                 font=("Segoe UI", 9, "bold"),
                 command=lambda: browse(entry2))
btn2.grid(row=1, column=1, padx=5)

# Check Button
check_btn = tk.Button(root, text="Check Similarity",
                      font=("Segoe UI", 12, "bold"),
                      bg="#22c55e", fg="black",
                      padx=10, pady=5,
                      command=check)
check_btn.pack(pady=15)

# Result Frame (Card style)
result_frame = tk.Frame(root, bg="#1e293b")
result_frame.pack(padx=20, pady=10, fill="both", expand=True)

scroll = tk.Scrollbar(result_frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

result = tk.Text(result_frame,
                 bg="#020617", fg="white",
                 font=("Consolas", 10),
                 yscrollcommand=scroll.set)
result.pack(fill="both", expand=True)

scroll.config(command=result.yview)

# Styling
result.tag_config("score", foreground="#22c55e", font=("Segoe UI", 12, "bold"))
result.tag_config("heading", foreground="#facc15", font=("Segoe UI", 11, "bold"))
result.tag_config("line", foreground="#e2e8f0")

# Run
root.mainloop()
