from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import font

def animasyon(label, image):
    for alpha in range(0, 101, 5):
        image_putalpha = image.copy()
        image_putalpha.putalpha(alpha)
        photo = ImageTk.PhotoImage(image_putalpha)
        label.configure(image=photo)
        label.image = photo
        label.update()
        root.after(50)

    root.after(2000, lambda: baslat_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER))  # Yazıyı 2 saniye sonra göster

    for alpha in range(100, -1, -5):
        image_putalpha = image.copy()
        image_putalpha.putalpha(alpha)
        photo = ImageTk.PhotoImage(image_putalpha)
        label.configure(image=photo)
        label.image = photo
        label.update()
        root.after(50)

    label.destroy()

def uygulama_kapat():
    root.destroy()

def uygulama_baslat():
    global baslat_label
    baslat_label = tk.Label(root, text='Uygulama başlatılıyor...', font=('Montserrat', 16, 'bold'), fg='white', bg='black')
    baslat_label.update()
    root.after(2000, lambda: baslat_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER))
    root.after(5000, lambda: baslat_label.destroy())

    logo_label.destroy()
    logo_image = Image.open('logo1.png').convert('RGBA')
    animasyon(logo_label, logo_image)
    sohbet_sahnesi()

def sohbet_sahnesi():
    # Burada sohbet botu ile ilgili kodları yazabilirsiniz
    pass

root = tk.Tk()
root.geometry('800x600')
root.title('Uygulama')
root.configure(bg='black')
root.attributes('-fullscreen', True)

font.nametofont("TkDefaultFont").configure(family="Montserrat")

logo_label = tk.Label(root, bg='black')
logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
logo_label.update()

logo_image = Image.open('logo1.png').convert('RGBA')

animasyon(logo_label, logo_image)

style = ttk.Style()
style.configure('Transparent.TButton', font=('Montserrat', 12), background='#E5E5E5', foreground='black')
style.configure('Transparent.TButton', font=('Montserrat', 12), background='black', foreground='black')
style.map('Transparent.TButton',
          background=[('active', 'black'), ('disabled', '#606060')])  # Butonun aktif ve devre dışı renkleri

kapat_button = ttk.Button(root, text="Kapat", style='Transparent.TButton', command=uygulama_kapat)
kapat_button.place(relx=0.02, rely=0.02, anchor=tk.NW)

root.after(1000, uygulama_baslat)  # 5 saniye sonra uygulama_baslat fonksiyonunu çağır

root.mainloop()
