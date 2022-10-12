## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Dalam synchronus programming pengguna harus menunggu pemrosesan data oleh server dan client hingga selesai sebelum pengguna dapat mlanjut berinteraksi dengan website.  
Dalam Asynchronus programming pengguna tetap dapat berinteraksi dengan website meskipun sedang menunggu response dari suatu request. 
## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming merupakan paradigma dimana suatu objek atau servis berkomunikasi secara tidak langsung dengan mengirimkan pesan melalui perantara. Salah satu penerapan paradigma event-driven programming pada tugas ini adalah tombol submit yang ketika diklik akan men-submit form dan membuat AJAX memperbarui daftar todolisr.
## Jelaskan penerapan asynchronous programming pada AJAX.
AJAX memungkinkan suatu halaman web untuk diperbaharui secara asynchronus sehingga tidak perlu melakukan reload untuk seluruh halaman web ketika hanya sebagian kecil dari halaman web yang berubah.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
#### AJAX GET
1. Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.  
2. Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.  
3. Lakukan pengambilan task menggunakan AJAX GET.  
#### AJAX POST
1. Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.  
2. Buatlah view baru untuk menambahkan task baru ke dalam database.  
3. Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.  
4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add.
5. Tutup modal setelah penambahan task telah berhasil dilakukan.  
6. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.    