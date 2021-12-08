import gamestate
import json
import csv
from shutil import copyfile

# A re-written funtion to manually build out a CSV that's simple to deal with from the user's side
class PayloadParser:
    def parse_payload(self, payload, gamestate):

        # Headers for each data group

        provider = ['name', 'appid', 'version', 'steamid', 'timestamp']
        phase_countdowns = ['phase', 'phase ends in']
        map = ['round wins', 'mode', 'name', 'phase', 'round', 'ct score', 'ct consec. round loss', 'ct timeouts rem.', 'ct matches won', 't score', 't consec. round loss', 't timeouts rem.', 't matches won', 'matches to win series', 'spectators', 'souvenirs']
        round = ['phase']
        bomb = ['state', 'position', 'player']
        player = ['kills', 'assists', 'deaths', 'mvps', 'score', 'spectating', 'position', 'forward', 'weapons', 'state', 'steamID', 'clan', 'name', 'observer slot', 'team', 'activity']
        allplayers = ['steamID', 'clan', 'name', 'observer slot', 'team', 'kills', 'assists', 'deaths', 'mvps', 'score', 'health', 'armor', 'helmet','flashed', 'burning', 'money', 'round_kills', 'round_killhs', 'round_totaldmg', 'equip_value']

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
                         data['map']['team_t']['score'], data['map']['team_t']['consecutive_round_losses'], data['map']['team_t']['timeouts_remaining'], data['map']['team_t']['matches_won_this_series']])
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
                         data['player']['spectarget'], data['player']['position'], data['player']['forward'], data['player']['spectarget'],
                         data['player']['weapons'], data['player']['state'], data['player']['steamid']
                            # , data['player']['clan']
                            , data['player']['name'], data['player']['observer_slot'], data['player']['team'], data['player']['activity']])
        writer.writerow([])


        writer.writerow('all players info')
        writer.writerow(allplayers)

        for playerID in data['allplayers']:
            print(playerID)
            writer.writerow([playerID, data['allplayers'][playerID]['name'], data['allplayers'][playerID]['name'], data['allplayers'][playerID]['observer_slot'], data['allplayers'][playerID]['team'],
                             data['allplayers'][playerID]['match_stats']['kills'], data['allplayers'][playerID]['match_stats']['assists'], data['allplayers'][playerID]['match_stats']['deaths'], data['allplayers'][playerID]['match_stats']['mvps'], data['allplayers'][playerID]['match_stats']['score'],
                             data['allplayers'][playerID]['state']['health'], data['allplayers'][playerID]['state']['armor'], data['allplayers'][playerID]['state']['helmet'],
                             data['allplayers'][playerID]['state']['flashed'], data['allplayers'][playerID]['state']['burning'], data['allplayers'][playerID]['state']['money'],
                             data['allplayers'][playerID]['state']['round_kills'], data['allplayers'][playerID]['state']['round_killhs'], data['allplayers'][playerID]['state']['round_totaldmg'], data['allplayers'][playerID]['state']['equip_value']])

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
