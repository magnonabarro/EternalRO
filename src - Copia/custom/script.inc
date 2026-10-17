// Copyright (c) rAthena Dev Teams - Licensed under GNU GPL
// For more information, see LICENCE in the main folder

/**
 * Custom Script Commands
 * Place the body of custom script commands in this file.
 * Format:
 *	BUILDIN_FUNC(command_name)
 *	{
 *		<code>;
 *	}
 **/

//BUILDIN_FUNC(example)
//{
//	ShowInfo("buildin_example: It works!\n");
//	script_pushint(st,1);
//	return 0;
//}

BUILDIN_FUNC(set_custom_rate)
{
	map_session_data* sd;
	int type = script_getnum(st,2),
		value = script_getnum(st,3);

	if( !script_charid2sd(4,sd) ) {
		script_pushint(st,0);
		return SCRIPT_CMD_FAILURE;
	}

	switch( type ) {
		case CR_BASE_EXP_RATE:			sd->custom_rate.base_exp_rate = value; break;
		case CR_JOB_EXP_RATE:			sd->custom_rate.job_exp_rate = value; break;
		case CR_MVP_EXP_RATE:			sd->custom_rate.mvp_exp_rate = value; break;
		case CR_QUEST_EXP_RATE:			sd->custom_rate.quest_exp_rate = value; break;
		case CR_HEAL_EXP_RATE:			sd->custom_rate.heal_exp = value; break;
		case CR_VIP_BASE_EXP_INCREASE:	sd->custom_rate.vip_base_exp_increase = value; break;
		case CR_VIP_JOB_EXP_INCREASE:	sd->custom_rate.vip_job_exp_increase = value; break;
		case CR_VIP_BM_INCREASE:		sd->custom_rate.vip_bm_increase = value; break;
		case CR_VIP_DROP_INCREASE:		sd->custom_rate.vip_drop_increase = value; break;
		case CR_IT_RATE_COMMON:			sd->custom_rate.item_rate_common = value; break;
		case CR_IT_RATE_COMMON_BOSS:	sd->custom_rate.item_rate_common_boss = value; break;
		case CR_IT_RATE_COMMON_MVP:		sd->custom_rate.item_rate_common_mvp = value; break;
		case CR_IT_DROP_COMMON_MIN:		sd->custom_rate.item_drop_common_min = value; break;
		case CR_IT_DROP_COMMON_MAX:		sd->custom_rate.item_drop_common_max = value; break;
		case CR_IT_RATE_HEAL:			sd->custom_rate.item_rate_heal = value; break;
		case CR_IT_RATE_HEAL_BOSS:		sd->custom_rate.item_rate_heal_boss = value; break;
		case CR_IT_RATE_HEAL_MVP:		sd->custom_rate.item_rate_heal_mvp = value; break;
		case CR_IT_DROP_HEAL_MIN:		sd->custom_rate.item_drop_heal_min = value; break;
		case CR_IT_DROP_HEAL_MAX:		sd->custom_rate.item_drop_heal_max = value; break;
		case CR_IT_RATE_USE:			sd->custom_rate.item_rate_use = value; break;
		case CR_IT_RATE_USE_BOSS:		sd->custom_rate.item_rate_use_boss = value; break;
		case CR_IT_RATE_USE_MVP:		sd->custom_rate.item_rate_use_mvp = value; break;
		case CR_IT_DROP_USE_MIN:		sd->custom_rate.item_drop_use_min = value; break;
		case CR_IT_DROP_USE_MAX:		sd->custom_rate.item_drop_use_max = value; break;
		case CR_IT_RATE_EQUIP:			sd->custom_rate.item_rate_equip = value; break;
		case CR_IT_RATE_EQUIP_BOSS:		sd->custom_rate.item_rate_equip_boss = value; break;
		case CR_IT_RATE_EQUIP_MVP:		sd->custom_rate.item_rate_equip_mvp = value; break;
		case CR_IT_DROP_EQUIP_MIN:		sd->custom_rate.item_drop_equip_min = value; break;
		case CR_IT_DROP_EQUIP_MAX:		sd->custom_rate.item_drop_equip_max = value; break;
		case CR_IT_RATE_CARD:			sd->custom_rate.item_rate_card = value; break;
		case CR_IT_RATE_CARD_BOSS:		sd->custom_rate.item_rate_card_boss = value; break;
		case CR_IT_RATE_CARD_MVP:		sd->custom_rate.item_rate_card_mvp = value; break;
		case CR_IT_DROP_CARD_MIN:		sd->custom_rate.item_drop_card_min = value; break;
		case CR_IT_DROP_CARD_MAX:		sd->custom_rate.item_drop_card_max = value; break;
		case CR_IT_RATE_MVP:			sd->custom_rate.item_rate_mvp = value; break;
		case CR_IT_DROP_MVP_MIN:		sd->custom_rate.item_drop_mvp_min = value; break;
		case CR_IT_DROP_MVP_MAX:		sd->custom_rate.item_drop_mvp_max = value; break;
		case CR_IT_RATE_TREASURE:		sd->custom_rate.item_rate_treasure = value; break;
		case CR_IT_DROP_TREASURE_MIN:	sd->custom_rate.item_drop_treasure_min = value; break;
		case CR_IT_DROP_TREASURE_MAX:	sd->custom_rate.item_drop_treasure_max = value; break;
		case CR_PVM_SEASONAL:
			sd->custom_rate.pvm_seasonal = (value != 0);
			status_calc_pc(sd, SCO_FORCE);
			break;
		default:
			ShowError("buildin_set_custom_rate: Invalid type %d\n", type);
			script_pushint(st,0);
			return SCRIPT_CMD_SUCCESS;
	}

	script_pushint(st,1);
	return SCRIPT_CMD_SUCCESS;
}

