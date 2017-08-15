import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=nCqtQLmJTl0"
                        )


apocalypto = media.Movie("Apocalypto",
                         "A Mayans culture, epic center film",
                         "https://upload.wikimedia.org/wikipedia/en/6/62/Apocalypto-poster01.jpg",
                         "https://www.youtube.com/watch?v=YUdr8yupdwo"
                         )

city_of_god = media.Movie("City of God",
                          "A drug war based on true story in brazil city",
                          "https://upload.wikimedia.org/wikipedia/en/1/10/CidadedeDeus.jpg",
                          "https://www.youtube.com/watch?v=dcUOO4Itgmw"
                          )

mongol = media.Movie("Mongul",
                     "A film about Ghengis khan",
                     "https://upload.wikimedia.org/wikipedia/en/8/81/Mongol_poster.jpg",
                     "https://www.youtube.com/watch?v=XAFnxV2GYRU"
                    )

texas_chainsaw_massacre = media.Movie("Texas chainsaw masscre",
                                      "Based on real story in texas chain murders",
                                      "https://upload.wikimedia.org/wikipedia/en/2/20/Texas_chainsaw_massacre.jpg",
                                      "https://www.youtube.com/watch?v=janre4HxsX4"
                                      )

final_destination = media.Movie("Final Destination",
                                "A super natural horror film",
                                "https://upload.wikimedia.org/wikipedia/en/a/a3/Final_Destination_movie.jpg",
                                "https://www.youtube.com/watch?v=1kICBQJ6eQw")


movies = [toy_story, apocalypto, city_of_god, mongol, texas_chainsaw_massacre, final_destination]

fresh_tomatoes.open_movies_page(movies)