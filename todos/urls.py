from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
    # path('todos/', views.get_todos),
    # path('todos/create/', views.create_todo),
    # path('todos/<int:pk>/', views.get_todo),
    # path('todos/<int:pk>/update/', views.update_todo),
    # path('todos/<int:pk>/delete/', views.delete_todo),
# ]
