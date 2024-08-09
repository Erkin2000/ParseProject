from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .api import request_get
from .models import Data
from .serializers import DataSerializer, CreateSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(responses=DataSerializer(many=True))
class GetFromUrl(APIView):

    def get(self, request):
        response = request_get()
        saved_articles = []
        try:
            for article in response['articles'][:10]:
                data_instance = Data.objects.create(
                    author=article.get('author'),
                    title=article.get('title'),
                    description=article.get('description'),
                    url=article.get('url'),
                    publishedAt=article.get('publishedAt'),
                    content=article.get('content')
                )
                saved_articles.append(data_instance)
            serialized_data = DataSerializer(saved_articles, many=True).data

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serialized_data)


@extend_schema(responses=DataSerializer(many=True))
class GetAll(APIView):
    def get(self, request):
        getAll = Data.objects.all()
        serialized_data = DataSerializer(getAll, many=True).data
        return Response(serialized_data)


@extend_schema(responses=DataSerializer(many=True))
class GetById(APIView):
    def get(self, request, pk):
        try:
            data_instance = Data.objects.get(pk=pk)
        except Data.DoesNotExist:
            return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        serialized_data = DataSerializer(data_instance).data
        return Response(serialized_data)


@extend_schema(request=CreateSerializer, responses=CreateSerializer)
class CreateData(APIView):
    def post(self, request):
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=DataSerializer, responses=DataSerializer)
class UpdateId(generics.UpdateAPIView):
    def put(self, request, pk):
        try:
            news = Data.objects.get(pk=pk)
        except Data.DoesNotExist:
            return Response({"error": "News not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DataSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(responses=DataSerializer(many=True))
class DeleteId(APIView):
    def delete(self, request, pk):
        try:
            news = Data.objects.get(pk=pk)
        except Data.DoesNotExist:
            return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        news.delete()
        return Response({"message": "Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)