import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

from main import process_images

app = ctk.CTk()
app.title("AI Auto Mosaic")
app.geometry("900x500")
app.minsize(700, 350)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def select_input_folder():
    folder = filedialog.askdirectory()

    if folder:
        input_entry.delete(0, "end")
        input_entry.insert(0, folder)



        
def select_output_folder():
    folder = filedialog.askdirectory()

    if folder:
        output_entry.delete(0, "end")
        output_entry.insert(0, folder)
        



def start_process():
    input_dir = Path(input_entry.get())
    output_dir = Path(output_entry.get())
    output_dir.mkdir(parents=True, exist_ok=True)
    blur_size = int(blur_slider.get()) * 2 + 1
    confidence = confidence_slider.get()
    if not input_dir.exists():
        print("入力フォルダが存在しません")
        return

    process_images(
        input_dir,
        output_dir,
        blur_size,
        confidence)

start_button = ctk.CTkButton(
    app,
    text="Start",
    command=start_process,
    
)


# input
input_label = ctk.CTkLabel(app, text="Input Folder")
input_label.grid(row=0, column=0, sticky="w", padx=10, pady=(20, 5))

input_frame = ctk.CTkFrame(app)
input_frame.grid(
    row=1,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)

input_entry = ctk.CTkEntry(input_frame)
input_entry.grid(
    row=0,
    column=0,
    padx=10,
    pady=5,
    sticky="ew"
)

input_button = ctk.CTkButton(
    input_frame,
    text="Browse",
    command=select_input_folder
)
input_button.grid(
    row=0,
    column=1,
    padx=10
)

# output
output_label = ctk.CTkLabel(app, text="Output Folder")
output_label.grid(
    row=2,
    column=0,
    padx=10,
    pady=(20, 5),
    sticky="w"
)

output_frame = ctk.CTkFrame(app)
output_frame.grid(
    row=3,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)


output_entry = ctk.CTkEntry(output_frame)
output_entry.grid(
    row=0,
    column=0,
    padx=10,
    pady=5,
    sticky="ew")

output_button = ctk.CTkButton(
    output_frame,
    text="Browse",
    command=select_output_folder
)
output_button.grid(row=0, column=1, padx=10)

# blur

def update_blur(value):
    blur_size = int(value) * 2 + 1
    blur_value_label.configure(text=f"Blur Size : {blur_size}")

blur_frame = ctk.CTkFrame(app)
blur_frame.grid(
    row=5,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)
min_label = ctk.CTkLabel(blur_frame, text="1")
max_label = ctk.CTkLabel(blur_frame, text="101")

min_label.grid(row=2, column=0, sticky="w",padx=10)

max_label.grid(row=2, column=1, sticky="e",padx=10)

blur_slider = ctk.CTkSlider(
    blur_frame,
    from_=0,
    to=50,
    command=update_blur
)

blur_slider.grid(
    row=1,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)


blur_value_label = ctk.CTkLabel(
    app,
    text="Blur Size : 31"
)
blur_slider.set(15)
update_blur(15)
blur_value_label.grid(
    row=4,
    column=0,
    padx=10,
    pady=(20, 5),
    sticky="w"
)

# confidence
def update_confidence(value):
    confidence_value_label.configure(
        text=f"Confidence : {value:.2f}"
    )

    
confidence_frame = ctk.CTkFrame(app)
confidence_frame.grid(
    row=7,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)
min_label = ctk.CTkLabel(confidence_frame, text="0.10")
max_label = ctk.CTkLabel(confidence_frame, text="0.90")

min_label.grid(row=2, column=0, sticky="w",padx=10)

max_label.grid(row=2, column=1, sticky="e",padx=10)

confidence_slider = ctk.CTkSlider(
    confidence_frame,
    from_=0.10,
    to=0.90,
    number_of_steps=80,   # 0.01刻み
    command=update_confidence
)

confidence_slider.grid(
    row=1,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)


confidence_value_label = ctk.CTkLabel(
    app,
    text="Confidence : 0.50"
)
confidence_slider.set(0.50)
update_confidence(0.50)
confidence_value_label.grid(
    row=6,
    column=0,
    padx=10,
    pady=(20, 5),
    sticky="w"
)

# start
start_button.grid(
    row=10,
    column=0,
    columnspan=2,
    padx=10,
    pady=10,
    sticky="ew"
)
input_frame.grid_columnconfigure(0, weight=1)
output_frame.grid_columnconfigure(0, weight=1)
blur_frame.grid_columnconfigure(0, weight=1)
confidence_frame.grid_columnconfigure(0, weight=1)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

app.mainloop()