# omie-notas-fiscais

<h1>Omie API - Listagem de Notas Fiscais<</h1>
  <p>
 um script Python para acessar a API da Omie e listar as notas fiscais emitidas entre janeiro e maio de 2024. Utiliza a função ListarNF da API, paginando os resultados para garantir a coleta completa dos dados de todas as notas fiscais, sem limites de registros por página.</p>

<h1>Funcionalidades</h1>
<p>Conecta à API da Omie usando requests.></p>
<p>Faz a chamada da função ListarNF para obter as notas fiscais entre o período especificado.</p>
<p>Pagina os resultados, garantindo que todas as notas fiscais sejam recuperadas, mesmo que o número de registros exceda o limite de 100 por página.</p>
<p>Exporta os dados coletados para os formatos CSV, JSON e Excel.</p>

<h1>Tecnologias Utilizadas</h1>
<ul>
  <li>Python: Linguagem de programação usada para acessar a API e processar os dados.</li>
    <li>requests: Biblioteca para fazer requisições HTTP.</li>
    <li>pandas: Biblioteca para manipulação de dados e exportação para diferentes formatos (CSV, JSON, Excel).</li>
</ul>

<h1>Como Rodar</h1>
Clone o repositório:



git clone https://github.com/SEU_USUARIO/omie-api-integration.git

<h3>Instale as dependências:</h3>

pip install requests pandas
Execute o script:


python omie_nf_listagem.py
<p>Após a execução, os arquivos de saída (CSV, JSON, Excel) estarão na pasta do repositório.</p>


