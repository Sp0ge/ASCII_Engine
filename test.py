import json
data = "{'players': {'1': {'pos_x': '6', 'pos_y': '12', 'health': '100', 'bullets': '10', 'name': 'TEST'}, '2': {'pos_x': '20', 'pos_y': '20', 'health': '100', 'bullets': '10', 'name': 'Connecting'}}, 'map': {'size_x': '400', 'size_y': '400', 'data': 'asda'}}"
info = json.loads(data)
print(info["players"])
