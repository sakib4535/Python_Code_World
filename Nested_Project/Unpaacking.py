movies = [("The Batman", "Matt Reeves", 8.3),
          ("The Dark Night Rises", "Christopher Nolan", 8.4),
          ("The Dark Night", "Christopher Nolan", 8.9),
          ("Batman Begins", "Liam Nesson", 8.3),
          ("Batman and Robin", "Joel Schumacher", 3.7),
          ]

print(len(movies))

#for album in movies:
    #print("Movie: {}, Person: {}, Rate: {}"
          #.format(album[0], album[1], album[2]))

for name, main_god, rate in movies:
    print("Title: {}, Main_God: {}, Rate: {}"
          .format(name, main_god, rate))

