/*Created Table*/
CREATE TABLE RocketData (
  Company varchar(200),
  Model varchar(200),
  Height varchar(200),
  EngineNum int,
  EngineName varchar(200),
  Launches int
);

/*Inserted data into table */
INSERT INTO RocketData
VALUES ("SpaceX", "Falcon 9", "70 m", 10, "Merlin", 122) 
VALUES ("SpaceX", "Falcon Heavy", "70 m", 28, "Merlin", 3)
VALUES ("SpaceX", "Starship", "120 m", 35, "Raptor", 0);

