class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.available = True

class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_movies = []


class MovieStore:
    def __init__(self):
        self.customers = []
        self.movies = []

    def add_movie(self, title, genre):
        movie = Movie(title, genre)
        self.movies.append(movie)

    def show_movies(self):
        for movie in self.movies:
            status = "Available" if movie.available else "Not available"
            print(f"{movie.name} - {movie.genre} - {status}")

    def add_customer(self, name):
        customer = Customer(name)
        self.customers.append(customer)

    def rent_movie(self,customer_name, title):
        #Search client
        for customer in self.customers:
            if customer.name.lower() == customer_name.lower():
                #Buscar peliculas
                for movie in self.movies:
                    if movie.title.lower() == title.lower():
                        if movie.available:
                            movie.available = False
                            customer.rented_movies.append(movie)
                            print(f"{customer.name} rented {movie.title}")
                        else:
                            print("Movie not available")
                        return
                    print("Movie not found")
                    return
        print("Customer not found")



    def return_movie(self, customer_name, movie_title):
        #Search customers
        for customer in self.customers:
            if customer.name.lower() == customer_name.lower():
                #Buscar peliculas en su lista dfe alquileres
                for movie in customer.rented_movies:
                    if movie.title.lower() == movie_title.lower():
                        movie.available = True
                        customer.rented_movies.remove(movie)
                        print(f"{customer.name} returned {movie.title}")
                        return
                    print(f"{customer.name} did not rent {movie.title}")
                    return
        print("Customer not found")


store = MovieStore()
store.add_movie("Inception", "Sci-Fi")
store.add_customer("Dani")

store.rent_movie("Dani", "Inception")
store.return_movie("Dani", "Inception")