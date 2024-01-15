import pandas as pd
from janome.tokenizer import Tokenizer
import collections
from wordcloud import WordCloud

df = pd.read_csv('/Users/Ken/Downloads/placenta_kuchikomi.csv', encoding="utf_8_sig", index_col=0)
t = Tokenizer()


words_list=[]
for review in df['Review']:
    words = []
    for token in t.tokenize(review):
        if (token.part_of_speech.split(',')[0] == '名詞')&(token.part_of_speech.split(',')[1] in ['一般','固有名詞','サ変接続','形容動詞語幹']):
            words.append(token.surface)
    words_list.append(words)

df['名詞'] = words_list


all_words = []
for words in df['名詞']:
    all_words.extend(words)
print(df.head())

wordcloud_book1 = WordCloud(font_path="/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",background_color = 'white', width=400, height=400, random_state=1).generate(' '.join(all_words))
wordcloud_book1.to_file('/Users/Ken/Downloads/placenta_kuchikomi.png')
