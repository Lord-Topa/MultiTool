//Set up and requirements
const path = require('path');
const express = require('express');
const exphbs = require('express-handlebars');
var fs = require('fs');
var socket =  require('net').Socket();
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

// Module IO paths
GENERATOR_PATH = 'generator-service.txt';
OTP_PATH = 'otpMicroservice.txt';
CEASER_PATH = 'ceaserCipher.txt';

//Ascii-to-hex translator server socket handling and the post handler
socket.connect(6374, "127.0.0.1");
var asciiToHex = "";
socket.on('data', function(d){
    asciiToHex = d.toString().slice(0);
    var firstInstance = asciiToHex.indexOf("!0!");
    asciiToHex = asciiToHex.slice(firstInstance + 3);
});
app.post('/translate-ascii-hex', function(req, res){
    let data = req.body;
    let message = data.asciiText;
    socket.write(message);
    let response = "";
    setTimeout(function(){
        response = asciiToHex;
        console.log("newResponse : " + response);
        res.send({
            asciiText: response
        });
    }, 100);
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

//This handler and all others after work similarly by watching a text file for changes
app.post('/generate-key', function(req, res){
    let data = req.body;
    let length = data.keyLength;

    fs.writeFileSync(GENERATOR_PATH, length);

    fs.watchFile(GENERATOR_PATH, {bigint: false, persistent: true, interval: 250}, (curr, prev) => {
        let fileData = fs.readFileSync(GENERATOR_PATH, {encoding:'utf8', flag:'r'});
        res.send({
            key: fileData.replaceAll('*', '')
        });
        fs.unwatchFile(GENERATOR_PATH);
    });
});

app.post('/otp-function', function(req, res){
    let data = req.body;
    let otpKey = data.keyText;
    let otpMessage = data.message;
    let otpType = data.type;
    let fileInput = otpType + '!0!' + otpKey + '!0!' + otpMessage;
    fs.writeFileSync(OTP_PATH, fileInput);
    fs.watchFile(OTP_PATH, {bigint: false, persistent: true, interval: 250}, (curr, prev) => {
        let fileData = fs.readFileSync(OTP_PATH, {encoding: 'utf8', flag:'r'});
        res.send({
            message: fileData
        });
        fs.unwatchFile(OTP_PATH);
    });

});

app.post('/ceaser-cipher', function(req, res){
    let data = req.body;
    let shift = data.shift;
    let message = data.message;

    console.log(message);
    let fileInput = shift + '!0!' + message;
    fs.writeFileSync(CEASER_PATH, fileInput);
    fs.watchFile(CEASER_PATH, {bigint: false, persistent: true, interval: 250}, (curr, prev) => {
        let fileData = fs.readFileSync(CEASER_PATH, {encoding: 'utf-8', flag: 'r'});
        res.send({message: fileData});
        fs.unwatchFile(CEASER_PATH);
    });

});

app.listen(PORT, function (){
    console.log("Server is running on localhost " + PORT);
});

//Handles exiting
process.on('SIGINT', () => { 
    console.log("Bye bye!");
    fs.writeFileSync(GENERATOR_PATH, 'exit');
    fs.writeFileSync(OTP_PATH, 'exit');
    fs.writeFileSync(CEASER_PATH, 'exit');
    process.exit();
 });