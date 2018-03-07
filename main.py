from Scraper import Scraper
from Plot import Plot
from MongoManage import MongoManage

scraper = Scraper()
arr_guap,arr_colider = scraper.getData()
mongo = MongoManage()

#popula o banco com os dados coletados pelo scraper
if mongo.populateCollection(arr_guap,"GUAPORÉ")!=1 or mongo.populateCollection(arr_colider,"COLIDER")!=1:
    print("Não foi possível encontrar o banco de dados local, certifique se de que o comando mongod.exe esta sendo executado")
    while True:#para permitir a leitura da mensagem sem fechar o programa com exit
        continue
    
#coleta os dados armazenados no banco
res_guap = mongo.readCollection("GUAPORÉ")
res_colider = mongo.readCollection("COLIDER")

#plota os dados coletados DO BANCO
plot = Plot()
plot.plotGraph(res_guap,"GUAPORÉ")
plot.plotGraph(res_colider,"COLIDER")
plot.showGraph()
