import pandas as pd
import tkinter as tk
from tkinter import ttk
import webbrowser  # Required for opening URLs

# Load the book dataset (replace with your dataset)
books = pd.read_csv('books.csv')

# Create a tkinter app
app = tk.Tk()
app.title("Book Recommendation System")

# Function to open a URL in the default web browser
def open_url(event):
    widget = event.widget
    index = widget.index(tk.CURRENT)
    line, char = map(int, index.split("."))
    book_info = clickable_books[line - 1]
    webbrowser.open_new(book_info['URL'])

# Function to make book titles clickable with a hand cursor
def make_clickable(event):
    widget = event.widget
    index = widget.index(tk.CURRENT)
    widget.config(cursor="hand2")  # Change cursor to hand when hovering
    widget.tag_configure("hyperlink", foreground="blue", underline=True)
    widget.tag_bind("hyperlink", "<Button-1>", open_url)

# Function to recommend books based on the selected genre
def recommend_books():
    selected_genre = genre_var.get()
    if selected_genre:
        genre_books = books[books['Genre'] == selected_genre]
        if not genre_books.empty:
            recommendation_text.delete(1.0, tk.END)  # Clear previous recommendations
            global clickable_books
            clickable_books = genre_books.nlargest(5, 'Rating')[['BookTitle', 'URL']].to_dict(orient='records')
            for index, book_info in enumerate(clickable_books, start=1):
                recommendation_text.insert(tk.END, f"{index}. {book_info['BookTitle']}\n", "hyperlink")
            recommendation_text.bind("<Enter>", make_clickable)
        else:
            recommendation_text.delete(1.0, tk.END)  # Clear previous recommendations
            recommendation_text.insert(tk.END, f"No books found in the {selected_genre} genre.")
    else:
        recommendation_text.delete(1.0, tk.END)  # Clear previous recommendations
        recommendation_text.insert(tk.END, "Please select a genre")

# Customize the design
app.geometry("400x400")  # Adjust the window size

# Label and dropdown for genre selection
genre_label = tk.Label(app, text="Select a genre:", font=("Time New Roman", 14))
genre_label.pack(pady=10)  # Add padding

genre_var = tk.StringVar()
genre_dropdown = ttk.Combobox(app, textvariable=genre_var, values=books['Genre'].unique().tolist(), font=("Time New Roman", 12))
genre_dropdown.pack()

# Button to recommend books
recommend_button = tk.Button(app, text="Recommend Books", command=recommend_books, font=("Time New Roman", 12), bg="#1e2120", fg="white")
recommend_button.pack(pady=10)

# Text widget for displaying recommendations (with clickable book titles)
recommendation_text = tk.Text(app, wrap=tk.WORD, font=("Time New Roman", 12), height=8, width=40)
recommendation_text.pack()

app.mainloop()
