import pickle

autoparts= pickle.load(open(".resources/autoparts_list.pkl", 'rb'))
autoparts_similarity = pickle.load(open(".resources/autoparts_similarity.pkl", 'rb'))

#print(similarity)
def recommend(keyword):
    index = autoparts[autoparts['part_name'] == keyword].index[0]
    #print(index)
    #print(similarity[index])
    distance = sorted(list(enumerate(autoparts_similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_list = []
    for i in distance[1:11]:
        recommend_list.append(autoparts.iloc[i[0]].title)

    return recommend_list

movie_name = recommend("Oil filter")
for i in movie_name:
    print(i)