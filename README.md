# TAG
Development for TAG monitoring &amp; metrics

Repository for all things TAG related. 

'tagApiCalls.js' is a script that polls muliple TAG endpoints and sends the payload to splunk. Each endpoint has a defined interval, ranging from 3-10 seconds. 

'exampleForTag.py' is an example script to create playable VMDS urls for TAG to use as a monitoring probe. The script is needed to digitally sign and authenticate the url.

It was noted that any further development of the .py script should be done by TAG. If that decision changes, as @Helior already alluded to, we should create a JSON config file, so that each URL can have Account & Channel specific parameters. 

Each account follows slightly different business logic that changes some of the parameters needed for the url. It follows a "public" vs a "non-public" concept.
