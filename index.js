//var ping = require('ping-net');

exports.handler = (event, context, callback) => {

    sleep(15000, function() {
        // executes after one second, and blocks the thread
        console.log("Sleeeepy");
        callback(null, 'Hello from Lambda');
    });
};

function sleep(time, callback) {
    var stop = new Date().getTime();
    while(new Date().getTime() < stop + time) {
        ;
    }
    callback();
}