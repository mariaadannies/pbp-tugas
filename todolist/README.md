## Link Heroku:
https://pbp-tugas-2.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen < form >? 
Cross-Site Request Forgery (CSRF) adalah serangan yang paling sering terjadi dan paling sederhana di web. CSRF token berfungsi untuk mencegah serangan CSRF yang membuat penyerang tidak mungkin melakukan submisi form yan bukan berasal dari website.

## Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen < form >?
Jika tidak ada potongan kode tersebut pada elemen < form > maka attacker tidak dapat membuat request yang valid ke[ada server backend.

## Apakah kita dapat membuat elemen < form > secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat < form > secara manual.
Ya, cara membuat form secara manual dapat dilakukan dengan membuat tag form, membuat form pertanyaan dengan label tag pada html, dan input sesuai dengan atribut type, dan membuat button untuk men-submit form tersebut.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Form yang telah disubmit oleh user akan di POST jika CSRF token sesuai makan form tersebut akan divalidasi. Setelah berhasihl tersubmit, user akan di redirect ke laman yang menampikan todo list.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.  
Dengan python manage.py startapp todolist dan menambahkan app todolist ke dalam installed app pada settings.py

2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.  
Menambahkan path pada urls.py

3. Membuat sebuah model Task  
Membuat model Task pada models.py

4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
Menggunakan form dari django untuk pengaplikasian registrasi dan cotoh template dari tutorial untuk implementasi login dan logout

5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.  
Membuat file html yang merupakan extend dari base.html dengan menambahkan button untuk menghapus dan menambah task

6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.  
Menggunakan modelForm untuk pembuatan task yang selanjutnya disimpan dalam database

7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL.  
Menambahkan urlpattern pada urls.py 

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Internal CSS:  
Internal CSS diletakkan di dalam bagian <head> pada halaman. Internal CSS hanya akan aktif pada halaman tersebut dan akan di-download setiap kali halaman dipanggil. CSS internal diletakkan di dalam tag <style></style>.

Eksternal CSS:  
perubahan apapun yang Anda buat pada file CSS akan tampil pada website Anda secara keseluruhan. File CSS eksternal biasanya diletakkan setelah bagian <head> pada halaman.
Contoh, <link rel="stylesheet" href="{% static 'css/login.css' %}">

## Jelaskan tag HTML5 yang kamu ketahui.
<title>  
Membuat judul pada halaman

<body>  
Membuat body dari halaman

<h1> to <h6>  
Membuat heading

<p>  
Membuat paragraf

<form>	
Membuat form yang digunakan untuk menerima input pengguna

<button>	
Membuat button

<img>	
Menyisipkan gambar

<ul>	
Membuat unordered list (list tanpa nomor)

<ol>	
Membuat ordered list (list dengan nomor)

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Selektor Tag: memilih elemen berdasarkan tag
2. Selektor Class: memilih elemen berdasarkan nama tag yang diberikan
3. Selektor ID: memilih elemen berdasarkan id yang diberikan
4. Selektor Atribut: memilih elemen berdasarkan atribut

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework
Melakukan kustomisasi dengan menggunakan templat yang sudah tersedia di internet :D
    - Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin  
    Menambahkan kode berikut pada file html  
    ```
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'css/login.css' %}">
    ```
    
    - Kustomisasi halaman utama todo list menggunakan cards
    Menambahkan kode berikut pada file html  
    ```
    <div class="row">
    {% for task in list_task %}
        <div class="col-sm-4">
            <div class="card">
                <div class="card-header">
                    {% if task.is_finished %}
                        <h5>Done</h5>
                    {% else %}
                        <h5>In Progress</h5>
                    {% endif %}
                </div>
                <div class="card-body">
                    <h5 class="card-title">{{task.title}}</h5>
                    <p class="card-text">{{task.description}}</p>
                </div>
                    
                <div class="card-footer">
                    <p class="card-text"><small class="text-muted">Task created {{task.date}}</small></p>
                    <div class = "btn-toolbar pull-right">
                        
                        <form method="post" action="{% url 'todolist:toggle-task' task.id %}" >
                            {% csrf_token %}
                            <button class="btn text-white me-1" style="background-color: #446DCA;" type="submit" name="toggle_done">
                                {% if task.is_finished %} Mark Not Done {% else %} Mark Done {% endif %}
                            </button>
                        </form>
    
                        <form method="post" action="{% url 'todolist:delete-task' task.id %}" >
                            {% csrf_token %}
                            <button class="btn text-white me-1" style="background-color: #446DCA;" type="submit" name="toggle_done">
                                Delete
                            </button>
                        </form>


                    </div>
                    
                </div>
            </div>
        </div>
    {% endfor %}
    </div>
    ```

2. Membuat keempat halaman yang dikustomisasi menjadi responsive
Penggunaan Bootstrap sedah otomatis membuat halaman menjadi responsif