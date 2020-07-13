from django.shortcuts import render, redirect

# Create your views here.
from .forms import PostForm
from .models import PostModel

# menampilkam semua artikel 
def allPost(request):
     # queryset
     posts = PostModel.objects.all();
     context = {
          'title':'Orplant Artikel',
          'Posts':posts,
     }
     return render(request,'artikel/index.html', context)

# manage artikel
def managePost(request):
     posts = PostModel.objects.all();
     context = {
          'title':'Orplant',
          'Posts':posts,
     }

     return render(request,'artikel/manage.html',context)

# detail artikel
def detailPost(request,slugInput):
     posts = PostModel.objects.get(slug=slugInput);
     context = {
          'title':'Orplant',
          'Posts':posts,
     }

     return render(request,'artikel/detail.html',context)

# membuat artikel
def createPost(request):
     post_form = PostForm(request.POST or None)

     if request.method == 'POST': 
          if post_form.is_valid():
               post_form.save()

               return redirect('artikel:allpost')

     context = {
          'title':'Orplant c',
          'page_title':'Membuat Artikel',
          'post_form':post_form,
     }

     return render(request,'artikel/create.html',context)

# menghapus artikel
def deletePost(request, delete_id):
     PostModel.objects.filter(id=delete_id).delete()
     return redirect('artikel:manage')

# edit artikel
def updatePost(request,update_id):
     post_update = PostModel.objects.get(id=update_id)
     
     data = {
          'judul'    : post_update.judul,
          'body'     : post_update.body,
     }
     post_form = PostForm(request.POST or None, initial=data, instance=post_update)

     if request.method == 'POST':
          if post_form.is_valid():
               post_form.save()

          return redirect('artikel:manage')

     context = {
          "page_title":"Update Artikel",
          'post_form':post_form,
     }

     return render(request,'artikel/create.html',context)

