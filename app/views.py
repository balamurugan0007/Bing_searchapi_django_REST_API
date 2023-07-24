
from bs4 import BeautifulSoup
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import search
from .serializer import search_serializer



@api_view(['POST'])
def searchs(request):
    find=search_serializer(data=request.data)
    print(find) 
    
   
    if find.is_valid():
        query=find.validated_data['find']
        search_response=[]
        
        
        def search(query):
            base_url = 'https://www.bing.com/search'
            params = {'q': query}
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

            response = requests.get(base_url, params=params, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

    # Process the search results
            results = soup.find_all('li', class_='b_algo')

            for result in results:
                title = result.find('h2').text
                url = result.find('a')['href']
                description = result.find('p').text
    
                search_result={
            "title":title,
            "link":url,
            "description":description
        }
        
                search_response.append(search_result)
            
        
        
        search(query)
       
        if search_response=="":
            return Response('sorry your search will not be identifyed.please try another one ')
        return Response(search_response)
        
    
    return Response('invalid search')