import json
import socket

host = "127.0.0.1"
# host = "81.96.9.95"
port = 5123

connectionOpen = False

baseCommand = """itemset("{0}", "{1}", "{2}");"""

playerIndexDict = {'T1': 'noneT1', 'T2': 'noneT1', 'T3': 'noneT3', 'T4': 'noneT4', 'T5': 'noneT5',
                   'CT1': 'noneT1', 'CT2': 'noneT2', 'CT3': 'noneT3', 'CT4': 'noneT4', 'CT5': 'noneT5'}

# Data structure for storage
dataDict = \
    {'T1Name': 'T1Name', 'T1Health': '100', 'T1Kills': 'T1Kills', 'T1Deaths': 'T1Deaths', 'T1Money': 'T1Money',
     'T1Bigslot': 'none', 'T1BombDefuser': 'none', 'T1Armour': 'none',
     'T1Nadeslot1': 'none', 'T1Nadeslot2': 'none', 'T1Nadeslot3': 'none', 'T1Nadeslot4': 'none',

     'T2Name': 'T2Name', 'T2Health': '100', 'T2Kills': 'T2Kills', 'T2Deaths': 'T2Deaths', 'T2Money': 'T2Money',
     'T2Bigslot': 'none', 'T2BombDefuser': 'none', 'T2Armour': 'none',
     'T2Nadeslot1': 'none', 'T2Nadeslot2': 'none', 'T2Nadeslot3': 'none', 'T2Nadeslot4': 'none',

     'T3Name': 'T3Name', 'T3Health': '100', 'T3Kills': 'T3Kills', 'T3Deaths': 'T3Deaths', 'T3Money': 'T3Money',
     'T3Bigslot': 'none', 'T3BombDefuser': 'none', 'T3Armour': 'none',
     'T3Nadeslot1': 'none', 'T3Nadeslot2': 'none', 'T3Nadeslot3': 'none', 'T3Nadeslot4': 'none',

     'T4Name': 'T4Name', 'T4Health': '100', 'T4Kills': 'T4Kills', 'T4Deaths': 'T4Deaths', 'T4Money': 'T4Money',
     'T4Bigslot': 'none', 'T4BombDefuser': 'none', 'T4Armour': 'none',
     'T4Nadeslot1': 'none', 'T4Nadeslot2': 'none', 'T4Nadeslot3': 'none', 'T4Nadeslot4': 'none',

     'T5Name': 'T5Name', 'T5Health': '100', 'T5Kills': 'T5Kills', 'T5Deaths': 'T5Deaths', 'T5Money': 'T5Money',
     'T5Bigslot': 'none', 'T5BombDefuser': 'none', 'T5Armour': 'none',
     'T5Nadeslot1': 'none', 'T5Nadeslot2': 'none', 'T5Nadeslot3': 'none', 'T5Nadeslot4': 'none',

     'CT1Name': 'CT1Name', 'CT1Health': '100', 'CT1Kills': 'CT1Kills', 'CT1Deaths': 'CT1Deaths', 'CT1Money': 'CT1Money',
     'CT1Bigslot': 'none', 'CT1BombDefuser': 'none', 'CT1Armour': 'none',
     'CT1Nadeslot1': 'none', 'CT1Nadeslot2': 'none', 'CT1Nadeslot3': 'none', 'CT1Nadeslot4': 'none',

     'CT2Name': 'CT2Name', 'CT2Health': '100', 'CT2Kills': 'CT2Kills', 'CT2Deaths': 'CT2Deaths', 'CT2Money': 'CT2Money',
     'CT2Bigslot': 'none', 'CT2BombDefuser': 'none', 'CT2Armour': 'none',
     'CT2Nadeslot1': 'none', 'CT2Nadeslot2': 'none', 'CT2Nadeslot3': 'none', 'CT2Nadeslot4': 'none',

     'CT3Name': 'CT3Name', 'CT3Health': '100', 'CT3Kills': 'CT3Kills', 'CT3Deaths': 'CT3Deaths', 'CT3Money': 'CT3Money',
     'CT3Bigslot': 'none', 'CT3BombDefuser': 'none', 'CT3Armour': 'none',
     'CT3Nadeslot1': 'none', 'CT3Nadeslot2': 'none', 'CT3Nadeslot3': 'none', 'CT3Nadeslot4': 'none',

     'CT4Name': 'CT4Name', 'CT4Health': '100', 'CT4Kills': 'CT4Kills', 'CT4Deaths': 'CT4Deaths', 'CT4Money': 'CT4Money',
     'CT4Bigslot': 'none', 'CT4BombDefuser': 'none', 'CT4Armour': 'none',
     'CT4Nadeslot1': 'none', 'CT4Nadeslot2': 'none', 'CT4Nadeslot3': 'none', 'CT4Nadeslot4': 'none',

     'CT5Name': 'CT5Name', 'CT5Health': '100', 'CT5Kills': 'CT5Kills', 'CT5Deaths': 'CT5Deaths', 'CT5Money': 'CT5Money',
     'CT5Bigslot': 'none', 'CT5BombDefuser': 'none', 'CT5Armour': 'none',
     'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none',

     'obsPlayerName': 'obsPlayerName', 'obsPlayerHealth': '100', 'obsPlayerKills': 'obsPlayerKills',
     'obsPlayerDeaths': 'obsPlayerDeaths', 'obsPlayerMoney': 'obsPlayerMoney',
     'obsPlayerBigslot': 'None', 'obsPlayerBombDefuser': 'None', 'obsPlayerArmour': 'None',
     'obsPlayerNadeslot1': 'None', 'obsPlayerNadeslot2': 'None', 'obsPlayerNadeslot3': 'None',
     'obsPlayerNadeslot4': 'None',

     'PhaseTimer': '00.00', 'Phase': 'Starting', 'RoundNumber': '0', 'T1Wins': '0', 'T2Wins': '0',

     'bombPhase': 'empty', 'bombTimer': '00'
     }