BUILDIN_FUNC(get_custom_rate)
{
	map_session_data* sd;
	int type = script_getnum(st,2),
		value = 0;

	if( !script_charid2sd(3,sd) ) {
		script_pushint(st,0);
		return SCRIPT_CMD_FAILURE;
	}

	switch( type ) {
		case CR_BASE_EXP_RATE:			value = sd->custom_rate.base_exp_rate; break;
		case CR_JOB_EXP_RATE:			value = sd->custom_rate.job_exp_rate; break;
		case CR_MVP_EXP_RATE:			value = sd->custom_rate.mvp_exp_rate; break;
		case CR_QUEST_EXP_RATE:			value = sd->custom_rate.quest_exp_rate; break;
		case CR_HEAL_EXP_RATE:			value = sd->custom_rate.heal_exp; break;
		case CR_VIP_BASE_EXP_INCREASE:	value = sd->custom_rate.vip_base_exp_increase; break;
		case CR_VIP_JOB_EXP_INCREASE:	value = sd->custom_rate.vip_job_exp_increase; break;
		case CR_VIP_BM_INCREASE:		value = sd->custom_rate.vip_bm_increase; break;
		case CR_VIP_DROP_INCREASE:		value = sd->custom_rate.vip_drop_increase; break;
		case CR_IT_RATE_COMMON:			value = sd->custom_rate.item_rate_common; break;
		case CR_IT_RATE_COMMON_BOSS:	value = sd->custom_rate.item_rate_common_boss; break;
		case CR_IT_RATE_COMMON_MVP:		value = sd->custom_rate.item_rate_common_mvp; break;
		case CR_IT_DROP_COMMON_MIN:		value = sd->custom_rate.item_drop_common_min; break;
		case CR_IT_DROP_COMMON_MAX:		value = sd->custom_rate.item_drop_common_max; break;
		case CR_IT_RATE_HEAL:			value = sd->custom_rate.item_rate_heal; break;
		case CR_IT_RATE_HEAL_BOSS:		value = sd->custom_rate.item_rate_heal_boss; break;
		case CR_IT_RATE_HEAL_MVP:		value = sd->custom_rate.item_rate_heal_mvp; break;
		case CR_IT_DROP_HEAL_MIN:		value = sd->custom_rate.item_drop_heal_min; break;
		case CR_IT_DROP_HEAL_MAX:		value = sd->custom_rate.item_drop_heal_max; break;
		case CR_IT_RATE_USE:			value = sd->custom_rate.item_rate_use; break;
		case CR_IT_RATE_USE_BOSS:		value = sd->custom_rate.item_rate_use_boss; break;
		case CR_IT_RATE_USE_MVP:		value = sd->custom_rate.item_rate_use_mvp; break;
		case CR_IT_DROP_USE_MIN:		value = sd->custom_rate.item_drop_use_min; break;
		case CR_IT_DROP_USE_MAX:		value = sd->custom_rate.item_drop_use_max; break;
		case CR_IT_RATE_EQUIP:			value = sd->custom_rate.item_rate_equip; break;
		case CR_IT_RATE_EQUIP_BOSS:		value = sd->custom_rate.item_rate_equip_boss; break;
		case CR_IT_RATE_EQUIP_MVP:		value = sd->custom_rate.item_rate_equip_mvp; break;
		case CR_IT_DROP_EQUIP_MIN:		value = sd->custom_rate.item_drop_equip_min; break;
		case CR_IT_DROP_EQUIP_MAX:		value = sd->custom_rate.item_drop_equip_max; break;
		case CR_IT_RATE_CARD:			value = sd->custom_rate.item_rate_card; break;
		case CR_IT_RATE_CARD_BOSS:		value = sd->custom_rate.item_rate_card_boss; break;
		case CR_IT_RATE_CARD_MVP:		value = sd->custom_rate.item_rate_card_mvp; break;
		case CR_IT_DROP_CARD_MIN:		value = sd->custom_rate.item_drop_card_min; break;
		case CR_IT_DROP_CARD_MAX:		value = sd->custom_rate.item_drop_card_max; break;
		case CR_IT_RATE_MVP:			value = sd->custom_rate.item_rate_mvp; break;
		case CR_IT_DROP_MVP_MIN:		value = sd->custom_rate.item_drop_mvp_min; break;
		case CR_IT_DROP_MVP_MAX:		value = sd->custom_rate.item_drop_mvp_max; break;
		case CR_IT_RATE_TREASURE:		value = sd->custom_rate.item_rate_treasure; break;
		case CR_IT_DROP_TREASURE_MIN:	value = sd->custom_rate.item_drop_treasure_min; break;
		case CR_IT_DROP_TREASURE_MAX:	value = sd->custom_rate.item_drop_treasure_max; break;
		case CR_PVM_SEASONAL:			value = sd->custom_rate.pvm_seasonal ? 1 : 0; break;
		default:
			ShowError("buildin_get_custom_rate: Invalid type %d\n", type);
			script_pushint(st,0);
			return SCRIPT_CMD_SUCCESS;
	}

	script_pushint(st,value);
	return SCRIPT_CMD_SUCCESS;
}
