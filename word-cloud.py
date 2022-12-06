# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("book1.csv")

df.head()

comment_words = ''
stopwords = set(STOPWORDS)

for x in df.AUTHOR:
    # typecaste each x to string
    x = str(x)

    # split the value
    token = x.split()

    # convert each token into lowercase
    for i in range(len(token)):
        token[i] = token[i].lower()

    comment_words = comment_words + " ".join(token) + " "
print(comment_words)

# Word Clould Lib
wordcloud = WordCloud(width=800, height=800, background_color = "white", stopwords = stopwords,\
                     min_font_size = 10).generate(comment_words)

# Plot the WordCloud Img
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

# plt.show()
plt.savefig('foo.png')
