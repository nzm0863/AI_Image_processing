import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
import threading

from main import process_images

app = ctk.CTk()
app.title("AI Auto Mosaic")
app.geometry("900x900")
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
    
    input_path = input_entry.get().strip()
    output_path = output_entry.get().strip()

    if not input_path:
        update_log("入力フォルダを指定してください")
        return
    
    input_dir = Path(input_path)
    output_dir = Path(output_path)
    if not input_dir.is_dir():
        update_log("入力先がフォルダではありません")
        return

    if not output_path:
        update_log("出力フォルダを指定してください")
        return
      
    # output_dir.mkdir(parents=True, exist_ok=True)
    progress_frame.grid()
    start_button.grid_remove()
    blur_size = int(blur_slider.get()) * 2 + 1
    confidence = confidence_slider.get()
      
    start_button.configure(
        state="disabled",
        text="Processing..."
    )
    
    thread = threading.Thread(
        target=run_process,
        args=(
            input_dir,
            output_dir,
            blur_size,
            confidence
        ),
        daemon=True
    )

    thread.start()





main_row=0
# input
input_label = ctk.CTkLabel(app, text="Input Folder")
input_label.grid(row=main_row, column=0, sticky="w", padx=10, pady=(20, 5))

main_row+=1
input_frame = ctk.CTkFrame(app)
input_frame.grid(
    row =main_row,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)


input_entry = ctk.CTkEntry(input_frame)
input_entry.grid(
    row =0,
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
    row =0,
    column=1,
    padx=10
)


# output
main_row +=2
output_label = ctk.CTkLabel(app, text="Output Folder")
output_label.grid(
    row =main_row,
    column=0,
    padx=10,
    pady=(20, 5),
    sticky="w"
)

main_row +=1
output_frame = ctk.CTkFrame(app)
output_frame.grid(
    row =main_row,
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

# parts
main_row += 2

target_label = ctk.CTkLabel(app, text="Detection Target")
target_label.grid(
    row=main_row,
    column=0,
    padx=10,
    pady=(20, 5),
    sticky="w"
)

main_row += 1

target_frame = ctk.CTkFrame(app)
target_frame.grid(
    row=main_row,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)

# チェック状態（初期値はON）
face_var = ctk.BooleanVar(value=True)
private_var = ctk.BooleanVar(value=True)

face_checkbox = ctk.CTkCheckBox(
    target_frame,
    text="Face (Photo)",
    variable=face_var
)
face_checkbox.grid(row=0, column=0, padx=10, pady=10, sticky="w")

private_checkbox = ctk.CTkCheckBox(
    target_frame,
    text="Private Parts (Illustration)",
    variable=private_var
)
private_checkbox.grid(row=0, column=1, padx=10, pady=10, sticky="w")



# blur
def update_blur(value):
    blur_size = int(value) * 2 + 1
    blur_value_label.configure(text=f"Blur Size : {blur_size}")

main_row+=2
blur_value_label = ctk.CTkLabel(
    app,
    text="Blur Size : 31"
)
blur_value_label.grid(
    row =main_row,
    column=0,
    padx=10,
    pady=(20, 5),
    sticky="w"
)

main_row+=2
blur_frame = ctk.CTkFrame(app)
blur_frame.grid(
    row =main_row,
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
blur_slider.set(15)
update_blur(15)

# confidence
def update_confidence(value):
    confidence_value_label.configure(
        text=f"Confidence : {value:.2f}"
    )
    
main_row+=2
confidence_value_label = ctk.CTkLabel(
    app,
    text="Confidence : 0.50"
)
confidence_value_label.grid(
    row =main_row,
    column=0,
    padx=10,
    pady=(20, 5),
    sticky="w"
)

main_row+=2
confidence_frame = ctk.CTkFrame(app)
confidence_frame.grid(
    row =main_row,
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


main_row+=2
confidence_slider.grid(
    row=main_row,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)

confidence_slider.set(0.50)
update_confidence(0.50)



# start,progress
main_row+=2
start_button = ctk.CTkButton(
    app,
    text="Start",
    command=start_process,
)
start_button.grid(
    row =main_row,
    column=0,
    columnspan=2,
    padx=10,
    pady=20,
    sticky="ew"
)
progress_frame = ctk.CTkFrame(app)

progress_bar = ctk.CTkProgressBar(progress_frame)
progress_bar.pack(fill="x", padx=10, pady=(10, 5))

progress_label = ctk.CTkLabel(
    progress_frame,
    text="0 / 0"
)
progress_label.pack(pady=(0, 10))
progress_frame.grid(
    row =main_row,
    column=0,
    columnspan=2,
    padx=10,
    pady=20,
    sticky="ew"
)
progress_frame.grid_remove()

def update_progress(current, total):
    app.after(
        0,
        lambda: update_progress_ui(current, total)
    )
    
def update_progress_ui(current, total):
    progress_bar.set(current / total)

    percent = int(current / total * 100)

    progress_label.configure(
        text=f"{current} / {total}  ({percent}%)"
    )
    
def process_finished():
    progress_bar.set(1)

    progress_label.configure(
        text="Finished!"
    )

    start_button.configure(
        state="normal",
        text="Start"
    )
    app.after(1500, reset_progress)
    
def reset_progress():
    progress_frame.grid_remove()
    start_button.grid()
    progress_bar.set(0)
    progress_label.configure(text="0 / 0")
    
    
# log
main_row+=2
log_text = ctk.CTkTextbox(
    app,
    state="disabled"
)
log_text.grid(
    row =main_row,
    column=0,
    columnspan=2,
    padx=10,
    pady=10,
    sticky="nsew"
)

def update_log(message):
    app.after(
        0,
        lambda: add_log(message)
    )

def add_log(message):
    log_text.configure(state="normal")
    log_text.insert("end", message + "\n")
    log_text.see("end")
    log_text.configure(state="disabled")
    

    
def run_process(
    input_dir,
    output_dir,
    blur_size,
    confidence
):
    parts = []

    targets = {
        "face": face_var,
        "private_parts": private_var,
    }

    for name, var in targets.items():
        if var.get():
            parts.append(name)

    if not parts:
        update_log("検出対象を1つ以上選択してください")
        return
    
    process_images(
        input_dir,
        output_dir,
        blur_size,
        confidence,
        parts,
        progress_callback=update_progress,
        log_callback=update_log,
    )

    app.after(0, process_finished)
    
input_frame.grid_columnconfigure(0, weight=1)
output_frame.grid_columnconfigure(0, weight=1)
blur_frame.grid_columnconfigure(0, weight=1)
confidence_frame.grid_columnconfigure(0, weight=1)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

app.mainloop()