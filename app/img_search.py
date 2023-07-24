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
            base_url="https://www.bing.com/images/search"
            params={'q':quary}
            headers={"user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
            
            response=requests.get(base_url,params=params,headers=headers)
            soup=BeautifulSoup(response.content,'html.parser')
            imges_result=soup.find_all('div',class_='imgpt')
            ref_image=soup.find_all('li',class_='item')
            
            
            for image in imges_result:
                images_link=image.find('img',class_="mimg")
                if image:
                    src=images_link.get('src')
                    if src:
                        b=src
                    else:
                        continue
                else:
                    continue
                a=image.find('a')['href']
        
       
               
        
        
                
        
                image_result={
            "image":b,
            "images_list":1
           
        }
                image_json_result.append(image_result)
            
        #====================referance_image================ 
        
            for i in ref_image:
                head=i.find('span').text
                if head=='':
                    continue
        
                ref_img_search={
            'ref_title':head
        }
               
                
        images()
        return Response(image_json_result)
    
    return Response("could't understand your need . Please try another one")