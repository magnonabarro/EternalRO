# EternalRO

Servidor de Ragnarok Online baseado em **rAthena pré-renovação**, com nível máximo 99 e sistemas personalizados.

## Organização

| Pasta | Conteúdo |
|---|---|
| `src/map` e `src/custom` | Código do emulador e extensões do servidor |
| `npc/pre-re/eternalro` | Sistemas, eventos, instâncias e NPCs personalizados |
| `db/pre-re` e `db/import` | Bases do jogo e sobreposições personalizadas |
| `conf` | Configurações gerais e exemplos padrão do rAthena |
| `conf/import` | Ajustes locais; apenas comandos, grupos e configurações de jogabilidade são versionados |
| `conf/import-examples` | Modelos sem credenciais reais para configurar uma instalação |
| `sql-files` | Estruturas e migrações SQL; não são backups das contas dos jogadores |
| `tools/eden` | Gerador das caçadas, objetivos e descrições do Éden |
| `doc` | Documentação do servidor |

Os arquivos principais de configuração ainda contêm valores padrão do rAthena. Defina suas conexões e senhas nos arquivos privados de `conf/import`, sem acrescentar credenciais aos arquivos versionados. Backups, árvores duplicadas, executáveis, símbolos de depuração e logs ficam somente no computador.

## Configuração de uma nova instalação

1. Clone este repositório e consulte os requisitos do rAthena para seu sistema operacional.
2. Copie os modelos de `conf/import-examples` para `conf/import`, retirando `.example` do nome. **Não substitua configurações locais que já existam.** Configure endereços, banco e credenciais nessa cópia privada.
3. Importe as estruturas necessárias de `sql-files` em um banco novo. Em bancos existentes, aplique somente migrações compatíveis, com backup prévio.
4. No Windows, abra `rAthena.sln` no Visual Studio, selecione **Release / x64** e compile a solução.
5. Inicie login-server, char-server e map-server conforme suas configurações. Verifique os logs de carregamento antes de disponibilizar o servidor.

O cliente do jogo e o site FluxCP ficam em pastas separadas e **não fazem parte deste repositório**. A instalação deles requer seus próprios arquivos e configurações. Os scripts do Éden que geram textos de cliente precisam ter o caminho local `CLIENT` ajustado se a organização das pastas mudar.

## Backup integral da pasta

Além do código versionado, a seção **Releases** recebe o ZIP de backup integral solicitado pelo administrador. Esse anexo contém também arquivos locais ignorados pelo Git: executáveis, configurações da instalação, logs e pastas auxiliares presentes no momento da cópia. Os metadados internos `.git` ficam fora do ZIP. Consulte o manifesto e o arquivo SHA256 anexos para conferir a cópia.

O ZIP reflete somente a pasta do servidor. O conteúdo do MySQL, o cliente e o site ficam fora dessa pasta. Por conter configurações locais, trate o backup como material da instalação; neste repositório público, os anexos da Release também são públicos.

## Documentação das personalizações

- [Caçadas do Éden](doc/EDEN_CACADAS.md)
- [Destinos das caçadas](doc/EDEN_DESTINOS.md)
- [Loja de ROPs em SQL](sql-files/LOJA_ROPS_SQL.md)
- [Como revisar e publicar alterações no GitHub](doc/PUBLICAR_GITHUB.md)

## Licença

Este projeto mantém a licença do rAthena. Consulte [LICENSE](LICENSE).
