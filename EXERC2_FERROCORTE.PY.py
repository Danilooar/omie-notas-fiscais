


import requests
import pandas as pd


url = "https://app.omie.com.br/api/v1/produtos/nfconsultar/"
headers = {
    'Content-type': 'application/json'
}
app_key = "38333295000"
app_secret = "fed2163e2e8dccb53ff914ce9e2f1258"
dEmiInicial = "01/01/2024"
dEmiFinal = "31/05/2024"
registros_por_pagina = 100


notas_fiscais = []


pagina = 1
mais_paginas = True


while mais_paginas:
    data = {
        "call": "ListarNF",
        "app_key": app_key,
        "app_secret": app_secret,
        "param": [{
            "pagina": pagina,
            "registros_por_pagina": registros_por_pagina,
            "apenas_importado_api": "N",
            "ordenar_por": "CODIGO",
            "dEmiInicial": dEmiInicial,
            "dEmiFinal": dEmiFinal
        }]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        nf_cadastro = response_data.get('nfCadastro', [])

     
        if nf_cadastro:
            print(f"Coletando dados da página {pagina}...")  
        
            for nf in nf_cadastro:
                nota = {
                    'nIdNF': nf.get('nIdNF', ''),
                    'nIdPedido': nf.get('nIdPedido', ''),
                    'nNF': nf.get('ide', {}).get('nNF', ''),
                    'dEmi': nf.get('ide', {}).get('dEmi', ''),
                    'vTotTrib': nf.get('total', {}).get('ICMSTot', {}).get('vTotTrib', 0.0),
                    'vNF': nf.get('total', {}).get('ICMSTot', {}).get('vNF', 0.0),
                    'cRazao': nf.get('nfDestInt', {}).get('cRazao', ''),
                    'cnpj_cpf': nf.get('nfDestInt', {}).get('cnpj_cpf', ''),
                    'xProd': nf.get('det', [{}])[0].get('prod', {}).get('xProd', ''),
                    'vProd': nf.get('det', [{}])[0].get('prod', {}).get('vProd', 0.0),
                    'vDesc': nf.get('det', [{}])[0].get('prod', {}).get('vDesc', 0.0)
                }
                notas_fiscais.append(nota)
                
                
                print(nota)

     
            pagina += 1
        else:
        
            print(f"Todas as notas fiscais foram coletadas até a página {pagina - 1}.")
            mais_paginas = False
    else:
        print(f"Erro ao acessar a API: {response.status_code} - {response.text}")
        mais_paginas = False


if notas_fiscais:

    df = pd.DataFrame(notas_fiscais)


    df.to_csv('notas_fiscais.csv', index=False)
    df.to_json('notas_fiscais.json', orient='records', lines=True)
    df.to_excel('notas_fiscais.xlsx', index=False)

    print("Dados exportados com sucesso!")
else:
    print("Não foram encontradas notas fiscais.")