prevDataDict = \
    {'T1Name': 'T1Name', 'T1Health': '100', 'T1Kills': 'T1Kills', 'T1Deaths': 'T1Deaths', 'T1Money': 'T1Money',
     'T1Bigslot': 'none', 'T1BombDefuser': 'none', 'T1Armour': 'none',
     'T1Nadeslot1': 'none', 'T1Nadeslot2': 'none', 'T1Nadeslot3': 'none', 'T1Nadeslot4': 'none',

     'T2Name': 'T2Name', 'T2Health': '100', 'T2Kills': 'T2Kills', 'T2Deaths': 'T2Deaths', 'T2Money': 'T2Money',
     'T2Bigslot': 'none', 'T2BombDefuser': 'none', 'T2Armour': 'none',
     'T2Nadeslot1': 'none', 'T2Nadeslot2': 'none', 'T2Nadeslot3': 'none', 'T2Nadeslot4': 'none',

     'T3Name': 'T3Name', 'T3Health': '100', 'T3Kills': 'T3Kills', 'T3Deaths': 'T3Deaths', 'T3Money': 'T3Money',
     'T3Bigslot': 'none', 'T3BombDefuser': 'none', 'T3Armour': 'none',
     'T3Nadeslot1': 'none', 'T3Nadeslot2': 'none', 'T3Nadeslot3': 'none', 'T3Nadeslot4': 'none',

     'T4Name': 'T4Name', 'T4Health': '100', 'T4Kills': 'T4Kills', 'T4Deaths': 'T4Deaths', 'T4Money': 'T4Money',
     'T4Bigslot': 'none', 'T4BombDefuser': 'none', 'T4Armour': 'none',
     'T4Nadeslot1': 'none', 'T4Nadeslot2': 'none', 'T4Nadeslot3': 'none', 'T4Nadeslot4': 'none',

     'T5Name': 'T5Name', 'T5Health': '100', 'T5Kills': 'T5Kills', 'T5Deaths': 'T5Deaths', 'T5Money': 'T5Money',
     'T5Bigslot': 'none', 'T5BombDefuser': 'none', 'T5Armour': 'none',
     'T5Nadeslot1': 'none', 'T5Nadeslot2': 'none', 'T5Nadeslot3': 'none', 'T5Nadeslot4': 'none',

     'CT1Name': 'CT1Name', 'CT1Health': '100', 'CT1Kills': 'CT1Kills', 'CT1Deaths': 'CT1Deaths', 'CT1Money': 'CT1Money',
     'CT1Bigslot': 'none', 'CT1BombDefuser': 'none', 'CT1Armour': 'none',
     'CT1Nadeslot1': 'none', 'CT1Nadeslot2': 'none', 'CT1Nadeslot3': 'none', 'CT1Nadeslot4': 'none',

     'CT2Name': 'CT2Name', 'CT2Health': '100', 'CT2Kills': 'CT2Kills', 'CT2Deaths': 'CT2Deaths', 'CT2Money': 'CT2Money',
     'CT2Bigslot': 'none', 'CT2BombDefuser': 'none', 'CT2Armour': 'none',
     'CT2Nadeslot1': 'none', 'CT2Nadeslot2': 'none', 'CT2Nadeslot3': 'none', 'CT2Nadeslot4': 'none',

     'CT3Name': 'CT3Name', 'CT3Health': '100', 'CT3Kills': 'CT3Kills', 'CT3Deaths': 'CT3Deaths', 'CT3Money': 'CT3Money',
     'CT3Bigslot': 'none', 'CT3BombDefuser': 'none', 'CT3Armour': 'none',
     'CT3Nadeslot1': 'none', 'CT3Nadeslot2': 'none', 'CT3Nadeslot3': 'none', 'CT3Nadeslot4': 'none',

     'CT4Name': 'CT4Name', 'CT4Health': '100', 'CT4Kills': 'CT4Kills', 'CT4Deaths': 'CT4Deaths', 'CT4Money': 'CT4Money',
     'CT4Bigslot': 'none', 'CT4BombDefuser': 'none', 'CT4Armour': 'none',
     'CT4Nadeslot1': 'none', 'CT4Nadeslot2': 'none', 'CT4Nadeslot3': 'none', 'CT4Nadeslot4': 'none',

     'CT5Name': 'CT5Name', 'CT5Health': '100', 'CT5Kills': 'CT5Kills', 'CT5Deaths': 'CT5Deaths', 'CT5Money': 'CT5Money',
     'CT5Bigslot': 'none', 'CT5BombDefuser': 'none', 'CT5Armour': 'none',
     'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none',

     'obsPlayerName': 'obsPlayerName', 'obsPlayerHealth': '100', 'obsPlayerKills': 'obsPlayerKills',
     'obsPlayerDeaths': 'obsPlayerDeaths', 'obsPlayerMoney': 'obsPlayerMoney',
     'obsPlayerBigslot': 'None', 'obsPlayerBombDefuser': 'None', 'obsPlayerArmour': 'None',
     'obsPlayerNadeslot1': 'None', 'obsPlayerNadeslot2': 'None', 'obsPlayerNadeslot3': 'None',
     'obsPlayerNadeslot4': 'None',

     'PhaseTimer': '00.00', 'Phase': 'Starting', 'RoundNumber': '0', 'T1Wins': '0', 'T2Wins': '0',

     'bombPhase': 'empty', 'bombTimer': '00'

     }

