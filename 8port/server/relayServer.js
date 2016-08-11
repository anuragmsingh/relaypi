module.paths.push('/usr/local/lib/node_modules');

"use strict";

var   
express        =     require("express"),
http           =     require('http'),
fs             =     require('fs'),
url            =     require('url'),
exec           =     require('child_process').exec,
app            =     express(),
//multer         =     require('multer'),
//upload         =     multer({ dest: __dirname+'/upload/'});

scriptExecutor  =   require('./scriptExecutor.js');

app.get('/index.html',function(req,res){

   var	recUrl          =   url.parse(req.url),
        path            =   recUrl.path,
        pathname        =   recUrl.pathname,
        scriptIndex     =   -1,
        speed           =   100,
        getParams       =   path.split("?")[1];

   scriptIndex  =   speed   =   getParams;
   
   scriptIndex  =   parseInt(scriptIndex.replace(/(?:.*?)index=(.*?)(?:&.*|$)/, "$1").toLowerCase().replace(/%20/g, " "));
   speed        =   parseInt(speed.replace(/(?:.*?)speed=(.*?)(?:&.*|$)/, "$1").toLowerCase().replace(/%20/g, " "));

   console.log("Index received '"+scriptIndex+"'");
   console.log("Speed received '"+speed+"'");

   var scriptName = "";

   if(scriptIndex<0)
       scriptName="RelaySeqSuperSet";
   else if(scriptIndex==0)
        scriptName="RelayTest";
    else if(scriptIndex==1)
        scriptName="RelaySeq1";
    else if(scriptIndex==2)
        scriptName="RelaySeq2";
    else if(scriptIndex==3)
        scriptName="RelaySeq3";
    else if(scriptIndex==4)
        scriptName="RelaySeq4";
    else if(scriptIndex==5)
        scriptName="RelaySeq5";
    else if(scriptIndex==11)
        scriptName="RelayBinary";

   scriptExecutor.processQuery(scriptName, speed, scriptIndex<0);

   res.sendFile(__dirname + "/index.html");
});

app.listen(8082, function(){
   console.log("Running on port 8082");
});
