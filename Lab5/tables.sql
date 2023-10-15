CREATE TABLE vaj_Relation(
	id serial primary key,
	name varchar(255) not null
);


CREATE TABLE vaj_Character(
	id serial primary key,
	name varchar(255) not null
);


CREATE TABLE vaj_WorkOcupation(
	id serial primary key,
	name varchar(255) not null
);


CREATE TABLE vaj_Alterego(
	id serial primary key,
	name varchar(255) not null
);


CREATE TABLE vaj_Superheroe(
	character_id bigint not null,
	primary key (character_id),
	foreign key (character_id) references character(id),
	name varchar(255) not null,
	intelligence integer not null,
	strength integer not null,
	speed integer not null
);


CREATE TABLE vaj_Relation_Character_Superheroe(
	relation_id bigint not null,
	character_id bigint not null,
	superheroe_id bigint not null,
	primary key (relation_id, character_id, superheroe_id),
	foreign key (relation_id) references vaj_Relation(id),
	foreign key (character_id) references vaj_Character(id),
	foreign key (superheroe_id) references vaj_Superheroe(character_id)
); 


CREATE TABLE vaj_Superheroe_WorkOcupation(
	workocupation_id bigint not null,
	superheroe_id bigint not null,
	primary key (workocupation_id, superheroe_id),
	foreign key (workocupation_id) references vaj_WorkOcupation(id),
	foreign key (superheroe_id) references vaj_Superheroe(character_id)
);


CREATE TABLE vaj_Superheroe_Alterego(
	alterego_id bigint not null,
	superheroe_id bigint not null,
	primary key (alterego_id, superheroe_id),
	foreign key (alterego_id) references vaj_Alterego(id),
	foreign key (superheroe_id) references vaj_Superheroe(character_id)
);


CREATE TABLE vaj_Superheroe_Character(
	character_id bigint not null,
	superheroe_id bigint not null,
	primary key (character_id, superheroe_id),
	foreign key (character_id) references vaj_Character(id),
	foreign key (superheroe_id) references vaj_Superheroe(character_id)
);





