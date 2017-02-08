CREATE TABLE Child (
	idChild INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL,
	Happy INTEGER NOT NULL
);

CREATE TABLE Toy (
	idToy INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL,
	idChild INTEGER NOT NULL,
	FOREIGN KEY (idChild) REFERENCES idChild(idChild)
);

