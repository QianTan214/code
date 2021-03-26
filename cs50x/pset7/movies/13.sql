--In 13.sql, write a SQL query to list the names of all people who starred in a movie
--in which Kevin Bacon also starred.
--Your query should output a table with a single column for the name of each person.
--There may be multiple people named Kevin Bacon in the database.
--Be sure to only select the Kevin Bacon born in 1958.
--Kevin Bacon himself should not be included in the resulting list.


select distinct name from people
join stars on people.id = stars.person_id
join movies on stars.movie_id = movies.id
where movies.id in

(select movies.id from movies
join stars on movies.id = stars.movie_id
join people on stars.person_id = people.id
where people.name = "Kevin Bacon" and people.birth = 1958)

and people.name != "Kevin Bacon";
