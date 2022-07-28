from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')

def home():
    return render_template("home.html")

@app.route('/product')

def product():
    return render_template("product.html")

@app.route('/sony')
def pro():
    return render_template("sony.html")

@app.route('/cart')
def prl():
    return render_template("cart.html")
@app.route('/dji')
def prw():
    return render_template("dji.html")


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
