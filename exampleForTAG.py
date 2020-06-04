import hashlib, time, hmac, urllib, random
import sys
import csv
from io import open

# THIS SCRIPT IS AN EXAMPLE OF MAKING A CALL TO ONE VERIZON CMS ACCOUNT
# BOTH PUBLIC AND NON-PUBLIC URL'S ARE CREATED AS THE OUTPUT
# WITH EACH SAID CHANNEL, CONTAINING SLIGHTLY DIFFERENT QUERY STRING PARAMETERS



# inputs
#change this to the account you want to create playback urls for
foxSportsKey = 'Acctoun Key Goes here' # Pass it in as parm on 55 


#Define the dictionary by VDMS CMS channel name and the channel GUID. These are the two inputs required to generate base url

# IF 'name' == 'Public', they have different, parameters than the other 'name''s in the dictionary. 

tokenDictionariesWrestleMania =   
# {'name': 'PPV Wrestlemania 36 | Public','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
{'name': ' Channel Name','cid': 'channel GUID'},
]

# For the dictionary above, append VDMS specific params needed to digitally sign, authenticate, and allow playback.

for index in range(len(tokenDictionariesWrestleMania)):
    # print(tokenDictionariesSports[index]["cid"])
    qs = {
        'tc': '1', # token check algorithm version
        'exp': int(time.time()) + 1578700800, # expiry
        'rn': str(random.randint(0, 2**32)), # random number
        'ct': 'c', #c = channel, a = asset, e = event
        'cid': tokenDictionariesWrestleMania[index]['cid'],
        'up.session_kill_rate': '6000',
        'repl': 'aboi', # Fox specifc blackout policy
        # 'rays': 'h' USED FOR 720P PUBLIC CHANNELS ONLY
        'rays': 'e', #USED FOR 720P NON-PUBLIC CHANNELS ONLY
        # 'rays': 'f', USED FOR UHD PUBLICS ONLY 
         # 'rays': 'b', USED FOR UDH NON-PUBLICS ONLY
        # 'm4fenctype': 'cenc', THIS IS ONLY NEEDED ON UHD CHANNELS  
    }

    queryStr = urllib.urlencode(dict(qs))
    # compute the digital signature and add it to the *end* of url
    sig = hmac.new(foxSportsKey, queryStr, hashlib.sha256).hexdigest()
    queryStr = queryStr + '&sig=' + sig

    # The token would then be added to a playback URL, e.g.
    url = 'https://somthing.here.com/channel/' + tokenDictionariesWrestleMania[index]["cid"] + '.m3u8'
    url = url + '?' + queryStr
    # tokenDictionariesSDR[index]['url'] = url
    

    # header = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36'
    # print("Printing tokenized probe for" + " " + tokenDictionariesSports[index]["name"] + '\n' + "==================================" + '\n' + url + '\n' + "==================================" '\n')
    # print("Now we have the url as well in the dict", tokenDictionariesHDR)
    print(tokenDictionariesWrestleMania[index]["name"] + " " + '\n' +  url + '\n')
