from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,DetailView,ListView,CreateView,DeleteView,UpdateView)
from blog_app.models import BlogPost,CommentOnPost
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog_app.forms import BlogPostForm,CommentOnPostForm
from django.urls import reverse_lazy

# Create your views here.


class AboutView(TemplateView):
    template_name = 'blog_app/about.html'

class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    context_object_name = "blogpost_list"

class BlogPostDetailView(DetailView):
    model = BlogPost

    
class BlogPostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = '/blog_app/blogpost_detail.html'
    form_class = BlogPostForm
    model = BlogPost

class BlogPostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = '/blog_app/blopgpost_detail.html'
    form_class = BlogPostForm
    model = BlogPost

class BlogPostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    success_url = reverse_lazy('blogpost_list')

class DraftListView(LoginRequiredMixin,ListView):
    context_object_name = 'blogpost_draft_list'
    login_url = '/login/'
    redirect_field_name = '/blog_app/blogpost_list.html'
    model = BlogPost
    
    template_name = 'blog_app/blogpost_draft.html'

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__isnull = True).order_by('created_date')


@login_required   
def blogpost_publish(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    post.publish()
    return redirect('blog_app:blogpost_detail',pk= pk)


@login_required
def add_comment_to_blogpost(request,pk):
    print('checkpoint 1')

    
    blogpost = get_object_or_404(BlogPost,pk=pk)
    if request.method == "POST":
        print('checkpoint 3')
        form = CommentOnPostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comment_post = blogpost
            comment.save()
            
            return redirect('blog_app:blogpost_detail',pk=blogpost.pk)

    else:
        form = CommentOnPostForm()
        print(type(form))
        print('checkpoint 2')
    
    
    return render(request,'blog_app/comment_form.html',{'form':form,'blogpost':blogpost})
@login_required   
def comment_remover(request,pk):
    comment = get_object_or_404(CommentOnPost,pk=pk)
    blogpost_pk = comment.comment_post.pk
    comment.delete()
    return redirect('blog_app:blogpost_detail',pk= blogpost_pk)




@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(CommentOnPost,pk=pk)
    comment.approve()
    return redirect('blog_app:blogpost_detail',pk=comment.comment_post.pk)


