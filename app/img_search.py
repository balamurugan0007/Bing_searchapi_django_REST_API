from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import search_serializer
from bs4 import BeautifulSoup
import requests


@api_view(['POST'])
def img(request):
    image_search=search_serializer(data=request.data)
    if image_search.is_valid():
        quary=image_search.validated_data['find']
        image_json_result=[]


        def images():
    
            url = f"https://www.bing.com/images/search?q={quary}"
            response=requests.get(url)
            soup=BeautifulSoup(response.content,'html.parser')
            imges_result=soup.find_all('div',class_='lnkw')
            ref_image=soup.find_all('li',class_='item')
            
            
            for image in imges_result:
                link=image.find('a')['href']
                title=image.find('a')['title']
        
        
                
        
                image_result={
            "image":link,
            "title":title
        }
                image_json_result.append(image_result)
            
        #====================referance_image================ 
        
            for i in ref_image:
                head=i.find('span').text
                if head=='':
                    continue
        
                ref_img_search={
            'title':head
        }
                image_json_result.append(ref_img_search)
                
        images()
        return Response(image_json_result)
    
    return Response("could't understand your need . Please try another one")