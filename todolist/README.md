# **PBP Assignment 4**

Nama : Carlene Annabel

NPM : 2106752211

Kelas :D

<a href="https://katalog-carlene.herokuapp.com/todolist/login/" target= "_blank">Link Login Aplikasi To Do List</a>

##  **Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?** 

Pada elemen <form>, developer dapat mengaktifkan perlindungan untuk template yang menggunakan POST form dengan memasukkan tag csrf_token di dalam elemen <form>. Hal ini tetapi hanya berlaku untuk form yang berada pada URL internal dan buka POST forms yang menargetkan URL eksternal. Jika tidak ada potongan kode tersebut pada elemen form, dan berada di luarnya maka csrf_token akan menargetkan URL eksternal. Token CSRF sendiri mencgah CSRF (jenis serangan yang terjadi ketika situs web, email, blog, pesan instan, atau program berbahaya menyebabkan browser web pengguna melakukan tindakan yang tidak diinginkan di situs tepercaya saat pengguna diautentikasi) karena tanpa token, hacker tidak dapat membuat request yang valid ke server backend. 

##  **Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.?** 


