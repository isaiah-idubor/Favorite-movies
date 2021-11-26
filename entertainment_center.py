import media
import fresh_tomatoes


# instances of favorite movies of the class Movie
pacific_rim_2018 = media.Movie(  # movie title
                               "Pacific Rim: Uprising",
                               # movie storyline goes here
                               "Storyline",
                               # movie poster link
                               # "https://vignette.wikia.nocookie.net
                               # /pacificrim/images/8/83/Pacific_Rim_Uprising_%28
                               # Theatrical_Poster%29.jpg
                               # /revision/latest?cb=20180124203204",
                               # link shortened on bitly.com
                               "https://bit.ly/2HxvqIu",
                               # movie trailer link
                               "https://www.youtube.com/watch?v=8BAhwgjMvnM")

blank_panther = media.Movie(  # movie title
                            "Black Panther",
                            # movie storyline goes here
                            "Storyline",
                            # movie poster link
                            # "http://t1.gstatic.com
                            # /images?q=tbn:ANd9GcQPpcKQ9eWZGxJe6eXy
                            # CW91eayLVm4KqruvJz3GP0F2T2w46yKZ"
                            # link shortened on bitly.com
                            "https://bit.ly/2ECr2qa",
                            # movie trailer link
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

doctor_strange = media.Movie(  # movie title
                             "Doctor Strange",
                             # movie storyline goes here
                             "Storyline",
                             # movie poster link
                             # http://t3.gstatic.com
                             # /images?q=tbn:ANd9GcSmG4ms8wxdnuKOwetpc
                             # 4qltTv7pHopDLRTi-t98dx-L-kt_b1t" '''
                             # link shortened on bitly.com
                             "https://bit.ly/2HvtQLt",
                             # movie trailer link
                             "https://www.youtube.com/watch?v=MWRUNTLisPo")

justice_league = media.Movie(  # movie title
                             "Justice League",
                             # movie storyline goes here
                             "Storyline",
                             # movie poster link
                             # http://t3.gstatic.com
                             # /images?q=tbn:ANd9GcQr8TLcGyFZmLsJSNZ3M_8
                             # CO2M9YbnucnpGTs6u2erH-SveV1O2" '''
                             # link shortened on bitly.com
                             "https://bit.ly/2HxaMsh",
                             # movie trailer link
                             "https://www.youtube.com/watch?v=3cxixDgHUYw")

wonder_woman = media.Movie(  # movie title
                           "Wonder Woman",
                           # movie storyline goes here
                           "Storyline",
                           # movie poster link
                           # http://t1.gstatic.com
                           # /images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ
                           # 2JLYDRLxeAcbH-541fzqq1H" '''
                           # link shortened on bitly.com
                           "https://bit.ly/2rRZASN",
                           # movie trailer link
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

mute = media.Movie(  # movie title
                   "Mute",
                   # movie storyline goes here
                   "Storyline",
                   # movie poster link
                   # http://t3.gstatic.com
                   # /images?q=tbn:ANd9GcRF3paN1-eKq1E0krXOq
                   # GqCbp6pjqSg4uddAHCwI2msTrMUqPn6" '''
                   # link shortened on bitly.com
                   "https://bit.ly/2r2eIeh",
                   # movie trailer link
                   "https://www.youtube.com/watch?v=ma8te7ywEio")

# list of favorite movies in an array movies
movies = [pacific_rim_2018, blank_panther, doctor_strange,
          justice_league, wonder_woman, mute]
# open.movies_page function is called with the list of favorite ,movies
# renders list of favorite movies unto an html page
fresh_tomatoes.open_movies_page(movies)
