--In 12.sql, write a SQL query to list the titles of all movies in which
--both Johnny Depp and Helena Bonham Carter starred.
--Your query should output a table with a single column for the title of each movie.
--You may assume that there is only one person in the database with the name Johnny Depp.
--You may assume that there is only one person in the database with the name Helena Bonham Carter.


select movies.title from people
join stars on people.id = stars.person_id
join movies on stars.movie_id = movies.id
where people.name = "Johnny Depp"
and
movies.title in (select movies.title from people
join stars on people.id = stars.person_id
join movies on stars.movie_id = movies.id
where people.name = "Helena Bonham Carter");