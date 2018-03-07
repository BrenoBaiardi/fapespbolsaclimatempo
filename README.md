# fapespbolsaclimatempo

O programa atualmente conta com 3 classes e depende do servidor mongod estar sendo executado na máquina com configurações padrão:

Scrape - > Utiliza beautifulSoup4 e urllib para acessar o link correspondente ao sensor escolhido

Plot - > utiliza matplotlib para realizar o trabalho de vizualização e de conversão dos valores para um formato desejado

MongoManage - > é responsável por criar a conexão e controlar as operações de inserção e busca no banco utilizando pymongo

main - > fluxo de execução padrão

Observações
Os dados são adquiridos na página da ANA e o link armazenado foi selecionado baseado no dia do início do projeto, 
O link que foi escolhido para coletar dados para o sempre oferece as medições do mesmo dia
Nenhum parâmatro foi encontrado dentro da estrutura do link para automatizar a busca sempre para o dia atual

INSTALAÇÂO:

Para a execução das classe main é necessária a intalação de python 3.5 ou mais recente 
incluindo os seguintes comandos no terminal para carregar os módulos 
utilizados pelas classes auxiliares:

pip install pymongo
pip install matplotlib
pip install beautifulsoup4

*os outros módulos utilizados devem ser nativos da instalação de python 3

Será necessário instalar o programa MongoDB community server pelo seguinte link:
https://www.mongodb.com/download-center?jmp=nav#community

Após a instalação dento da pasta especificada executar o programa encontrado em ...bin/mongod.exe
que vai abrir as conexões com o banco e esperar os comandos vindo das classes em python

Após certificar se que o mongod está rodando sem erros, executar main.py com python