var express = require('express');
var router = express.Router();
var app = express();
var path = require('path');
var formidable = require('formidable');
var fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Build Your Own Classifier' });
});

app.get('/', function(req, res){
  res.sendFile(path.join(__dirname, 'views/index.ejs'));
});
app.get('/', function(req, res){
  res.sendFile(path.join(__dirname, 'views/train.ejs'));
});




module.exports = router;