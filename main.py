import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

#pip install nltk
#pip install textblob
#pip install newspaper3k
def summarize():

    url = urltext.get('1.0',"end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    
    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

root  = tk.Tk()
root.title("News Article Summarizer")
root.geometry('1200x600')

ulabel = tk.Label(root, text="URL")
ulabel.pack()
urltext = tk.Text(root, height=1, width=140)
urltext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

tlabel = tk.Label(root, text="Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Published Date")
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()
summary = tk.Text(root, height=20, width=150)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

root.mainloop()
