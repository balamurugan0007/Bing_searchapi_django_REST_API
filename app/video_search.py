from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import search_serializer
from bs4 import BeautifulSoup
import requests


@api_view(['POST'])
def video(request):
    image_search=search_serializer(data=request.data)
    if image_search.is_valid():
        quary=image_search.validated_data['find']
        video_json_result=[]
        
        
        def videos(quary):
            base_url="https://www.bing.com/images/search"
            params={'q':quary}
            headers={"user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
            
            response=requests.get(base_url,params=params,headers=headers)
            soup=BeautifulSoup(response.content,'html.parser')
            vid=soup.find_all("div",class_="dg_u")
            vid_ref=soup.find_all("li",class_='item col')
    
    
    #==================videoes searches============================
            for video in vid :
                vid_link=video.find('div',class_='mc_vtvc_con_rc')['ourl']
                title=video.find('strong').text
                views=video.find('div',class_='mc_vtvc_meta_row').span.text
                img=video.find('div',class_='rms_iac')
                if img:
                    img_link=img.get('data-src')
                    if img_link:
                        image=img_link
                    else:
                        image="none"
                else:
                    image="none"
        
       
        
      
                video_result={
            "title":title,
            "image":image,
            "views":views,
            "video":vid_link,
            "video_list":1
        }     
                video_json_result.append(video_result)   
    
    
    #=================referance_videous ===================
            for j in vid_ref:
                #link=j.find('a')['href']
                title=j.find('strong').text
        #print(title)
        
                video_ref={
            "ref_title":title,
            #"link":link
        }
                
        
        
        
    
        videos(quary)

        return Response(video_json_result)
    return Response('Try another one ....!')