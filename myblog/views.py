from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView,CreateView, UpdateView , DeleteView
from .models import Post, Profile
from .forms import PostForm,EditPostForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

def LikeView(request,pk):
    post = get_object_or_404(Post,id = request.POST.get('post_id'))
    liked=False
    if (post.likes.filter(id=request.user.id).exists()):
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('detail-view',args=[str(pk)]))




class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
    

class ArticalDetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'

    def get_context_data(self, *args, **kwargs):
        liked=False
        context = super(ArticalDetailView,self).get_context_data( *args, **kwargs)
        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        if (stuff.likes.filter(id=self.request.user.id).exists()):
            liked=True
        total_likes= stuff.total_likes()
        context['total_likes']=total_likes
        context['liked']=liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model =Post
    form_class = EditPostForm
    template_name = 'update_post.html'
    #fields ='__all__'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url=reverse_lazy('home')


# class ProfileView(CreateView):
#     model = Profile
#     form_class = ProfileForm
#     template_name = 'profile.html'




    
