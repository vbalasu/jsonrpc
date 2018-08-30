# json rpc

You can easily create a python server script and expose functions that can be called remotely.

`pip install jsonrpclib-pelix`
#### server.py
```
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
```

#### client.py
```
import jsonrpclib
server = jsonrpclib.ServerProxy('http://127.0.0.1:8080')
print(server.add(5,6))
```

## Javascript Client

#### client.js
```
//npm install -g jayson
var jayson = require('jayson')
var client = jayson.client.http({host:"127.0.0.1", port:8080})
client.request('add', [2,3], function(err, response) {console.log(response)})
```