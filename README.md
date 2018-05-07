# apitest

Code for the technical round.

**Assumptions made**
1. System already has the following installed:
    * PostgreSQL (local development used latest for testing - Postgres 10)
    * Python (3.6.x preferred)
2. Database will be created by the superuser,
hence the program does not include any scripts for creating the db.
The database to be used can be specified by DATABASE_URL environment variable.

**Online Resources Used**
* https://stackoverflow.com/questions/37245931/how-to-map-a-postgres-earth-column-in-sqlalchemy
* Other quick google searches for small things, all major stuff,
from which code might have directly been taken, has been mentioned in the above points.

## Documentation

### Stack / Technologies used

1. Flask-Restful (on top of Flask)
2. PostgreSQL (Handled by the ORM SQLAlchemy)
3. bah bah black sheep magic
