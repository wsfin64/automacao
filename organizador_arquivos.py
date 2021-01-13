import os
from os import listdir


user = os.getlogin()

system = os.name  


#######################  VERIFICANDO O SISTEMA OPERACIONAL  #################################

if system == 'posix':

    ####################### Verificando o idioma do sistema ###############################

    if os.getenv('LANG') == 'pt_BR.UTF-8':    

        DOWNLOADS_DIR = f"/home/{user}/Downloads/"

        IMAGENS_DIR = f"/home/{user}/Imagens/"

        VIDEOS_DIR = f"/home/{user}/Vídeos/"

    else:
        DOWNLOADS_DIR = f"/home/{user}/Downloads/"

        IMAGENS_DIR = f"/home/{user}/Pictures/"

        VIDEOS_DIR = f"/home/{user}/Videos/"
else:

    DOWNLOADS_DIR = f"C:/Users/{user}/Downloads/"

    IMAGENS_DIR = f"C:/Users/{user}/Pictures/"

    VIDEOS_DIR = f"C:/Users/{user}/Videos/"


###################### Percorrendo os arquivos ########################################


files = listdir(DOWNLOADS_DIR)
cont = 0


for i in range(len(files)):
    if files[i].endswith('.jpg') or files[i].endswith('.png') or files[i].endswith('.gif'):
        caminho_arquivo = os.path.join(DOWNLOADS_DIR, files[i])
        os.system(f"mv {caminho_arquivo} {IMAGENS_DIR}")
        print(f"{files[i]} movido!")
        cont += 1
    
    elif files[i].endswith('.mp4') or files[i].endswith('.mkv'):
        caminho_arquivo = os.path.join(DOWNLOADS_DIR, files[i])
        os.system(f"mv {caminho_arquivo} {VIDEOS_DIR}")
        print(f"{files[i]} movido!")
        cont += 1


print(f"Tarefa finalizada, foram movidos {cont} arquivos")