labelsDict = \
    {'T1Name': 'Text39', 'T1Health': 'Text43', 'T1Kills': 'Text41', 'T1Deaths': 'Text42', 'T1Money': 'Text40',
     'T1Bigslot': 'T1Bigslot', 'T1BombDefuser': 'T1BombDefuser', 'T1Armour': 'T1Armour',
     'T1Nadeslot1': 'T1Nadeslot1', 'T1Nadeslot2': 'T1Nadeslot2', 'T1Nadeslot3': 'T1Nadeslot3',
     'T1Nadeslot4': 'T1Nadeslot4',

     'T2Name': 'Text44', 'T2Health': 'Text48', 'T2Kills': 'Text46', 'T2Deaths': 'Text47', 'T2Money': 'Text45',
     'T2Bigslot': 'T2Bigslot', 'T2BombDefuser': 'T2BombDefuser', 'T2Armour': 'T2Armour',
     'T2Nadeslot1': 'T2Nadeslot1', 'T2Nadeslot2': 'T2Nadeslot2', 'T2Nadeslot3': 'T2Nadeslot3',
     'T2Nadeslot4': 'T2Nadeslot4',

     'T3Name': 'T3Name', 'T3Health': '100', 'T3Kills': 'T3Kills', 'T3Deaths': 'T3Deaths', 'T3Money': 'T3Money',
     'T3Bigslot': 'none', 'T3BombDefuser': 'none', 'T3Armour': 'none',
     'T3Nadeslot1': 'none', 'T3Nadeslot2': 'none', 'T3Nadeslot3': 'none', 'T3Nadeslot4': 'none',

     'T4Name': 'T4Name', 'T4Health': '100', 'T4Kills': 'T4Kills', 'T4Deaths': 'T4Deaths', 'T4Money': 'T4Money',
     'T4Bigslot': 'none', 'T4BombDefuser': 'none', 'T4Armour': 'none',
     'T4Nadeslot1': 'none', 'T4Nadeslot2': 'none', 'T4Nadeslot3': 'none', 'T4Nadeslot4': 'none',

     'T5Name': 'T5Name', 'T5Health': '100', 'T5Kills': 'T5Kills', 'T5Deaths': 'T5Deaths', 'T5Money': 'T5Money',
     'T5Bigslot': 'none', 'T5BombDefuser': 'none', 'T5Armour': 'none',
     'T5Nadeslot1': 'none', 'T5Nadeslot2': 'none', 'T5Nadeslot3': 'none', 'T5Nadeslot4': 'none',

     'CT1Name': 'Text22', 'CT1Health': 'Text24', 'CT1Kills': 'Text32', 'CT1Deaths': 'Text33', 'CT1Money': 'Text25',
     'CT1Bigslot': 'CT1Bigslot', 'CT1BombDefuser': 'CT1BombDefuser', 'CT1Armour': 'CT1Armour',
     'CT1Nadeslot1': 'CT1Nadeslot1', 'CT1Nadeslot2': 'CT1Nadeslot2', 'CT1Nadeslot3': 'CT1Nadeslot3',
     'CT1Nadeslot4': 'CT1Nadeslot4',

     'CT2Name': 'Text34', 'CT2Health': 'Text38', 'CT2Kills': 'Text36', 'CT2Deaths': 'Text37', 'CT2Money': 'Text35',
     'CT2Bigslot': 'CT2Bigslot', 'CT2BombDefuser': 'CT2BombDefuser', 'CT2Armour': 'CT2Armour',
     'CT2Nadeslot1': 'CT2Nadeslot1', 'CT2Nadeslot2': 'CT2Nadeslot2', 'CT2Nadeslot3': 'CT2Nadeslot3',
     'CT2Nadeslot4': 'CT2Nadeslot4',

     'CT3Name': 'CT3Name', 'CT3Health': '100', 'CT3Kills': 'CT3Kills', 'CT3Deaths': 'CT3Deaths', 'CT3Money': 'CT3Money',
     'CT3Bigslot': 'none', 'CT3BombDefuser': 'none', 'CT3Armour': 'none',
     'CT3Nadeslot1': 'none', 'CT3Nadeslot2': 'none', 'CT3Nadeslot3': 'none', 'CT3Nadeslot4': 'none',

     'CT4Name': 'CT4Name', 'CT4Health': '100', 'CT4Kills': 'CT4Kills', 'CT4Deaths': 'CT4Deaths', 'CT4Money': 'CT4Money',
     'CT4Bigslot': 'none', 'CT4BombDefuser': 'none', 'CT4Armour': 'none',
     'CT4Nadeslot1': 'none', 'CT4Nadeslot2': 'none', 'CT4Nadeslot3': 'none', 'CT4Nadeslot4': 'none',

     'CT5Name': 'CT5Name', 'CT5Health': '100', 'CT5Kills': 'CT5Kills', 'CT5Deaths': 'CT5Deaths', 'CT5Money': 'CT5Money',
     'CT5Bigslot': 'none', 'CT5BombDefuser': 'none', 'CT5Armour': 'none',
     'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none'
     }

