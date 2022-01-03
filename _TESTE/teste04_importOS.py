# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

def testeImportOsPowershell():
    import os

    os.system('compmgmt.msc')
    # os.system('get-process')

testeImportOsPowershell()
