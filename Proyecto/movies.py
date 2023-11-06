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

# Funciones para buscar o en su defecto insertar
def findOrInsert(table, name):
    cursor.execute("select id from "+table+" where nombre = %s limit 1", [name])
    r = cursor.fetchone()
    if(r):
        return r[0]
    else:
        cursor.execute("insert into "+table+" (nombre) values (%s) returning id", [name])
        return cursor.fetchone()[0]

def findOrInsertPelicula(table, id, title, imdb, rt, anho, edad, duracion):
    cursor.execute("select * from "+table+" where id = %s limit 1", [id])
    r = cursor.fetchone()
    if(r):
        return r[0]
    else:
        cursor.execute("insert into "+table+" (titulo, imdb, rottentomatoes, anho, edad, duracion) values (%s, %s, %s, %s, %s, %s) returning id", [title,imdb,rt,anho,edad,duracion])
        return cursor.fetchone()[0]

def findOrInsertRelacion(table,atributo,atributo_id,pelicula_id):
    cursor.execute("select * from "+table+" where id_"+atributo+" = %s and id_pelicula = %s limit 1", [atributo_id,pelicula_id])
    r = cursor.fetchone()
    if(r):
        return r[0]
    else:
        cursor.execute("insert into "+table+" (id_"+atributo+",id_pelicula) values (%s, %s) returning id_"+atributo+", id_pelicula", [atributo_id,pelicula_id])
        return cursor.fetchone()[0]

# Lectura del csv
with open("MoviesOnStreamingPlatforms_updated.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            platforms = row[6:10]
            continue

        # Atributos de pelicula
        id = row[0]
        title = row[1]
        year = row[2]
        if row[3]!= "all" and row[3]:
            age = int(row[3].split('+')[0]) 
        elif row[3]=="all":
            age = 0 
        else:
            age = None
        imdb = row[4] if row[4] else None
        rt = int(row[5].split('%')[0])/10 if row[5] else None
        runtime = row[15] if row[15] else None

        # Inserción de las películas
        findOrInsertPelicula('pelicula', id, title, imdb, rt, year, age, runtime)

        directors = row[11].split(',')

        # Inserción de los directores y en la tabla dirige
        for director in directors:
            if director != '':
                director_id = findOrInsert('director',director)
                findOrInsertRelacion('dirige','director',director_id,id)

        genres = row[12].split(',')
        
        # Inserción de los géneros
        for genre in genres:
            if genre != '':
                genero_id = findOrInsert('genero',genre)
                findOrInsertRelacion('es_de','genero',genero_id,id)
        
        countries = row[13].split(',')
        
        # Inserción de los países y en la tabla origen
        for country in countries:
            if country != '':
                country_id = findOrInsert('pais',country)
                findOrInsertRelacion('origen','pais',country_id,id)

        languages = row[14].split(',')

        # Inserción de los idiomas y en la tabla disponible
        for language in languages:
            if language != '':
                language_id = findOrInsert('idioma',language)
                findOrInsertRelacion('disponible','idioma',language_id,id)

        # Inserción de las plataformas y en la tabla esta_en
        for platform in platforms:
             platform_id = findOrInsert('plataforma',platform)
             is_on = int(round(float(row[platform_id+5])))
             if(is_on):
                findOrInsertRelacion('esta_en','plataforma',platform_id,id)

conn.commit()

conn.close()
