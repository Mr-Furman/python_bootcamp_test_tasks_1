import pandas as pd
import csv
import copy

class Film:

    def __init__(self, film_name:str, rating:int, note:str):
        self.film_name = film_name
        self.rating = rating
        self.note = note
        self.films = None

    def read_csv(self, path_to_file: str):
        if self.films is None:
            self.films = pd.read_csv(path_to_file)
        else: 
            self.films = pd.concat([self.films, pd.read_csv(path_to_file)])

    def add_note(self):

      if self.film_name in self.films['film_name'].values:
          print(f'We have {self.film_name} in our library')
      else:
          film = {"film_name": [self.film_name], " rating": [self.rating], " note": [self.note]}
          self.films = pd.concat([self.films, pd.DataFrame.from_dict(film)], ignore_index=True)
          self.films.to_csv("Book1.csv", index=False)


    def remove_note(self):
        self.films = self.films[~((self.films["film_name"]==self.film_name) & (self.films[" rating"]==self.rating) & (self.films[" note"]==self.note))]
        self.films.to_csv("Book1.csv", index=False)

    def print_notes_to_console(self):
        print(self.films)

    def highest_rating(self):
      """Get films with the highest rating"""
      print(self.films[self.films[' rating'] == self.films[' rating'].max()])
   
   
    def lowest_rating(self):
      """Get films with the lowest rating"""
      print(self.films[self.films[' rating'] == self.films[' rating'].min()])

    def middle_of_all(self):
      """Get average rating among all films"""
      print(self.films[' rating'].mean())
 




film_1 = Film('Speed', 5, 'norm')
film_1.read_csv('Book1.csv')
film_1.add_note()

film_1.print_notes_to_console()
film_1.highest_rating()
film_1.lowest_rating()
film_1.middle_of_all()
