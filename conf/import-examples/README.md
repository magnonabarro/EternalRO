# Configurações privadas

Copie cada modelo para `conf/import` e retire o sufixo `.example`. Edite somente a cópia privada. Não substitua arquivos que já contenham a configuração de uma instalação existente.

Os textos `CHANGE_ME_USER` e `CHANGE_ME_PASSWORD` são placeholders, não credenciais de uma instalação. Ajuste banco, senhas, endereços e portas antes de iniciar o servidor.

Os arquivos de conexão em `conf/import` são ignorados pelo Git. Já `atcommands.yml`, `groups.yml`, `battle_conf.txt`, `packet_conf.txt` e `script_conf.txt` nessa pasta são versionados, pois guardam personalizações de jogabilidade. Não coloque segredos nesses arquivos.

Os arquivos principais em `conf` mantêm os exemplos padrão do rAthena. Seus ajustes privados devem entrar na importação correspondente para que não seja necessário publicar as credenciais.
