import sqlite3


fileList = ['information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']
comList = []

def createTBL():
    conn = sqlite3.connect('fileDB.db')

    with conn:
        #cursor to interact with db
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname STRING \
            )")
        conn.commit()
    conn.close()



def findTXT():
    for file in fileList:
        if file.endswith(".txt"):
            comList.append(file)
            

def insert():
    conn = sqlite3.connect('fileDB.db')

    with conn:
        #cursor to interact with db
        cur = conn.cursor()
        for file in comList:
            cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)",(file,))
        conn.commit()
    conn.close()


def grabPrint():
    conn = sqlite3.connect('fileDB.db')

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_fname FROM tbl_files WHERE col_fname LIKE '%.txt'")
        varFile = cur.fetchall()
        for item in varFile:
            msg = "File Name: {}\n".format(item)
            print(msg)
    conn.close()



if __name__ == "__main__":
    createTBL()
    findTXT()
    insert()
    grabPrint()
