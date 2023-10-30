### Changelog
### Hor

#### [Released]
#### [0.7.0] - 2023-10-29
##### Added
 - Adicionado função de ajuda no script de instalação e tornado
 opção help como default.

#### [Released]
#### [0.6.1] - 2023-10-29
##### Fixed
 - Adicionado mensagem de erro quando a pasta informada como parâmetro no 
 escaneamento rápido não existe.

#### [Released]
#### [0.6.0] - 2023-10-09
##### Added
- Adicionado opção de escaneamento rápido, ignorando arquivo de configuração. 

#### [Released] - 2023-08-30
#### [0.5.3]
#### Fixed
- Ajustado para que antivirus não escaneie uma segunda vez os arquivos na pasta de infectados.

#### [Released] - 2023-08-18
#### [0.5.2]
##### Fixed
- Adicionado parãmetro pra evitar mensagem de erro ao enviar e-mail.

#### [Released] - 2023-08-18
#### [0.5.1]
##### Fixed
- Ajustado nome incorreto de variável.
- Ajustado também a busca pelo nome do correto
no arquivo de configuração.

#### [Released] - 2023-08-18
#### [0.5.0]
##### Added
- Adicionado novo parametro no arquivo de configuração chamado hostname para dar
suporte ao envio de e-mail com o nome do servidor no assunto.
##### Changed
- Alterado assunto do e-mail para conter nome do servidor e nome da rotina de scan.

#### [Released]
#### [0.4.0] - 2023-08-13
##### Changed
- Adicionado mensagem para indicando o fim da execução e também quando não há configuração criada.

#### [Released]
#### [0.3.1] - 2023-08-12
##### Changed
- Adicionado encoding ao read do configparser.
- Ajustado para excluir a pasta /sys dos scans por padrão.

#### [Released]
#### [0.3.0] - 2023-08-12
##### Added
- Adicionado arquivo de configuração cron para executar.
tarefas uma vez por semana. 

#### [Released]
#### [0.2.3] - 2023-08-07
##### Fixed
- Adicionado nome da pasta escaneada no assunto.

#### [Released]
#### [0.2.2] - 2023-08-07
#### Fixed
- Ajustado comando pra ter suporte de execução em múltiplas linhas

#### [Released]
#### [0.2.1] - 2023-08-07
#### Fixed
- Adicionado campo assunto no e-mail relatório.
- Ajustado para mostrar no e-mail somente arquivos 
  infectados e o relatório final do scan.

#### [Released]
#### [0.2.0] - 2023-08-07
##### Added
- Envio de e-mail para o administrador mostrando relatório do scanner.

#### [Released]
#### [0.1.1] - 2023-07-30
##### Fixed
- Ajustado erros nos nomes de variáveis.
- Ajustado erros no nome do caminho de arquivo.

#### [Released]
#### [0.1.0] - 2023-07-24
##### Added
- Scanner de vírus.
- Arquivo de configuração com parâmetros de execução.
- Opção de apagar arquivos infectados no arquivo de configuração.
- Move arquivos infectados para diretório (infected_files) dentro da pasta do projeto.
