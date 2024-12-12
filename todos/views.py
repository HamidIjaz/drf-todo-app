from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from .models import Todo
from .serializers import TodoSerializer




class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def get_queryset(self):
        """
        Restrict the queryset to todos created by the current user.
        """
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically associate the current user with the todo being created.
        """
        serializer.save(user=self.request.user)




# # List all todos
# @api_view(['GET'])
# def get_todos(request):
#     todos = Todo.objects.all()
#     serializer = TodoSerializer(todos, many=True)
#     return Response(serializer.data)

# # Create a new todo
# @api_view(['POST'])
# def create_todo(request):
#     serializer = TodoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Get a specific todo
# @api_view(['GET'])
# def get_todo(request, pk):
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = TodoSerializer(todo)
#     return Response(serializer.data)

# # Update a specific todo
# @api_view(['PUT'])
# def update_todo(request, pk):
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = TodoSerializer(todo, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Delete a specific todo
# @api_view(['DELETE'])
# def delete_todo(request, pk):
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     todo.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

