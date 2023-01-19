from dfcx_scrapi.core.pages import Pages
from dfcx_scrapi.tools.maker_util import MakerUtil
import pandas as pd


def create_routes(creds_path, csv_file, intent_id, target_page_id, category1, category2, entity_name, page_id_to_update):
   
    db = pd.read_csv(csv_file, sep=";")

    c = Pages(creds_path = creds_path)
    
    j = MakerUtil()
    
    i = 0
    for row in db.iterrows():
        if category1 in db["type"][i]:
            if category2 in db["listed_in"][i]:
                title = db["title"][i]
                condition = f'''$session.params.{entity_name} = "{title}"'''
                route = j.make_transition_route(intent=intent_id,condition=condition,target_page=target_page_id)
                dsf = c.get_page(page_id_to_update)
                dsf.transition_routes.append(route)
                c.update_page(page_id=page_id_to_update, obj=dsf, transition_routes=dsf.transition_routes)    
        i += 1
    
creds_path = 'alert-vista-366713-15e1dff5c322.json'
csv_file = "data_chatbotACTION.csv"
intent_id_children = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/4d4655b9-fb69-42e3-be06-0c3671de2cd1"
target_page_id_children = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/3c41914b-269c-4def-837f-9cb8ccf13a43/pages/826a9226-9648-40fe-96c6-aecc9aa254fc"
category1_children = "Movie"
category2_children = "Children & Family Movies"
entity_name_children = "Children_and_Family_Movies"
page_id_to_update_children = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/3c41914b-269c-4def-837f-9cb8ccf13a43/pages/0eb6cea5-3f16-4b77-bf92-97f8c0404c05"

intent_id_anime = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/b550d99f-3072-47ef-b04e-3da8a97afeb6"
target_page_id_anime = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/135cf518-a6cc-4ca3-bba4-0268ee22db79/pages/59c72069-146f-4f99-9e06-cd0d3f9259f5"
category1_anime = "Movie"
category2_anime = "Anime Features"
entity_name_anime = "Anime_Features"
page_id_to_update_anime = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/135cf518-a6cc-4ca3-bba4-0268ee22db79/pages/d14b2aa6-d29b-4991-9ae0-0fbfcf0a9cc4"

intent_id_action = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/54203179-32ce-49cd-98a4-ec246d14ef10"
target_page_id_action = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/b0c1ea79-e1b8-4b31-aef8-acce16cc7bce/pages/ee1ad121-8229-40e4-8881-2ac0dcf1122c"
category1_action = "Movie"
category2_action = "Action & Adventure"
entity_name_action = "Action_and_Adventure"
page_id_to_update_action = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/b0c1ea79-e1b8-4b31-aef8-acce16cc7bce/pages/412de223-fed1-4b8f-a701-f6e9a419a972"

intent_id_classic = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/0ffddbd3-216b-4e5e-b4cd-a32595224a3e"
target_page_id_classic = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/f4c96c1e-1110-4ee0-93b4-6aaaa2007f8c/pages/d429a204-124f-4e01-8f7c-57cd0117c28a"
category1_classic = "Movie"
category2_classic = "Classic Movies"
entity_name_classic = "Classic_Movies"
page_id_to_update_classic = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/f4c96c1e-1110-4ee0-93b4-6aaaa2007f8c/pages/b3320290-d150-46dd-bac8-de04a40c0810"

intent_id_comedies = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/2cb40354-3ac7-4799-ae5f-c075bf5780e9"
target_page_id_comedies = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/cb2dabed-3e18-4361-800f-f03caa8c15a5/pages/7325f836-7d54-4caf-8acb-c658b4d4b858"
category1_comedies = "Movie"
category2_comedies = "Comedies"
entity_name_comedies = "Comedies"
page_id_to_update_comedies = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/cb2dabed-3e18-4361-800f-f03caa8c15a5/pages/46e73197-941b-40e0-9ca3-66e4656b6f0a"

intent_id_cult= "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/a9cd680b-ef95-4648-bd99-e76249852f71"
target_page_id_cult = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/66c2cc77-3c6b-4b2b-b9fc-64ce1a59407f/pages/34e34aed-32fe-4d5d-beec-19847b2edc12"
category1_cult = "Movie"
category2_cult = "Cult Movies"
entity_name_cult = "Cult_Movies"
page_id_to_update_cult = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/66c2cc77-3c6b-4b2b-b9fc-64ce1a59407f/pages/7ff241f9-eb1b-46c8-b0cb-926ea6472a07"

