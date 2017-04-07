import dbms
import cgi

constDBMS = './../../PycharmProjects/bigpicture_to_sqlite/output_dbms/db_bigpicture.db'
constSQLSelect = 'SELECT seq, textdata FROM tb_item WHERE pseq = ? ORDER BY seq ASC'

constHContentType = "Content-type: text/html;\n\n"
constNewLine = "<BR>"

constBItem = "<a href=db_item_image.py?seq=%s>%s</a>"


def selectItem():
    #Get Parameter
    arguments = cgi.FieldStorage()

    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLSelect, (arguments["seq"].value, ))

    for item in cur.fetchall():
        print(constBItem %(item["seq"], item["textdata"])  , constNewLine, constNewLine)

    return


if __name__ == '__main__':
    print(constHContentType)
    selectItem()
