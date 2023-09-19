# Jual Kurban Adaptable
### https://jualkurban.adaptable.app/main/ 

# **Jawaban Tugas 3**

### 📘 **Perbedaan Antara Metode `POST` dan `GET` dalam Django:**
- **📮 POST**:
    - Mengirim informasi ke tujuan tanpa menampilkannya pada URL
    - Variabel `$_POST` menampung informasi yang dikirim
    - Memungkinkan pengiriman informasi dalam jumlah besar tanpa batasan khusus

- **🔍 GET**:
    - Mengirim informasi dengan menampilkan data di URL
    - Variabel `$_GET` menampung informasi dari URL
    - Keterbatasan panjang URL: hingga 2047 karakter

---

### 🌐 **Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**
- **🔖 XML**:
    - Fasilitasi pertukaran data dengan format yang kuat melalui tag-tag khusus
    - Berguna untuk konfigurasi aplikasi dan integrasi lintas platform

- **📄 JSON**:
    - Menyajikan data dengan format intuitif, menyerupai notasi objek
    - Ideal untuk komunikasi web dan API

- **🌍 HTML**:
    - Fokus pada tampilan konten di browser
    - Mengatur tampilan dan interaksi konten

---

### 🚀 **Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
- **🔍 Bacaan Intuitif**: Mudah dibaca dan dipahami
- **⚡ Penggunaan Efisien**: Struktur ringkas untuk penggunaan data optimal
- **🌍 Dukungan Luas**: Kompatibel dengan hampir semua bahasa pemrograman
- **💡 Keterkaitan dengan JavaScript**: Integrasi sempurna dengan web
- **🔗 Popularitas di API**: Format pilihan untuk banyak API web
- **🔗 Orientasi Objek**: Representasi objektif yang jelas
- **🛡 Aspek Keamanan**: Risiko keamanan lebih rendah

### 📝 **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. Mengembangkan form input untuk menambahkan objek model pada aplikasi yang telah ada:
    - Dalam folder "main", buat sebuah file dengan nama `forms.py`. Di dalam file ini, definisikan sebuah class bernama `ItemForm` yang berfungsi sebagai `ModelForm` dari model `Item`. Class ini akan menentukan atribut mana saja yang akan ditampilkan pada form.
    - Pada `views.py`, definisikan fungsi dengan nama `create_item`. Fungsi ini akan bertanggung jawab atas proses pengisian form `ItemForm` dengan data dari `request.POST` serta memvalidasinya. Apabila data yang diinput valid, maka akan disimpan dan selanjutnya pengguna akan diarahkan kembali ke halaman awal.
    - Sisipkan fungsi untuk menampilkan `create_item.html`.
    - Di dalam fungsi `show_main` yang berada di `views.py`, tambahkan kode `items = Item.objects.all()`. Fungsi ini akan mengambil semua objek `Item` yang tersimpan di database dan menyertakannya dalam konteks.
    - Di dalam `urls.py` yang berada di folder "main", tambahkan path URL yang diperlukan untuk mengakses semua fungsi yang telah dibuat sebelumnya.
    - Di folder "templates" dalam "main", buat file dengan nama `create_item.html`. Isikan file tersebut dengan kode yang relevan untuk membuat tampilan tabel dan form.
    - Pada `main.html`, masukkan kode yang diperlukan untuk menampilkan data item dalam bentuk tabel. Tambahkan juga tombol "Add New Product" yang saat diklik akan mengarahkan pengguna ke halaman form input.
    
2. Menyediakan fungsi views untuk menampilkan data dengan berbagai format:
    - Di dalam `views.py`, definisikan fungsi bernama `show_xml` dan tambahkan path URL untuk mengakses fungsi tersebut. Tugas dari fungsi ini adalah mengambil semua data `Item` dan menampilkannya dalam format XML.
    - Definisikan fungsi lain dengan nama `show_json` di `views.py` serta sisipkan path URL untuk mengakses fungsi ini. Fungsi ini akan mengambil semua data `Item` dan menampilkannya dalam format JSON.
    - Di `views.py`, tambahkan fungsi dengan nama `show_xml_by_id` serta path URL untuk mengakses fungsi tersebut. Fungsi ini bertugas mengambil data `Item` berdasarkan ID yang diberikan dan menampilkan data tersebut dalam format XML.
    - Tambahkan fungsi `show_json_by_id` di `views.py` dan path URL untuk mengakses fungsi ini. Fungsi ini akan mengambil data `Item` berdasarkan ID yang disuplai dan menampilkan hasilnya dalam format JSON.

