import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print(f'O site Pudim não está acessível nesse momento')
else:
    print('consegui acessar o site com sucesso.')
    print()
    # Com o comando abaixo é possível mostrar o conteúdo do site.
    print(site.read())

"""
TAGS:
- Testar conexão urllib.
- Verificar conteúdo do site.
"""