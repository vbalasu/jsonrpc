import jsonrpclib
server = jsonrpclib.ServerProxy('http://34.234.119.236:8080')
print(server.add(5,6))
