# bilit foroushi , film , sans




class Movie:
    all_movies = []
    def __init__(self,name,time,sans):
        self.name = name
        self.time = time
        self.sans = sans
        Movie.all_movies.append(self)
    @classmethod
    def get_all_movies(cls):
        return cls.all_movies



class Sans:
    def __init__(self,seat,start_t,finish_t,):
        self.set_of_seats = []
        self.seat = seat
        self.start_t =start_t
        self.finish_t =finish_t



class Ticket:
    
    def __init__(self,movie,seat_num):
      if seat_num not in movie.sans.set_of_seats and seat_num < movie.sans.seat :
        movie.sans.set_of_seats.append(seat_num)
        self.seat_num = seat_num
        self.movie = movie  
      else:
        print("this seat is taken")




sans_asr = Sans(30,18,20)
sans_sob = Sans(20,10,12)

interstellar = Movie("interstellar",2,sans_sob)
ghourbaghe = Movie("ghourbaghe",2,sans_asr)


while True:
   print("welcome choose your movie")
   for id,movie in enumerate(Movie.get_all_movies(),1)  :
      print(id , movie.name)
   movie = int(input()) - 1
   seat_num = int(input("choose your seat ==> "))
   Ticket(Movie.all_movies[movie],seat_num)
   print(Movie.all_movies[movie].sans.set_of_seats)