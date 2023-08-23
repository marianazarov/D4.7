from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import AddPostForm

from .models import Post


class PostsList(ListView):
    """ Представление всех постов в виде списка. """
    model = Post
    ordering = 'dateCreation'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'
    paginate_by = 3


class PostDetail(DetailView):
    """ Представление отдельного поста. """
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'


class SearchPosts(ListView):
    """ Представление всех постов в виде списка. """
    paginate_by = 3
    model = Post
    ordering = 'dateCreation'
    template_name = 'flatpages/search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """ Переопределяем функцию получения списка статей. """
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs) -> dict:
        """ Метод get_context_data позволяет изменить набор данных, который будет передан в шаблон. """
        context = super().get_context_data(**kwargs)
        context['search_filter'] = self.filterset
        return context

class PostCreate( LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_post',)
    form_class = AddPostForm
    model = Post
    raise_exception = True
    template_name = 'flatpages/news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'NW'
        post.author = self.request.user.author
        post.save()
        return super().form_valid(form)




class PostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_post',)
    form_class = AddPostForm
    model = Post
    template_name = 'flatpages/news_create.html'


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_post',)
    model = Post
    template_name = 'flatpages/news_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Удалить статью"
        context['previous_page_url'] = reverse_lazy('posts_list')
        return context