import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

#pip install nltk
#pip install textblob
#pip install newspaper3k

url = 'https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')


analysis = TextBlob(article.text)

print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "Neutral"}')

root  = tk.Tk()
root.title("News Article Summarizer")
root.geometry('1200x600')

tlabel = tk.label(root, text="Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.label(root, text="Author")
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.label(root, text="Published Date")
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

plabel = tk.label(root, text="Published Date")
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()



root.mainloop()




