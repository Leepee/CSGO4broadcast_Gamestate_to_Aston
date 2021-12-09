import gamestate
import json
import csv
from shutil import copyfile

# A re-written function to manually build out a CSV that's simple to deal with from the user's side
class PayloadParser:

    # def geddit (self, dict, *keys):
    #
    #     print(keys)
    #
    #     for key in keys:
    #         try:
    #             print(key)
    #             return dict.get(key)
    #             # dict = dict[key]
    #             # print(_dict)
    #         except KeyError:
    #             return 'n/a'
    #
    #
    #     # try:
    #     #     return dict[keys]
    #     # except:
    #     #     return 'n/a'


    def parse_payload(self, payload, gamestate):

        # print(payload)

        # Headers for each data group

        provider = ['name', 'appid', 'version', 'steamid', 'timestamp']
        phase_countdowns = ['phase', 'phase ends in']
        map = ['round wins', 'mode', 'name', 'phase', 'round', 'ct score', 'ct consec. round loss', 'ct timeouts rem.', 'ct matches won', 't score', 't consec. round loss', 't timeouts rem.', 't matches won', 'matches to win series', 'spectators', 'souvenirs']
        round = ['phase']
        bomb = ['state', 'position', 'player']
        player = ['kills', 'assists', 'deaths', 'mvps', 'score', 'spectating', 'position', 'forward', 'weapons', 'state', 'steamID', 'name', 'observer slot', 'team', 'activity']
        allplayers = ['steamID', 'name', 'observer slot', 'team', 'kills', 'assists', 'deaths', 'mvps', 'score', 'health', 'armor', 'helmet','flashed', 'burning', 'money', 'round_kills', 'round_killhs', 'round_totaldmg', 'equip_value',
                      'weapon 0 name', 'weapon 0 paintkit', 'weapon 0 type', 'weapon 0 state', 'weapon 0 max ammo', 'weapon 0 ammo reserve', 'weapon 0 state',
                      'weapon 1 name', 'weapon 1 paintkit', 'weapon 1 type', 'weapon 1 ammo', 'weapon 1 max ammo', 'weapon 1 ammo reserve', 'weapon 1 state',
                      'weapon 2 name', 'weapon 2 paintkit', 'weapon 2 type', 'weapon 2 ammo', 'weapon 2 max ammo', 'weapon 2 ammo reserve', 'weapon 2 state',
                      'weapon 3 name', 'weapon 3 paintkit', 'weapon 3 type', 'weapon 3 state', 'weapon 3 max ammo', 'weapon 3 ammo reserve', 'weapon 3 state',
                      'weapon 4 name', 'weapon 4 paintkit', 'weapon 4 type', 'weapon 4 state', 'weapon 4 max ammo', 'weapon 4 ammo reserve', 'weapon 4 state',
                      'weapon 5 name', 'weapon 5 paintkit', 'weapon 5 type', 'weapon 5 state', 'weapon 5 max ammo', 'weapon 5 ammo reserve', 'weapon 5 state',
                      'weapon 6 name', 'weapon 6 paintkit', 'weapon 6 type', 'weapon 6 state', 'weapon 6 max ammo', 'weapon 6 ammo reserve', 'weapon 6 state',
                      'weapon 7 name', 'weapon 5 paintkit', 'weapon 7 type', 'weapon 7 state', 'weapon 7 max ammo', 'weapon 7 ammo reserve', 'weapon 7 state',
                      'weapon 8 name', 'weapon 8 paintkit', 'weapon 8 type', 'weapon 8 state', 'weapon 8 max ammo', 'weapon 8 ammo reserve', 'weapon 8 state'
                      ]

        f = open('data_out.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(f)

        dump = json.dumps(payload)
        data = json.loads(dump)

        writer.writerow('app info')
        writer.writerow(provider)
        writer.writerow([data['provider']['name'], data['provider']['appid'], data['provider']['version'], data['provider']['steamid'], data['provider']['timestamp']])
        writer.writerow([])


        writer.writerow('game phase info')
        writer.writerow(phase_countdowns)
        writer.writerow([data['phase_countdowns']['phase'], data['phase_countdowns']['phase_ends_in']])
        writer.writerow([])


        writer.writerow('map info')
        writer.writerow(map)
        writer.writerow([data['map']['round_wins'], data['map']['mode'], data['map']['name'], data['map']['phase'], data['map']['round'],
                         data['map']['team_ct']['score'], data['map']['team_ct']['consecutive_round_losses'], data['map']['team_ct']['timeouts_remaining'], data['map']['team_ct']['matches_won_this_series'],
                         data['map']['team_t']['score'], data['map']['team_t']['consecutive_round_losses'], data['map']['team_t']['timeouts_remaining'], data['map']['team_t']['matches_won_this_series'],
                         data['map']['num_matches_to_win_series'], data['map']['current_spectators'], data['map']['souvenirs_total']])
        writer.writerow([])


        writer.writerow('round info')
        writer.writerow(round)
        writer.writerow([data['round']['phase']])
        writer.writerow([])


        writer.writerow('bomb info')
        writer.writerow(bomb)
        writer.writerow([data['bomb']['state'], data['bomb']['position']
                            # , data['bomb']['player']
                         ])
        writer.writerow([])


        writer.writerow('observed player info')
        writer.writerow(player)
        writer.writerow([data['player']['match_stats']['kills'], data['player']['match_stats']['assists'], data['player']['match_stats']['deaths'], data['player']['match_stats']['mvps'], data['player']['match_stats']['score'],
                         data['player']['spectarget'], data['player']['position'], data['player']['forward'],
                         data['player']['weapons'], data['player']['state'], data['player']['steamid'], data['player']['name'], data['player']['observer_slot'], data['player']['team'], data['player']['activity']])
        writer.writerow([])


        writer.writerow('all players info')
        writer.writerow(allplayers)

        for playerID in data['allplayers']:

            allplayerRow = ([playerID, data['allplayers'][playerID]['name'], data['allplayers'][playerID]['observer_slot'], data['allplayers'][playerID]['team'],
                             data['allplayers'][playerID]['match_stats']['kills'], data['allplayers'][playerID]['match_stats']['assists'], data['allplayers'][playerID]['match_stats']['deaths'], data['allplayers'][playerID]['match_stats']['mvps'], data['allplayers'][playerID]['match_stats']['score'],
                             data['allplayers'][playerID]['state']['health'], data['allplayers'][playerID]['state']['armor'], data['allplayers'][playerID]['state']['helmet'],
                             data['allplayers'][playerID]['state']['flashed'], data['allplayers'][playerID]['state']['burning'], data['allplayers'][playerID]['state']['money'],
                             data['allplayers'][playerID]['state']['round_kills'], data['allplayers'][playerID]['state']['round_killhs'], data['allplayers'][playerID]['state']['round_totaldmg'], data['allplayers'][playerID]['state']['equip_value']])

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            # Weapon 0 - knife data
            print(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_0').get('state', 'n/a'))

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_1').get('state', 'n/a'))

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_2').get('state', 'n/a'))

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_3').get('state', 'n/a'))

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_4').get('state', 'n/a'))

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_5').get('state', 'n/a'))

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_6').get('state', 'n/a'))

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_7').get('state', 'n/a'))

            try:
                data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('name', 'n/a')
            except AttributeError:
                writer.writerow(allplayerRow)
                continue

            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('name', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('paintkit', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('type', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('ammo_clip', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('ammo_clip_max', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('ammo_reserve', 'n/a'))
            allplayerRow.append(data.get('allplayers').get(playerID).get('weapons').get('weapon_8').get('state', 'n/a'))


            writer.writerow(allplayerRow)


        # print(data['allplayers'][playerID])

        writer.writerow([])

        f.close()

        copyfile('data_out.csv', 'data_read.csv')








        # print(current_object)











# class PayloadParser:
#     def parse_payload(self, payload, gamestate):
#         for item in payload:
#             for i in payload[item]:
#                 try:
#                     x = i.isnumeric()
#                     if x:
#                         i = "allplayers_entry"
#                         # print("Getattr: " + getattr(gamestate, item) + " putting in " + i + payload[item][i])
#                         # print(i)
#                     setattr(getattr(gamestate, item), i, payload[item][i])
#                     # print(i)
#
#
#                     print(item)
#                     print(payload[item][i])
#                 except:
#                     # print(i)
#                     pass
