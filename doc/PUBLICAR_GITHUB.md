# Publicação no GitHub

O servidor local utiliza a branch `master` e o remoto `origin` aponta para `https://github.com/magnonabarro/EternalRO`. O repositório remoto também tem uma branch `main`; enviar para `master` atualiza somente `master`. Confira a branch selecionada na página do GitHub ao consultar os arquivos.

## Antes de adicionar arquivos

- Versione as personalizações de `db/import`, `src/custom` e os scripts e configurações de jogabilidade.
- Mantenha conexões, credenciais e endereços da instalação nos arquivos privados de `conf/import`. Os modelos públicos ficam em `conf/import-examples`.
- Não use `git add -f` para contornar as exclusões de backups, logs, executáveis ou configurações privadas.
- As regras do `.gitignore` não retiram do histórico conteúdo que já foi publicado. Esta organização não reescreve o histórico remoto.
- As cópias antigas `src - Copia` e `db - Copia` foram retiradas do índice Git, sem apagar as cópias existentes no computador. As exclusões desses diretórios no próximo commit são esperadas.
- Outras exclusões já pendentes, como antigos scripts de `npc/custom`, foram preservadas para revisão; nenhum arquivo foi restaurado ou apagado automaticamente.

## Revisão

No PowerShell, dentro da pasta do servidor:

```powershell
git status --short
git diff --stat
git diff --cached --stat
```

As alterações locais foram preparadas no índice durante a organização, incluindo as remoções das cópias antigas e as demais exclusões feitas pelo administrador. Confira o diff preparado antes de criar o commit.

Para preparar um arquivo ou uma pasta revisada, por exemplo:

```powershell
git add -- .gitignore README.md doc conf/import-examples
git add -- src/map src/custom db/import
git add -- conf/import/atcommands.yml conf/import/groups.yml
```

Esses comandos são exemplos de seleção, não uma lista completa de todas as personalizações. Revise também as alterações em `db/pre-re`, NPCs, `conf/battle`, configurações gerais e migrações SQL. Se desejar registrar as exclusões antigas, use `git add -u` somente depois de conferir todas elas. Para conferir arquivos novos que serão incluídos, use `git status --short --untracked-files=all`.

Após revisar e selecionar tudo:

```powershell
git diff --cached --stat
git diff --cached
git commit -m "Organiza EternalRO e versiona personalizacoes"
git push origin master
```

Se o GitHub recusar o envio por histórico divergente, examine as diferenças e sincronize antes de reenviar. Não use `push --force` para resolver isso automaticamente.

O site e o cliente não são enviados por esses comandos, pois ficam fora da pasta deste repositório.

## Backup integral em Releases

Para guardar a pasta inteira, incluindo arquivos ignorados, use o ZIP de backup anexado à Release correspondente. O código em `master` mantém os filtros de arquivos privados e temporários; o ZIP é uma cópia separada de todos os arquivos da pasta, exceto metadados `.git`. O administrador solicitou explicitamente a inclusão das configurações locais nesse anexo público.

O manifesto lista os arquivos do backup e seus hashes. O SHA256 do ZIP permite conferir o download. A pasta do MySQL e outros diretórios externos ao servidor não integram esse backup.
