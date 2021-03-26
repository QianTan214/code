--In 10.sql, write a SQL query to list the names of all people
--who have directed a movie that received a rating of at least 9.0.
--Your query should output a table with a single column for the name of each person.


select name from
(select distinct people.id, people.name from people
join directors on people.id = directors.person_id
join ratings on directors.movie_id = ratings.movie_id
where ratings.rating >= 9.0);





