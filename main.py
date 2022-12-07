import os
import openai
import json
# import datetime
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

openai.api_key = 'xxxxx'


def get_res(input):
    # print("开始处理: ", input)
    try:
        # openai.log = True
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{input}\n",
            temperature=0.9,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        # print(response)
    except Exception as e:

        print(e)
        return e
    return response["choices"][0].text


@server.route('/chat', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template('chat.html', question="null", res="问题不能为空")
        question = request.form['question']
        print("======================================")
        print("接到请求:", question)
        res = get_res(question)

        return render_template('chat.html', question=question, res=str(res))
    return render_template('chat.html', question=0)


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=80)

