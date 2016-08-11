"use strict";

var child = undefined,

killPreviouslyRunning = function() {
    if(child){
        var killCommand = "pkill -f Relay",
            cleanCommand = "python /home/pi/relaypi/8port/RelayCleaner.py";
        executeShellCommand(killCommand, executeShellCommand, cleanCommand);
        child = undefined
    }
},

executeShellCommand = function(commandToExecute, callbackFunc, callbackFuncArg) {

	child = require('child_process').exec(commandToExecute, [], function(){
        //OnCompletion
        if(callbackFunc)
            callbackFunc(callbackFuncArg, null, null);
    });
	
    child.on('error', function (err) { 
        console.log("Error executing shell command :" + commandToExecute);
        console.log(err);    
    }); 
};

exports.processQuery = function(scriptSource, scriptSpeed, isShellScript) {

    var scriptRunCommand = isShellScript ?  "cd /home/pi/relaypi/8port/; sh ./"+scriptSource+".sh" : "python /home/pi/relaypi/8port/"+scriptSource+".py "+scriptSpeed;
    
    killPreviouslyRunning();
    executeShellCommand(scriptRunCommand, null, null);
};
