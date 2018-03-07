from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

class MongoManage():

    def __init__(self): #Inicialização de conexão e variáveis de collection
        self.client = MongoClient()
        self.db = self.client.test
        self.col = self.db.col

    def populateCollection(self,arr,label):
        print("Salvando dados")
        for i in arr:
            aux=i[:]
            #formata o _id para uma string ao invés de utilizar o _id padrão
            aux[0] = aux[0].replace("/","")#esse novo _id é baseado no horario de medição
            aux[0] = aux[0].replace(":","")#dessa forma se o programa em duas execuções diferentes
            aux[0] = aux[0].replace(" ","")#encontrar dados com mesma hora e data, ele não armazena
            aux[0] = aux[0] + label #com a label, ele adiciona e separa as entradas de origens diferentes
            aux={"_id" : aux[0],"value" : aux[1],"label" : label}
            try:
                self.col.insert(aux);
            except DuplicateKeyError:
                print("Dado repetido, não foi adicionado ao banco")
            except Exception as e:
                print("Erro:"+str(e))
                return(-1)
        print("Inserção de dados completa")
        return(1)

    def readCollection(self,label):
        cursor = self.col.find({"label" : label})
        res=[]
        #para a leitura, o formato do _id com nova string retorna
        # ao padrão utilizado pela classe Plot
        for i in cursor:
            res.append(
                [i["_id"][0:2]+"/"+i["_id"][2:4]+"/"+i["_id"][4:8]+" "+i["_id"][8:10]+":"+i["_id"][10:12]+":"+i["_id"][12:14],i["value"]]
            )
        return res