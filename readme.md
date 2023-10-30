#### Hor

#### Descrição

Hor é um sosftware que utiliza o clamav/clamscan para verificar e 
remover arquivos infectados por vírus em sistemas operacionais Linux de acordo 
com as preferências do usário. 

Seu objetivo principal é automatizar a execução através do cron sem que sejam 
necessários inserir uma gama longa de parâmetros na linha de comando como quando 
usando o clamscam diretamente. 

Ele também incorpora pequenas funcionalidades adicionais como o envio de e-mail após a 
conclusão do scaneamento informando o cliente sobre a conclusão da verificação.

#### Uso

    ~# hor /tmp

Se for usado um parâmetro, este precisa ser uma pasta que deverá ser escaneada. Caso
essa pasta não exista, o programa irá informar que o arquivo ou pasta não existe. 

    ~# hor

Executar o hor sem parâmetro irá fazer com que o programa execute o escaneamento nas pastas
configuradas no arquivo de configuração. O Escaneamento será sequencial, sendo cada seção
configurada de cima pra baixo, também a ordem ao qual será executado o escaneamento.

##### cron

O pacote gerado pelo installer.sh também adiciona o arquivo hor.cron ao cron do sistema linux, sendo
a data padrão, todo sábado as 00:30 a execução agendada.

##### pyinstaller

Para utilizar o installer.sh, será necessário ter o pyinstaller rodando no seu computador. No linux,
o ideal é criar um ambiente virtual para instalar seus pacotes via pip. O modelo aqui passado é o 
recomendado, embora haja outras maneiras de efetuar a instalação do pyinstaller.

    ~# apt-get install python3-venv
    ~# apt-get install python3-pip
    ~# cd /opt
    ~# python3 -m venv venv
    ~# source /opt/venv/bin/activate
    (venv)~# pip install --upgrade pip
    (venv)~# pip install pyinstaller
    (venv)~# ln -s /opt/venv/bin/pyinstaller /usr/bin/pyinstaller
    (venv)# deactivate

É importante lembrar que ao usar o pyinstaller da maneira aqui proposta,
toda vez que houver dependências adicionais instaladas pelo pip, ao 
compilar usando o pyinstaller, esse pacotes de ser instalados pelo
pip no ambiente virtual onde se encontra o pyinstaller. 

Por exemplo, se se seu programa também depende do psycopg2 para poder
rodar:
    ~# apt-get install python3-dev
    ~# apt-get install libpq-dev
    ~# source /opt/venv/bin/activate
    (venv)~# pip install psycopg2

No exemplo acima, foi instalado o pyscopg2 dentro do ambiente virtual do
pyinstaller para que ao compilar seu programa via pyinstaller, não fique
faltando a adição das bibliotecas referentes ao psycopg2 na pasta resultante
da compilação do pyinstaller. 

Lembrando que, mesmo que falte bibliotecas adicionais ao compilar, o programa
será compilado, porém, ocorrerão erros na execução do código compilado, causado
pela falta das bibliotecas que não estavam no mesmo ambiente virtual do pyinstaller.

#### installer.sh

##### Baixando projeto
    ~# git clone git@github.com:elipe-pereira/hor.git
##### Dando permissão ao installer.sh
    ~# cd hor 
    ~# chmod +x installer.sh
##### Utilizando
    ~# ./installer.sh pack

O parâmetro pack compila o projeto e logo em seguida gera um pacote .deb dentro da pasta
raiz do projeto. Lembre-se que o pyinstaller precisa estar instalado como mostrado acima.

    ~# ./installer build

Somente compila o projeto e armazena o projeto compilado na pasta /tmp/build/dist. 
Lembre se de seguir o processo de instalação do pyinstaller explicado logo acima, 
para que não haja erros durante o build.

    ~# ./installer

Exibe uma mensagem de ajuda. assim como:
    ~$ ./installer help

Ambos, exibem a mesma mensagem. 

    ~# ./installer clear

Apaga a pasta /tmp/build, que é onde ficam armazenados os arquivos 
resultantes do empacotamento e build. Sempre é bom executar esse 
comando se deseja fazer um novo build ou se simplesmente deseja 
limpar arquivos que não são mais necessários. 

#### Instalando pacote deb gerado
    ~# apt-get install ./hor_x.x.x_amd64.deb
  
Faz a instalação via apt do arquivo .deb local.
