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
Menambahkan kode berikut pada views.py  
```
@login_required(login_url='/todolist/login/')
def show_json(request):
    task = Task.objects.filter(user=request.user)
    data = serializers.serialize('json', task)

    return HttpResponse(data, content_type='application/json')
```
2. Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.  
Menambahkan path berikut pada urls.py  
```
path('json/', show_json, name='show_json'),
```
3. Lakukan pengambilan task menggunakan AJAX GET.  
Menambahkan kode berikut pada todolist.html  
```
var row = document.createElement("div")
        row.classList.add("row")

        function loadTask() {
            row.innerHTML=""

            $.get("{% url 'todolist:show_json' %}", function(data) {
                $.each(data, function(i,value) {
                    var field = value.fields

                    console.log(value)

                    var colSm4 = document.createElement("div")
                    colSm4.classList.add("col-sm-4")

                    var card = document.createElement("div")
                    card.classList.add("card")
                    colSm4.appendChild(card)

                    var header = document.createElement("div")
                    header.classList.add("card-header")
                    card.appendChild(header)

                    var status = document.createElement("h5")
                    if (field.is_finished) {
                        
                        status.innerHTML = "Done"
                    } else {
                        status.innerHTML = "In Progress"
                    }
                    header.appendChild(status)

                    var body = document.createElement("div")
                    body.classList.add("card-body")
                    card.appendChild(body)

                    var title = document.createElement("h5")
                    title.classList.add("card-title")
                    title.innerHTML = field.title
                    body.appendChild(title)

                    var desc = document.createElement("p")
                    desc.classList.add("card-text")
                    desc.innerHTML = field.description
                    body.appendChild(desc)

                    var footer = document.createElement("div")
                    footer.classList.add("card-footer")
                    card.appendChild(footer)

                    var date = document.createElement("p")
                    date.classList.add("text-muted")
                    date.innerHTML = `Task created ${field.date}`
                    footer.appendChild(date)

                    var btnBar = document.createElement("div")
                    btnBar.classList.add("btn-toolbar","pull-right")
                    footer.appendChild(btnBar)
                    
                    var updBtn = document.createElement("a")
                    updBtn.classList.add("btn","btn-primary","btn-sm")
                    updBtn.innerHTML = "Update Task"
                    updBtn.setAttribute("onclick", `updTask(${value.pk})`)
                    btnBar.appendChild(updBtn)

                    var delBtn = document.createElement("a")
                    delBtn.classList.add("btn","btn-danger","btn-sm")
                    delBtn.innerHTML = "Delete Task"
                    delBtn.setAttribute("onclick", `delTask(${value.pk})`)
                    btnBar.appendChild(delBtn)

                    row.appendChild(colSm4)
                })

                
                document.body.append(row)
            })

        }
```
#### AJAX POST
1. Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.  
Menggunakan link yang diletakan pada navbar di file todolist.html
```
<a class="nav-item nav-link" data-bs-toggle="modal" href="#exampleModal">Modal</a>

```
2. Buatlah view baru untuk menambahkan task baru ke dalam database.  
Menambahkan kode berikut pada views.py
```
@login_required(login_url='/todolist/login/')
def add_new_task(request):
    if request.method == "POST":
        data = json.loads(request.POST['data'])

        new_task = Task(title=data["title"], description=data["description"], user=request.user)
        new_task.save()

        return HttpResponse(serializers.serialize("json", [new_task]), content_type="application/json")

    return HttpResponse()
```
3. Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.  
Menambahkan kode berikut pada views.py
```
path('add/', add_new_task, name='add_new_task'),
```
4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add.
Menambahkan kode berikut pada todolist.html
```
$(document).ready(function () {
            // Get Cards
            loadTask();

            // Add Card
            $("#addTask").submit(function (e) {
                e.preventDefault();
                console.log("t")
                
                var data = JSON.stringify($("#addTask").serializeJSON())
                console.log("data", data)
                $.ajax({
                    type: "POST",
                    url: "{% url 'todolist:add_new_task' %}",
                    data: {
                        data: data,
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },

                    success: function(response) {
                        $('#addTask').each(function () {
                            this.reset();
                        });

                        console.log("sukses")
                        loadTask();
                        $('#exampleModal').modal('toggle');
                    },

                    error: function(xhr, resp, text) {
                        console.log("xhr", xhr)
                        console.log("resp", resp)
                        console.log("text", text)
                    }
                })
            })



        });
```
5. Tutup modal setelah penambahan task telah berhasil dilakukan.  
Menambahkan kode berikut pada todolist.html
```
$('#exampleModal').modal('toggle');
```
6. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.   
Menggunakan fungsi loadTask() pada todolist.html 