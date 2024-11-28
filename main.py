#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord = button_discord, button_html = button_html, button_db = button_db)

@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    text = request.form['text']
    
    email = request.form['email']
    


    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                            #Помести переменные
                            text=text,
                            email = email,
                            )


if __name__ == "__main__":
    app.run(debug=True)