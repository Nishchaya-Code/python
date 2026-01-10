from config import HF_API_KEY
import requests
from PTL import Image
import io
import os
from colorama import init,Fore,Style

init(autoreset=True)

#Utiliy function to send api keys
def query_hf_api(api_url,payload=None,files=None,method="post"):
    headers={"Authorization":f"Bearer{HF_API_KEY}"}
    try:
        if method.lower()=="post":
            #when files provided send them along with payload
            response=requests.post(api_url,headers=headers,json=payload,files=files)
        else:
            response= requests.get(api_url,headers=headers,params=payload)
        if response.status_code!=200:
            raise Exception(f'Status{response.status_code}:{response.text}')
        return response.content
    except Exception as e:
        print(f"{Fore.RED} Error while calling api:{e}")
        raise

    #get a basic ca[ption] from image 
def get_basic_caption (image, model='nlpconnect/vit-gpt2-imge-captioning')
        print(f"{Fore.YELLOW}????? Generating basic caption using vit-gpt2-image-captioning...")
        api_url=f"https://api-inference.huggingface.co/models/{model}"
        buffered=io.BytesIO
        #SAVE JPEG
        image.save(buffered, format='JPEG')
        buffered.seek(0)
        header={"Authorization":f"Bearer{HF_API_KEY}"}
        response=requests.post(api_url, headers=headers, data=buffered.read())
        result=response.json()
        if isnstance(result, dict) and 'error' in result:
            return f"[Error {result['error']}]"
            #Expect result to be a list of dicts with 'generated text'
            caption = result[0].get('generated_text','No caption generated')
            return caption

    #Task: generate text using a text generation model
def generate_text (promt,model='gpt-2',max_new_tokens=60):
        print(f"{Fore.CYAN}???? Generating text with promt:{promt}")
        api_url=f'https://api-inference.huggingface.co/model{model}'
        payload= {'inputs':promt,'parameters':{'max_new_tokens':max_new_tokens}}
        text_bytes=query_hf_api(api_url,payload=payload)
        try:
            result=json.loads(text_bytes.decode('utf-8'))
        except Exception as e:
                raise Exception('Failed to decodd text generation response.')
        if isinstance(result,dict) and 'error ' in result:
            raise Exception (result['error'])
        generated= result[0].get('genetated_text','')
        return generated

def truncate_text(text,word_limit):
    words=text.strip().split()
    return " ".join (words [:word_limit])

def print_menu():
    print(f"""""")