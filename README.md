pip install --upgrade openai
pip install flask

gunicorn -w 4  -b 127.0.0.1:80 main:server --timeout 200  --worker-class gevent
