//Set up
const path = require('path');
const express = require('express');
const exphbs = require('express-handlebars');
const jsdom = require('jsdom');
const dom = new jsdom.JSDOM("");
const $ = require('jquery')(dom.window);
const  readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
var fs = require('fs');
var s =  require('net').Socket();
var app = express();

app.use(express.json());
app.use(express.urlencoded({extended: true}));

const { engine } = require('express-handlebars');
const { read } = require('fs');
const { response } = require('express');
const { setMaxIdleHTTPParsers } = require('http');
const { getSystemErrorMap } = require('util');
app.engine('.hbs', exphbs.engine({
    extname: ".hbs",
    defaultLayout: "main"
}));
app.set('views', path.join(__dirname, 'public/views'));
app.set('view engine', '.hbs');
app.use(express.static(path.join(__dirname, 'public')));
PORT = 3000;


//General Stuff
s.connect(6374, "127.0.0.1"); //ascii-to-hex translator
var asciiToHex = "";
s.on('data', function(d){
    asciiToHex = d.toString().slice(0);
    var firstInstance = asciiToHex.indexOf("!0!");
    asciiToHex = asciiToHex.slice(firstInstance + 3);
});

//Routing
app.get("/", function(req, res) {
    res.render('keyGen');
});

/*
* Uses :name so that new modules are easy to add in the future and wont require 
* A new route to be made for them.
*/
app.get('/:name', function(req, res){
    var filename = req.params.name;
    res.render(filename);
});

app.post('/generate-key', function(req, res){

    /*
    * Message Format: 
    * length
    */

    let data = req.body;
    let length = data.keyLength;

    fs.writeFileSync('generator-service.txt', length);

    let fileData = fs.readFileSync('generator-service.txt', {encoding:'utf8', flag:'r'});
    res.send({
        key: fileData
    });
});


app.post('/translate-ascii-hex', function(req, res){

    /*
    * message format: 
    * length!0!message
    */
    let data = req.body;
    let msg = data.asciiText;
    console.log(msg);
    s.write(msg);
    let response = "";
    setTimeout(function(){
        response = asciiToHex;
        console.log("newResponse : " + response);
        res.send({
            asciiText: response
        });
    }, 100);
});

app.listen(PORT, function (){
    console.log("Server is running on localhost " + PORT);
});