commandDict = \
    {'T1Name': 'TEXT_STRING', 'T1Health': 'TEXT_STRING', 'T1Kills': 'TEXT_STRING', 'T1Deaths': 'TEXT_STRING',
     'T1Money': 'TEXT_STRING',
     'T1Bigslot': 'MAT_SELSURF', 'T1BombDefuser': 'MAT_SELSURF', 'T1Armour': 'MAT_SELSURF',
     'T1Nadeslot1': 'MAT_SELSURF', 'T1Nadeslot2': 'MAT_SELSURF', 'T1Nadeslot3': 'MAT_SELSURF',
     'T1Nadeslot4': 'MAT_SELSURF',

     'T2Name': 'TEXT_STRING', 'T2Health': 'TEXT_STRING', 'T2Kills': 'TEXT_STRING', 'T2Deaths': 'TEXT_STRING',
     'T2Money': 'TEXT_STRING',
     'T2Bigslot': 'MAT_SELSURF', 'T2BombDefuser': 'MAT_SELSURF', 'T2Armour': 'MAT_SELSURF',
     'T2Nadeslot1': 'MAT_SELSURF', 'T2Nadeslot2': 'MAT_SELSURF', 'T2Nadeslot3': 'MAT_SELSURF',
     'T2Nadeslot4': 'MAT_SELSURF',

     'CT1Name': 'TEXT_STRING', 'CT1Health': 'TEXT_STRING', 'CT1Kills': 'TEXT_STRING', 'CT1Deaths': 'TEXT_STRING',
     'CT1Money': 'TEXT_STRING',
     'CT1Bigslot': 'MAT_SELSURF', 'CT1BombDefuser': 'MAT_SELSURF', 'CT1Armour': 'MAT_SELSURF',
     'CT1Nadeslot1': 'MAT_SELSURF', 'CT1Nadeslot2': 'MAT_SELSURF', 'CT1Nadeslot3': 'MAT_SELSURF',
     'CT1Nadeslot4': 'MAT_SELSURF',

     'CT2Name': 'TEXT_STRING', 'CT2Health': 'TEXT_STRING', 'CT2Kills': 'TEXT_STRING', 'CT2Deaths': 'TEXT_STRING',
     'CT2Money': 'TEXT_STRING',
     'CT2Bigslot': 'MAT_SELSURF', 'CT2BombDefuser': 'MAT_SELSURF', 'CT2Armour': 'MAT_SELSURF',
     'CT2Nadeslot1': 'MAT_SELSURF', 'CT2Nadeslot2': 'MAT_SELSURF', 'CT2Nadeslot3': 'MAT_SELSURF',
     'CT2Nadeslot4': 'MAT_SELSURF'
     }

