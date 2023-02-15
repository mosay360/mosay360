from django.urls import path
from .views import BlogIndex,  PostDetail,  AddPostView, UpdatePostView,  DeletePostView, AddCategoryView
from .import views

#from .feeds import LatestPostsFeed



app_name= 'blog'

urlpatterns = [
    path('blog', views.BlogIndex, name="blogIndex"),
    
    #path('post/<int:pk>', PostDetail.as_view(), name="postDetail"),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.PostDetail, name="postDetail" ),
    path('<int:post_id>/share/',views.post_share, name='post_share'),
    
    path('add_post/', AddPostView.as_view(), name="add_post"),

    #path('add_category/', AddCategoryView.as_view(), name="add_category"),

    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    
    
    path('post/<int:pk>/remove', DeletePostView.as_view(), name="deletepost"),
    
   # path('category/<str:cats>/', CategoryView, name='category'),
    
   # path('like/<int:pk>', LikeView, name='like_post'),
    path('tag/<slug:tag_slug>/' ,views.BlogIndex, name='blogIndex_by_tag'),

    #path('feed/', LatestPostsFeed(), name='post_feed'),
    
    path('search/',views.postSearch, name='search'),
    

]
