import dbms

constDBMS = './../../PycharmProjects/bigpicture_to_sqlite/output_dbms/db_bigpicture.db'
constSQLSelect = 'SELECT a.pubdate, a.seq, a.title, (SELECT COUNT(t.seq) FROM tb_item t WHERE a.seq = t.pseq) cnt_item FROM tb_article a ORDER BY a.pubdate DESC'

constHContentType = "Content-type: text/html;\n\n"
constNewLine = "<BR>"

constBArticle = "<a href=db_item_list.py?seq=%s>%s</a> (%s개)"

def selectArticle():
    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLSelect)

    for item in cur.fetchall():
        print(constBArticle %(item["seq"], item["title"], item["cnt_item"])  , constNewLine, constNewLine)

    return

if __name__ == '__main__':
    print(constHContentType)
    selectArticle()
