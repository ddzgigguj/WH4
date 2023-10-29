from django.urls import path
from . import views

urlpatterns = [
    path('comix_list/', views.mangaListView, name='comixList'),
    path('comix_detail/<int:id>/', views.mangaDetailView, name='detail'),
    path('manga_detail/<int:id>/delete/',
         views.deleteMangaView, name='delete'),
    path('comix_detail/<int:id>/update/',
         views.updateMangaView, name='update'),
    path('/create_comix/', views.createComixView, name='createComix')
]

