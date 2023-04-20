from flask import Flask , render_template


app = Flask(__name__)


@app.route('/')
def Home_Page():
    return render_template('Home.html')

@app.route('/shop')
def Shop_Page():
    return render_template('Shop.html')

@app.route('/detail')
def Detail_Page():
    return render_template('Detail.html')

@app.route('/cart')
def ShoppingCart():
    return render_template('Cart.html')

@app.route('/checkout')
def CheckOut():
    return render_template('Checkout.html')

@app.route('/contact')
def Contact():
    return render_template('Contact.html')