# allPlayerCommandsDict = \
#     {'T1Name': 'T1Name', 'T1Health': '100', 'T1Kills': 'T1Kills', 'T1Deaths': 'T1Deaths', 'T1Money': 'T1Money',
#      'T1Bigslot': 'none', 'T1BombDefuser': 'none', 'T1Armour': 'none',
#      'T1Nadeslot1': 'none', 'T1Nadeslot2': 'none', 'T1Nadeslot3': 'none', 'T1Nadeslot4': 'none',
#
#      'T2Name': 'T2Name', 'T2Health': '100', 'T2Kills': 'T2Kills', 'T2Deaths': 'T2Deaths', 'T2Money': 'T2Money',
#      'T2Bigslot': 'none', 'T2BombDefuser': 'none', 'T2Armour': 'none',
#      'T2Nadeslot1': 'none', 'T2Nadeslot2': 'none', 'T2Nadeslot3': 'none', 'T2Nadeslot4': 'none',
#
#      'T3Name': 'T3Name', 'T3Health': '100', 'T3Kills': 'T3Kills', 'T3Deaths': 'T3Deaths', 'T3Money': 'T3Money',
#      'T3Bigslot': 'none', 'T3BombDefuser': 'none', 'T3Armour': 'none',
#      'T3Nadeslot1': 'none', 'T3Nadeslot2': 'none', 'T3Nadeslot3': 'none', 'T3Nadeslot4': 'none',
#
#      'T4Name': 'T4Name', 'T4Health': '100', 'T4Kills': 'T4Kills', 'T4Deaths': 'T4Deaths', 'T4Money': 'T4Money',
#      'T4Bigslot': 'none', 'T4BombDefuser': 'none', 'T4Armour': 'none',
#      'T4Nadeslot1': 'none', 'T4Nadeslot2': 'none', 'T4Nadeslot3': 'none', 'T4Nadeslot4': 'none',
#
#      'T5Name': 'T5Name', 'T5Health': '100', 'T5Kills': 'T5Kills', 'T5Deaths': 'T5Deaths', 'T5Money': 'T5Money',
#      'T5Bigslot': 'none', 'T5BombDefuser': 'none', 'T5Armour': 'none',
#      'T5Nadeslot1': 'none', 'T5Nadeslot2': 'none', 'T5Nadeslot3': 'none', 'T5Nadeslot4': 'none',
#
#      'CT1Name': 'CT1Name', 'CT1Health': '100', 'CT1Kills': 'CT1Kills', 'CT1Deaths': 'CT1Deaths', 'CT1Money': 'CT1Money',
#      'CT1Bigslot': 'none', 'CT1BombDefuser': 'none', 'CT1Armour': 'none',
#      'CT1Nadeslot1': 'none', 'CT1Nadeslot2': 'none', 'CT1Nadeslot3': 'none', 'CT1Nadeslot4': 'none',
#
#      'CT2Name': 'CT2Name', 'CT2Health': '100', 'CT2Kills': 'CT2Kills', 'CT2Deaths': 'CT2Deaths', 'CT2Money': 'CT2Money',
#      'CT2Bigslot': 'none', 'CT2BombDefuser': 'none', 'CT2Armour': 'none',
#      'CT2Nadeslot1': 'none', 'CT2Nadeslot2': 'none', 'CT2Nadeslot3': 'none', 'CT2Nadeslot4': 'none',
#
#      'CT3Name': 'CT3Name', 'CT3Health': '100', 'CT3Kills': 'CT3Kills', 'CT3Deaths': 'CT3Deaths', 'CT3Money': 'CT3Money',
#      'CT3Bigslot': 'none', 'CT3BombDefuser': 'none', 'CT3Armour': 'none',
#      'CT3Nadeslot1': 'none', 'CT3Nadeslot2': 'none', 'CT3Nadeslot3': 'none', 'CT3Nadeslot4': 'none',
#
#      'CT4Name': 'CT4Name', 'CT4Health': '100', 'CT4Kills': 'CT4Kills', 'CT4Deaths': 'CT4Deaths', 'CT4Money': 'CT4Money',
#      'CT4Bigslot': 'none', 'CT4BombDefuser': 'none', 'CT4Armour': 'none',
#      'CT4Nadeslot1': 'none', 'CT4Nadeslot2': 'none', 'CT4Nadeslot3': 'none', 'CT4Nadeslot4': 'none',
#
#      'CT5Name': 'CT5Name', 'CT5Health': '100', 'CT5Kills': 'CT5Kills', 'CT5Deaths': 'CT5Deaths', 'CT5Money': 'CT5Money',
#      'CT5Bigslot': 'none', 'CT5BombDefuser': 'none', 'CT5Armour': 'none',
#      'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none',
#
#      'obsPlayerName': 'obsPlayerName', 'obsPlayerHealth': '100', 'obsPlayerKills': 'obsPlayerKills',
#      'obsPlayerDeaths': 'obsPlayerDeaths', 'obsPlayerMoney': 'obsPlayerMoney',
#      'obsPlayerBigslot': 'None', 'obsPlayerBombDefuser': 'None', 'obsPlayerArmour': 'None',
#      'obsPlayerNadeslot1': 'None', 'obsPlayerNadeslot2': 'None', 'obsPlayerNadeslot3': 'None',
#      'obsPlayerNadeslot4': 'None',
#
#      'PhaseTimer': '00.00', 'Phase': 'Starting', 'RoundNumber': '0', 'T1Wins': '0', 'T2Wins': '0',
#
#      'bombPhase': 'empty', 'bombTimer': '00'
#
#      }
#
# prevAllPlayerCommandsDict = \
#     {'T1Name': 'T1Name', 'T1Health': '100', 'T1Kills': 'T1Kills', 'T1Deaths': 'T1Deaths', 'T1Money': 'T1Money',
#      'T1Bigslot': 'empty', 'T1BombDefuser': 'empty', 'T1Armour': 'empty',
#      'T1Nadeslot1': 'empty', 'T1Nadeslot2': 'empty', 'T1Nadeslot3': 'empty', 'T1Nadeslot4': 'empty',
#
#      'T2Name': 'T2Name', 'T2Health': '100', 'T2Kills': 'T2Kills', 'T2Deaths': 'T2Deaths', 'T2Money': 'T2Money',
#      'T2Bigslot': 'empty', 'T2BombDefuser': 'empty', 'T2Armour': 'empty',
#      'T2Nadeslot1': 'empty', 'T2Nadeslot2': 'empty', 'T2Nadeslot3': 'empty', 'T2Nadeslot4': 'empty',
#
#      'T3Name': 'T3Name', 'T3Health': '100', 'T3Kills': 'T3Kills', 'T3Deaths': 'T3Deaths', 'T3Money': 'T3Money',
#      'T3Bigslot': 'empty', 'T3BombDefuser': 'empty', 'T3Armour': 'empty',
#      'T3Nadeslot1': 'empty', 'T3Nadeslot2': 'empty', 'T3Nadeslot3': 'empty', 'T3Nadeslot4': 'empty',
#
#      'T4Name': 'T4Name', 'T4Health': '100', 'T4Kills': 'T4Kills', 'T4Deaths': 'T4Deaths', 'T4Money': 'T4Money',
#      'T4Bigslot': 'empty', 'T4BombDefuser': 'empty', 'T4Armour': 'empty',
#      'T4Nadeslot1': 'empty', 'T4Nadeslot2': 'empty', 'T4Nadeslot3': 'empty', 'T4Nadeslot4': 'empty',
#
#      'T5Name': 'T5Name', 'T5Health': '100', 'T5Kills': 'T5Kills', 'T5Deaths': 'T5Deaths', 'T5Money': 'T5Money',
#      'T5Bigslot': 'empty', 'T5BombDefuser': 'empty', 'T5Armour': 'empty',
#      'T5Nadeslot1': 'empty', 'T5Nadeslot2': 'empty', 'T5Nadeslot3': 'empty', 'T5Nadeslot4': 'empty',
#
#      'CT1Name': 'CT1Name', 'CT1Health': '100', 'CT1Kills': 'CT1Kills', 'CT1Deaths': 'CT1Deaths', 'CT1Money': 'CT1Money',
#      'CT1Bigslot': 'empty', 'CT1BombDefuser': 'empty', 'CT1Armour': 'empty',
#      'CT1Nadeslot1': 'empty', 'CT1Nadeslot2': 'empty', 'CT1Nadeslot3': 'empty', 'CT1Nadeslot4': 'empty',
#
#      'CT2Name': 'CT2Name', 'CT2Health': '100', 'CT2Kills': 'CT2Kills', 'CT2Deaths': 'CT2Deaths', 'CT2Money': 'CT2Money',
#      'CT2Bigslot': 'empty', 'CT2BombDefuser': 'empty', 'CT2Armour': 'empty',
#      'CT2Nadeslot1': 'empty', 'CT2Nadeslot2': 'empty', 'CT2Nadeslot3': 'empty', 'CT2Nadeslot4': 'empty',
#
#      'CT3Name': 'CT3Name', 'CT3Health': '100', 'CT3Kills': 'CT3Kills', 'CT3Deaths': 'CT3Deaths', 'CT3Money': 'CT3Money',
#      'CT3Bigslot': 'empty', 'CT3BombDefuser': 'empty', 'CT3Armour': 'empty',
#      'CT3Nadeslot1': 'empty', 'CT3Nadeslot2': 'empty', 'CT3Nadeslot3': 'empty', 'CT3Nadeslot4': 'empty',
#
#      'CT4Name': 'CT4Name', 'CT4Health': '100', 'CT4Kills': 'CT4Kills', 'CT4Deaths': 'CT4Deaths', 'CT4Money': 'CT4Money',
#      'CT4Bigslot': 'empty', 'CT4BombDefuser': 'empty', 'CT4Armour': 'empty',
#      'CT4Nadeslot1': 'empty', 'CT4Nadeslot2': 'empty', 'CT4Nadeslot3': 'empty', 'CT4Nadeslot4': 'empty',
#
#      'CT5Name': 'CT5Name', 'CT5Health': '100', 'CT5Kills': 'CT5Kills', 'CT5Deaths': 'CT5Deaths', 'CT5Money': 'CT5Money',
#      'CT5Bigslot': 'empty', 'CT5BombDefuser': 'empty', 'CT5Armour': 'empty',
#      'CT5Nadeslot1': 'empty', 'CT5Nadeslot2': 'empty', 'CT5Nadeslot3': 'empty', 'CT5Nadeslot4': 'empty'
#      }

