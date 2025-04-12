import sys
import time

def fade_in_text(text, delay=0.05, steps=10):
    output = "🎵 "  # Thêm nốt nhạc vào đầu dòng
    sys.stdout.write(output)  # In nốt nhạc trước
    sys.stdout.flush()
    time.sleep(delay)

    for char in text:
        for i in range(1, steps + 1):
            brightness = int(255 * i / steps)
            color = f"\033[38;2;{brightness};{brightness};{brightness}m"
            sys.stdout.write(f"\r{output}{color}{char}\033[0m")
            sys.stdout.flush()
            time.sleep(delay / steps)
        output += char  # Thêm ký tự vào chuỗi đã in
    print()  # Xuống dòng sau khi in xong

# Đọc file lời bài hát và in từng dòng với hiệu ứng chữ xuất hiện từ từ
def display_lyrics(filename, delay=0.1):
    with open(filename, 'r', encoding='utf-8') as file:
        lyrics = file.readlines()
    
    for line in lyrics:
        fade_in_text(line.strip(), delay)
        time.sleep(delay)

# Chạy chương trình với file lời bài hát
display_lyrics("<file_name>.txt")  # Đảm bảo có file lyrics.txt trong thư mục chạy script
