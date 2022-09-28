# **PBP Assignment 4**

Nama : Carlene Annabel

NPM : 2106752211

Kelas :D

<a href="https://katalog-carlene.herokuapp.com/todolist/login/" target= "_blank">Link Login Aplikasi To Do List</a>

##  **Apa kegunaan {% csrf_token %} pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?** 

Pada elemen `<form>`, developer dapat mengaktifkan perlindungan untuk template yang menggunakan POST form dengan memasukkan tag csrf_token di dalam elemen `<form>`. Hal ini tetapi hanya berlaku untuk form yang berada pada URL internal dan buka POST forms yang menargetkan URL eksternal. Jika tidak ada potongan kode tersebut pada elemen form, dan berada di luarnya maka csrf_token akan menargetkan URL eksternal. Token CSRF sendiri mencgah CSRF (jenis serangan yang terjadi ketika situs web, email, blog, pesan instan, atau program berbahaya menyebabkan browser web pengguna melakukan tindakan yang tidak diinginkan di situs tepercaya saat pengguna diautentikasi) karena tanpa token, hacker tidak dapat membuat request yang valid ke server backend. 

##  **Apakah kita dapat membuat elemen `<form>`secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.?** 

Ya, kita bisa membuat elemen `<form>` secara manual. Kita dapat membuat form manual dengan membuat POST method dan memakai elemen {% csrf_token %}. Kemudian kita dapat memakai elemen yang ada pada HTML seperti `<table>`, `<input>`, dll untuk membuat form. Untuk mengambil data yang ada pada HTML form yang sudah kita buat, kita dapat menggunakan method `request.POST.get(input name)`.

## **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

Kita dapat mengecek apakah form nya telah di submisi oleh user dengan 

```js
    if request.method == 'POST':
```
Kemudian, kita dapat menyimpan data yang sudah diinput oleh user dari HTML dengan kode berikut.Setelah kita mendapatkan data yang sudah kita input, kita dapat menyimpan data - data tersebut ke dalam data base dengan menggunakan method save().Kita menggunakan new_task = form.save(commit=False) sebelumnya, karena dengan menyimpan dengan commit=False, kita mendapatkan objek model, kemudian baru kita akan menambahkan data ekstra dan menyimpannya.

```js
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()

```
Setelah itu, kita dapat merender data kedalam HTML. Lalu, kita dapat iterasi data ke dalam HTML.

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Menjalankan kode untuk membuat aplikasi `todolist`

    ```js
    django-admin startapp todolist
    ```
2.  Membuat models todolist dengan menambahkan potongan kode berikut ke dalam models.py

    ```js
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    ```
3. Melakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

4. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

5. Menambahkan `path('todolist/',include('todolist.urls')),` pada urls.py yang ada pada project dan django.

6. Membuat `forms.py` untuk membuat form untuk menerima data dengan kode berikut

```js
from django import forms

from .models import *

class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'size':'30'}))
    description= forms.CharField(widget=forms.Textarea(attrs={'size': '60'}))

    class Meta:
        model = Task
        fields = ('title', 'description')
```

7. Menambahkan fungsi pada views.py sesuai kebutuhan

```js
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *



@login_required(login_url="/todolist/login/")
# Create your views here.
def show_todolist(request):
    # user_name = User.objects.get(username=request.user)   
    if request.user.is_authenticated:
        user_name = request.user.username 
        data_tasklist = Task.objects.filter(user= request.user)
        context = {'todolist': data_tasklist, 
                    'username': user_name,
                    # 'last_login': request.COOKIES['last_login']
        }
    return render(request, 'todolist.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            # response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    user_name = User.objects.get(username=request.user)    
    form = TaskForm()
    new_task = None
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    context = {'form': form}
    return render(request, 'create-task.html', context)

def mark_as_finished(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not(task.is_finished)
    task.save(update_fields = ['is_finished'])
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))
```
8. Membuat folder create-task.html, login.html, register.html, dan todolist.html untuk tampilan user

9. Membuat sebuah berkas di dalam folder aplikasi todolist bernama urls.py untuk melakukan routing terhadap fungsi views. Sebagai berikut

```js
from django.urls import path
from todolist.views import register
from todolist.views import login_user,delete_task
from todolist.views import logout_user, show_todolist, create_task, mark_as_finished

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name = 'show_todolist'),
    path('register/', register, name= 'register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('mark-as-finished/<int:id>/', mark_as_finished, name='mark_as_finished'),
    path('delete/<int:id>/', delete_task, name='delete')
]
```

10. Kemudian melakukan mapping data yang ada pada fungsi views dan memunculkannya di halaman HTML

11. Deploy aplikasi ke heroku 






