----TABLAS ATRIBUTOS----

CREATE TABLE director(
	ID SERIAL PRIMARY KEY,
	nombre VARCHAR(255) UNIQUE
);

CREATE TABLE idioma(
	ID SERIAL PRIMARY KEY,
	nombre VARCHAR(255) UNIQUE
);

CREATE TABLE pais(
	ID SERIAL PRIMARY KEY,
	nombre VARCHAR(255) UNIQUE
);

CREATE TABLE genero(
	ID SERIAL PRIMARY KEY,
	nombre VARCHAR(255) UNIQUE
);

CREATE TABLE plataforma(
	ID SERIAL PRIMARY KEY,
	nombre VARCHAR(255) UNIQUE
);

CREATE TABLE pelicula(
	ID SERIAL PRIMARY KEY,
	titulo VARCHAR(255),
	IMDB DECIMAL,
	RottenTomatoes DECIMAL,
	Año SMALLINT NOT NULL,
	edad SMALLINT,
	duracion SMALLINT 
 
);

----TABLAS RELACIONES----

CREATE TABLE dirige(
	ID_director BIGINT NOT NULL,
	ID_pelicula BIGINT NOT NULL,
	PRIMARY KEY (ID_director, ID_pelicula),
	FOREIGN KEY (ID_director) REFERENCES director(ID),
	FOREIGN KEY (ID_pelicula) REFERENCES pelicula(ID)
);

CREATE TABLE disponible(
	ID_idioma BIGINT NOT NULL,
	ID_pelicula BIGINT NOT NULL,
	PRIMARY KEY (ID_idioma, ID_pelicula),
	FOREIGN KEY (ID_idioma) REFERENCES idioma(ID),
	FOREIGN KEY (ID_pelicula) REFERENCES pelicula(ID)
);

CREATE TABLE origen(
	ID_pais BIGINT NOT NULL,
	ID_pelicula BIGINT NOT NULL,
	PRIMARY KEY (ID_pais, ID_pelicula),
	FOREIGN KEY (ID_pais) REFERENCES pais(ID),
	FOREIGN KEY (ID_pelicula) REFERENCES pelicula(ID)
);

CREATE TABLE es_de(
	ID_genero BIGINT NOT NULL,
	ID_pelicula BIGINT NOT NULL,
	PRIMARY KEY (ID_genero, ID_pelicula),
	FOREIGN KEY (ID_genero) REFERENCES genero(ID),
	FOREIGN KEY (ID_pelicula) REFERENCES pelicula(ID)
);

CREATE TABLE esta_en(
	ID_plataforma BIGINT NOT NULL,
	ID_pelicula BIGINT NOT NULL,
	PRIMARY KEY (ID_plataforma, ID_pelicula),
	FOREIGN KEY (ID_plataforma) REFERENCES plataforma(ID),
	FOREIGN KEY (ID_pelicula) REFERENCES pelicula(ID)
);
