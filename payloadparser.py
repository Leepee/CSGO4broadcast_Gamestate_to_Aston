import json
import csv
import socket
from shutil import copyfile

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

roundInfoDict = {'PhaseTimer': '00.00', 'Phase': 'Starting', 'RoundNumber': '0', 'T1Wins': '0', 'T2Wins': '0'}

observedPlayerDict = {
    'obsPlayerName': 'obsPlayerName', 'obsPlayerHealth': '100', 'obsPlayerKills': 'obsPlayerKills',
    'obsPlayerDeaths': 'obsPlayerDeaths', 'obsPlayerMoney': 'obsPlayerMoney',
    'obsPlayerBigslot': 'None', 'obsPlayerBombDefuser': 'None', 'obsPlayerArmour': 'None',
    'obsPlayerNadeslot1': 'None', 'obsPlayerNadeslot2': 'None', 'obsPlayerNadeslot3': 'None',
    'obsPlayerNadeslot4': 'None'}

player1Name = "Text24"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
except ConnectionRefusedError:
    print("I no server worky")


def sendCommand(commands_to_send):
    try:
        if commands_to_send == "end":

            s.sendall("print(Laters players!);".encode('utf-8'))
            s.close()
        else:
            s.sendall(commands_to_send.encode('utf-8'))
            print(commands_to_send)
    except OSError:
        pass


