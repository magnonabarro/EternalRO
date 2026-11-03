# Caçadas do Éden

As sete placas anteriores foram substituídas nas mesmas coordenadas. O nível indicado é uma categoria de dificuldade, não um limite máximo: um personagem 99 pode usar todas as placas. A Marca do Grupo Éden continua necessária.

| Categoria | Nível mínimo | Alvos por caçada | Moedas | EXP base | EXP classe |
|---|---:|---:|---:|---:|---:|
| Iniciante (11–25) | 11 | 20 | 2 | 1.800 | 450 |
| Aprendiz (26–40) | 26 | 30 | 4 | 5.000 | 1.250 |
| Intermediária (41–55) | 41 | 40 | 6 | 15.000 | 3.750 |
| Avançada (56–70) | 56 | 50 | 8 | 30.000 | 7.500 |
| Veterana (71–85) | 71 | 60 | 10 | 60.000 | 15.000 |
| Elite (86–90) | 86 | 70 | 12 | 100.000 | 25.000 |
| Mestre (91–99) | 91 | 80 | 15 | 140.000 | 35.000 |

Cada categoria oferece cinco monstros no fluxo simples original: escolha uma caçada e aceite. É possível iniciar somente uma caçada por vez; não há menus para aceitar ou receber em lote. Durante uma missão, as opções são continuar, teleportar ou cancelar essa missão. As mortes são contadas pelo mecanismo nativo de quests, após a aceitação. A recompensa é retirada individualmente em qualquer placa acessível. A espera para repetir o mesmo alvo é de três horas após o recebimento; outros alvos ficam disponíveis. A moeda é Para_Team_Coin (25223), usada pelas lojas uniao_top, uniao_mid e uniao_baixo. EXP segue os ajustes normais do comando getexp do servidor. Registros previamente aceitos durante a versão com várias caçadas não são apagados; ficam disponíveis para conclusão individual.

O teleporte é opcional e gratuito após aceitar uma missão ou durante a missão atual. O destino é calculado pelo gerador a partir dos arquivos NPC incluídos em npc/pre-re/scripts_main.conf: soma os spawns de cada alvo por mapa, escolhe a maior população e desempata pelo nome do mapa. Mapas de instância, PvP/GvG, restritos e com nowarpto são excluídos. Destinos definidos em DESTINOS_PREFERIDOS no gerador têm prioridade, desde que possuam spawn público ativo do alvo. Guerreiro Orc foi definido para gef_fild10 por solicitação do administrador. Os números representam a população configurada, não a quantidade viva no momento. Ao teleportar, o script também respeita nowarp na origem e nowarpto no destino. Se mudar os spawns, execute novamente o gerador e recarregue o servidor. A conferência dos 35 alvos fica em doc/EDEN_DESTINOS.md.

## Arquivos

- `db/import/quest_db.yml`: importa o arquivo específico do Éden.
- `db/import/quests/eden_cacadas.yml`: 35 caçadas (61000–61034), com Targets/Mob/Count, e 35 esperas (61100–61134), com TimeLimit +3h.
- `npc/pre-re/eternalro/quests/eden/eden_cacadas.txt`: quadros e resgate. Recompensas e níveis ficam no OnInit de EdenCacadas.
- `npc/pre-re/scripts_eternal.conf`: carrega os novos quadros e desativa os sete arquivos antigos. Outros NPCs do Éden continuam carregados.
- `tools/eden/gerar_cacadas.py`: catálogo dos monstros e gerador sincronizado de quest_db, arrays de alvos/destinos do NPC e descrições do cliente. Os títulos seguem Quest do Éden [faixa] - monstro.

O gerador usa PyYAML e o cliente local em PATH 2026. Para mudar monstros, quantidades ou recompensas, edite GROUPS/COUNTS/COINS/BEXP/JEXP no gerador e execute-o. Ele sincroniza o quest_db, os arrays do NPC e as descrições do cliente. Os arquivos legados foram preservados, e registros de quests antigas dos personagens não são apagados ou convertidos automaticamente.

## Aplicação e conferência

Reinicie o map-server e feche completamente/abra o cliente para carregar os novos scripts, banco de quests e descrições de Alt+U. Não requer recompilar. No jogo: aceite uma caçada, confira o contador em Alt+U, use o teleporte opcional, elimine o alvo e retire a recompensa no quadro. Uma segunda tentativa de resgate não deve pagar novamente. Nível 40 acessa as categorias 11 e 26; nível 99 acessa todas; nível 10 não aceita nenhuma. Cada escolha inicia apenas uma missão.

Os arquivos OngoingQuestInfoList em System/SystemEN, SystemEN/OngoingQuests e questinfo/questinfo_f no cliente receberam as novas descrições. As consultas de informações das quests reaplicam somente os IDs do Éden para evitar títulos antigos de outra tabela de idioma. Arquivos compilados originais foram preservados com sufixo `_eden_base.lub` e são carregados antes das novas entradas. Backups da implantação inicial estão em `backups/eden_cacadas_20261102_202040` e da ampliação em `backups/eden_multicacadas_20261102_203847`.