intent_id_doc= "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/bb2e44ef-db3e-42ff-acb3-19b5b1892c9b"
target_page_id_doc = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/2c544ee5-936e-48d8-82d8-8b4380609458/pages/aa4856ec-32e6-47c6-96ec-73d5350c0658"
category1_doc = "Movie"
category2_doc = "Documentaries"
entity_name_doc = "Documentaries"
page_id_to_update_doc = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/2c544ee5-936e-48d8-82d8-8b4380609458/pages/719cab70-f2dc-4de3-ab31-0a4a12d9abd6"

intent_id_dramas= "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/a02c75d8-fdd0-420f-9179-7dc7f4795927"
target_page_id_dramas = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/2873fbae-9d0c-47c6-ba66-88dd562f516a/pages/705e991e-7118-4007-8288-546312c2d44b"
category1_dramas = "Movie"
category2_dramas = "Dramas"
entity_name_dramas = "Dramas"
page_id_to_update_dramas = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/2873fbae-9d0c-47c6-ba66-88dd562f516a/pages/20d32013-cb20-4b17-bfec-86fa529db611"

intent_id_horror= "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/b6daedf6-c630-45ef-9560-e43f493c92f3"
target_page_id_horror = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/858752b1-a854-40b4-97d1-59e61fea608f/pages/7bceeb6b-ce6c-4acf-a96c-f5eef118fd4c"
category1_horror = "Movie"
category2_horror = "Horror Movies"
entity_name_horror = "Horror_Movies"
page_id_to_update_horror = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/858752b1-a854-40b4-97d1-59e61fea608f/pages/3ae72321-03d5-4231-b8fa-69dadf4c25d9"

intent_id_ind= "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/a468a19d-4436-40a0-b2f8-f52da21c6c06"
target_page_id_ind = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/5031c084-1f17-4cab-abf6-7d747d1581a0/pages/a3ab3b20-95e8-439b-a06e-8bd39f3d3543"
category1_ind = "Movie"
category2_ind = "Independent Movies"
entity_name_ind = "Independent_Movies"
page_id_to_update_ind = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/5031c084-1f17-4cab-abf6-7d747d1581a0/pages/1d237db5-3a1c-4a4e-92bf-3553692983b1"

intent_id_int= "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/e1b7297f-79b6-456b-b340-0243d15c4476"
target_page_id_int = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/5becd854-ccd6-478a-897c-de46d9bbfaeb/pages/b11179de-1af6-47c7-9e33-a00f0219dcfa"
category1_int = "Movie"
category2_int = "International Movies"
entity_name_int = "International_Movies"
page_id_to_update_int = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/5becd854-ccd6-478a-897c-de46d9bbfaeb/pages/a9a4e64f-47e4-4970-9e53-c75bdbf495d1"

intent_id_scifi= "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/2a747df2-0ef4-4619-9baf-c37c62db3ba4"
target_page_id_scifi = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/b1c07484-3386-4bb0-b4be-fbd5a4431b29/pages/1d3c8bcb-33eb-4410-a081-01341aacf465"
category1_scifi = "Movie"
category2_scifi = "Sci-Fi & Fantasy"
entity_name_scifi = "Sci-Fi_&_Fantasy"
page_id_to_update_scifi = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/b1c07484-3386-4bb0-b4be-fbd5a4431b29/pages/899c5c35-aa96-48c6-bc73-cbd4a959f32f"

intent_id_romantic= "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/6dc2b3c4-0de0-4031-b332-ced37ab3aef6"
target_page_id_romantic = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/e1c3db25-ade5-415f-876b-f13769b6859e/pages/06aaabd7-ff6e-45a1-b398-04f53b7268da"
category1_romantic = "Movie"
category2_romantic = "Romantic Movies"
entity_name_romantic = "Romantic_Movies"
page_id_to_update_romantic = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/e1c3db25-ade5-415f-876b-f13769b6859e/pages/5e45404e-c9c8-48d5-bda8-22602532ebe6"

intent_id_lgbtq = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/fb34fbb1-a9ba-4309-8a6b-2b2e6c72a45a"
target_page_id_lgbtq = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/fabf307b-82e3-4d2a-a12b-7100fdd47073/pages/38c4cd2c-2f1a-4ea8-bb82-ab6ce2330a8a"
category1_lgbtq = "Movie"
category2_lgbtq = "LGBTQ Movies"
entity_name_lgbtq = "LGBTQ_Movies"
page_id_to_update_lgbtq = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/fabf307b-82e3-4d2a-a12b-7100fdd47073/pages/336c9c13-9220-46a7-aa29-f96e91b1b16e"

