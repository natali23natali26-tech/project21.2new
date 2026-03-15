from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/categories')
def categories():
    return render_template('categories.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/contacts')
def contacts():
    # Используем render_template вместо чтения файла
    return render_template('contacts.html')


# Обработка всех остальных GET-запросов — возвращаем страницу "Контакты"
@app.route('/<path>')
def catch_all(_):
    # Также используем render_template
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
