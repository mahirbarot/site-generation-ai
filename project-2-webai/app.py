from flask import Flask, redirect, url_for, render_template, request, flash
import openai


app = Flask(__name__)
openai.api_key = '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'

@app.route('/',methods=["POST", "GET"])
def index():
    if request.method=='POST':
        code=request.form['code']
        print(code)
        response=openai.Image.create(
        prompt=code,
        n=4,
        size="512x512"
        )
        img_list=[]
        for val in response['data']:
            img_list.append(val['url'])


        response2=openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a tagline for {code}",
        max_tokens=25,
        temperature=0
        )
        tagline=response2['choices'][0]['text']

        response2=openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a name for {code}",
        max_tokens=25,
        temperature=0
        )
        title=response2['choices'][0]['text']

        response2=openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write product description about {code} in less than 50 words",
        max_tokens=90,
        temperature=0
        )
        description=response2['choices'][0]['text']


        return render_template('dummy.html',tagline=tagline,list=img_list,title=title ,description=description)
        
    else:
        return render_template('inputbizz.html')


app.run(debug=True)