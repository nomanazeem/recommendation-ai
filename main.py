import pickle

movies_list = pickle.load(open(".resources/movies_list.pkl", 'rb'))
similarity = pickle.load(open(".resources/similarity.pkl", 'rb'))

#print(similarity)
def recommend(keyword):
    index = movies_list[movies_list['title'] == keyword].index[0]
    #print(index)
    #print(similarity[index])
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_list = []
    for i in distance[1:11]:
        recommend_list.append(movies_list.iloc[i[0]].title)

    return recommend_list

movie_name = recommend("Iron Man")
for i in movie_name:
    print(i)