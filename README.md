### PBP Tugas 2
###### link: https://pbp-tugas-2.herokuapp.com/


###### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://drive.google.com/file/d/1AgnyrkQ-irYvZXoCUTJ82eSFvx0nhahR/view?usp=sharing">
  <img alt="Bagan client request and response" src="https://drive.google.com/file/d/1AgnyrkQ-irYvZXoCUTJ82eSFvx0nhahR/view?usp=sharing">
</picture>
berkas html merupakan sebuah text file berisi template untuk menampilkan tampilan pada laman web.
urls.py mengembalikan elemen urlpatterns untuk mengakses laman pada aplikasi yang kita buat.
views.py berisi fungsi yang bertugas menerima web request dan mengembalikan web response.
models.py berisi informasi esensial mengenai data yang tersimpan.

###### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment berfungsi untuk mengisolasi suatu environments dimana setiap versi yang terunduh hanya terunduh pada environment tertentu. Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment.

###### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Membuat fungsi untuk mengambil model yang akan ditampilkan pada html.
2. Menambahkan path katalog pada urlpatterns di urls.py
3. Menggunakan for loop untuk menampilkan data katalog yang dirender oleh fungsi show_CatalogItem pada views.py di tabel tamplate html.
4. Membuat aplikasi baru pada heroku dan menghubungkannya dengan repository pada github untuk selanjutnya di-deploy. 