# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import psycopg2

from sqlalchemy import create_engine
def connection(data):
    import sqlalchemy as sa

    db_name = "survey"
    db_user = "postgres"
    db_pwd = "Password@123"
    db_host = "localhost"
    db_client = "postgresql"

    connection_url = sa.engine.URL.create(
        drivername=db_client,
        username=db_user,
        password=db_pwd,
        host=db_host,
        database=db_name
    )
    conn_string = 'postgresql://postgres:Password@123@localhost:5432/survey'

    db = create_engine(connection_url)
    conn = db.connect()

    df = pd.DataFrame(data)
    df.to_sql('data', con=conn, if_exists='replace',
              index=False)

    # fetch data from postgres
    conn = psycopg2.connect(
        database="survey", user='postgres', password='Password@123', host='127.0.0.1', port='5432'
    )

    # conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    cursor = conn.cursor()

    sql1 = '''select * from data;'''
    cursor.execute(sql1)
    # for i in cursor.fetchall():
    #     print(i)

    df = pd.read_sql_query('select * from "data"', con=conn)
    print(df)

    # conn.commit()
    conn.close()
    return df



import pandas as pd
def importData():


    df = pd.read_excel(r'java.xlsx')
    rdf = df[["ID", 'can say few words what went well in java Track?',
       'can you few words about your mentor and track lead ?',
       'How easy was your assignment?']]

    # print(rdf)

    return rdf


import matplotlib.pyplot as plt
from wordcloud import WordCloud
def createWordCloud(df):

    txt = " ".join(word.lower() for word in data["can say few words what went well in java Track?"])
    print("txt -> ", txt)
    wordcloud = WordCloud().generate(txt)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = importData()
    # print(data)
    df = connection(data)
    createWordCloud(df)


