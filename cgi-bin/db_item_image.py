import dbms
import cgi
import os
import sys
import base64

constDBMS = './../../PycharmProjects/bigpicture_to_sqlite/output_dbms/db_bigpicture.db'
constSQLSelect = 'SELECT textdata, rawdata FROM tb_item WHERE seq = ?'

constHContentType = "Content-type: text/html;\n\n"
constNewLine = "<BR>"

def selectItem():
    #Get Parameter
    arguments = cgi.FieldStorage()

    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLSelect, (arguments["seq"].value, ))

    for item in cur.fetchall():
        data_uri = base64.b64encode(item["rawdata"]).decode()
        img_tag = '<img src="data:image/jpeg;base64,{0}" height=90%% alt="" />'.format(data_uri)
        print(img_tag)
        print(constNewLine)
        print(item["textdata"])

    return


if __name__ == '__main__':
    print(constHContentType)
    print("<meta charset=utf-8>")
    selectItem()
