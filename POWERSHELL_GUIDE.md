# Panduan dan Dokumentasi Perintah PowerShell
## Project: Stok Forecasting (Django REST Framework)

Dokumen ini memuat dokumentasi komprehensif seluruh perintah PowerShell dan CLI yang digunakan dalam siklus pengembangan project Stok Forecasting. Setiap bagian disusun dengan penjelasan teknis mendalam mengenai fungsi perintah, sintaks, parameter, serta konteks penggunaannya.

---

## 1. Alur Operasional Standar (Daily Workflow)

Urutan perintah yang dijalankan setiap kali memulai dan mengakhiri sesi pengembangan:

### Memulai Sesi Pengembangan
```powershell
# Masuk ke direktori utama project
cd "c:\Ngoding\PORTFOLIO FLOWDEV TEAMS\STOKFORECASTING"

# Mengaktifkan virtual environment
stok-forecasting\Scripts\Activate

# Menjalankan development server
python manage.py runserver
```

### Mengakhiri Sesi Pengembangan
1. Hentikan server Django dengan menekan kombinasi tombol `Ctrl + C` pada terminal.
2. Nonaktifkan virtual environment:
```powershell
deactivate
```

---

## 2. Manajemen Virtual Environment (venv)

Virtual environment menyediakan lingkungan Python yang terisolasi dari instalasi global sistem operasi. Ini mencegah konflik versi antar-library dari project yang berbeda.

### 2.1. Inisialisasi Virtual Environment
```powershell
python -m venv stok-forecasting
```
* **Fungsi:** Membuat direktori lingkungan virtual baru bernama `stok-forecasting`.
* **Mekanisme:** Perintah memanggil modul bawaan Python `venv` untuk membuat direktori lokal yang berisi salinan biner Python interpreter, pustaka standar, dan pengelola paket `pip`.
* **Kapan Digunakan:** Hanya dijalankan satu kali saat setup awal repository/workspace.

### 2.2. Aktivasi Virtual Environment
```powershell
stok-forecasting\Scripts\Activate
```
* **Fungsi:** Mengalihkan path eksekusi perintah `python` dan `pip` ke dalam direktori `stok-forecasting\Scripts`.
* **Indikator Keberhasilan:** Prefix `(stok-forecasting)` akan muncul di sisi kiri prompt terminal PowerShell.
* **Kapan Digunakan:** Wajib dieksekusi di setiap terminal baru sebelum menjalankan perintah Python atau Django.

### 2.3. Deaktivasi Virtual Environment
```powershell
deactivate
```
* **Fungsi:** Mengembalikan variabel lingkungan `PATH` terminal ke konfigurasi sistem global.
* **Kapan Digunakan:** Setelah selesai bekerja atau saat hendak berpindah ke project lain.

---

## 3. Manajemen Paket dan Dependensi (pip)

### 3.1. Pembaruan Paket Pip
```powershell
python.exe -m pip install --upgrade pip
```
* **Fungsi:** Memperbarui executable `pip` ke rilis stabil terbaru.
* **Alasan:** Menghindari peringatan versi kedaluwarsa serta memastikan kompatibilitas wheel paket modern.

### 3.2. Instalasi Framework Inti
```powershell
python -m pip install django
pip install djangorestframework
```
* **Fungsi:**
  * `django`: Menginstal framework inti Django untuk arsitektur backend, ORM, routing, dan admin interface.
  * `djangorestframework`: Menginstal pustaka Django REST Framework (DRF) untuk pembangunan web API (serialisasi, views API, autentikasi).

### 3.3. Pencatatan Dependensi ke Berkas requirements.txt
```powershell
pip freeze > requirements.txt
```
* **Fungsi:** Mengekspor seluruh nama dan versi pustaka yang terpasang di virtual environment ke dalam file `requirements.txt`.
* **Catatan Teknis PowerShell:** Redireksi `>` pada Windows PowerShell versi bawaan (5.1) secara default menyimpan dengan encoding UTF-16LE. Jika file perlu dibaca oleh tool berbasis UTF-8, gunakan alternatif:
```powershell
pip freeze | Out-File -Encoding utf8 requirements.txt
```

### 3.4. Instalasi Massal dari requirements.txt
```powershell
pip install -r requirements.txt
```
* **Fungsi:** Menginstal seluruh daftar pustaka beserta versinya secara deterministik dari file `requirements.txt`.
* **Kapan Digunakan:** Saat clone project di perangkat baru atau deployment server.

---

## 4. Inisialisasi Arsitektur Project dan Aplikasi Django

