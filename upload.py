import sqlite3

fhand = open('xxx.txt')
int = 12983



conn = sqlite3.connect('db1.db')
cur = conn.cursor()

for line in fhand:
    if '1VI' in line:

        x=line.split()

        USN = x[1]
        ST = x[2:]
        NAME = " "
        for ele in ST:
            NAME +=" "+ele


        print(NAME)



        cur.execute('''INSERT INTO studentdetail (usn , name, code ) VALUES ( ? , ? , ?)''',
                (USN , NAME , int))
        int = int + 82


conn.commit()


cur.close()
