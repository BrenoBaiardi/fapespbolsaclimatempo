from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class MongoManage():

    def __init__(self):
        client = MongoClient()
        db = client.test
        col = db.col

    def populateCollection(arr):
        for i in arr:
            i[0] = i[0].replace("/","")
            i[0] = i[0].replace(":","")
            i[0] = i[0].replace(" ","")
            aux={"_id":i[0],"value":i[1]}
            try:
                col.insert(aux);
            except DuplicateKeyError:
                print("Dado já existente ignorado")
            except Exception as e:
                print("Erro:"+e)
                return(-1)
        print("Inserção de dados completa")
        return(1)

    
