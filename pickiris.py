import requests 
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text


list = data.split("\n")


list2 = [i.split(",") for i in list if len(i)!=0]

print(list2)

with open("pickiris.pkl", "wb") as f:
    pickle.dump(list,f)

# For reading the file s
# with open("pickiris.pkl", "rb") as f:
#     print(pickle.load(f))