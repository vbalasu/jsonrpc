//npm install -g jayson
var jayson = require('jayson')
var client = jayson.client.http({host:"34.234.119.236", port:8080})
//var client = jayson.client.http({host:"127.0.0.1", port:8080})
client.request('add', [2,3], function(err, response) {console.log(response)})
