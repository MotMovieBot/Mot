import pandas as pd
import json

def create_json_with_titles(csv_file, category1, category2, json_file):
    db = pd.read_csv(csv_file, sep=";")

    #extract action and adventure 
    dic_action = dict()
    movies = []
    i = 0
    for row in db.iterrows():
        if category1 in db["type"][i]:
            if category2 in db["listed_in"][i]:
                dic_i = dict()
                buttons = dict()
                action = dict()
                message=dict()
                buttons_list=[]
                dic_i["title"] = db["title"][i]
                dic_i["subtitle"] = db["listed_in"][i]
                dic_i["description"] = db["description"][i]
                buttons["name"] = "Tell me more"
                message["message"] = "Tell me more about"+ " "+db["title"][i] 
                action["payload"] = message
                action["type"] = "quickReply"
                buttons["action"] = action
                buttons_list.append(buttons)
                dic_i["buttons"] = buttons_list
                #dic_i["message"] = "Tell me more about"+" "+ db["title"][i]
                movies.append(dic_i)
        i += 1
    dic_action["payload"] = movies



    with open(json_file,'r') as jsonfile:
        json_content = json.load(jsonfile)

    json_content["metadata"]["payload"]= movies

    with open(json_file,'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)

#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Action & Adventure", "action_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Anime Features", "anime_features_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Children & Family Movies", "children_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Classic Movies", "classic_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Comedies", "comedies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Cult Movies", "cult_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Documentaries", "documentaries_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Dramas", "dramas_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Horror Movies", "horror_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Independent Movies", "independent_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "International Movies", "international_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Sci-Fi & Fantasy", "sci-fi_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Romantic Movies", "romantic_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "LGBTQ Movies", "LGBTQ_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Faith & Spirituality", "fate_movies_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Thrillers", "thrillers_titles.json")
#create_json_with_titles("data_chatbotACTION.csv", "Movie", "Sports Movies", "sports_movies_titles.json")
create_json_with_titles("data_chatbotACTION.csv", "Movie", "Music & Musicals", "music_movies_titles.json")