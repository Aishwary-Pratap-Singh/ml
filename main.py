import json
import psycopg2

def get_db_connection():

    conn = psycopg2.connect(
        database="dna1", user='postgres', password='Password@123', host='127.0.0.1', port='54321'
        # database="wap", user='root', password='root', host='10.109.178.43', port='5432'
    )
    return conn




def fetch_feedback():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT feedback_pos FROM pulse_survey')
    response = cur.fetchall()
    cur.close()
    conn.close()
    return response

def create_string():
    feedback = fetch_feedback()

    feedback_list = list(map(lambda x: x[0], feedback))

    feed = " "
    for feeds in feedback_list :


        if feeds != None :
            feed += " "
            feed +=  feeds
    return feed

import yake
def tag_extractor(text):
    kw_extractor = yake.KeywordExtractor()

    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9 #repetition of words is allowed. [(0.1) -> do not allow]
    numOfKeywords = 40
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size,
                                                dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    print("custom_kw_extractor -> ", custom_kw_extractor)
    keywords = custom_kw_extractor.extract_keywords(text)
    return keywords
    # for kw in keywords:
    #     print(kw)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
def generate_wordcloud(txt) :
    wordcloud = WordCloud().generate(txt)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    data = create_string()
    data = tag_extractor(data)
    wrd = []
    for i in data :
        # wrd[i[0]] = i[1]
        temp = {}
        temp['text'] = i[0]
        temp['value'] = round(i[1]*10000,2)
        wrd.append(temp)
    # print(wrd)
    with open('result.json', 'a') as f :
        json.dump(wrd, f,indent = 4)