### 4.1. Pembuatan Struktur Project Utama
```powershell
django-admin startproject stokforecasting .
```
* **Fungsi:** Menginisialisasi kerangka project Django bernama `stokforecasting`.
* **Arti Argumen Titik (`.`):** Parameter titik menginstruksikan Django untuk menaruh file konfigurasi (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`) di subfolder `stokforecasting/`, dan menaruh `manage.py` langsung pada direktori root saat ini.
* **Penting:** Jika titik dihilangkan, Django akan membuat direktori bersarang ganda (`stokforecasting/stokforecasting/...`) yang menyulitkan navigasi.

### 4.2. Pembuatan Modul Aplikasi (App)
```powershell
python manage.py startapp sales
```
* **Fungsi:** Membuat sub-modul bernama `sales` yang memuat komponen fungsional terisolasi (`models.py`, `views.py`, `admin.py`, `apps.py`, `tests.py`, dan folder `migrations/`).
* **Langkah Lanjutan Wajib:** Setiap aplikasi baru harus didaftarkan di dalam list `INSTALLED_APPS` pada file `stokforecasting/settings.py`.

---

## 5. Manajemen Skema Database dan Migrasi

Django ORM menggunakan sistem migrasi untuk menerjemahkan model Python ke dalam perintah DDL (Data Definition Language) SQL secara otomatis.

### 5.1. Kompilasi Perubahan Model ke Berkas Migrasi
```powershell
python manage.py makemigrations
```
* **Fungsi:** Memeriksa seluruh file `models.py` pada aplikasi terdaftar dan menghasilkan berkas skrip migrasi baru di folder `sales/migrations/` (misal: `0001_initial.py`).
* **Kapan Digunakan:** Dijalankan setiap kali ada penambahan model baru, penambahan field, perubahan tipe data, atau penghapusan kolom.

### 5.2. Penerapan Migrasi ke Database SQLite
```powershell
python manage.py migrate
```
* **Fungsi:** Membaca berkas migrasi yang belum dieksekusi dan menjalankan query SQL ke file database `db.sqlite3`.
* **Kapan Digunakan:** 
  1. Setup awal project (menerapkan tabel bawaan Django: auth, session, admin, contenttypes).
  2. Tepat setelah perintah `makemigrations` selesai dijalankan.

---

## 6. Manajemen Kredensial Administrator (Superuser)

```powershell
python manage.py createsuperuser
```
* **Fungsi:** Membuat akun level root/superuser pada sistem autentikasi Django.
* **Input yang Diminta:**
  * `Username`: Nama pengguna admin.
  * `Email address`: Alamat email (opsional).
  * `Password`: Kata sandi (tidak akan ditampilkan di layar saat diketik untuk alasan keamanan).
* **Kapan Digunakan:** Minimal satu kali di awal project untuk login ke antarmuka admin di browser pada URL `/admin/`.

---

## 7. Eksekusi Server Pengembangan (Development Server)

### 7.1. Menjalankan Server Standar
```powershell
python manage.py runserver
```
* **Fungsi:** Menjalankan web server HTTP lokal berbasis WSGI bawaan Django.
* **Host & Port Bawaan:** `http://127.0.0.1:8000/` (localhost).
* **Karakteristik:**
  * **Auto-reloader:** Memantau perubahan pada berkas kode `.py`. Server otomatis restart setiap kali file disimpan.
  * **Stat Reloader:** Menampilkan log request HTTP (GET, POST, status code 200, 404, 500) secara langsung di konsol PowerShell.

### 7.2. Menjalankan Server pada Port Tertentu (Opsional)
```powershell
python manage.py runserver 8080
```
* **Fungsi:** Digunakan apabila port 8000 default sedang digunakan oleh aplikasi lain.

---

## 8. Utilitas Sistem, Git, dan File Handling di PowerShell

### 8.1. Verifikasi Versi Environment
```powershell
python --version
python -m django --version
```
* **Fungsi:** Memverifikasi versi interpreter Python aktif dan versi framework Django yang terikat pada environment tersebut.

### 8.2. Mengubah Nama Berkas (Rename File)
```powershell
ren requirments.txt requirements.txt
```
* **Fungsi:** Mengubah nama file lama ke nama file baru (alias dari perintah PowerShell `Rename-Item`).

### 8.3. Inisialisasi Version Control Git
```powershell
git init
```
* **Fungsi:** Menginisialisasi folder project sebagai repository lokal Git baru.

---

## 9. Penanganan Masalah dan Troubleshooting PowerShell

### 9.1. Error Eksekusi Script Dinonaktifkan (ExecutionPolicy)
* **Gejala:** Muncul error teks merah saat menjalankan `stok-forecasting\Scripts\Activate`:
  ```
  File ... cannot be loaded because running scripts is disabled on this system.
  ```
* **Penyebab:** Kebijakan keamanan default Windows PowerShell memblokir eksekusi script tidak terverifikasi.
* **Solusi Teknis:** Buka PowerShell dan jalankan perintah bypass untuk sesi proses saat ini:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```
  Setelah itu, jalankan kembali `stok-forecasting\Scripts\Activate`.

### 9.2. Koreksi Kesalahan Sintaks (Typo Tracking)
Berikut daftar kesalahan pengetikan umum yang terjadi beserta koreksi standarnya:

| Perintah Salah | Perintah Valid | Analisis Kesalahan |
| :--- | :--- | :--- |
| `python manage.py migrations` | `python manage.py makemigrations` | `migrations` bukan sub-command Django. Perintah yang benar adalah `makemigrations`. |
| `pip install djangoforestframework` | `pip install djangorestframework` | Kesalahan penulisan nama modul Django REST Framework. |
| `django-admin startproject stok-forecasting` | `django-admin startproject stokforecasting .` | Identifier package Python tidak mengizinkan tanda strip/hyphen (`-`). Karakter yang valid adalah huruf, angka, dan underscore (`_`). |
| `pyhton` / `pyton` / `pythob` | `python` | Typo pemanggilan biner eksekusi Python. |
| `pip freeze requirments.txt` | `pip freeze > requirements.txt` | `pip freeze` memerlukan operator redirect `>` untuk menulis output terminal ke dalam berkas. |
