from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from api.models import Todo
from api.serializers import TodoSerializer

# Create your views here.


class TodoViewSet(GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [
        AllowAny
    ]

    @action(methods=['GET'], detail=False, url_path='get-all-todos', url_name='get-all-todos')
    def get_all_todos(self, request: Request, *args, **kwargs):
        try:
            queryset = Todo.objects.all()
            serializer = TodoSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': "details not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(methods=['GET'], detail=True, url_path='get-todo', url_name='get-todo')
    def get_todo_by_id(self, request: Request, *args, **kwargs):
        todo_id = kwargs.get('pk')
        todo = get_object_or_404(Todo, id=todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, url_path='create-todo', url_name='create-todo')
    def create_todo(self, request: Request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['PATCH'], detail=True, url_path='update-todo', url_name='update-todo')
    def update_todo_by_id(self, request: Request, *args, **kwargs):
        todo_id = kwargs.get('pk')
        todo = get_object_or_404(Todo, id=todo_id)
        serializer = TodoSerializer(
            instance=todo,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['DELETE'], detail=True, url_path='delete-todo', url_name='delete-todo')
    def delete_todo_by_id(self, request: Request, *args, **kwargs):
        try:
            todo_id = kwargs.get('pk')
            todo = get_object_or_404(Todo, id=todo_id)
            todo.delete()
            return Response({'message': 'Todo deleted successfully'}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({'message': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)