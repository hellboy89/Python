"""
Preciso montar uma rotina de backup para envio de dados para o S3 do Big File. Para isso preciso seguir alguns passos.

() - Abrir conexão no bucket do S3
() - Criar o diretório no bucket com a data atual como nome.
() - Copiar tudo que tem no diretório D: que tenham as extenções dbf,cdx,fpt,dbc,dct,dcx... Para a pasta do bucket acima.
() - Depois disso irá analisar se não tem arquivos de mais de 7 dias atrás. Pegando pela data do nome da pasta.
() - Irá salvar toda essa saída num diretório como log, em arquivo .txt.
"""

