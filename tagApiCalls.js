// require('dnscache')({ enable: true });
//imports at the top
const package = require('./package.json');
var SplunkLogger = require("splunk-logging").Logger;
var request = require("request");


const endpoints = [
  {
    tagURL: 'http://address/api/2.0/channels/events/.json',
    // each source inside the splunk index, has a specified token
    Logger: new SplunkLogger({token: 'token', url: 'splunk-url'}),
    interval: 3000,
    logChannelItems: false
  },
  {
    tagURL: 'http://address/api/2.0/channels/statistics/.json',
    Logger: new SplunkLogger({token: 'token', url: 'splunk-url',}),
    interval: 3000,
    logChannelItems: true,
    channelLogger: new SplunkLogger({token: 'token', url: 'splunk-url', }),
  },
  {
    tagURL: 'http://address/api/2.0/channels/statistics/audio_pids_statistics/.json',
    Logger: new SplunkLogger({token: 'token', url: 'splunk-url',}),
    interval: 5000,
    logChannelItems: false    
  },
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

  // The following line is optional
//   console.log("Sending payload", JSON.stringify(payload, null, 4));

  Logger.send(payload, function (err, response, body) {
    // If successful, body will be { text: 'Success', code: 0 }
    console.log("Response from Splunk", body);
  });

  Logger.error = function (err, context) {
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


const run = (endpoint) => () => {
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
    if (error) {
      // Need to define a funciton logErrorToSplunk(). 
      //Create payload > send message to splunk. Similar to log response to splunk. Send error and not api response
      // logger.send request (write to splunk)

    } else {

      if (endpoint.logChannelItems) {    
        const body = JSON.parse(response.body)   
        body.forEach(it => {
          var id = it.ChannelStatistics.id
          var url = endpoint.tagURL.replace('.json', `${id}/.json`)          
          run({ tagURL: url, Logger: endpoint.channelLogger, logChannelItems:false })()
        })
      }
      //function to define (var paylod)
      logResponseToSplunk(endpoint.Logger, options, response)
      if (endpoint.processResponse) {
        endpoint.processResponse()
      }

    }
  })
};

// console.log('Congratulations! Now run it for real, and see if the response will still post!')



endpoints.forEach(endpoint => setInterval(run(endpoint), endpoint.interval))
