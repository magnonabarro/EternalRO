# Loja de ROPs por SQL

Tabela usada pelo map-server: cashshop_catalog (tab, nameid, price).
Abas: 0 New, 1 Hot, 2 Limited, 3 Rental, 4 Permanent, 5 Scrolls, 6 Consumables, 7 Other, 8 Sale.
O arquivo db/import/item_cash.yml foi preservado como referencia/rollback; o novo executavel nao o carrega para a loja.
Ofertas programadas continuam usando a tabela sales para inicio, fim e estoque.

## Publicacao em hospedagens diferentes
- Importar cashshop_catalog_export.sql no banco char/map usado pelo servidor.
- Configurar esse mesmo banco no FluxCP (charMapDatabase e credenciais de conexao).
- Autorizar o acesso do IP do site ao MySQL por conexao privada/tunel ou TLS conforme a hospedagem.
- Copiar modules/rops, views themes/revolutionro/rops e themes/default/rops e manter as entradas de acesso/menu.
- O site nao necessita dos arquivos locais do servidor. O catalogo de busca vem de cp_rops_catalog_items.
- Ao cadastrar novos itens no emulador, atualizar cp_rops_catalog_items com os mesmos IDs/nomes. Essa tabela e apenas de busca; o map-server valida os IDs contra o item_db real.

## Operacao
Salvar no painel, executar @reloadcashdb como GM, sair da conta e entrar novamente para atualizar o cache do cliente.
Gravacoes usam transacao InnoDB, lock de versao, CSRF e auditoria cp_rops_audit com snapshot anterior.
O painel nao executa comandos no servidor remotamente.

## Falhas e reversao
Falha na leitura SQL preserva o catalogo ja carregado em memoria; na primeira inicializacao uma falha deixa a loja vazia e registra erro. Nao existe fallback silencioso para YAML.
Antes de alterar schema, manter backup SQL. Para rollback completo, restaurar o executavel anterior, os arquivos PHP salvos e o item_cash.yml preservado.