# roundInfoDict = {'PhaseTimer': '00.00', 'Phase': 'Starting', 'RoundNumber': '0', 'T1Wins': '0', 'T2Wins': '0'}
#
# observedPlayerDict = {
#     'obsPlayerName': 'obsPlayerName', 'obsPlayerHealth': '100', 'obsPlayerKills': 'obsPlayerKills',
#     'obsPlayerDeaths': 'obsPlayerDeaths', 'obsPlayerMoney': 'obsPlayerMoney',
#     'obsPlayerBigslot': 'None', 'obsPlayerBombDefuser': 'None', 'obsPlayerArmour': 'None',
#     'obsPlayerNadeslot1': 'None', 'obsPlayerNadeslot2': 'None', 'obsPlayerNadeslot3': 'None',
#     'obsPlayerNadeslot4': 'None'}

commandString = ''

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    connectionOpen = True
except ConnectionRefusedError:
    print("I no server worky")
except TimeoutError:
    print('Timed out.')


def sendCommand(commands_to_send):
    global connectionOpen
    try:
        if commands_to_send == "end" and connectionOpen:
            print(commands_to_send)
            s.sendall("print(Laters players!);".encode('utf-8'))
            s.close()
            connectionOpen = False
        else:
            print(commands_to_send)
            s.sendall(commands_to_send.encode('utf-8'))
    except OSError:
        # print('Cannot reach Aston')
        pass


