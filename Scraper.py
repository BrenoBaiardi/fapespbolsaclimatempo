from bs4 import BeautifulSoup
import urllib.request

class Scraper:
   
   def getData(self):
      print("Coletando dados...")
      soup = BeautifulSoup(urllib.request.urlopen('http://mapas-hidro.ana.gov.br/Usuario/DadoPesquisar.aspx?est=150358540&dado=Chuva&fim=636554214000000000').read(), "html.parser")
      table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="grd") 
      rows = table.findAll(lambda tag: tag.name=='tr')
      #remove a primeira linha correspondente ao título das colunas
      rows.pop(0)
      values_guap=[]
      for row in rows:
         aux=[]
         cells = row.findChildren('td')
         if len(cells)==4:
             aux.append(cells[-2].getText())
             aux.append(cells[-1].getText())
             values_guap.append(aux)

      #UHE COLIDER METEOROLÓGICA
      soup = BeautifulSoup(urllib.request.urlopen("http://mapas-hidro.ana.gov.br/Usuario/DadoPesquisar.aspx?est=105755460&dado=Chuva&fim=636553728000000000").read(), "html.parser")
      table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="grd") 
      rows = table.findAll(lambda tag: tag.name=='tr')
      rows.pop(0)
      values_colider=[]
      for row in rows:
         aux=[]
         cells = row.findChildren('td')
         if len(cells)==4:
             aux.append(cells[-2].getText())
             aux.append(cells[-1].getText())
             values_colider.append(aux)
      print("Dados coletados")
      return values_guap,values_colider


#o site da um link diferente pra cada dia em que o acesso é realizado
#então o programa não está pegando dados em tempo real
#e sim pegando todos 4 dias antes do dia 28, (acessado 28/01)
#http://mapas-hidro.ana.gov.br/Usuario/DadoPesquisar.aspx?est=150358540&dado=Chuva&fim=636554214000000000
#http://mapas-hidro.ana.gov.br/Usuario/DadoPesquisar.aspx?est=150358540&dado=Chuva&fim=636555870000000000
   
