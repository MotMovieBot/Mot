from dfcx_scrapi.core.scrapi_base import ScrapiBase
from dfcx_scrapi.core.entity_types import EntityTypes
import pandas as pd 
from google.cloud.dialogflowcx_v3beta1.types import entity_type
import re

creds_path = 'alert-vista-366713-15e1dff5c322.json'
agent_path = 'projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395'

# DFCX Agent ID paths are in this format:
# 'projects/<project_id>/locations/<location_id>/agents/<agent_id>'

db = pd.read_csv("data_chatbotACTION.csv", sep=";")

#extract movies categories 
set_movies=set()
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        for value in (db["listed_in"][i]).split(","):
            value = value.replace('"','')
            value = re.sub('^\s*', '', value)
            set_movies.add(value)
    i += 1
entity_movies = []
for each in set_movies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_movies.append(each_entity_value)


#extract documentaries from the csv
list_documentaries=[]
i = 0
for row in db.iterrows():
    if "Documentaries" in db["listed_in"][i]:
        list_documentaries.append(db["title"][i])
    i += 1
entity_doc = []
for each in list_documentaries:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_doc.append(each_entity_value)

#extract action and adventure 
list_action=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Action & Adventure" in db["listed_in"][i]:
            list_action.append(db["title"][i])
    i += 1
entity_action = []
for each in list_action:
    each_entity_value = {}
    each_entity_value['value'] = str(each)
    each_entity_value['synonyms'] = [each]
    entity_action.append(each_entity_value)

#extract anime features
list_anime_feat=[]
i = 0
for row in db.iterrows():
    if "Anime Features" in db["listed_in"][i]:
        list_anime_feat.append(db["title"][i])
    i += 1
entity_anime_feat = []
for each in list_anime_feat:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_anime_feat.append(each_entity_value)


#extract family movies
list_family_movies=[]
i = 0
for row in db.iterrows():
    if "Children & Family Movies" in db["listed_in"][i]:
        list_family_movies.append(db["title"][i])
    i += 1
entity_family_movies = []
for each in list_family_movies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_family_movies.append(each_entity_value)


#extract classic movies
list_classic_movies=[]
i = 0
for row in db.iterrows():
    if "Classic Movies" in db["listed_in"][i]:
        list_classic_movies.append(db["title"][i])
    i += 1
entity_classic_movies = []
for each in list_classic_movies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_classic_movies.append(each_entity_value)

#extract comedies
list_comedies=[]
i = 0
for row in db.iterrows():
    if "Comedies" in db["listed_in"][i]:
        list_comedies.append(db["title"][i])
    i += 1
entity_comedies = []
for each in list_comedies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_comedies.append(each_entity_value)

#extract cult movies
list_cult_movies=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Cult Movies" in db["listed_in"][i]:
            list_cult_movies.append(db["title"][i])
    i += 1
entity_cult_movies = []
for each in list_cult_movies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_cult_movies.append(each_entity_value)

#extract dramas
list_dramas=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Dramas" in db["listed_in"][i]:
            list_dramas.append(db["title"][i])
    i += 1
entity_dramas = []
for each in list_dramas:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_dramas.append(each_entity_value)

#extract romantic movies  
list_romantic_movies=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Romantic Movies" in db["listed_in"][i]:
            list_romantic_movies.append(db["title"][i])
    i += 1
entity_romantic_movies = []
for each in list_romantic_movies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_romantic_movies.append(each_entity_value)

#extract thriller  
list_thriller=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Thrillers" in db["listed_in"][i]:
            list_thriller.append(db["title"][i])
    i += 1
entity_thriller = []
for each in list_thriller:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_thriller.append(each_entity_value)

#extract faith & spirituality  
list_fate=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Faith & Spirituality" in db["listed_in"][i]:
            list_fate.append(db["title"][i])
    i += 1
entity_fate = []
for each in list_fate:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_fate.append(each_entity_value)


#extract horror
list_horror_movies=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Horror Movies" in db["listed_in"][i]:
            list_horror_movies.append(db["title"][i])
    i += 1
entity_horror_movies = []
for each in list_horror_movies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_horror_movies.append(each_entity_value)

#extract independent movies
list_ind_movies=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Independent Movies" in db["listed_in"][i]:
            list_ind_movies.append(db["title"][i])
    i += 1
entity_ind_movies = []
for each in list_ind_movies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_ind_movies.append(each_entity_value)

#extract international movies
list_int_movies=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "International Movies" in db["listed_in"][i]:
            list_int_movies.append(db["title"][i])
    i += 1
entity_int_movies = []
for each in list_int_movies:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_int_movies.append(each_entity_value)

#extract LGBTQ movies
list_lgbtq=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "LGBTQ Movies" in db["listed_in"][i]:
            list_lgbtq.append(db["title"][i])
    i += 1
entity_lgbtq = []
for each in list_lgbtq:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_lgbtq.append(each_entity_value)

#extract sport movies
list_sport=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Sports Movies" in db["listed_in"][i]:
            list_sport.append(db["title"][i])
    i += 1
entity_sport = []
for each in list_sport:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_sport.append(each_entity_value)

#extract musicals
list_musicals=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Music & Musicals" in db["listed_in"][i]:
            list_musicals.append(db["title"][i])
    i += 1
entity_musicals = []
for each in list_musicals:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_musicals.append(each_entity_value)

#extract sci-fi movies
list_scifi=[]
i = 0
for row in db.iterrows():
    if "Movie" in db["type"][i]:
        if "Sci-Fi & Fantasy" in db["listed_in"][i]:
            list_scifi.append(db["title"][i])
    i += 1
entity_scifi = []
for each in list_scifi:
    each_entity_value = {}
    each_entity_value['value'] = each
    each_entity_value['synonyms'] = [each]
    entity_scifi.append(each_entity_value)

# Instantiate your class object and pass in your credentials
i = EntityTypes(creds_path, agent_id=agent_path)

# Create entities 
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Movies_categories", entities=entity_movies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Documentaries", entities=entity_doc)
i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Action_and_Adventure", entities=entity_action)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Anime_Features", entities=entity_anime_feat)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Children_and_Family_Movies", entities=entity_family_movies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Classic_Movies", entities=entity_classic_movies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Comedies", entities=entity_comedies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Cult_Movies", entities=entity_cult_movies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Dramas", entities=entity_dramas)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Horror_Movies", entities=entity_horror_movies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Independent_Movies", entities=entity_ind_movies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="International_Movies", entities=entity_int_movies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Music_and_Musicals", entities=entity_musicals)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Sci-Fi_and_Fantasy", entities=entity_scifi)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Romantic_Movies", entities=entity_romantic_movies)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Thrillers", entities=entity_thriller)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Faith_and_Spirituality", entities=entity_fate)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="LGBTQ_Movies", entities=entity_lgbtq)
#i.create_entity_type(kind = entity_type.EntityType.Kind.KIND_MAP, display_name="Sports_Movies", entities=entity_sport)
