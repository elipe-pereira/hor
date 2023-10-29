#### Hor

#### Descrição

  Hor é um sosftware que utiliza o clamav/clamscan para verificar e 
  remover arquivos infectados por vírus de acordo com as preferências do 
  usário. 

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
