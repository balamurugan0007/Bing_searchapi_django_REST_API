
from bs4 import BeautifulSoup
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import search
from .serializer import search_serializer



@api_view(['post'])
def searchs(request):
    find=search_serializer(data=request.data) 
    
   
    if find.is_valid():
        search_quary=find.validated_data['find']
        search_response=[]
        
        
        def search():
            url = f"https://www.bing.com/search?q={search_quary}"
            response=requests.get(url)
            soup=BeautifulSoup(response.text,"html.parser")
            result=soup.find_all('li', class_='b_algo')
            for results in result:
                title = results.find('h2').text
                link = results.find('a')['href']
    
    
    #des=results.find('div',class_='Z26q7c UK95Uc')
                description = results.find("p").text
    
                search_result={
            "title":title,
            "link":link,
            "description":description
        }
        
                search_response.append(search_result)
            
        
        
        search()
       
        if search_response=="":
            return Response('sorry your search will not be identifyed.please try another one ')
        return Response(search_response)
        
    
    return Response('invalid search')