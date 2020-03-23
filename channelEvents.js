// require('dnscache')({ enable: true });
//imports at the top
const package = require('./package.json');
var SplunkLogger = require("splunk-logging").Logger;
var request = require("request");

//All new code can delete all the up to "const endpoints"

const endpoints = [
  {
  tagURL: 'http://34.210.83.47/api/2.0/channels/events/.json',
  // each source inside the splunk index, has a specified token
  Logger: new SplunkLogger({token:'6EA37CCC-3004-488F-856E-DABDFD0CBAC1', url:'https://http-inputs-fox.splunkcloud.com:443'}),
  interval: 3000,
  },
  {
  tagURL: 'http://34.210.83.47/api/2.0/channels/statistics/.json',
  Logger: new SplunkLogger({token:'FDD818FB-D069-441F-B5F1-EE62D9601B71', url:'https://http-inputs-fox.splunkcloud.com:443',}),
  interval: 3000,
  },

  // Add endpoints if we expand
];


// Counter is your API iterator. This will increase incrementally on the console after each call. 
      let counter = 0; 

      function logResponseToSplunk(Logger, options, response) {
        const body = JSON.parse(response.body)
        // const body = JSON.stringify(response.body)
        var payload = {
          // Message can be anything; doesn't have to be an object
          message: {
            "requestURL": options.url,
            "event": body,
            "httpStatus": response.statusCode,
            "message": response.statusMessage,
            // "error": error.message,
            // "method": response.method.message,
            // "errorContext": response.error.context
            // "hello": "world",
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
console.log(response.error)
console.log(response.statusCode)
console.log(`API call ${counter}` + ' ' + 'complete.');
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
      // logErrorToSplunk()
    }else {
      //function to define (var paylod)
logResponseToSplunk(endpoint.Logger, options, response)
    }
  })
};

  //Write new error funciton 
  // if error, call 'log error'<-- inside log error, prepare the payload and make logger.send request (write to splunk)
 
// for perofmance of each call, do this inside of 'run' function
endpoints.forEach(endpoint => setInterval(run(endpoint), endpoint.interval))
