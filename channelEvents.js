// require('dnscache')({ enable: true });
//imports at the top
var SplunkLogger = require("splunk-logging").Logger;
var request = require("request");

const endpoints = [
  {
  tagURL: 'http://34.210.83.47/api/2.0/channels/events/.json',
  Logger: new SplunkLogger({token:'6EA37CCC-3004-488F-856E-DABDFD0CBAC1', url:'https://http-inputs-fox.splunkcloud.com:443'}),
  interval: 5000,
  },
  {
  tagURL: 'http://34.210.83.47/api/2.0/channels/statistics/.json',
  Logger: new SplunkLogger({token:'FDD818FB-D069-441F-B5F1-EE62D9601B71', url:'https://http-inputs-fox.splunkcloud.com:443',}),
  interval: 5000,
  },
];


// Counter is your API iterator. This will increase incrementally on the console after each call. 
let counter = 0; 

function logResponseToSplunk(Logger, options, response) {
  const body = JSON.parse(response.body)
  var payload = {
    // Message can be anything; doesn't have to be an object
    message: {
      // "endpoint": "Channel Events",
      "requestURL": options.url,
      "event": body,
      "httpStatus": response.statusCode,
      "error": response.error,
      "hello": "world",
      // "executionTime": results.preciseWords,
      // "runtime": end,
    }
};

console.log("Sending payload", payload);
Logger.send(payload, function(err, response, body) {
    // If successful, body will be { text: 'Success', code: 0 }
console.log("Response from Splunk", body);
});

Logger.error = function(err, context) {
  // Handle errors here
  console.log("error", err, "context", context);
};



console.log(JSON.stringify(body, null , 2))
// console.log(response.body);
console.log(response.error)
console.log(response.statusCode)
console.log("DONE")
console.log(`with API call ${counter}. Next call will be logged in 10 seconds`);
console.log("=======================")
console.log(options.url)
}


const run = (endpoint)=> () => {
  // paste options here:
  var options = {
    "method": "GET", 
    "url": endpoint.tagURL,
    "headers": {
      "Content-Type": "application/x-www-form-urlencoded",
      "Authorization": "Basic QWRtaW46QWRtaW4=",
    }
  };

return request(options, function (error, response) { 
    if (error){
      // Function to define -- this needs to be defined. Create payload. Send message to splunk. Similar to log response to splunk. Send error and not api response
      logErrorToSplunk()
    }else {
      //function to define (var paylod)
logResponseToSplunk(endpoint.Logger, options, response)
    }
  })
};
    // if (error) throw new Error(error);

  //Write new error funciton 
  // if error, call 'log error'<-- inside log error, prepare the payload and make logger.send request (write to splunk)


// Set 1 second interval for each API call 
// for perofmance of each call, do this inside of 'run' function
endpoints.forEach(endpoint => setInterval(run(endpoint), endpoint.interval))
// setInterval(run, 1000);


// this won't give you real value on 'execution time'
// const results = perf.stop('apiCall');
// console.log(results.time);  // in milliseconds
// console.log(results.preciseWords);  // in words