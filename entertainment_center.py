import media
import fresh_tomatoes

#creating the instances of the class Movie
Star_Wars=media.Movie("Star Wars","Inter Gallactic Battles,Sith Lords and Jedi","Star-Wars-Poster-7.jpg","https://www.youtube.com/watch?v=5UnjrG_N8hU","PG","Harrison Ford,Mark Hamill,Carrie Fisher,Hayden Christensen")
Harry_Potter=media.Movie("Harry Potter series","Story of a boy Wizard and his adventures","-Harry-Potter-and-the-Order-of-the-Phoenix.jpg","https://www.youtube.com/watch?v=y6ZW7KXaXYk","PG-13","Danniel Radcliff,Emma watson,Rupert Grint,Tom Felton")
Star_Trek=media.Movie("Star Trek series","Voyage of the crew of USS Enterprise and their adventures","startrek.jpg","https://www.youtube.com/watch?v=QAEkuVgt6Aw","PG-13","Chris Pine,Zachary Quinto,Zoe Saldana,Benedict Cumberbatch")
Hotel_Transylvania=media.Movie("Hotel Transylvania","Story of a Dracula,his friends and his daughter","hotel_Transylvania.jpg","https://www.youtube.com/watch?v=2Ioqovct5Vs","PG","Salena Gomez,Adam Sandler,Kevin James,Andy Samberg")
Chak_De_India=media.Movie("Chak De India","Story of Indian Women's Hockey Team","chakDeIndia.jpe","https://www.youtube.com/watch?v=6a0-dSMWm5g","U","Shah Rukh Khan,Anaitha Nair,Tanya Abrol,Shilpa Shukla")
Kabhi_Khushi_Kabhi_Gham=media.Movie("Kabhi Khushi Kabhi Gham","Story of a rich Indian family and their adopted son,all the bad and good times they undergo,","KKKG.jpg","https://www.youtube.com/watch?v=7uY1JbWZKPA","U","Shahrukh Khan,Amitabh bacchan,Kajol,Hritik Roshan")
#list of all instances
movies=[Star_Wars,Harry_Potter,Star_Trek,Hotel_Transylvania,Chak_De_India,Kabhi_Khushi_Kabhi_Gham]
#movie instance list with movies that have valid rating
movie_valid_rating=[]
#checking if the rating of the movie is valid
for i in range(0,len(movies)):    
    check_rating=movies[i].check_rating()
    
    if check_rating=="Valid rating":
        movie_valid_rating.append(movies[i])


        
fresh_tomatoes.open_movies_page(movie_valid_rating)
    
