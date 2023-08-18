### Changelog
### Hor

#### [Released] - 2023-08-18
#### [0.5.0]
##### Added
- Adicionado novo parametro no arquivo de configuração chamado servername para dar
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
