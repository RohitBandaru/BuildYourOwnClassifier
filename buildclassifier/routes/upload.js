'use strict';

 var Express = require('express');
 var multer = require('multer');
 var bodyParser = require('body-parser');
 var app = Express();
 app.use(bodyParser.json());

module.exports = function(app){

 var Storage = multer.diskStorage({
     destination: function(req, file, callback) {
         callback(null, "public/data");
     },
     filename: function(req, file, callback) {
         callback(null, file.originalname);
     }
 });
  var upload = multer({
     storage: Storage
 }).array("imgUploader", 3); //Field name and max count

  app.post('/upload', (req, res) => {
    console.log('file upload')
    upload(req, res, function(err) {
      if (err) {
         return res.end("Something went wrong!");
      }
      return res.end("File uploaded sucessfully!.");
    });
  });

  /*function upload(req, res){
    console.log("ye")
  } */

}