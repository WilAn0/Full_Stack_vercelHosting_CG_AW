#Cameron
contact_us_query = 'select name, phonenumber, emailaddress, country, cityandpostalcode, address from tartare.contactus'

movie_info_query = "SELECT title, description, Pricingadult, Pricingchildren, nowseenmoviesid FROM tartare.nowseenmovies order by genre;"

movie_playtime_query = "select day, TIME_FORMAT(starttime, '%H:%i') AS starttime, TIME_FORMAT(endtime, '%H:%i') AS endtime from tartare.playtime where nowseenmoviesid = %s;"

insert_message_query = 'INSERT INTO tartare.messageus (fullname, emailaddress, subject, message) VALUES (%s, %s, %s, %s);'


#Anton
movie_details_query = "SELECT movieName, synopsis, length, country, genre, actor1, actor2, actor3, actor4, actor5, actor6, director FROM tartare.movie  WHERE movieName = %s"

movie_review_query = "SELECT movieName, review, stars FROM tartare.review WHERE movieName = %s"

movie_test_query = "SELECT movieName from tartare.movie;"