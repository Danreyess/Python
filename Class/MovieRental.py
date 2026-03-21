class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.available = True

class MovieStore:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre):
        movie = Movie(title, genre)
        self.movies.append(movie)

    def show_movie(self):
        for movie in self.movies:
            status = "Available" if movie.available else "Not available"
            print(f"{movie.title}: {status}")

    def borrow_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                if movie.available:
                    movie.available = False
                    print("Movie borrowed")
                    return
                else:
                    print("Movie not available")
        print("Movie not available")

    def return_movies(self, title):
        for movie in self.movies:
            if movie.title == title:
                if movie.available:
                    movie.available = True
                    print("Movie returned")
                    return

movie1 = MovieStore()
movie1.add_movie("My first movie", "guillermo")
movie1.show_movie()


#add_movie title genre
#show movie
#rent movie busca la peli, si esta disponible
#return movie marca la pelicula como disponile otra vez

#Operador Ternario
#valor_si_true if condicion else valor_si_false