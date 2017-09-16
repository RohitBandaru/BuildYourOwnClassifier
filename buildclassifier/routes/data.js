/*
Take data and send to python for compution and retrieve results

*/
var fs = require('fs');

module.exports = function(app){
	//http://www.sohamkamani.com/blog/2015/08/21/python-nodejs-comm/
	fs.readFile('public/data/data.json', (err, data) => {  
	    if (err) throw err;
	    let parsedData = JSON.parse(data)["data"];

		var spawn = require('child_process').spawn
		var py = spawn('python3', ['./python/data_test.py'])

		var count = 0
		var dataString = ""
		var count = 0

		py.stdout.on('data', function(data){
			dataString += data
		});
		
		py.stdout.on('end', function(){
			response = JSON.parse(dataString);
			console.log(response);
		});

		//send JSON to python as string
		py.stdin.write(JSON.stringify(data));

		py.stdin.end();

	}); 

}