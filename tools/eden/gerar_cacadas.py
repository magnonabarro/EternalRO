"""Gera objetivos nativos, catalogo do NPC e textos do cliente sem sobrescrever outras quests."""
from pathlib import Path
import re
import shutil
from collections import defaultdict
import yaml

ROOT = Path(__file__).resolve().parents[2]
CLIENT = ROOT.parent.parent / 'PATH 2026'
BACKUP = ROOT / 'backups/eden_cacadas_20261102_202040'
MIN = [11, 26, 41, 56, 71, 86, 91]
COUNTS = [20, 30, 40, 50, 60, 70, 80]
COINS = [2, 4, 6, 8, 10, 12, 15]
BEXP = [1800, 5000, 15000, 30000, 60000, 100000, 140000]
JEXP = [450, 1250, 3750, 7500, 15000, 25000, 35000]
# Destinos escolhidos pelo administrador. A populacao e validada nos spawns ativos.
# gef_fild10 concentra a Vila dos Orcs: 20 Guerreiros + 70 Senhoras Orc.
DESTINOS_PREFERIDOS = {'ORK_WARRIOR': 'gef_fild10'}
GROUPS = [
    [('HORNET','Zangão'),('ROCKER','Rocker'),('SPORE','Esporo'),('WORM_TAIL','Cauda de Verme'),('PECOPECO','Peco Peco')],
    [('POISON_SPORE','Esporo Venenoso'),('SMOKIE','Smokie'),('ELDER_WILOW','Salgueiro Ancião'),('COCO','Coco'),('THARA_FROG','Sapo de Thara')],
    [('ORK_WARRIOR','Guerreiro Orc'),('ORC_LADY','Senhora Orc'),('SAVAGE','Selvagem'),('MUMMY','Múmia'),('MANTIS','Mantis')],
    [('SOHEE','Sohee'),('MUNAK','Munak'),('ZENORC','Zenorc'),('ISIS','Isis'),('ARGIOPE','Argiope')],
    [('PASANA','Pasana'),('MARDUK','Marduk'),('RAYDRIC','Raydric'),('DEVIRUCHI','Deviruchi'),('EVIL_DRUID','Druida Maligno')],
    [('NIGHTMARE_TERROR','Pesadelo Sombrio'),('DELETER','Deletério Voador'),('DELETER_','Deletério Terrestre'),('MAJORUROS','Majoruros'),('ANOLIAN','Anolian')],
    [('KNIGHT_OF_ABYSS','Cavaleiro do Abismo'),('INCUBUS','Incubus'),('SUCCUBUS','Succubus'),('OWL_DUKE','Duque Coruja'),('OWL_BARON','Barão Coruja')],
]

def spawn_destinations():
    """Conta somente declaracoes de spawn dos arquivos NPC efetivamente incluidos."""
    seen = set()
    population = defaultdict(lambda: defaultdict(int))
    blocked = set()
    def walk(relative):
        path = (ROOT / relative).resolve()
        if not path.exists() or path in seen:
            return
        seen.add(path)
        text = path.read_bytes().decode('cp1252', errors='replace')
        text = re.sub(r'/\*.*?\*/', lambda match: '\n'*match[0].count('\n'), text, flags=re.S)
        for raw in text.splitlines():
            line = raw.split('//', 1)[0].strip()
            include = re.match(r'(?:import|npc):\s*(.+)', line)
            if include:
                walk(include[1].strip())
                continue
            spawn = re.match(r'([^,\s]+),[^\t]*\t(?:monster|boss_monster)\t[^\t]*\t(\d+),(\d+)', line)
            if spawn:
                population[int(spawn[2])][spawn[1]] += int(spawn[3])
            flag = re.match(r'(\S+)\s+mapflag\s+(nowarpto|pvp|gvg|gvg_castle|restricted)(?:\s|$)', line)
            if flag:
                blocked.add(flag[1])
    walk('npc/pre-re/scripts_main.conf')
    return {mob: sorted(((count, name) for name, count in maps.items()
                         if name not in blocked and '@' not in name),
                        key=lambda entry: (-entry[0], entry[1]))
            for mob, maps in population.items()}

def patch_block(path, block, start, end, encoding):
    text = path.read_text(encoding=encoding)
    if start in text:
        text = re.sub(re.escape(start)+r'.*?'+re.escape(end), lambda _: block, text, flags=re.S)
    else:
        text += '\n'+block+'\n'
    path.write_text(text, encoding=encoding)

