# Jual Kurban Adaptable
### https://jualkurban.adaptable.app/main/ 

---

## 📘 **Jawaban Tugas 4**

2. 📸 Membuat **dua** akun pengguna dengan masing-masing **tiga** data contoh menggunakan model yang sudah ada pada aplikasi sebelumnya untuk setiap akun **secara lokal**
   - afzaal - apjalwib
   - apjal - afzaalwib

### 📚 Apa itu Django `UserCreationForm` dan apa keunggulan serta kelemahannya?

- 🌟 **Keunggulan**
    - **Cepat dan Praktis:** UserCreationForm memungkinkan pembuat untuk dengan cepat membuat formulir pendaftaran tanpa menulis kode dari awal
    - **Terintegrasi dengan Django:** UserCreationForm terintegrasi dengan fitur otentikasi Django, termasuk penggunaan kata sandi yang dienkripsi dan proses validasi
    - **Keamanan Terintegrasi:** UserCreationForm sudah memiliki mekanisme keamanan untuk mencegah serangan seperti SQL injection dan cross-site scripting (XSS)
- 🚫 **Kelemahan**
    - **Terbatas pada Fungsi Dasar:** UserCreationForm hanya dirancang untuk pendaftaran dasar, sehingga memerlukan modifikasi jika diperlukan atribut tambahan
    - **Tidak Lengkap:** Hanya mencakup dasar seperti nama pengguna dan kata sandi, jadi fitur tambahan seperti verifikasi email atau konfirmasi kata sandi harus ditambahkan secara manual
    - **Bergantung pada Django:** Harus menggunakan Django sebagai kerangka kerja jika ingin menggunakan UserCreationForm

### 🛡️ Apa bedanya autentikasi dan otorisasi dalam konteks Django dan mengapa keduanya penting?

**Autentikasi** dalam konteks Django adalah proses memverifikasi identitas pengguna yang mencoba masuk. Biasanya melibatkan proses masuk dengan kombinasi nama pengguna dan kata sandi.

**Otorisasi** menentukan apa yang boleh dilakukan pengguna setelah mereka terotentikasi. Ini mengatur akses ke halaman atau sumber daya tertentu.

Keduanya penting karena autentikasi memastikan identitas pengguna, sementara otorisasi mengontrol akses mereka. Ini penting untuk menjaga keamanan data dan sumber daya di aplikasi web.

### 🍪 Apa itu *cookies* dalam konteks aplikasi web dan bagaimana Django memanfaatkan *cookies* untuk mengelola data sesi pengguna?

*Cookies* dalam aplikasi web adalah data kecil yang disimpan di perangkat pengguna. Fungsinya adalah untuk menyimpan informasi seperti ID sesi atau preferensi yang dapat diakses oleh server web saat pengguna berinteraksi dengan situs.

Django memanfaatkan *cookies* untuk mengelola data sesi pengguna dengan cara:
- **Membuat Sesi:** Menghasilkan sesi pengguna dan ID sesi unik saat pertama kali masuk
- **Menyimpan Data Sesi:** Menyimpan informasi sesi dalam cookies dan mengenkripsinya jika diperlukan
- **Mengakses Data Sesi:** Membaca cookies pengguna saat permintaan berikutnya
- **Memperbarui Data Sesi:** Memperbolehkan pembuat untuk memperbarui data sesi pengguna
- **Mengakhiri Sesi:** Menghapus data sesi saat pengguna keluar atau sesi berakhir

### 🚫 Apakah penggunaan *cookies* secara default aman dalam pengembangan web atau ada potensi risiko yang perlu diwaspadai?

Meskipun dengan implementasi yang tepat dan penggunaan di lingkungan yang aman, penggunaan *cookies* biasanya aman, namun ada risiko seperti pelanggaran privasi, pencurian cookie, dan kerentanan terhadap serangan. Penting bagi pembuat untuk memvalidasi data, menggunakan HTTPS, dan melindungi aplikasi dari ancaman serangan untuk menjaga keamanan data pengguna dan privasi.

### 🚀 Bagaimana langkah-langkah yang kamu lakukan untuk menerapkan *checklist* di atas (tanpa hanya mengikuti tutorial)?

1. 📌 **Melaksanakan fungsi pendaftaran, masuk, dan keluar** agar pengguna dapat mengakses aplikasi sebelumnya dengan mudah.
    - 📝 **PENDAFTARAN**
        - Di `views.py`, tambahkan `redirect`, `UserCreationForm`, dan `messages`
        - Buat fungsi `register` yang menghasilkan formulir pendaftaran otomatis dan membuat akun pengguna saat data dikirim dari formulir
        - Buat file HTML baru bernama `register.html` di folder `main/template` untuk mendesain templat pendaftaran
        - Tambahkan fungsi `register` ke `urls.py`
        - Sisipkan jalur URL ke `urlpatterns`
    - 📝 **MASUK**
        - Di `views.py`, tambahkan fungsi `authenticate` dan `login`
        - Buat fungsi `login` untuk mengotentikasi pengguna yang ingin masuk
        - Buat file HTML baru bernama `login.html` di folder `main/template` untuk mendesain templat masuk
        - Tambahkan `login_user` ke `urls.py`
        - Sisipkan jalur URL ke `urlpatterns`
    - 📝 **KELUAR**
        - Di `views.py`, tambahkan fungsi `logout`
        - Buat fungsi `logout` untuk mengatur mekanisme keluar
        - Buka file `main.html` dan tambahkan kode untuk Add New Product
        - Tambahkan `logout_user` ke `urls.py`
        - Sisipkan jalur URL ke `urlpatterns`


3. 🔗 **Mengkaitkan model `Item` dengan `User`**.
    - Tambahkan `user` di `models.py`
    - Pada model `Item` yang sudah ada, sisipkan `ForeignKey` untuk mengkaitkan satu produk dengan satu pengguna melalui hubungan, di mana satu produk pasti terkait dengan satu pengguna
        - Di `views.py` modifikasi fungsi `create_item`
        - Sisipkan parameter `commit=False` untuk mencegah Django menyimpan objek ke basis data secara langsung
        - Isi bidang `user` dengan objek `User` dari nilai balik `request.user` untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang masuk

4. 🖼️ **Menunjukkan informasi detail pengguna yang sedang masuk** seperti nama pengguna dan menerapkan `cookies` seperti `last login` di halaman utama aplikasi
    - Modifikasi fungsi `show_main`
        - Tampilkan objek `Item` yang terkait dengan pengguna yang sedang masuk dengan `items = Item.objects.filter(user=request.user)`
        - Sisipkan kode `request.user.username`
    - Di `views.py`, tambahkan `HttpResponseRedirect`, `reverse`, dan `datetime`
    - Pada fungsi `login_user`, tambahkan fungsi `last_login` untuk melihat kapan terakhir pengguna masuk. Modifikasi **blok** `if user is not None` dengan menambahkan kode:
        - `login(request, user)`
        - `response = HttpResponseRedirect(reverse("main:show_main"))`
        - `response.set_cookie('last_login', str(datetime.datetime.now()))`
        - `return response`
    - Pada fungsi `show_main`, tambahkan `'last_login': request.COOKIES['last_login']` ke dalam variabel `context`
    - Modifikasi fungsi `logout_user` dengan menambahkan kode:
        - `response = HttpResponseRedirect(reverse('main:login'))`
        - `response.delete_cookie('last_login')`
        - `return response`
    - Pada file `main.html`, tambahkan kode `<h5>Sesi terakhir masuk: {{ last_login }}</h5>`
---

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

