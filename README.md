# This project is a school project, the purpose of it was to learn how to manipulate data through an ORM with Python and Flask

# Setup the project

## Step 1

> Docker is required to run the following commands

Run this command to build the docker image: `docker compose build`

## Step 2

> now we need to start the project

Run this command to start the containers: `docker compose up`

> there might be a problem at the first run, because for some reasons web can start before database, if it occurs, run the following command:</br> > `docker compose restart web`

## Step 3

> You should be good to go, now we will see the diffrents routes and their required body/params to run correctly

> It is recommended to use Postman or any alternative

> Here are the different routes:

> ROOMS:

- `/api/chambres`-`[POST]`- body:`{
    "type":"",
    "prix": ,
    "numero":
}`

- `/api/chambres/<id>`-`[PUT]`- body:`{
    "type":"",
    "prix": ,
    "numero":
}`

- `/api/chambres/<id>`-`[DELETE]`

> CLIENTS:

- `/api/client`-`[POST]`- body:`{
    "nom":"",
    "email":""
}`

> RESERVATIONS:

- `/api/reservations`-`[POST]`- body:`{
    "id_client": ,
    "id_chambre": ,
    "date_arrivee": "",
    "date_depart": ""
}`

- `/api/reservations/<id>` - `[DELETE]`

- `/api/reservations` - `[GET]` - params:`date_arrivee` & `date_depart`
