## Link Heroku:
https://pbp-tugas-2.herokuapp.com/todolist/

# Apa kegunaan {% csrf_token %} pada elemen < form >? 
Cross-Site Request Forgery (CSRF) adalah serangan yang paling sering terjadi dan paling sederhana di web. CSRF token berfungsi untuk mencegah serangan CSRF yang membuat penyerang tidak mungkin melakukan submisi form yan bukan berasal dari website.

# Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen < form >?
Jika tidak ada potongan kode tersebut pada elemen < form > maka attacker tidak dapat membuat request yang valid ke[ada server backend.

# Apakah kita dapat membuat elemen < form > secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat < form > secara manual.
Ya, 

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.