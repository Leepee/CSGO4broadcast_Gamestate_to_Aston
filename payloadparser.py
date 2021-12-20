import json
import socket

host = "127.0.0.1"
port = 5123

baseCommand = """itemset("{0}", "TEXT_STRING", "{1}");"""

playerIndexDict = {'T1': 'noneT1', 'T2': 'noneT1', 'T3': 'noneT3', 'T4': 'noneT4', 'T5': 'noneT5',
                   'CT1': 'noneT1', 'CT2': 'noneT2', 'CT3': 'noneT3', 'CT4': 'noneT4', 'CT5': 'noneT5'}

# Data structure for allplayer data (sidebars)

allPlayerDataDict = \
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
     'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none'
     }

allPlayerLabelsDict = \
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
     'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none'
     }

allPlayerCommandsDict = \
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
     'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none'
     }

prevAllPlayerCommandsDict = \
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
     'CT5Nadeslot1': 'none', 'CT5Nadeslot2': 'none', 'CT5Nadeslot3': 'none', 'CT5Nadeslot4': 'none'
     }

roundInfoDict = {'PhaseTimer': '00.00', 'Phase': 'Starting', 'RoundNumber': '0', 'T1Wins': '0', 'T2Wins': '0'}

observedPlayerDict = {
    'obsPlayerName': 'obsPlayerName', 'obsPlayerHealth': '100', 'obsPlayerKills': 'obsPlayerKills',
    'obsPlayerDeaths': 'obsPlayerDeaths', 'obsPlayerMoney': 'obsPlayerMoney',
    'obsPlayerBigslot': 'None', 'obsPlayerBombDefuser': 'None', 'obsPlayerArmour': 'None',
    'obsPlayerNadeslot1': 'None', 'obsPlayerNadeslot2': 'None', 'obsPlayerNadeslot3': 'None',
    'obsPlayerNadeslot4': 'None'}

player1Name = "Text24"
commandString = ''

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
except ConnectionRefusedError:
    print("I no server worky")


def sendCommand(commands_to_send):
    try:
        print(commands_to_send)

        if commands_to_send == "end":
            print(commands_to_send)
            s.sendall("print(Laters players!);".encode('utf-8'))
            s.close()
        else:
            s.sendall(commands_to_send.encode('utf-8'))
    except OSError:
        print('Cannot reach Aston')
        pass


# A re-written function to send the data to Aston
class PayloadParser:

    @staticmethod
    def parse_payload(payload):

        global prevAllPlayerCommandsDict, allPlayerCommandsDict, commandString

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=4)
        dump = json.dumps(payload)
        data = json.loads(dump)

        # print(data)

        if data.get("player").get("activity") == "playing":

            # Setting up some player identifiers (T1, CT4), and checking into player instances

            Ts = 1
            CTs = 1
            for playerID in data['allplayers']:
                playerIndex = data.get("allplayers").get(playerID).get("team")

                if playerIndex == "T":
                    playerIndex = playerIndex + str(Ts)
                    Ts = Ts + 1

                    if 'C4' in data:
                        # data.get("allplayers").get(playerID).contains('C4'):
                        allPlayerDataDict[playerIndex + 'BombDefuser'] = 'bomb'
                    else:
                        allPlayerDataDict[playerIndex + 'BombDefuser'] = 'none'


                elif playerIndex == "CT":
                    playerIndex = playerIndex + str(CTs)
                    # print(playerIndex)
                    CTs = CTs + 1

                    if data.get("allplayers").get(playerID).get('state').get("defusekit") == 'true':
                        allPlayerDataDict[playerIndex + 'BombDefuser'] = 'defuser'
                    else:
                        allPlayerDataDict[playerIndex + 'BombDefuser'] = 'none'

                    # Let's grab some data using this player identifier.

                allPlayerDataDict[playerIndex + 'Name'] = \
                    data.get("allplayers").get(playerID).get("name")

                allPlayerDataDict[playerIndex + 'Health'] = \
                    data.get("allplayers").get(playerID).get('state').get("health")

                allPlayerDataDict[playerIndex + 'Kills'] = \
                    data.get("allplayers").get(playerID).get('match_stats').get("kills")

                allPlayerDataDict[playerIndex + 'Deaths'] = \
                    data.get("allplayers").get(playerID).get('match_stats').get("deaths")

                allPlayerDataDict[playerIndex + 'Money'] = \
                    data.get("allplayers").get(playerID).get('state').get("money")

                # Getting armour state (armour/both/none)
                if int(data.get("allplayers").get(playerID).get('state').get("armor")) >= 1:
                    if data.get("allplayers").get(playerID).get('state').get("helmet"):
                        allPlayerDataDict[playerIndex + 'Armour'] = 'both'
                    else:
                        allPlayerDataDict[playerIndex + 'Armour'] = 'armour'
                else:
                    allPlayerDataDict[playerIndex + 'Armour'] = 'none'

                # Now let's figure out what weapons the player has...
                nadeSlot = 1

                for weapon in data.get("allplayers").get(playerID).get('weapons'):

                    # First lets see if they have a pistol. If so, set that to the bigslot
                    if data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Pistol':
                        allPlayerDataDict[playerIndex + 'Bigslot'] = \
                            data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name')
                        # print(data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name'))

                    # If they have a rifle, shotgun, or SMG then place this over the top of the slot (replaces pistol)
                    elif data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Shotgun' \
                            or data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Rifle' \
                            or data.get("allplayers").get(playerID).get('weapons').get(weapon).get(
                        'type') == 'Submachine Gun':
                        allPlayerDataDict[playerIndex + 'Bigslot'] = \
                            data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name')

                    # Now we populate the nade slots
                    if data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Grenade':
                        allPlayerDataDict[playerIndex + 'Nadeslot' + str(nadeSlot)] = \
                            data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name')
                        nadeSlot = nadeSlot + 1

            # print(allPlayerDataDict)

            # entry gives key

            for entry in allPlayerCommandsDict:

                allPlayerCommandsDict[entry] = baseCommand.format(allPlayerLabelsDict[entry], allPlayerDataDict[entry])
                if allPlayerCommandsDict[entry] != prevAllPlayerCommandsDict[entry]:
                    # print(allPlayerCommandsDict[entry] + prevAllPlayerCommandsDict[entry])
                    commandString = commandString + allPlayerCommandsDict[entry]
                    # prevAllPlayerCommandsDict[entry] = allPlayerCommandsDict[entry]
            prevAllPlayerCommandsDict = dict(allPlayerCommandsDict)

            try:
                sendCommand(commandString)
            except AttributeError:
                print("Command was empty")

            commandString = ''

        else:
            sendCommand("end")

        # allCommands = baseCommand.format("Text22", data.get("player").get("name")) + baseCommand.format("Text22", data.get("player").get("name")

        # print(payload)
