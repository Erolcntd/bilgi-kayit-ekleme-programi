import tkinter as tk
from tkinter import ttk, messagebox

def ekle():
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    dogum_tarihi = dogum_tarihi_entry.get()
    tc = tc_entry.get()
    adres = adres_entry.get()

    if not ad or not soyad or not dogum_tarihi or not tc or not adres:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm bilgileri doldurun!")
        return

    yeni_kisi = (ad, soyad, dogum_tarihi, tc, adres)
    liste_box.insert("", tk.END, values=yeni_kisi)
    messagebox.showinfo("Ekle", "Kullanıcı başarıyla eklendi!")
    kaydet()

def kaydet():
    with open("kullanicilar.txt", "w") as dosya:
        for item in liste_box.get_children():
            dosya.write(",".join(liste_box.item(item)['values']) + "\n")

def sil():
    secili = liste_box.focus()
    if not secili:
        return
    cevap = messagebox.askyesno("Sil", "Seçili kullanıcıyı silmek istediğinizden emin misiniz?")
    if cevap:
        liste_box.delete(secili)
        messagebox.showinfo("Sil", "Kullanıcı başarıyla silindi!")
        kaydet()

def guncelle():
    secili = liste_box.focus()
    if not secili:
        return
    ad, soyad, dogum_tarihi, tc, adres = liste_box.item(secili)['values']

    ad_entry.delete(0, tk.END)
    ad_entry.insert(0, ad)
    soyad_entry.delete(0, tk.END)
    soyad_entry.insert(0, soyad)
    dogum_tarihi_entry.delete(0, tk.END)
    dogum_tarihi_entry.insert(0, dogum_tarihi)
    tc_entry.delete(0, tk.END)
    tc_entry.insert(0, tc)
    adres_entry.delete(0, tk.END)
    adres_entry.insert(0, adres)

    messagebox.showinfo("Güncelle", "Kullanıcının bilgileri güncellenmeye hazır!")

def cikis():
    cevap = messagebox.askyesno("Çıkış", "Uygulamadan çıkmak istediğinizden emin misiniz?")
    if cevap:
        kaydet()
        pencere.destroy()

pencere = tk.Tk()
pencere.title("Kullanıcı Yönetimi")
pencere.geometry("800x600")
pencere.configure(bg="#ECECEC")
pencere.protocol("WM_DELETE_WINDOW", cikis)

frame = ttk.Frame(pencere, padding=20)
frame.pack(expand=True, fill="both")

ad_label = ttk.Label(frame, text="Ad:")
ad_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
soyad_label = ttk.Label(frame, text="Soyad:")
soyad_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
dogum_tarihi_label = ttk.Label(frame, text="Doğum Tarihi:")
dogum_tarihi_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
tc_label = ttk.Label(frame, text="TC Kimlik No:")
tc_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
adres_label = ttk.Label(frame, text="Adres:")
adres_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)

ad_entry = ttk.Entry(frame, width=30)
ad_entry.grid(row=0, column=1, padx=10, pady=5)
soyad_entry = ttk.Entry(frame, width=30)
soyad_entry.grid(row=1, column=1, padx=10, pady=5)
dogum_tarihi_entry = ttk.Entry(frame, width=30)
dogum_tarihi_entry.grid(row=2, column=1, padx=10, pady=5)
tc_entry = ttk.Entry(frame, width=30)
tc_entry.grid(row=3, column=1, padx=10, pady=5)
adres_entry = ttk.Entry(frame, width=30)
adres_entry.grid(row=4, column=1, padx=10, pady=5)

ekle_buton = ttk.Button(frame, text="Ekle", command=ekle)
ekle_buton.grid(row=5, column=1, pady=10)

sil_buton = ttk.Button(frame, text="Sil", command=sil)
sil_buton.grid(row=5, column=2, padx=5, pady=10)

guncelle_buton = ttk.Button(frame, text="Güncelle", command=guncelle)
guncelle_buton.grid(row=5, column=3, padx=5, pady=10)

liste_box = ttk.Treeview(frame, columns=("Ad", "Soyad", "Doğum Tarihi", "TC Kimlik No", "Adres"), show="headings")
liste_box.grid(row=6, column=0, columnspan=4, pady=10, padx=10)

# Sütun başlıkları
liste_box.heading("Ad", text="Ad")
liste_box.heading("Soyad", text="Soyad")
liste_box.heading("Doğum Tarihi", text="Doğum Tarihi")
liste_box.heading("TC Kimlik No", text="TC Kimlik No")
liste_box.heading("Adres", text="Adres")

# Sütun genişlikleri
liste_box.column("Ad", width=120)
liste_box.column("Soyad", width=120)
liste_box.column("Doğum Tarihi", width=120)
liste_box.column("TC Kimlik No", width=150)
liste_box.column("Adres", width=200)

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=liste_box.yview)
scrollbar.grid(row=6, column=4, sticky="ns")

liste_box.configure(yscrollcommand=scrollbar.set)

cikis_buton = ttk.Button(frame, text="Çık", command=cikis)
cikis_buton.grid(row=7, column=0, columnspan=4, pady=10)

# Tabloyu daha zarif hale getirmek için stil ayarları
style = ttk.Style()
style.theme_use("clam")

# Tablo başlığı için stil ayarları
style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#4A4")
style.configure("Treeview", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))

# Diğer bileşenlerin stil ayarları
frame.configure(style="TFrame")
ad_label.configure(style="TLabel")
soyad_label.configure(style="TLabel")
dogum_tarihi_label.configure(style="TLabel")
tc_label.configure(style="TLabel")
adres_label.configure(style="TLabel")
ad_entry.configure(style="TEntry")
soyad_entry.configure(style="TEntry")
dogum_tarihi_entry.configure(style="TEntry")
tc_entry.configure(style="TEntry")
adres_entry.configure(style="TEntry")
ekle_buton.configure(style="TButton")
sil_buton.configure(style="TButton")
guncelle_buton.configure(style="TButton")
cikis_buton.configure(style="TButton")

pencere.mainloop()
