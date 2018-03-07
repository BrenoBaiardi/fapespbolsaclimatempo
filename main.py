from Scraper import Scraper         # O projeto utiliza classes
from Plot import Plot               # próprias para cada função requerida
from MongoManage import MongoManage # que devem estar no mesmo diretório

# Recebendo dados do url contido na classe Scraper
scraper = Scraper()
<<<<<<< HEAD
arr_guap,arr_colider = scraper.getData()
mongo = MongoManage()
=======
arr_guap = scraper.getData("http://mapas-hidro.ana.gov.br/Usuario/DadoPesquisar.aspx?est=150358540&dado=Chuva&fim=636554214000000000")
arr_colider = scraper.getData("http://mapas-hidro.ana.gov.br/Usuario/DadoPesquisar.aspx?est=105755460&dado=Chuva&fim=636553728000000000")

#popula o banco com os dados coletados pelo scraper
mongo = MongoManage()
mongo.populateCollection(arr_guap,"GUAPORÉ")
mongo.populateCollection(arr_colider,"COLIDER")
>>>>>>> 7fee290bed187e8e97e123848f3df4bc802f6285

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