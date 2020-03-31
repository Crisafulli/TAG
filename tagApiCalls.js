// require('dnscache')({ enable: true });
//imports at the top
const package = require('./package.json');
var SplunkLogger = require("splunk-logging").Logger;
var request = require("request");

function loopThroughJSON() {
  // If this gets too big, don't have it in
   console.log("This is working. Don't forget to define the rest of your function!")
  }



const endpoints = [
  {
  tagURL: 'http://52.12.21.142/api/2.0/channels/events/.json',
  // each source inside the splunk index, has a specified token
  Logger: new SplunkLogger({token:'6EA37CCC-3004-488F-856E-DABDFD0CBAC1', url:'https://http-inputs-fox.splunkcloud.com:443'}),
  interval: 3000,
  },
  {
  tagURL: 'http://52.12.21.142/api/2.0/channels/statistics/.json',
  Logger: new SplunkLogger({token:'FDD818FB-D069-441F-B5F1-EE62D9601B71', url:'https://http-inputs-fox.splunkcloud.com:443',}),
  interval: 3000,
  processResponse: loopThroughJSON,
  },

  {
  tagURL: 'http://52.12.21.142/api/2.0/channels/statistics/audio_pids_statistics/.json',
  Logger: new SplunkLogger({token:'84A5DBF1-D7F2-4403-9BA0-46C33B173A3C', url:'https://http-inputs-fox.splunkcloud.com:443',}),
  interval: 10000,
  },
  // {
  // tagURL: 'http://34.210.83.47/api/2.0/channels/statistics/{ID INTEGER}/.json',
  // Logger: new SplunkLogger({token:'84A5DBF1-D7F2-4403-9BA0-46C33B173A3C', url:'https://http-inputs-fox.splunkcloud.com:443',}),
  // interval: 10000,
  // },
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

// This line is optional
console.log("Sending payload", JSON.stringify(payload, null, 4));





Logger.send(payload, function(err, response, body) {
    // If successful, body will be { text: 'Success', code: 0 }
console.log("Response from Splunk", body);
});

Logger.error = function(err, context) {
  // Handle errors here
  console.log("error", err, "context", context);
};

// console.log(JSON.stringify(body, null , 2))
// console.log(response.error)
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
      // Need to define a funciton logErrorToSplunk(). 
      //Create payload > send message to splunk. Similar to log response to splunk. Send error and not api response
      // logger.send request (write to splunk)
    
    }else {
      //function to define (var paylod)
logResponseToSplunk(endpoint.Logger, options, response)
if (endpoint.processResponse) {
  endpoint.processResponse()
}

    }
  })
};

endpoints.forEach(endpoint => setInterval(run(endpoint), endpoint.interval))
