from flask import *

vro = Flask(__name__)


@vro.route('/')
def shop():
    return render_template('shoppinglist.html')


@vro.route('/kart', methods=['POST'])
def login():
    item = request.form['name']
    ID = request.form['id']
    quantity = request.form['quantity']
    price = request.form['price']
    data = []
    data.append((item, ID, quantity, price))

    return render_template('List.html', data=data)


if __name__ == '__main__':
    vro.run(debug=True)
