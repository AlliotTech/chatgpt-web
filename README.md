``` 
pip install --upgrade openai  
pip install flask  
``` 

run:   
```
gunicorn -w 4  -b 127.0.0.1:80 main:server --timeout 200  --worker-class gevent
```  
url: localhost:80/chat 

### 国区朋友体验   

可以微信公众号搜索 AlliotTech   
发送 “客服“ 二字就可以直接在微信公众号免费体验 ChatGPT 了。   
