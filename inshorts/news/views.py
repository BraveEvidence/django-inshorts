from inshorts.news.models import News
from inshorts.news.serializers import NewsSerializer
from rest_framework import generics,status
from rest_framework.response import Response

class NewsList(generics.ListCreateAPIView):
    def get(self,request,format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news,many=True)
        return Response({"status":1,"msg":"Success","body":serializer.data})

    def post(self,request,format=None):
        print(request.data)
        print("0")
        serializer = NewsSerializer(data=request.data)
        print("1")
        # print(serializer)
        # print(serializer.error)
        print(serializer.is_valid())
        print(serializer.errors)
        # print(serializer.data)
        if serializer.is_valid():
            print("2")
            serializer.save()
            print("3")
            return Response({"status":1,"msg":"Success","body":serializer.data})
        else:
            return Response({"status":0})
        

