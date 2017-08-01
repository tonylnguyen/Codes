import movie
import fresh_tomatoes


toy_story3 = movie.Movies('Toy Story 3', 'The final chapter for Woody and his friends.',
                          'https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg', 'https://www.youtube.com/watch?v=ZZv1vki4ou4', 'Rotten Tomatoes: 99% ')

kingsman = movie.Movies('Kingsman', "Eggsy's initiation to a secret spy organization",
                        'https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg', 'https://www.youtube.com/watch?v=kl8F-8tR8to', 'Rotten Tomatoes: 77%')

the_sand = movie.Movies('The Sand', 'Killer sand eats people.', 'http://www.gstatic.com/tv/thumb/movieposters/12020601/p12020601_p_v8_aa.jpg',
                        'https://www.youtube.com/watch?v=3JNe6iBWcwI', 'Rotten Tomatoes: 21%')

peregrine = movie.Movies("Miss Peregrine's Home for Peculiar Children", 'A home for gifted children.',
                         'https://upload.wikimedia.org/wikipedia/en/7/74/Miss_Peregrine_Film_Poster.jpg', 'https://www.youtube.com/watch?v=tV_IhWE4LP0', 'Rotten Tomatoes: N/A')

inception = movie.Movies("Inception", "A world of dreams.", 'https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg',
                         'https://www.youtube.com/watch?v=66TuSJo4dZM', 'Rotten Tomatoes: 86%')

intersteller = movie.Movies("intersteller", "Finding a new home in space.", "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                            'https://www.youtube.com/watch?v=0vxOhd4qlnA', "Rotten Tomatoes: 71%")

films = [toy_story3, kingsman, the_sand, peregrine, inception, intersteller]

fresh_tomatoes.open_movies_page(films)
