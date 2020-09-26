from flask import Flask, render_template, request
import newsApi
app = Flask(__name__)

@app.route('/')
def index():
    topHeadlinesOfDay = newsApi.topHeadlines()
    print(topHeadlinesOfDay)
    articles = topHeadlinesOfDay["articles"]
    return render_template('index.html', result = articles)


@app.route('/topHeadline')
def topHeadline():
    topHeadlinesOfDay = newsApi.topHeadlines()
    articles = topHeadlinesOfDay["articles"]
    return render_template('index.html', result=articles)

@app.route('/category', methods = ["GET", "POST"])
def category():
    if request.method == 'POST':
        category = request.form.get('news-category').lower()
        topHeadlinesOfDay = newsApi.categoryNews(category)
        articles = topHeadlinesOfDay["articles"]
        return render_template('category.html', result=articles, category=category.upper())
    return render_template('category.html')

if __name__ == '__main__':
    app.run(debug=True)