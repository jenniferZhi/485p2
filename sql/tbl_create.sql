
CREATE TABLE User (
    username  VARCHAR(20),
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    password VARCHAR(256) NOT NULL,
    email VARCHAR(40),
    PRIMARY KEY (username)) ENGINE=INNODB;

CREATE TABLE Album (
    albumid INTEGER NOT NULL AUTO_INCREMENT,
    title VARCHAR(50),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastupdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    username VARCHAR(20),
    access VARCHAR(10),
    CHECK (access='private' or access='public'),
    PRIMARY KEY (albumid),
    FOREIGN KEY (username) REFERENCES User (username) 
    ON DELETE CASCADE
    ON UPDATE CASCADE) ENGINE=INNODB;

CREATE TABLE Photo (
    picid   VARCHAR(40),
    format  VARCHAR(3),
    date    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (format = 'JPG' or format = 'GIF' or format = 'PNG'),
    PRIMARY KEY (picid)) ENGINE=INNODB;

CREATE TABLE Contain (
    sequencenum INTEGER,
    albumid INTEGER,
    picid   VARCHAR(40),
    caption VARCHAR(255),
    PRIMARY KEY (sequencenum),
    FOREIGN KEY (albumid) REFERENCES Album (albumid) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (picid) REFERENCES Photo (picid) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=INNODB;

CREATE TABLE AlbumAccess(
     albumid INTEGER,
     username VARCHAR(20),
     PRIMARY KEY(albumid,username),
     FOREIGN KEY (albumid)  REFERENCES Album(albumid) ON DELETE CASCADE ON UPDATE CASCADE,
     FOREIGN KEY (username) REFERENCES User(username) ON DELETE CASCADE ON UPDATE CASCADE ) ENGINE=INNODB;

