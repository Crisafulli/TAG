import hashlib, time, hmac, urllib, random
import sys
import csv
from io import open

# THIS SCRIPT IS AN EXAMPLE OF MAKING A CALL TO ONE VERIZON CMS ACCOUNT
# BOTH PUBLIC AND NON-PUBLIC URL'S ARE CREATED AS THE OUTPUT
# WITH EACH SAID CHANNEL, CONTAINING SLIGHTLY DIFFERENT QUERY STRING PARAMETERS



# inputs
foxSportsKey = 'Acctoun Key Goes here' #


#Define the dictionary by VDMS CMS channel name and the channel GUID. These are the two inputs required to generate base url

# IF 'name' == 'Public', they have different, parameters than the other 'name''s in the dictionary. 

tokenDictionariesWrestleMania =   
# {'name': 'PPV Wrestlemania 36 | Public','cid': '8f88881faa334ab59484e999c6c5c318'},
{'name': 'TX711 | RBO | FXA - Pri','cid': '3ca9571bbb594403883b0a2f252c5ce9'},
{'name': 'TX711 | RBO | FXA - Sec','cid': 'a2d886c9106a4137b6f8907c885adf87'},
{'name': 'TX711 | RBO | FXB - Pri','cid': 'a2a71903ad254959905be305530a4288'},
{'name': 'TX711 | RBO | FXC - Sec','cid': '2994b2fe0cb74162b40b10c4deda223d'},
{'name': 'TX712 | RBO | FXA - Pri','cid': '8eed2e1150aa4f4bbed5f4cb5141191c'},
{'name': 'TX712 | RBO | FXA - Sec','cid': '1fa77fa623de42fb8634f86dffbd90a8'},
{'name': 'TX712 | RBO | FXB - Pri','cid': '8fa21a0fd0424af1b9ab2a577cc88abf'},
{'name': 'TX712 | RBO | FXC - Sec','cid': '00cc2c34d59843faa4fd9157bc8eee6a'},
{'name': 'AUX 992 | Pico | Unauthenticated','cid': 'c5eb8ab657f1487e85f26171a9e2db1b'},
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
    url = 'https://content.uplynk.com/channel/' + tokenDictionariesWrestleMania[index]["cid"] + '.m3u8'
    url = url + '?' + queryStr
    # tokenDictionariesSDR[index]['url'] = url

    


    # header = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36'
    # print("Printing tokenized probe for" + " " + tokenDictionariesSports[index]["name"] + '\n' + "==================================" + '\n' + url + '\n' + "==================================" '\n')
    # print("Now we have the url as well in the dict", tokenDictionariesHDR)
    print(tokenDictionariesWrestleMania[index]["name"] + " " + '\n' +  url + '\n')
  
    

   

















