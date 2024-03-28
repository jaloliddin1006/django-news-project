from django.urls import path
from .views import index, detail, category_list, create_article, update_article, delete_article, delete

urlpatterns = [
    path('', index, name='home'),
    path("<int:id>/detail/", detail, name='detail'),
    path("<int:id>/category", category_list, name='category'),
    path("create/", create_article, name='create'),
    path("update/<int:id>/", update_article, name='update'),
    path("delete/<int:id>/", delete_article, name='delete'),
    path("delete-ar/<int:id>/", delete, name='delete-ar'),
]

