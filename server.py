#pip install jsonrpclib-pelix
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import datetime
def months():
  return ['Jan','Feb','Mar']

def now():
  return str(datetime.datetime.now())

server = SimpleJSONRPCServer(('localhost', 8080))
server.register_function(pow)
server.register_function(months)
server.register_function(now)
server.register_function(lambda x,y: x+y, 'add')
server.register_function(lambda x: x, 'ping')
server.serve_forever()
