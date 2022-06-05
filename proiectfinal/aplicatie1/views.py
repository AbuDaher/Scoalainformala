from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
from .models import Post
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from .forms import BookForm
from .models import Book


@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("aplicatie1.delete_post")):
                post.delete()
        elif user_id:
            user= User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.filter(name="default")
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.filter(name="mod")
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'aplicatie1/home.html', {"posts" : posts})


@login_required(login_url='/login')
def actuals(request):
    posts1 = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("aplicatie1.delete_post")):
                post.delete()
        elif user_id:
            user= User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.filter(name="default")
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.filter(name="mod")
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'aplicatie1/actuals.html', {"posts1" : posts1})

@login_required(login_url='/login')
def planning(request):
    posts2 = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("aplicatie1.delete_post")):
                post.delete()
        elif user_id:
            user= User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.filter(name="default")
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.filter(name="mod")
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'aplicatie1/planning.html', {"posts2" : posts2})


@login_required(login_url="/login")
@permission_required("aplicatie1.add_post", login_url="/login", raise_exception=True)
def create_post_actuals(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/actuals")
    else:
        form = PostForm()

    return render(request, 'aplicatie1/create_post_actuals.html', {"form": form})


@login_required(login_url="/login")
@permission_required("aplicatie1.add_post", login_url="/login", raise_exception=True)
def create_post_planning(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/planning")
    else:
        form = PostForm()

    return render(request, 'aplicatie1/create_post_planning.html', {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request,'registration/sign_up.html', {"form": form})

@login_required(login_url="/login")
@permission_required("aplicatie1.add_post", login_url="/login", raise_exception=True)
def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']

        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'aplicatie1/upload.html', context)

@login_required(login_url="/login")
def book_list(request):
    books = Book.objects.all()
    p = Paginator(Book.objects.all(), 4)
    page = request.GET.get('page')
    bookview = p.get_page(page)
    return render(request, 'aplicatie1/book_list.html', {'books':books, 'bookview': bookview })

@login_required(login_url="/login")
@permission_required("aplicatie1.add_post", login_url="/login", raise_exception=True)
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'aplicatie1/upload_book.html', {
        'form': form
    })


@login_required(login_url="/login")
@permission_required("aplicatie1.add_post", login_url="/login", raise_exception=True)
def delete_book(request, pk):
    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


def search_books(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'aplicatie1/search_books.html', {'searched':searched, 'books':books})
    else:
        return render(request, 'aplicatie1/search_books.html',{})