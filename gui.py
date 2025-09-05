import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from main import run_code

def execute():
    code = editor.get("1.0", tk.END)
    output = run_code(code)
    result.config(state='normal')
    result.delete("1.0", tk.END)
    result.insert(tk.END, output)
    result.config(state='disabled')

def copy_output():
    result.config(state='normal')
    text = result.get("1.0", tk.END)
    result.config(state='disabled')
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("کپی شد", "ฅʕ•̫͡•ʔฅ خروجی در کلیپ‌بورد ذخیره شد")

def clear_all():
    editor.delete("1.0", tk.END)
    result.config(state='normal')
    result.delete("1.0", tk.END)
    result.config(state='disabled')

root = tk.Tk()
root.title("شبیه‌ساز کامپایلر با پایتون")
root.geometry("800x600")
root.configure(bg="#f5f5f5")

# عنوان
title = tk.Label(root, text="(●'◡'●) شبیه‌ساز کامپایلر", font=("B Nazanin", 18, "bold"), bg="#f5f5f5")
title.pack(pady=10)

# ویرایشگر کد
editor_label = tk.Label(root, text=":کد ورودی", font=("B Nazanin", 12), bg="#f5f5f5")
editor_label.pack()
editor = scrolledtext.ScrolledText(root, height=12, width=90, font=("Courier New", 12))
editor.pack(pady=5)

# دکمه‌ها
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)

run_btn = tk.Button(btn_frame, text="اجرا", command=execute, width=12, bg="#4CAF50", fg="white", font=("B Nazanin", 11, "bold"))
run_btn.grid(row=0, column=0, padx=5)

copy_btn = tk.Button(btn_frame, text="کپی خروجی", command=copy_output, width=12, bg="#2196F3", fg="white", font=("B Nazanin", 11, "bold"))
copy_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="پاک کردن", command=clear_all, width=12, bg="#f44336", fg="white", font=("B Nazanin", 11, "bold"))
clear_btn.grid(row=0, column=2, padx=5)

# خروجی
result_label = tk.Label(root, text=":خروجی", font=("B Nazanin", 12), bg="#f5f5f5")
result_label.pack()
result = scrolledtext.ScrolledText(root, height=10, width=90, font=("Courier New", 12), bg="#eeeeee")
result.pack(pady=5)
result.config(state='disabled')

root.mainloop()
