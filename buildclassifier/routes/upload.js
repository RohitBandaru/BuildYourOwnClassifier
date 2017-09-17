'use strict';

 var Express = require('express');
 var multer = require('multer');
 var bodyParser = require('body-parser');
 var app = Express();
 var fs = require('fs');
 app.use(bodyParser.json());
 var shortid = require('shortid');

module.exports = function(app){
  app.post('/upload', (req, res) => {
    var filename = "data"+shortid.generate();
    fs.writeFile("public/data/+"+filename+".json", JSON.stringify(req.body), 'utf8', function (err) {
        if (err) {
            return console.log(err);
        }
        console.log(filename+" was saved!");
    }); 
  });
}