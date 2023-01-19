import pandas as pd
import json
from similarity import response

def create_scheda_film(csv_file, category1, category2, json_file):
    db = pd.read_csv(csv_file, sep=";")

    #extract action and adventure 
    dic_titles = dict()
    i = 0
    for row in db.iterrows():
        if category1 in db["type"][i]:
            if category2 in db["listed_in"][i]:
                dic_i = dict()
                dic_i["messageType"] = "html"
                dic_i["platform"] = "kommunicate"
                suggested_titles = response(db["title"][i])
                dic_i["message"] = f"""<b>{db["title"][i]}</b></br><p>{db["description"][i]}</p><p><b>Cast: </b>{db["cast"][i]}</p><p><b>Director: </b>{db["director"][i]}</p><p><b>Released in: </b>{db["release_year"][i]}</p><p><b>Duration: </b>{db["duration"][i]}</p><p><b>You could also like: </b>{suggested_titles}</p>"""
                #dic_i["message"] = "Tell me more about"+" "+ db["title"][i]
                dic_titles[db["title"][i]]= dic_i
        i += 1


    json_content=dic_titles

    with open(json_file,'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)

#create_scheda_film("data_chatbotACTION.csv", "Movie", "Action & Adventure", "scheda_film_action_movies.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Romantic Movies", "scheda_film_romantic.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Children & Family Movies", "children_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Classic Movies", "classic_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Comedies", "comedies_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Cult Movies", "cult_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Documentaries", "documentaries_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Dramas", "dramas_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Horror Movies", "horror_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Independent Movies", "independent_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "International Movies", "international_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Music & Musicals", "music_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Sci-Fi & Fantasy", "scifi_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Sports Movies", "sport_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Thrillers", "thrillers_scheda_film.json")
#create_scheda_film("data_chatbotACTION.csv", "Movie", "Anime Features", "anime_scheda_film.json")
create_scheda_film("data_chatbotACTION.csv", "Movie", "LGBTQ Movies", "LGBTQ_scheda_film.json")