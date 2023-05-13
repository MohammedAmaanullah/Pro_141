from flask import Flask, jsonify, request

app = Flask(__name__)
all_article = []

@app.route("/get-article",encoding="utf-8")
def get_article():
    article_data = {
        "title": all_article[0][19],
        "poster_link": all_article[0][27],
        "release_date": all_article[0][13] or "N/A",
        "duration": all_article[0][15],
        "rating": all_article[0][20],
        "overview": all_article[0][9]
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"],encoding="utf-8")
def liked_article():
    liked_articles = []
    article = all_article[0]
    liked_articles.append(article)
    all_article.pop(0)
    return jsonify({
        "status": "success"
    }), 200

@app.route("/unliked-article" ,methods=["POST"],encoding="utf-8")
def unliked_article():
    not_liked_articles = []
    article = all_article[0]
    not_liked_articles.append(article)
    all_article.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch-article" ,methods=["POST"],encoding="utf-8")
def did_not_watch_view():
    did_not_watch_article = []
    article = all_article[0]
    did_not_watch_article.append(article)
    all_article.pop(0)
    return jsonify({
        "status": "success"
    }), 200