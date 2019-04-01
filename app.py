from flask import Flask,jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'Store',
        'items':[

                {
                    'name':'My Item',
                    'price':15.99

                }
                
                 ]
    }

    ]

@app.route('/')
def home():
    return 'hello world'


@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    return 'stores'

@app.route('/store/<string:name>/item',method=['POST'])
def create_item():
    pass

@app.route('/store/<string:name>/item')
def get_item():
    pass
           

app.run(port=5000)
