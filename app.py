from flask import Flask, request, render_template, send_file
import pandas as pd
from io import BytesIO
from scraper import scrape_amazon, scrape_flipkart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search_term']
        min_price = request.form.get('min_price')
        max_price = request.form.get('max_price')
        websites = request.form.getlist('websites')
        products = []
        if 'amazon' in websites:
            products += scrape_amazon(search_term, min_price, max_price)
        if 'flipkart' in websites:
            products += scrape_flipkart(search_term, min_price, max_price)
        return render_template('results.html', products=products, search_term=search_term, min_price=min_price, max_price=max_price, websites=websites)
    return render_template('index.html')

@app.route('/download')
def download():
    search_term = request.args.get('search_term')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    websites = request.args.getlist('websites')
    products = []
    if 'amazon' in websites:
        products += scrape_amazon(search_term, min_price, max_price)
    if 'flipkart' in websites:
        products += scrape_flipkart(search_term, min_price, max_price)
    df = pd.DataFrame(products).rename(columns={'title': 'Product Name', 'price': 'Price (INR)', 'link': 'Link'})
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return send_file(output, download_name='products.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
