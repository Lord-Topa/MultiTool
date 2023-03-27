# MultiTool

## Contents:

* [Description](https://github.com/Lord-Topa/MultiTool#description)
* [Video Demonstration](https://github.com/Lord-Topa/MultiTool#video-demonstration)
* [Instructions](https://github.com/Lord-Topa/MultiTool#instructions)
	1. [Key Generator](https://github.com/Lord-Topa/MultiTool#key-gen)
	2. [OTP Encryption/Decryption](https://github.com/Lord-Topa/MultiTool##otp-encryptiondecryption)
	3. [Caesar Cipher](https://github.com/Lord-Topa/MultiTool#caesar-cipher)
	4. [Ascii to Hex](https://github.com/Lord-Topa/MultiTool#ascii-to-hex)
	5. [A Note on Modularity](https://github.com/Lord-Topa/MultiTool#a-note-on-modularity)

## Description:
A multitool that I made for my front end software engineering class in order to help me with really simple yet tedious tasks. These tasks include: key generation, One time pad encryption and decryption, caeser cipher encoding, and ascii to hexadecimal conversions. Since this project was made for my front end class the primary focus was integration and front end systems. 

Some of the characteristics I wanted this tool to have were:
* Easily maintainable

* Modular

* Easily upgradable

In order to meet the maintainable goal I made sure my code was free of code smells, well documented, and included a logging system 

In order to meet the modular goal I created each tool on its own making sure that they could run independently of the front end node server.

In order to meet the upgradability goal I used handlebars in order to make pages modular (as to not require a lot of re-writing code) and made pathing work off of file names. Adding new modules should be as easy as writing the front end page, creating a post/pull/etc. for the new page and implementing the start up of the new module into the npm start function. If the new module has an exit procedure then the signaling of the exit can be handled on the nodejs server.

## Video Demonstration:
<a href="https://youtu.be/VwoPMqud4Nw" title="MultiTool Showcase">
  <p align="center">
    <img width="75%" src="https://img.youtube.com/vi/VwoPMqud4Nw/maxresdefault.jpg" alt="Music Caster Video Demo Thumbnail"/>
  </p>
</a>

## Instructions:
In order to run the entire program one simply needs to get the dependencies for the project, at that point simply bring a terminal to the location of the project and run 
>npm start

At this point the user is ready to use any of the tools in the multitool.

When exiting after running this way the server will handle shutting down all microservices for the user

------------------
### Key Gen: 
------------------
*This micro-service was written by my partner in this class [Gabby North](https://github.com/GabbyNorth/CS361Microservice).*

1. Navigate to localhost:3000/keyGen or localhost:3000/ (the key generator is the home page)
2. Input integer into text area labeled "Key Length"
3. Press "Generate Key" button
4. Retreive key from "Key Output" text area
<img width="1317" alt="Screen Shot 2023-03-27 at 11 07 15 AM" src="https://user-images.githubusercontent.com/48222621/228029165-8ff72b72-1af9-4f67-ba78-6679a755bbb9.png">

------------------
### OTP Encryption/Decryption:
------------------
1. Navigate to localhost:3000/otp

2. Input a key into the "Key" text area.

	**Key Requirements:**
	* Must be same length as message being encrypted or decrypted
	* Key may only contain characters A-Z and space
	* All A-Z characters must be capital

	*A key meeting these requirements can be easily made using the key generator tool*
3. Input a message, consisting of only A-Z characters and space, into the "Message" text area
4. Press either the "Encrypt" or "Decrypt" button depending on desired function
5. Collect output from text area labeled "Output"
<img width="1317" alt="Screen Shot 2023-03-27 at 11 10 58 AM" src="https://user-images.githubusercontent.com/48222621/228029625-3f3eb8c8-ca6b-4dde-9b1d-e0484f479818.png">

------------------
### Caesar Cipher:
------------------
*I am aware that during the development of this project I mispelt the word "Caesar" the entire time, however at this point I can not be bothered to go back and change it*

1. Navigate to localhost:3000/ceaser
2. Input an integer into the "Shift" text area
3. Input a message, consisting of only A-Z characters and space, into the "Message" text area
4. Press the "Convert" button
5. Collect output from the text area labeled "Encoded"

------------------
### Ascii to Hex:
------------------
1. Navigate to localhost:3000/asciiToHex
2. Put a message, consisting of only valid ascii characters, into the "Ascii" text area
3. Press the "Translate" button
4. Collect hexadecimal version of message from the "Hexadecimal" text area

------------------
### A Note on Modularity:
------------------
Given the modular nature of this project each module also has its own set of instructions associated with them in the event that they should be run independently. These instructions are located in each modules respective README:

*It is worth noting that for all micro-services that used text files as a communication pipe the text file is not located within the micro-service's directory as they would normally need to be. This is because the npm start command implemented here makes each of the micro-services look for their respective text files within the directory that the main nodejs server is run in.*
* [Key Gen README](https://github.com/GabbyNorth/CS361Microservice)
* [OTP Encryption/Decryption README](https://github.com/Lord-Topa/MultiTool/tree/main/OTP)
* [Caesar Cipher README](https://github.com/Lord-Topa/MultiTool/tree/main/ceaserCipher)
* [AsciiToHex README](https://github.com/Lord-Topa/MultiTool/tree/main/asciiToHex)
