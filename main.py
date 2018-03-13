from flask import Flask, flash, redirect, render_template, request, session, url_for
from get_news import lookup
from Sentiment import sentiment
from Twitter import tweet
app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('homepage.html')

@app.route('/politics')
def politics():
    news=lookup('politics')
    output=list()
    for ne in news:
        t_reviews=tweet(ne['title'])#t_reviews is a list of tweets
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url']=ne['url']
        out['reviews']=list()
        for rev in t_reviews:
            sent=sentiment(rev)
            if sent[0]["sentiment"] != 0:
                sen=dict()
                sen['tweet']=rev
                sen['sentiment']=sent[0]['sentiment']
                out['reviews'].append(sen)
        output.append(out)
    return render_template('news.html',output=output,topic='politics')

@app.route('/sports')
def sports():
    news=lookup('sports')
    output=list()
    for ne in news:
        t_reviews=tweet(ne['title'])#t_reviews is a list of tweets
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url']=ne['url']
        out['reviews']=list()
        for rev in t_reviews:
            sent=sentiment(rev)
            if sent[0]["sentiment"] != 0:
                sen=dict()
                sen['tweet']=rev
                sen['sentiment']=sent[0]['sentiment']
                out['reviews'].append(sen)
        output.append(out)
    return render_template('news.html',output=output,topic='sports')

@app.route('/entertainment')
def entertainment():
    news=lookup('entertainment')
    output=list()
    for ne in news:
        t_reviews=tweet(ne['title'])#t_reviews is a list of tweets
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url']=ne['url']
        out['reviews']=list()
        for rev in t_reviews:
            sent=sentiment(rev)
            if sent[0]["sentiment"] != 0:
                sen=dict()
                sen['tweet']=rev
                sen['sentiment']=sent[0]['sentiment']
                out['reviews'].append(sen)
        output.append(out)
    return render_template('news.html',output=output,topic='entertainment')

@app.route('/technology')
def technology():
    news=lookup('technology')
    output=list()
    for ne in news:
        t_reviews=tweet(ne['title'])#t_reviews is a list of tweets
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url']=ne['url']
        out['reviews']=list()
        for rev in t_reviews:
            sent=sentiment(rev)
            if sent[0]["sentiment"] != 0:
                sen=dict()
                sen['tweet']=rev
                sen['sentiment']=sent[0]['sentiment']
                out['reviews'].append(sen)
        output.append(out)
    return render_template('news.html',output=output,topic='Tech')

if __name__ == '__main__':
  app.run()
