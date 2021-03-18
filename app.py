from flask import Flask,render_template
import pyodbc, requests, json
from flask import request, Response
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def getWords():
   errors = []
   userInput = ''
   if request.method == "POST":
      # get url that the person has entered
      try:
         userInput = request.form['english']
         print("user input", userInput)

      except:
         errors.append(
               "Unable to get URL. Please make sure it's valid and try again."
         )
         return render_template('index.html', errors=errors)
   kanji=''
   hirigana = ''
   englishWord = ''
   response = requests.request("GET", 'https://jisho.org/api/v1/search/words?keyword=' + userInput)
   datas = json.loads(response.text)
   # print("words", datas['data'][0]['japanese'][0])
   if len(datas['data'][0]['japanese'][0]) == 1:
      kanji = 'None'
   else: 
      kanji = datas['data'][0]['japanese'][0]['word']
   hirigana = datas['data'][0]['japanese'][0]['reading']
   englishWord = datas['data'][0]['senses'][0]['english_definitions'][0]
   print(kanji, hirigana, englishWord)

   # for value in datas['data']:
      # print(value['japanese'][0]['word'])
      #   for word in value['japanese'][0]:
      # kanji = value['japanese'][0][0]['word']
   #    print(kanji)
   # return kanji
   return render_template('index.html', kanji=kanji, hirigana=hirigana, englishWord=englishWord)

   # request.form['english']
   # response = requests.request("GET", 'https://jisho.org/api/v1/search/words?keyword=house')
   # print(response)

# if __name__ == '__main__':
app.run()