def generate():
    mobs = {row['AegisName']: row for row in yaml.safe_load((ROOT/'db/pre-re/mob_db.yml').read_text(encoding='utf8'))['Body']}
    hunt_ids = set(range(61000,61035)) | set(range(61100,61135))
    for path in [ROOT/'db/pre-re/quest_db.yml', ROOT/'db/re/quest_db.yml', ROOT/'db/import/quest_db.yml']:
        for row in yaml.safe_load(path.read_text(encoding='utf8')).get('Body',[]) or []:
            if row['Id'] in hunt_ids:
                raise ValueError(f'ID {row["Id"]} já usado em {path}')
    destinations = spawn_destinations()
    quests, catalog, client_entries, audit = [], [], [], []
    coords=[(36,38),(38,38),(40,38),(42,38),(44,38),(48,175),(48,177)]
    for tier, group in enumerate(GROUPS):
        for target, name in group:
            index=len(catalog); qid=61000+index; cool=61100+index
            mob=mobs[target]; count=COUNTS[tier]
            upper = MIN[tier+1]-1 if tier<6 else 99
            title = f'Quest do Éden [{MIN[tier]}-{upper}] - {name}'
            wait_title = f'Espera Éden [{MIN[tier]}-{upper}] - {name}'
            quests.append({'Id':qid,'Title':title, 'Targets':[{'Mob':target,'Count':count}]})
            quests.append({'Id':cool,'Title':wait_title, 'TimeLimit':'+3h'})
            available = destinations.get(mob['Id'], [])
            if not available:
                raise ValueError(f'Sem spawn publico carregado para {target}')
            map_count, map_name = available[0]
            preferred = DESTINOS_PREFERIDOS.get(target)
            if preferred:
                match = next((entry for entry in available if entry[1] == preferred), None)
                if not match:
                    raise ValueError(f'Destino preferido {preferred} sem spawn publico ativo de {target}')
                map_count, map_name = match
            audit.append((qid, name, map_name, map_count, 'Preferido pelo administrador' if preferred else 'Maior quantidade do alvo', available))
            catalog.append((qid,cool,mob['Id'],name,count,map_name,map_count))
            x,y=coords[tier]
            def quote(value): return '"'+str(value).replace('\\','\\\\').replace('"','\\"')+'"'
            shared=f'IconName = "", NpcSpr = "", NpcNavi = "moc_para01", NpcPosX = {x}, NpcPosY = {y}'
            desc=f'Derrote {count} {name}. Nível mínimo: {MIN[tier]}. Volte a um quadro do Éden para receber {COINS[tier]} moedas. Teleporte opcional no quadro para {map_name} ({map_count} spawns). Uma caçada ativa por vez.'
            client_entries.append(f'edenQuestInfo[{qid}] = {{Title = {quote(title)}, Summary = {quote(str(count)+" "+name)}, Description = {{{quote(desc)}}}, {shared}, RewardEXP = {BEXP[tier]}, RewardJEXP = {JEXP[tier]}, CoolTimeQuest = {cool}, RewardItemList = {{{{ItemID = 25223, ItemNum = {COINS[tier]}}}}}}}')
            client_entries.append(f'edenQuestInfo[{cool}] = {{Title = {quote(wait_title)}, Summary = "Aguarde 3 horas", Description = {{"Você pode aceitar esta caçada novamente após o tempo de espera. Outras caçadas continuam disponíveis."}}, {shared}, RewardEXP = 0, RewardJEXP = 0, CoolTimeQuest = 0, RewardItemList = {{}}}}')
    out=ROOT/'db/import/quests/eden_cacadas.yml';out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text('# Caçadas 61000-61034; espera individual 61100-61134.\n# Objetivos nativos: sem contadores por OnNPCKillEvent.\n'+yaml.safe_dump({'Header':{'Type':'QUEST_DB','Version':3},'Body':quests},allow_unicode=True,sort_keys=False),encoding='utf8')
    report = ['# Destinos das caçadas do Éden', '',
              'Gerado a partir dos scripts NPC realmente importados em npc/pre-re/scripts_main.conf (pré-renovação). Contagem por ID exato do monstro, não pela soma de monstros de nomes semelhantes. Apenas spawns estáticos públicos; não representa a população viva naquele instante.', '',
              'Guerreiro Orc usa gef_fild10 por escolha do administrador. Os scripts atuais têm 60 Guerreiros em gef_fild02 e gef_fild03, e 20 em gef_fild10; neste último também existem 70 Senhoras Orc. Essas declarações usam o tempo padrão de reaparecimento (sem atraso próprio no arquivo). Nenhuma população foi alterada.', '',
              '| Quest | Alvo | Destino | População do alvo | Critério | Alternativas (população) |',
              '|---:|---|---|---:|---|---|']
    for qid, name, dest, population, reason, options in audit:
        alternatives = ', '.join(f'{m} ({n})' for n, m in options[:3])
        report.append(f'| {qid} | {name} | {dest} | {population} | {reason} | {alternatives} |')
    (ROOT/'doc/EDEN_DESTINOS.md').write_text('\n'.join(report)+'\n', encoding='utf8')
    arrays=[]
    for offset, var in [(0,'Quest'),(1,'Cooldown'),(2,'Mob'),(3,'Name$'),(4,'Count'),(5,'Map$'),(6,'MapCount')]:
        vals=[quote(c[offset]) if offset in (3,5) else str(c[offset]) for c in catalog]
        arrays.append('\tsetarray .'+var+'[0],'+','.join(vals)+';')
    npc=ROOT/'npc/pre-re/eternalro/quests/eden/eden_cacadas.txt'
    raw=npc.read_bytes()
    try: raw.decode('utf8'); enc='utf8'
    except UnicodeDecodeError: enc='cp1252'
    text=raw.decode(enc)
    for var, values in [('Min', MIN), ('Coins', COINS), ('BaseExp', BEXP), ('JobExp', JEXP)]:
        text=re.sub(r'\tsetarray \.'+var+r'\[0\],[^;]+;',lambda _: '\tsetarray .'+var+'[0],'+','.join(map(str,values))+';',text)
    text=re.sub(r'\t// BEGIN GENERATED HUNT CATALOG.*?\t// END GENERATED HUNT CATALOG',lambda _: '\t// BEGIN GENERATED HUNT CATALOG\n'+'\n'.join(arrays)+'\n\t// END GENERATED HUNT CATALOG',text,flags=re.S)
    npc.write_text(text,encoding='cp1252')
    start='-- BEGIN EDEN CACADAS';end='-- END EDEN CACADAS'
    wrappers='''
for id, info in pairs(edenQuestInfo) do QuestInfoList[id] = info end
-- Reaplica somente as quests do Eden quando o cliente consulta outra tabela de idioma.
for _, name in ipairs({"GetOngoingQuestInfoByID", "GetOngoingDescription", "GetOngoingRewardInfo", "GetCoolTimeQuest"}) do
    local original = _G[name]
    if type(original) == "function" then
        _G[name] = function(questID, ...)
            if edenQuestInfo[questID] then
                QuestInfoList = QuestInfoList or {}
                QuestInfoList[questID] = edenQuestInfo[questID]
            end
            return original(questID, ...)
        end
    end
end
'''
    block=start+'\ndo\nQuestInfoList = QuestInfoList or {}\nlocal edenQuestInfo = {}\n'+'\n'.join(client_entries)+'\n'+wrappers+'end\n'+end
    targets=['System/OngoingQuestInfoList.lub','System/OngoingQuestInfoList.lua','SystemEN/OngoingQuestInfoList.lub','SystemEN/OngoingQuests.lub','data/luafiles514/lua files/datainfo/questinfo.lub','data/luafiles514/lua files/datainfo/questinfo.lua','data/luafiles514/lua files/datainfo/questinfo_f.lub','data/luafiles514/lua files/datainfo/questinfo_f.lua']
    for rel in targets:
        path=CLIENT/rel
        if not path.exists(): continue
        saved=BACKUP/'client'/rel;saved.parent.mkdir(parents=True,exist_ok=True)
        if not saved.exists(): shutil.copy2(path,saved)
        raw=path.read_bytes()
        if raw.startswith(b'\x1bLua'):
            base=path.with_name(path.stem+'_eden_base'+path.suffix)
            if not base.exists(): shutil.copy2(path,base)
            base_rel=base.relative_to(CLIENT).as_posix()
            path.write_text('assert(loadfile("'+base_rel+'"))()\n',encoding='cp1252')
            enc='cp1252'
        else:
            try: raw.decode('utf8'); enc='utf8'
            except UnicodeDecodeError: enc='cp1252'
        patch_block(path,block,start,end,enc)
    print('35 caçadas + 35 esperas geradas; NPC e descrições do cliente sincronizados.')

if __name__ == '__main__': generate()
