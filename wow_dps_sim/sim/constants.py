from wow_dps_sim.enums import OnUseEffect
from .enums import EventType


class Constants:
    ability_names_lookup = {
        'bloodrage': 'Bloodrage',
        'bloodthirst': 'Bloodthirst',
        'death_wish': 'Death Wish',
        'execute': 'Execute',
        'hand_of_justice_proc': 'Hand of Justice Proc',
        'heroic_strike': 'Heroic Strike',
        'ironfoe_proc': 'Ironfoe Proc',
        'kiss_of_the_spider': 'Kiss of the Spider',
        'overpower': 'Overpower',
        'recklessness': 'Recklessness',
        'slayers_crest': "Slayer's Crest",
        'thrash_blade_proc': 'Thrash Blade Proc',
        'whirlwind': 'Whirlwind',
        'white_main': 'White Hit Main',
        'white_off': 'White Hit Off',
        'white': 'White Hit',
    }

    on_use_effect_to_cd_end_event_type = {
        OnUseEffect.KISS_OF_THE_SPIDER: EventType.KISS_OF_THE_SPIDER_CD_END,
        OnUseEffect.SLAYERS_CREST: EventType.SLAYERS_CREST_CD_END,
    }

    statistics_ability_mapping = {
        'bloodthirst': 'bloodthirst',
        'execute': 'execute',
        'hand_of_justice_proc': 'hand_of_justice_proc',
        'heroic_strike': 'heroic_strike',
        'ironfoe_proc': 'ironfoe_proc',
        'overpower': 'overpower',
        'thrash_blade_proc': 'thrash_blade_proc',
        'whirlwind': 'whirlwind',
        'white_main': 'white',
        'white_off': 'white',
    }
