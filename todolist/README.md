## Link Heroku:
https://pbp-tugas-2.herokuapp.com/todolist/

# Apa kegunaan {% csrf_token %} pada elemen < form >? 
Cross-Site Request Forgery (CSRF) adalah serangan yang paling sering terjadi dan paling sederhana di web. CSRF token berfungsi untuk mencegah serangan CSRF yang membuat penyerang tidak mungkin melakukan submisi form yan bukan berasal dari website.

# Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen < form >?
Jika tidak ada potongan kode tersebut pada elemen < form > maka attacker tidak dapat membuat request yang valid ke[ada server backend.

# Apakah kita dapat membuat elemen < form > secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat < form > secara manual.
Ya, cara membuat form secara manual dapat dilakukan dengan membuat tag form, membuat form pertanyaan dengan label tag pada html, dan input sesuai dengan atribut type, dan membuat button untuk men-submit form tersebut.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Form yang telah disubmit oleh user akan di POST jika CSRF token sesuai makan form tersebut akan divalidasi. Setelah berhasihl tersubmit, user akan di redirect ke laman yang menampikan todo list.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

## Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
Dengan python manage.py startapp todolist

## Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Menambahkan path pada urls.py

## Membuat sebuah model Task
Membuat model Task pada models.py

## Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.

## Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
Membuat file html yang merupakan extend dari base.html

## Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

## Membuat routing sehingga beberapa fungsi dapat diakses melalui URL
Menambahkan urlpattern pada urls.py 

## Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
