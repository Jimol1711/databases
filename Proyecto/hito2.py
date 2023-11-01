import psycopg2
import psycopg2.extras
import csv

try:
    conn = psycopg2.connect (host ="localhost",
                             database ="proyecto_cc3201",
                             user ="postgres",
                             password ="0123456789", 
                             port ="5432")
    
    cursor = conn.cursor()
except:
    print("No connection")

with open("MoviesOnStreamingPlatforms_updated.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            continue
        id = row[0]
        title = row[1]
        year = row[2]
        age = None
        if row[3]!= "all" and row[3]:
            age = int(row[3].split('+')[0]) 
        elif row[3]=="all":
            age = 0 
        else:
            age = None
        IMDb = row[4] if row[4] else None
        RT = int(row[5].split('%')[0])/100 if row[5] else None
        runtime = row[15] if row[15] else None

def findOrInsert(table, name):
    cursor.execute("select id from "+table+" where name=%s limit1", [name])
    r = cursor.fetchone()
    if(r):
        return r[0]
    else:
        cursor.execute("insert into "+table+" (name) values (%s) returning id", [name])
    return cursor.fetchone()[0]

conn.commit()

conn.close()
