# fapespbolsaclimatempo

O programa atualmente conta com 3 classes:

Scrape - > Utiliza beautifulSoup4 e urllib para acessar o link correspondente ao sensor escolhido

Plot - > utiliza matplotlib para realizar o trabalho de vizualização e de conversão dos valores para um formato desejado

MongoManage - > é responsável por criar a conexão e controlar as operações de inserção e busca no banco utilizando pymongo

main - > fluxo de execução padrão

Observações
Os dados são adquiridos na página da ANA e o link armazenado foi selecionado baseado no dia do início do projeto, 
O link que foi escolhido para coletar dados para o sempre oferece as medições do mesmo dia
Nenhum parâmatro foi encontrado dentro da estrutura do link para automatizar a busca sempre para o dia atual
