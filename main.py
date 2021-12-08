from server import GSIServer
import csv

server = GSIServer(("127.0.0.1", 3000), "S8RL9Z6Y22TYQK45JB4V8PHRJJMD9DS9")
server.start_server()

# header = ['player', 'money', 'kills', 'assists', 'deaths', 'HS%', 'K/D', 'ADR']
#
# data = [server.get_info("player", "name"), server.get_info("player", "state", "money"), server.get_info("player", "match_stats", "kills"), server.get_info("player", "match_stats", "assists"), server.get_info("player", "match_stats", "deaths")
#
#
#
# ]
#
#
# f = open('data_out', 'w')
# writer = csv.writer(f)




# print(server.get_info("map", "name"))
# print(server.get_info("player", "state", "flashed"))
# print(server.get_info("player", "match_stats", "kills"))
# print(server.get_info("player", "match_stats", "deaths"))
# print(server.get_info("player", "match_stats", "score"))
# print(server.get_info("allplayers", "match_stats", "kills"))
# print(server.get_info("allplayers", "allplayers_entry"))
#


# self.assists = None
# self.deaths = None
# self.kills = None
# self.mvps = None
# self.score = None
