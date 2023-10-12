from django.urls import path


from .views import PostsList, PostDetail, SearchPosts, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60*1)(PostsList.as_view()), name='posts_list'),  #список постов
    path('<int:pk>/', cache_page(60*5)(PostDetail.as_view()), name='news_detail'),  #вывод одного поста
    path('search/', SearchPosts.as_view(), name='search_posts'),#страница фильтрации
    path('add/', PostCreate.as_view(), name='news_create'),# форма создания поста
    path('<int:pk>/', PostDetail.as_view(), name='news_edit'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),

    path('categories/<int:pk',CategoryListView.as_view(), name='category_list'),
    path('catigories/<int:pk>/subscribe', subscribe, name='subscribe'),
]