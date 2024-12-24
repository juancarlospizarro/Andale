CREATE DATABASE IF NOT EXISTS andalé;
USE andalé;

CREATE TABLE IF NOT EXISTS curiosidades(
	id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(255) NOT NULL
);

INSERT INTO curiosidades (texto) VALUES ("Andalucía es reconocida mundialmente como la cuna del flamenco, una de las expresiones culturales más importantes de España."), 
("La Alhambra de Granada, un majestuoso palacio y fortaleza de la época musulmana, es uno de los monumentos más visitados de Europa."), 
("Andalucía produce más aceite de oliva que cualquier otra región del planeta. Los extensos olivares de Jaén y Córdoba son responsables de casi el 20% de la producción mundial."),
("Andalucía es una de las pocas regiones en Europa donde puedes disfrutar de playas paradisíacas, desiertos como el de Tabernas (Almería), y montañas nevadas en Sierra Nevada, todo en un mismo día."),
("El 28 de febrero se celebra el Día de Andalucía, conmemorando el referéndum de 1980 en el que se aprobó la autonomía de la región."
);

UPDATE curiosidades
SET texto = "Andalucía es una de las pocas regiones en Europa donde puedes disfrutar de playas paradisíacas y montañas nevadas todo en un mismo día."
WHERE id = 4;
