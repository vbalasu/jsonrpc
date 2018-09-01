#pip install jsonrpclib-pelix
import jsonrpclib
server = jsonrpclib.ServerProxy('http://127.0.0.1:8080')
print(server.add(5,6))