# A re-written function to manually build out a CSV that's simple to deal with from the user's side
class PayloadParser:

    def parse_payload(self, payload, gamestate):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=4)
        dump = json.dumps(payload)
        data = json.loads(dump)

        while data.get("player").get("activity") == "playing":

            # Setting up some player identifiers (T1, CT4), and checking into player instances

            Ts = 1
            CTs = 1
            for playerID in data['allplayers']:
                playerIndex = data.get("allplayers").get(playerID).get("team")

                if playerIndex == "T":
                    playerIndex = playerIndex + str(Ts)
                    print(playerIndex)
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
                    elif data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Shotgun'\
                        or data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Rifle' \
                        or data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Submachine Gun':
                        allPlayerDataDict[playerIndex + 'Bigslot'] = \
                            data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name')
                        print(data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name'))

                    # Now we populate the nade slots
                    if data.get("allplayers").get(playerID).get('weapons').get(weapon).get('type') == 'Grenade':
                        allPlayerDataDict[playerIndex + 'Nadeslot' + str(nadeSlot)] = \
                            data.get("allplayers").get(playerID).get('weapons').get(weapon).get('name')
                        nadeSlot = nadeSlot + 1

            print(allPlayerDataDict)





                # print(data.get("allplayers").get(playerID).get("name"))

        sendCommand("end")

        # allCommands = baseCommand.format("Text22", data.get("player").get("name")) + baseCommand.format("Text22", data.get("player").get("name")

        # print(payload)

        # Headers for each data group

        provider = ['name', 'appid', 'version', 'steamid', 'timestamp']
        phase_countdowns = ['phase', 'phase ends in']
        map = ['round wins', 'mode', 'name', 'phase', 'round', 'ct score', 'ct consec. round loss', 'ct timeouts rem.',
               'ct matches won', 't score', 't consec. round loss', 't timeouts rem.', 't matches won',
               'matches to win series', 'spectators', 'souvenirs']
        round = ['phase']
        bomb = ['state', 'position', 'player']
        player = ['kills', 'assists', 'deaths', 'mvps', 'score', 'spectating', 'position', 'forward', 'weapons',
                  'state', 'steamID', 'name', 'observer slot', 'team', 'activity']
        allplayers = ['steamID', 'name', 'observer slot', 'team', 'kills', 'assists', 'deaths', 'mvps', 'score',
                      'health', 'armor', 'helmet', 'flashed', 'burning', 'money', 'round_kills', 'round_killhs',
                      'round_totaldmg', 'equip_value',
                      'weapon 0 name', 'weapon 0 paintkit', 'weapon 0 type', 'weapon 0 state', 'weapon 0 max ammo',
                      'weapon 0 ammo reserve', 'weapon 0 state',
                      'weapon 1 name', 'weapon 1 paintkit', 'weapon 1 type', 'weapon 1 ammo', 'weapon 1 max ammo',
                      'weapon 1 ammo reserve', 'weapon 1 state',
                      'weapon 2 name', 'weapon 2 paintkit', 'weapon 2 type', 'weapon 2 ammo', 'weapon 2 max ammo',
                      'weapon 2 ammo reserve', 'weapon 2 state',
                      'weapon 3 name', 'weapon 3 paintkit', 'weapon 3 type', 'weapon 3 state', 'weapon 3 max ammo',
                      'weapon 3 ammo reserve', 'weapon 3 state',
                      'weapon 4 name', 'weapon 4 paintkit', 'weapon 4 type', 'weapon 4 state', 'weapon 4 max ammo',
                      'weapon 4 ammo reserve', 'weapon 4 state',
                      'weapon 5 name', 'weapon 5 paintkit', 'weapon 5 type', 'weapon 5 state', 'weapon 5 max ammo',
                      'weapon 5 ammo reserve', 'weapon 5 state',
                      'weapon 6 name', 'weapon 6 paintkit', 'weapon 6 type', 'weapon 6 state', 'weapon 6 max ammo',
                      'weapon 6 ammo reserve', 'weapon 6 state',
                      'weapon 7 name', 'weapon 5 paintkit', 'weapon 7 type', 'weapon 7 state', 'weapon 7 max ammo',
                      'weapon 7 ammo reserve', 'weapon 7 state',
                      'weapon 8 name', 'weapon 8 paintkit', 'weapon 8 type', 'weapon 8 state', 'weapon 8 max ammo',
                      'weapon 8 ammo reserve', 'weapon 8 state'
                      ]

        #
        # if data.get('player').get('activity') == 'menu':
        #     print('Please observe a game')
        # else:
        #     f = open('data_out.csv', 'w', newline='', encoding='utf-8')
        #     writer = csv.writer(f)
        #
        #
        #     writer.writerow('app info')
        #     writer.writerow(provider)
        #     writer.writerow([data['provider']['name'], data['provider']['appid'], data['provider']['version'], data['provider']['steamid'], data['provider']['timestamp']])
        #     writer.writerow([])
        #
        #
        #     writer.writerow('game phase info')
        #     writer.writerow(phase_countdowns)
        #     writer.writerow([data['phase_countdowns']['phase'], data['phase_countdowns']['phase_ends_in']])
        #     writer.writerow([])
        #
        #
        #     writer.writerow('map info')
        #     writer.writerow(map)
        #     writer.writerow([data['map']['round_wins'], data['map']['mode'], data['map']['name'], data['map']['phase'], data['map']['round'],
        #                      data['map']['team_ct']['score'], data['map']['team_ct']['consecutive_round_losses'], data['map']['team_ct']['timeouts_remaining'], data['map']['team_ct']['matches_won_this_series'],
        #                      data['map']['team_t']['score'], data['map']['team_t']['consecutive_round_losses'], data['map']['team_t']['timeouts_remaining'], data['map']['team_t']['matches_won_this_series'],
        #                      data['map']['num_matches_to_win_series'], data['map']['current_spectators'], data['map']['souvenirs_total']])
        #     writer.writerow([])
        #
        #
        #     writer.writerow('round info')
        #     writer.writerow(round)
        #     writer.writerow([data['round']['phase']])
        #     writer.writerow([])
        #
        #
        #     writer.writerow('bomb info')
        #     writer.writerow(bomb)
        #     writer.writerow([data['bomb']['state'], data['bomb']['position']
        #                         # , data['bomb']['player']
        #                      ])
        #     writer.writerow([])
        #
        #
        #     writer.writerow('observed player info')
        #     writer.writerow(player)
        #     writer.writerow([data['player']['match_stats']['kills'], data['player']['match_stats']['assists'], data['player']['match_stats']['deaths'], data['player']['match_stats']['mvps'], data['player']['match_stats']['score'],
        #                      data['player']['spectarget'], data['player']['position'], data['player']['forward'],
        #                      data['player']['weapons'], data['player']['state'], data['player']['steamid'], data['player']['name'], data['player']['observer_slot'], data['player']['team'], data['player']['activity']])
        #     writer.writerow([])
        #
        #
        #     writer.writerow('all players info')
        #     writer.writerow(allplayers)
        #
        #     for playerID in data['allplayers']:
        #
        #         allplayerRow = ([playerID, data['allplayers'][playerID]['name'], data['allplayers'][playerID]['observer_slot'], data['allplayers'][playerID]['team'],
        #                          data['allplayers'][playerID]['match_stats']['kills'], data['allplayers'][playerID]['match_stats']['assists'], data['allplayers'][playerID]['match_stats']['deaths'], data['allplayers'][playerID]['match_stats']['mvps'], data['allplayers'][playerID]['match_stats']['score'],
        #                          data['allplayers'][playerID]['state']['health'], data['allplayers'][playerID]['state']['armor'], data['allplayers'][playerID]['state']['helmet'],
        #                          data['allplayers'][playerID]['state']['flashed'], data['allplayers'][playerID]['state']['burning'], data['allplayers'][playerID]['state']['money'],
        #                          data['allplayers'][playerID]['state']['round_kills'], data['allplayers'][playerID]['state']['round_killhs'], data['allplayers'][playerID]['state']['round_totaldmg'], data['allplayers'][playerID]['state']['equip_value']])
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         # Weapon 0 - knife data
        #         print(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('state', 'n/a'))
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('state', 'n/a'))
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('state', 'n/a'))
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('state', 'n/a'))
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('state', 'n/a'))
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('state', 'n/a'))
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('state', 'n/a'))
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('state', 'n/a'))
        #
        #         try:
        #             data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('name', 'n/a')
        #         except AttributeError:
        #             writer.writerow(allplayerRow)
        #             continue
        #
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('name', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('paintkit', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('type', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('ammo_clip', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('ammo_clip_max', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('ammo_reserve', 'n/a'))
        #         allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('state', 'n/a'))
        #
        #
        #         writer.writerow(allplayerRow)
        #
        #     f.close()
        #
        #     try:
        #         copyfile('data_out.csv', 'data_read.csv')
        #     except PermissionError:
        #         pass