# A re-written function to send the data to Aston
class PayloadParser:

    @staticmethod
    def parse_payload(payload, gamestate):

        global prevAllPlayerCommandsDict, allPlayerCommandsDict, commandString, connectionOpen, prevDataDict, dataDict

        # Full data dump for debugging:
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(payload, f, ensure_ascii=False, indent=4)

        dump = json.dumps(payload)
        data = json.loads(dump)

        # print(data)

        if data.get("player").get("activity") == "playing":
            if connectionOpen:

                # Setting up some player identifiers (T1, CT4), and checking into player instances
                Ts = 1
                CTs = 1

                # Iterate through the allplayers and find the needed data
                for playerID in data['allplayers']:

                    # Find the team of the players, so we can increment through them (CT1, T3 etc.)
                    playerIndex = data.get("allplayers").get(playerID).get("team")

                    if playerIndex == "T":
                        playerIndex = playerIndex + str(Ts)
                        Ts = Ts + 1

                    if playerIndex == "CT":
                        playerIndex = playerIndex + str(CTs)
                        CTs = CTs + 1

                        # As it's team specific, we see if the CT has a defuse kit (don't be a loser...)
                        if data.get("allplayers").get(playerID).get('state').get("defusekit") == True:
                            dataDict[playerIndex + 'BombDefuser'] = 'defuser'
                        else:
                            dataDict[playerIndex + 'BombDefuser'] = 'none'

                    # Let's grab some data using this player identifier.

                    # Name
                    dataDict[playerIndex + 'Name'] = \
                        data.get("allplayers").get(playerID).get("name")

                    # Health
                    dataDict[playerIndex + 'Health'] = \
                        data.get("allplayers").get(playerID).get('state').get("health")

                    # Kills
                    dataDict[playerIndex + 'Kills'] = \
                        data.get("allplayers").get(playerID).get('match_stats').get("kills")

                    # Deaths
                    dataDict[playerIndex + 'Deaths'] = \
                        data.get("allplayers").get(playerID).get('match_stats').get("deaths")

                    # Money
                    dataDict[playerIndex + 'Money'] = \
                        data.get("allplayers").get(playerID).get('state').get("money")

                    # Getting armour state (armour/both/none)
                    if int(data.get("allplayers").get(playerID).get('state').get("armor")) >= 1:
                        if data.get("allplayers").get(playerID).get('state').get("helmet"):
                            dataDict[playerIndex + 'Armour'] = 'both'
                        else:
                            dataDict[playerIndex + 'Armour'] = 'armour'
                    else:
                        dataDict[playerIndex + 'Armour'] = 'none'

                    # Now let's figure out what weapons the player has...

                    # Reset the slots for the nades
                    nadeSlot = 1

                    for weapon in data.get("allplayers").get(playerID).get('weapons'):

                        # First lets see if they have a pistol. If so, set that to the bigslot
                        if data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Pistol':
                            dataDict[playerIndex + 'Bigslot'] = \
                                data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name')
                            # print(data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name'))

                        # If they have a rifle, shotgun, or SMG then place in the 'bigslot' (replaces pistol)
                        elif data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Shotgun' \
                                or data.get("allplayers").get(playerID).get('weapons').get(weapon).get(
                            'type') == 'Rifle' \
                                or data.get("allplayers").get(playerID).get('weapons').get(weapon).get(
                            'type') == 'Submachine Gun':
                            dataDict[playerIndex + 'Bigslot'] = \
                                data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name')

                        # Now we populate the nade slots
                        if data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Grenade':
                            dataDict[playerIndex + 'Nadeslot' + str(nadeSlot)] = \
                                data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name')
                            nadeSlot = nadeSlot + 1

                        # Does this player have the bomb?
                        if data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'C4':
                            dataDict[playerIndex + 'BombDefuser'] = 'bomb'

                # entry gives key, iteerate through looking for changes in data
                for entry in dataDict:
                    if dataDict[entry] != prevDataDict[entry]:
                        try:
                            commandString = commandString + baseCommand.format(labelsDict[entry],
                                                                               commandDict[entry],
                                                                               dataDict[entry])
                        except KeyError:
                            pass

                prevDataDict = dict(dataDict)

                # for entry in allPlayerCommandsDict:
                #     try:
                #         allPlayerCommandsDict[entry] = baseCommand.format(allPlayerLabelsDict[entry],
                #                                                           allPlayerTypeDict[entry],
                #                                                           allPlayerDataDict[entry])
                #     # Exception here ignores players not catered for in the layout (key doesn't exist)
                #     except KeyError:
                #         pass
                #
                #     # Check if the command entry is new, and if it is, add it to the
                #     if allPlayerCommandsDict[entry] != prevAllPlayerCommandsDict[entry]:
                #         # print(allPlayerCommandsDict[entry] + prevAllPlayerCommandsDict[entry])
                #         commandString = commandString + allPlayerCommandsDict[entry]
                #         # prevAllPlayerCommandsDict[entry] = allPlayerCommandsDict[entry]
                # prevAllPlayerCommandsDict = dict(allPlayerCommandsDict)

                # After all the data is found and only the different commands are added to the sting, send.
                try:
                    if commandString != "":
                        sendCommand(commandString)
                except AttributeError:
                    print("Command was empty")

                commandString = ''
            else:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((host, port))
                    connectionOpen = True
                except ConnectionRefusedError:
                    print("I no server worky")
                    # If there's no connection, do this
                    connectionOpen = True

        else:
            sendCommand("end")

        # print(payload)
