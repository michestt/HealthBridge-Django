from django.urls import path
from .views import home_view, detail_view, tagged, homepage, blog_sport, blog_weight_lost, like, show_my_posts, delete_my_posts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('blog/', home_view, name="post_homepage"),
    path('blog/post/<slug:slug>/', detail_view, name="detail"),
    path('like/<slug:slug>/', like, name='postlike'),
    path('blog/tag/<slug:slug>/', tagged, name="tagged"),
    path('', homepage, name='blog_homepage'),
    path('MyPosts/', show_my_posts, name='blog_show_my_posts'),
    path('DeletePosts/<int:id>/', delete_my_posts, name='blog_delete_my_posts'),
    path('sport', blog_sport, name='blog_sport'),
    path('weight_lost', blog_weight_lost, name='blog_weight_lost'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
