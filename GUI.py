import customtkinter
import tkinter as tk
from recommendation_system import get_recommendations, indices

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("600x400")
app.title("Movie Recommendation System")

# Function to handle button click event
def button_click_event():
    title = entry.get()
    if title not in indices:
        result_text.set("Movie not found!")
        return
    recommendations = get_recommendations(title)
    result_text.set("\n".join(recommendations))

# Create the main frame
main_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title 
title_label = customtkinter.CTkLabel(main_frame, text="Movie Recommendation System", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

entry_frame = customtkinter.CTkFrame(main_frame)
entry_frame.pack(pady=10, fill="x")

entry_label = customtkinter.CTkLabel(entry_frame, text="Enter movie title:", font=("Helvetica", 12))
entry_label.pack(side="left", padx=5, pady=5)

entry = customtkinter.CTkEntry(entry_frame, placeholder_text="Type movie title here", width=300)
entry.pack(side="left", padx=5, pady=5)

# Button to trigger recommendation
button = customtkinter.CTkButton(main_frame, text="Get Recommendations", command=button_click_event)
button.pack(pady=10)

# Text widget to display recommendations
result_frame = customtkinter.CTkFrame(main_frame)
result_frame.pack(pady=10, fill="both", expand=True)

result_text = tk.StringVar()

result_label = customtkinter.CTkLabel(result_frame, textvariable=result_text, wraplength=500, font=("Helvetica", 12))
result_label.pack(fill="both", expand=True, padx=10, pady=10)

app.mainloop()
