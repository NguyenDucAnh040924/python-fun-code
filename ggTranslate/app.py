from tkinter import *
from PIL import Image, ImageTk
from deep_translator import GoogleTranslator

# Tạo tinker window
tk = Tk()
tk.title('Google Dịch')
tk.geometry('500x630')
tk.iconbitmap('logo.ico')

# Thiết lập hình nền
load = Image.open('background.jpg')
render = ImageTk.PhotoImage(load)
img = Label(tk, image=render)
img.place(x=0, y=0)

# Tiêu đề
name = Label(tk, text="Translator", fg="#FFFFFF")
name.config(font=("Transformer Movie", 30))
name.pack(pady=10)

# Nhập văn bản
label_from = Label(tk, text="Nhập văn bản:", fg="#FFFFFF", font=("Arial", 12))
label_from.pack(pady=5)
input_text = Text(tk, height=5, width=40)
input_text.pack(pady=5)

# Hiển thị kết quả dịch
label_to = Label(tk, text="Kết quả dịch:", fg="#FFFFFF", font=("Arial", 12))
label_to.pack(pady=5)
output_text = Text(tk, height=5, width=40)
output_text.pack(pady=5)
output_text.config(state=DISABLED)

# Hàm dịch văn bản
def translate_text():
    input_content = input_text.get("1.0", "end-1c")  # Lấy nội dung nhập vào
    if input_content.strip() != "":  # Kiểm tra nếu có văn bản để dịch
        try:
            translated = GoogleTranslator(source='auto', target='vi').translate(input_content)  # Dịch sang tiếng Việt
            output_text.config(state=NORMAL)  # Cho phép chỉnh sửa text output
            output_text.delete(1.0, END)  # Xóa kết quả cũ
            output_text.insert(END, translated)  # Chèn kết quả mới vào
            output_text.config(state=DISABLED)  # Khóa lại text để không chỉnh sửa
        except Exception as e:
            output_text.config(state=NORMAL)
            output_text.delete(1.0, END)
            output_text.insert(END, f"Lỗi: {e}")
            output_text.config(state=DISABLED)

# Nút dịch
translate_button = Button(tk, text="Dịch", font=("Arial", 14), command=translate_text)
translate_button.pack(pady=20)

tk.mainloop()