intent_id_thriller = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/452edb2b-4be1-4a28-bbf1-61d18ec01a98"
target_page_id_thriller = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/199d4bab-e8be-4012-b117-23e4bd16c5ff/pages/cc6a7b8f-2d8d-43e8-a513-9741e98deab3"
category1_thriller = "Movie"
category2_thriller = "Thrillers"
entity_name_thriller = "Thrillers"
page_id_to_update_thriller = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/199d4bab-e8be-4012-b117-23e4bd16c5ff/pages/64359af1-1365-42e5-8212-bc0c0f80b829"

intent_id_sport = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/0bacfe0b-44e1-4cec-8502-e9d8024daf3e"
target_page_id_sport = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/61809613-fd8d-4240-bef1-ac3d357a586e/pages/7982e961-6ce0-46f6-a9b9-8e11542f3f6e"
category1_sport = "Movie"
category2_sport = "Sports Movies"
entity_name_sport = "Sports_Movies"
page_id_to_update_sport = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/61809613-fd8d-4240-bef1-ac3d357a586e/pages/8ec23af3-84db-4ce9-9b15-bdef1bc1929b"

intent_id_music = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/intents/4a0472a1-c874-4ac7-a24e-e3793e6857df"
target_page_id_music = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/36fc14d1-9063-4607-8b54-b0d3842ee9ee/pages/9612060f-253f-4c17-a2de-ea93aad91802"
category1_music = "Movie"
category2_music = "Music & Musicals"
entity_name_music = "Music_and_Musicals"
page_id_to_update_music = "projects/alert-vista-366713/locations/europe-west3/agents/5baf2b13-8689-4784-bd58-38df4aa55395/flows/36fc14d1-9063-4607-8b54-b0d3842ee9ee/pages/d66c91ba-ae6f-4a38-acdb-a0f4879ee797"

#create_routes(creds_path, csv_file, intent_id_action, target_page_id_action, category1_action, category2_action, entity_name_action, page_id_to_update_action)
#create_routes(creds_path, csv_file, intent_id_anime, target_page_id_anime, category1_anime, category2_anime, entity_name_anime, page_id_to_update_anime)
#create_routes(creds_path, csv_file, intent_id_children, target_page_id_children, category1_children, category2_children, entity_name_children, page_id_to_update_children)
#create_routes(creds_path, csv_file, intent_id_classic, target_page_id_classic, category1_classic, category2_classic, entity_name_classic, page_id_to_update_classic)
#create_routes(creds_path, csv_file, intent_id_comedies, target_page_id_comedies, category1_comedies, category2_comedies, entity_name_comedies, page_id_to_update_comedies)
#create_routes(creds_path, csv_file, intent_id_cult, target_page_id_cult, category1_cult, category2_cult, entity_name_cult, page_id_to_update_cult)
#create_routes(creds_path, csv_file, intent_id_doc, target_page_id_doc, category1_doc, category2_doc, entity_name_doc, page_id_to_update_doc)
#create_routes(creds_path, csv_file, intent_id_dramas, target_page_id_dramas, category1_dramas, category2_dramas, entity_name_dramas, page_id_to_update_dramas)
#create_routes(creds_path, csv_file, intent_id_horror, target_page_id_horror, category1_horror, category2_horror, entity_name_horror, page_id_to_update_horror)
#create_routes(creds_path, csv_file, intent_id_ind, target_page_id_ind, category1_ind, category2_ind, entity_name_ind, page_id_to_update_ind)
#create_routes(creds_path, csv_file, intent_id_int, target_page_id_int, category1_int, category2_int, entity_name_int, page_id_to_update_int)
#create_routes(creds_path, csv_file, intent_id_scifi, target_page_id_scifi, category1_scifi, category2_scifi, entity_name_scifi, page_id_to_update_scifi)
#create_routes(creds_path, csv_file, intent_id_romantic, target_page_id_romantic, category1_romantic, category2_romantic, entity_name_romantic, page_id_to_update_romantic)
#create_routes(creds_path, csv_file, intent_id_lgbtq, target_page_id_lgbtq, category1_lgbtq, category2_lgbtq, entity_name_lgbtq, page_id_to_update_lgbtq)
#create_routes(creds_path, csv_file, intent_id_thriller, target_page_id_thriller, category1_thriller, category2_thriller, entity_name_thriller, page_id_to_update_thriller)
#create_routes(creds_path, csv_file, intent_id_sport, target_page_id_sport, category1_sport, category2_sport, entity_name_sport, page_id_to_update_sport)
create_routes(creds_path, csv_file, intent_id_music, target_page_id_music, category1_music, category2_music, entity_name_music, page_id_to_update_music)