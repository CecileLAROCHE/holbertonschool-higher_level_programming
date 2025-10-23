# python-object_relational_mapping

0. Get all states
1. Filter states
2. Filter states by user input
3. SQL Injection...
4. Cities by states
5. All cities by state
6. First state model
7. All states via SQLAlchemy
8. First state
9. Contains `a`
10. Get a state
11. Add a new state
12. Update a state
13. Delete states
14. Cities in state

## Install MySQL 8.0 on Ubuntu 20.04 LTS

`mysql --version`
→ mysql  Ver 8.0.43-0ubuntu0.24.04.2 for Linux on x86_64 ((Ubuntu))

`sudo mysql`
[sudo] Mot de passe de cecile : MOT DE PASSE SUDO

## Install MySQLdb module version 2.0.x

`sudo apt-get install python3-dev`
`sudo apt-get install libmysqlclient-dev`
`sudo apt-get install zlib1g-dev`

    --> Créer un environnement virtuel
    `python3 -m venv venv`
    `source venv/bin/activate`

`pip install mysqlclient==2.0.3`
`pip install SQLAlchemy==1.4.22`

--> creation utilisateur
`sudo mysql`
dans mysql création un utilisateur MySQL avec mot de passe (recommandé pour ton script Python)
`CREATE USER 'CLA'@'localhost' IDENTIFIED BY 'CLA';
GRANT ALL PRIVILEGES ON *.* TO 'CLA'@'localhost';
FLUSH PRIVILEGES;`