### 📸 **Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.**
<img src='/asset/html.png'>
<img src='/asset/xml.png'>
<img src='/asset/json.png'>
<img src='/asset/xml id.png'>
<img src='/asset/json id.png'>


# **Jawaban Tugas 2**
## Step by step
### Creating new Django project
1. membuat file 'requirements.txt' serta menambahkan dependancies yang diperlukan. Pada kasus ini saya menambahkan
    ```text
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ``` 
kemudian install dependancies tersebut dengan mengetikkan `pip install -r requirements.txt` pada env. selanjutnya kita membuat aplikasi django baru dengan `django-admin startproject Tugas2PBP`

2. membuat app main dengan cara mengaktifkan env pada direktori Tugas2PBP serta menjalankan perintah `python manage.py startapp main`. Selanjutnya kita perlu mendaftarkan `main` pada variabel di dalam `INSTALLED_APPS` yang ada di `settings.py`
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
3. di file `models.py` yang ada di direktori main, kita perlu membuat model baru dan ini adalah versi saya.
```python 
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
```
selanjutnya juga perlu dilakukan migrasi model dengan `python manage.py makemigrations` dan dilanjutkan dengan menambahkannya ke database lokal dengan `python manage.py migrate`

4. selanjutnya kita akan membuat dan menghubungkan `views.py` dengan template yang ada. kita perlu menambahkan`import render` pada file `views.py` serta fungsi `show main` agar `main.html`bisa ditampilkan. berikut adalah kodenya
```python 
from django.shortcuts import render
# Create your views here.
def show_main(request):
    context = {
        'name': 'Maulana Afzaal Wibowo',
        'class': 'PBP E',
        'description' : 'Mahasiswa PBP'
    }

    return render(request, "main.html", context)
```
di file `main.html`, terdapat variabel yang nilainya bisa diganti dari model seperti berikut.
```python 
<h1>Toko Hewan Kurban Piket</h1>

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>class: </h5>
<p>{{ class }}<p>
<h5>Description: </h5>
<p>{{ description }}<p>

```
5. untuk melakukan routing URL pada aplikasi main, kita perlu membuat berkas bernama`urls.py` pada aplikasi main dan diisi dengan kode sebagai berikut.

```python 
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
dan supaya proyek `Tugas2PBP` bisa mengimpor url dari `main` maka kita perlu menambahkan fungsi `from django.urls import path, include` pada `urls.py` yang ada di `Tugas2PBP` serta memasukkan `main` pada `urlpatterns` seperti berikut.
```python
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```
bila sudah seharusnya halaman main sudah bisa dilihat pada local server dengan perintah `python manage.py runserver`. Dan terakhir kita tinggal mengupload ke adaptable dengan format `Python App Template` dan database type `PostgreSQL`

## bagan
<img src='/asset/Bagan.jpg'>

### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Venv memiliki peran penting dalam web development berbasis django karena membantu mengisolasi proyek, sehingga memungkinkan manajemen dependensi yang efisien. Dengan Venv proyek memiliki dependensi dan python package yang terisolasi sehingga mencegah konflik serta masalah versi.

Bisa saja kita membuat web app berbasis django tanpa Venv, tetapi akan ada resiko konflik dependancies antar proyek.

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Model-View-Controller (MVC), Model-View-Template (MVT), dan Model-View-ViewModel (MVVM) adalah tiga pendekatan desain perangkat lunak yang berfokus pada manajemen data, tampilan, dan logika aplikasi. Dalam MVC, Model bertanggung jawab untuk menyimpan data dan logika aplikasi, sedangkan View digunakan untuk menampilkan data dari Model dan menghubungkannya dengan template. MVT juga memiliki komponen Model yang sama dengan MVC, tetapi menggantikan Controller dengan Template, yang bertanggung jawab mengatur tampilan HTML dan cara data dari Model ditampilkan dalam halaman web. Di sisi lain, MVVM memperkenalkan komponen tambahan yaitu ViewModel, yang berfungsi untuk memproses data dari Model dan mempersiapkannya agar dapat ditampilkan oleh View. 

Perbedaan utama antara ketiga pendekatan ini terletak pada pengelolaan alur aplikasi, di mana MVC menggunakan Controller, MVT menggunakan Template, dan MVVM mengandalkan ViewModel untuk mengatur logika dan alur aplikasi.

