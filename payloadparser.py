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

     'PhaseTimer': '00.00', 'Phase': 'Starting', 'RoundNumber': '0', 'TWins': '0', 'CTWins': '0',

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

     'PhaseTimer': '00.00', 'Phase': 'Starting', 'RoundNumber': '0', 'TWins': '0', 'CTWins': '0',

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
     'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none',

     'obsPlayerName': 'Text49', 'obsPlayerHealth': 'Text53', 'obsPlayerKills': 'Text52',
     'obsPlayerDeaths': 'Text51', 'obsPlayerMoney': 'obsPlayerMoney',
     'obsPlayerBigslot': 'None', 'obsPlayerBombDefuser': 'obsPlayerBombDefuser', 'obsPlayerArmour': 'obsPlayerArmour',
     'obsPlayerNadeslot1': 'obsPlayerNadeslot1', 'obsPlayerNadeslot2': 'obsPlayerNadeslot2',
     'obsPlayerNadeslot3': 'obsPlayerNadeslot3',
     'obsPlayerNadeslot4': 'obsPlayerNadeslot4',

     'PhaseTimer': 'Text30', 'Phase': 'Text58', 'RoundNumber': 'Text31', 'TWins': 'Text28', 'CTWins': 'Text29',

     'bombPhase': 'Text20', 'bombTimer': 'Countdown Dummy'}

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
     'CT2Nadeslot4': 'MAT_SELSURF',

     'obsPlayerName': 'TEXT_STRING', 'obsPlayerHealth': 'TEXT_STRING', 'obsPlayerKills': 'TEXT_STRING',
     'obsPlayerDeaths': 'TEXT_STRING', 'obsPlayerMoney': 'obsPlayerMoney',
     'obsPlayerBigslot': 'None', 'obsPlayerBombDefuser': 'MAT_SELSURF', 'obsPlayerArmour': 'MAT_SELSURF',
     'obsPlayerNadeslot1': 'MAT_SELSURF', 'obsPlayerNadeslot2': 'MAT_SELSURF', 'obsPlayerNadeslot3': 'MAT_SELSURF',
     'obsPlayerNadeslot4': 'MAT_SELSURF',

     'PhaseTimer': 'TEXT_STRING', 'Phase': 'TEXT_STRING', 'RoundNumber': 'TEXT_STRING', 'TWins': 'TEXT_STRING',
     'CTWins': 'TEXT_STRING',

     'bombPhase': 'TEXT_STRING', 'bombTimer': 'MAP_FLOAT_PAR'
     }

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

                # Wipe the data dictionary
                for stuffToKill in dataDict:
                    dataDict[stuffToKill] = 'none'

                # Get a load of general data
                dataDict['Phase'] = data.get('phase_countdowns').get('phase')
                dataDict['PhaseTimer'] = round(float(data.get('phase_countdowns').get('phase_ends_in')))
                dataDict['RoundNumber'] = data.get('map').get('round')

                dataDict['TWins'] = data.get('map').get('team_t').get('score')
                dataDict['CTWins'] = data.get('map').get('team_ct').get('score')

                dataDict['bombPhase'] = data.get('bomb').get('state')
                dataDict['bombTimer'] = data.get('bomb').get('countdown')

                # Get a load of observed player data
                dataDict['obsPlayerName'] = data.get('player').get('name')
                dataDict['obsPlayerHealth'] = data.get('player').get('state').get('health')
                dataDict['obsPlayerMoney'] = data.get('player').get('state').get('money')
                dataDict['obsPlayerKills'] = data.get('player').get('match_stats').get('kills')
                dataDict['obsPlayerDeaths'] = data.get('player').get('match_stats').get('deaths')

                # Getting armour state(armour / both / none) for observed player
                if int(data.get("player").get('state').get("armor")) >= 1:
                    if data.get("player").get('state').get("helmet"):
                        dataDict['obsPlayerArmour'] = 'both'
                    else:
                        dataDict['obsPlayerArmour'] = 'armour'
                else:
                    dataDict['obsPlayerArmour'] = 'none'

                # Check for a defuser on the obsPlayer
                if data.get("player").get('state').get("defusekit"):
                    dataDict['obsPlayerBombDefuser'] = 'defuser'
                else:
                    dataDict['obsPlayerBombDefuser'] = 'none'

                # Check all the weapon slots to see if there's any nades, or C4
                nadeSlot = 1

                for weapon in data.get('player').get('weapons'):
                    if data.get("player").get('weapons').get(weapon).get('type') == 'Grenade':
                        dataDict['obsPlayerNadeslot' + str(nadeSlot)] = \
                            data.get("player").get('weapons').get(weapon).get('name')
                        nadeSlot = nadeSlot + 1
                    elif data.get("player").get('weapons').get(weapon).get('type') == 'C4':
                        dataDict['obsPlayerBombDefuser'] = 'bomb'

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
                            'type') == 'Submachine Gun' \
                                or data.get("allplayers").get(playerID).get('weapons').get(weapon).get(
                            'type') == 'SniperRifle' \
                                or data.get("allplayers").get(playerID).get('weapons').get(weapon).get(
                            'type') == 'Machine Gun':

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

                # entry gives key, iterate through looking for changes in data
                for entry in dataDict:
                    if dataDict[entry] != prevDataDict[entry]:
                        try:
                            commandString = commandString + baseCommand.format(labelsDict[entry],
                                                                               commandDict[entry],
                                                                               dataDict[entry])
                        except KeyError:
                            pass

                prevDataDict = dict(dataDict)

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
                    # connectionOpen = True

        else:
            sendCommand("end")

        # print(payload)
