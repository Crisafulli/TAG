import hashlib, time, hmac, urllib, random

AccountDict = [
    {
        "account": "fox_sports",
        "owner":"replace with ID",
        "publicDictionary" : 
        [
            {
                "channel": "FS1 | National | Public",
                "cid": "ab9513294ec74cc8affeeb95acd413ce",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "ab9513294ec74cc8affeeb95acd413ce",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P NON-PUBLIC CHANNELS ONLY What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.acid": "FS1",
                    "ad.hylda": "1",
                    "ad.hylda_aiid_date": "0",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fs1",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below (line 32) If on FBC, add different values 
                    "ad.kv": "_fw_ae|{param:mvpd:nomvpd}|_fw_us_privacy|{param:_fw_us_privacy}|_fw_did_idfa|{param:idfa}|_fw_did_google_advertising_id|{param:google_advertising_id}|_fw_did_android_id|{param:android_id}|_fw_did|{param:did}|_fw_nielsen_app_id|{param:nielsen_app_id}|_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbsz8qqux,sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flexv": "2", # These will change in week or 2
                    "ad.flex": "15", # These will change
                    # "ad.cping": "1", Need to confirm
                    # "ad.pingf": "4", Need to confirm
                    "ad._debug": "tagFS1",
                    # "affiliate": "FS1", #does this mattter?
                    "v": "2",
                    "repl":"esni",
                    "cdn":"ec",

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX701 | National | Public",
                "cid": "f719c5102b2f45c7b9d2c3cc2d503736",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "f719c5102b2f45c7b9d2c3cc2d503736",
                    "up.session_kill_rate": "6000", #might not need this param
                    "rays": "h", #What ray do we want to use? This will change
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Keep these ad flags for TX routes
                    "ad.csid": "foxnow/webdesktop/live/fox", # advertising won't match to actual production config for contigency scenarios 
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", 
                    "ad.pingf": "4", 
                    "ad._debug": "tagTX701",
                    "affiliate": "KTTV", #half KTTV | half WNYW
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",                    
                    # "tag.identifier": "tagTX701", #Clayton to get back to us on what param should be (key + value) this would actually go in 'ad.kv' param

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX702 | National | Public",
                "cid": "1ce85fcdc39246248703a2632bfddd6a",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "1ce85fcdc39246248703a2632bfddd6a",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX702",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec", 
                    
                    #Clayton to get back to us on what param should be (key + value)
                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX703 | National | Public",
                "cid": "fd7df7a745884b3ca12c17fba3d6ff02",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "fd7df7a745884b3ca12c17fba3d6ff02",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX703",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",

                    #Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX704 | National | Public",
                "cid": "9682cf4424014d85a1f26b5191d74bac",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "9682cf4424014d85a1f26b5191d74bac",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX704",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
                  #Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX705 | National | Public",
                "cid": "610c2daed47c4e2c9597c34d7744412c",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "610c2daed47c4e2c9597c34d7744412c",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX705",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
#Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX706 | National | Public",
                "cid": "e878a286626743f0bc72260e21724122",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "e878a286626743f0bc72260e21724122",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX706",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
#Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX707 | National | Public",
                "cid": "881160e199434a15a01cdadaf26eddad",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "881160e199434a15a01cdadaf26eddad",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX707",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
                    
                    #Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX708 | National | Public",
                "cid": "a64461da15494af5b85fd2cf8d9e7578",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "a64461da15494af5b85fd2cf8d9e7578",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX708",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
#Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX709 | National | Public",
                "cid": "766150aff29646739f9d284471744072",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "766150aff29646739f9d284471744072",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX709",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
#Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX710 | National | Public",
                "cid": "05d851eb79c54f088350d1b516c4520d",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "05d851eb79c54f088350d1b516c4520d",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX710",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
#Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX711 | National | Public",
                "cid": "43e6970382264c5e9e351e65cc59e55f",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "43e6970382264c5e9e351e65cc59e55f",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX711",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
#Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            },
            {
                "channel": "TX712 | National | Public",
                "cid": "7fc7b3f8c5c64d98b457325bc5b8ac19",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "7fc7b3f8c5c64d98b457325bc5b8ac19",
                    "up.session_kill_rate": "6000",
                    "rays": "h", #What ray do we want to use?
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb", # Don't need beacons?
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    # only We need vcid2 for ad.kv param below | If on FBC, add different key values 
                    "ad.kv": "fnl-affiliate|KTTV|fs-affiliate|KTTV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr": "1031",
                    "ad.flex": "1", # These will change
                    "ad.cping": "1", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad.pingf": "4", # Need to confirm (can confirm this is in response for TX701 on delta-qa site)
                    "ad._debug": "tagTX712",
                    "affiliate": "KTTV",
                    "v": "2",
                    "repl":"aboi",
                    "cdn":"ec",
#Clayton to get back to us on what param should be (key + value)

                    #FBC channels: may need to pass in a location override param (What is this param?)
                    # Ad new param for tag specification
                    # Don't need ad debug for non public
                }
            }
        ],

        "nonPublicDictionary" :
        [
            {
                "channel": "FS1 | FXA | Primary",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "ab9513294ec74cc8affeeb95acd413ce",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "ab9513294ec74cc8affeeb95acd413ce",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX701 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "0eb1948699394327bc15a74115104c8e",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "0eb1948699394327bc15a74115104c8e",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX701 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "a904f9c683f64e3aaa99a275d14e0dcd",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "a904f9c683f64e3aaa99a275d14e0dcd",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX701 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "2cf22b4c204841409670b2df5a78ce99",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "2cf22b4c204841409670b2df5a78ce99",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX701 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "1ff3c601c90441f68a431511eb90df6c",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "1ff3c601c90441f68a431511eb90df6c",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX702 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "c7b46d33531c48d6bd10b00d0c00a1e6",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "c7b46d33531c48d6bd10b00d0c00a1e6",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX702 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "c934ab6e0df5464fbb6772c71ae65713",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "c934ab6e0df5464fbb6772c71ae65713",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX702 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "73bee087c22f4487ada16b6cede7396c",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "73bee087c22f4487ada16b6cede7396c",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX702 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "208a6b48211c448b935d2aa6ca5c0377",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "208a6b48211c448b935d2aa6ca5c0377",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX703 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "d2ef93cb84864b13b1cd1c48f7e98df9",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "d2ef93cb84864b13b1cd1c48f7e98df9",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX703 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "298d25ba67b74a859b1261e0d7458d89",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "298d25ba67b74a859b1261e0d7458d89",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX703 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "1e99895fcc8d44b8bf075d526ed39f62",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "1e99895fcc8d44b8bf075d526ed39f62",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX703 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "48930aa350764c948e12c2fcaa91e43f",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "48930aa350764c948e12c2fcaa91e43f",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX704 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "d0b02243f6c84380a9bf4d601c8357d4",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "d0b02243f6c84380a9bf4d601c8357d4",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX704 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "f182976d3b694c44b5015ae389345301",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "f182976d3b694c44b5015ae389345301",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX704 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "8b52af073bae4cc382fd3b5da7e0914a",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "8b52af073bae4cc382fd3b5da7e0914a",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX704 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "de9e6080527948919494e01f7b37967d",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "de9e6080527948919494e01f7b37967d",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX705 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "8864d5aee1dd48a69fe157c71a22246d",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "8864d5aee1dd48a69fe157c71a22246d",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX705 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "bbc8ba428d9343a0b5c238cd608aa794",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "bbc8ba428d9343a0b5c238cd608aa794",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX705 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "7fa1713f7c55486e9800ee8319e07f93",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "7fa1713f7c55486e9800ee8319e07f93",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX705 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "644c3aabc870475a939d6ddb6dad6980",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "644c3aabc870475a939d6ddb6dad6980",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX706 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "b10c98bd760046909ed80067e7e8e384",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "b10c98bd760046909ed80067e7e8e384",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX706 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "fe74c225f0a5455da55ad79d66095a26",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "fe74c225f0a5455da55ad79d66095a26",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX706 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "d756c2d062fb4ee586d1b210901eb0e2",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "d756c2d062fb4ee586d1b210901eb0e2",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX706 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "6842b715a5d540d08eed521eb5cde9d9",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "6842b715a5d540d08eed521eb5cde9d9",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX707 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "9d30094e0a83442bba2ddb5041cdf85f",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "9d30094e0a83442bba2ddb5041cdf85f",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX707 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "886ab9516d284359bf6f464daa00e37a",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "886ab9516d284359bf6f464daa00e37a",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX707 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "8f2e1f6862d5428f8ad5d521cf1394db",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "8f2e1f6862d5428f8ad5d521cf1394db",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX707 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "534d0ce35642496583cd590591ed64f6",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "534d0ce35642496583cd590591ed64f6",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX708 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "61191fcb059e462e8caa12a421fc621d",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "61191fcb059e462e8caa12a421fc621d",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX708 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "7011659bdcb24591bbc43fbd7dddf441",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "7011659bdcb24591bbc43fbd7dddf441",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX708 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "328df39a029d4f279feb7ed4e3cb8010",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "328df39a029d4f279feb7ed4e3cb8010",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX708 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "28fc816c18ea43e49987cddfdff7a703",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "28fc816c18ea43e49987cddfdff7a703",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX709 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "7987c520525a427b87b4080b089540d9",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "7987c520525a427b87b4080b089540d9",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX709 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "b35a24dc67324deaac29533d2abb16ec",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "b35a24dc67324deaac29533d2abb16ec",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX709 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "db2512779f144a8b97ca77f5844ab4d6",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "db2512779f144a8b97ca77f5844ab4d6",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX709 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "45d5ec0e32ed4967bd170d90203a848f",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "45d5ec0e32ed4967bd170d90203a848f",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX710 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "a544482dbe5f4646ad77ab3bb9dc3988",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "a544482dbe5f4646ad77ab3bb9dc3988",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX710 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "d6dc101697c54a879589df218f784a2d",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "d6dc101697c54a879589df218f784a2d",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX710 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "f9a55cb0ce224c0e882d5bf04522d840",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "f9a55cb0ce224c0e882d5bf04522d840",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX710 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "5ae41b2e17fb441ba307350c5175ef02",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "5ae41b2e17fb441ba307350c5175ef02",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX711 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "3ca9571bbb594403883b0a2f252c5ce9",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "3ca9571bbb594403883b0a2f252c5ce9",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX711 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "a2d886c9106a4137b6f8907c885adf87",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "a2d886c9106a4137b6f8907c885adf87",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX711 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "a2a71903ad254959905be305530a4288",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "a2a71903ad254959905be305530a4288",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX711 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "2994b2fe0cb74162b40b10c4deda223d",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "2994b2fe0cb74162b40b10c4deda223d",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX712 | National | FXA - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "8eed2e1150aa4f4bbed5f4cb5141191c",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "8eed2e1150aa4f4bbed5f4cb5141191c",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX712 | National | FXA - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "1fa77fa623de42fb8634f86dffbd90a8",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "1fa77fa623de42fb8634f86dffbd90a8",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX712 | National | FXB - Pri",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "8fa21a0fd0424af1b9ab2a577cc88abf",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "8fa21a0fd0424af1b9ab2a577cc88abf",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "TX712 | National | FXC - Sec",
                # "key": "pIbMLo934cPQtk0fLGO2CCYUp7BN3nhEyfktPnnz",
                "cid": "00cc2c34d59843faa4fd9157bc8eee6a",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "00cc2c34d59843faa4fd9157bc8eee6a",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            }
        ],
    },
    {
        "account": "fox_news",
        "owner":"replace with ID",
        "publicDictionary" : 
        [
            {
                "channel": "Fox News Channel | National | Public",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "1e298c9d65a245b3bd37f339cadcca58",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "1e298c9d65a245b3bd37f339cadcca58",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fnc",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.flex": 1,
                    "v": 2,
                    "ad._debug": "tagFNCTest",
                    "affiliate": "FNC",
                    "cdn": "ec",
                }
            }
        ],

        "nonPublicDictionary" :
        [
            {
                "channel": "Fox News Channel | FXA | Primary",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "29b42d799605404a925d45b437ada61d",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "29b42d799605404a925d45b437ada61d",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            }
        ],
    },
    {
        "account": "fox_owned_affiliates",
        "owner":"replace with ID",
        "publicDictionary" : 
        [
            {
                "channel": "KDFW | Fox-4 Dallas TX | Public",
                "cid": "f327b0440dfe43089bacfd977c6e0ec7",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "f327b0440dfe43089bacfd977c6e0ec7",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY
                    "ad": "fw_prod",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox", #always .../fox for csid unless on linear sports network
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|KDFW|fs-affiliate|KDFW|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagKDFW",
                    "ad.pingf": "4",
                    "affiliate": "KDFW",
                    "cdn": "ec",
                    "repl":"esni",
                    #  # don't need this parameter
                }
            },
            {
                "channel": "KMSP | Fox-9 Minneapolis | Public",
                "cid": "778175727d834ea8b057c6fcbb31e3c4",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "778175727d834ea8b057c6fcbb31e3c4",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|KMSP|fs-affiliate|KMSP|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagKMSP",
                    "ad.pingf": "4",
                    "affiliate": "KMSP",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "KRIV | Fox-26 Houston TX | Public",
                "cid": "3cba00c9351a496b97d4302f76677fc0",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "3cba00c9351a496b97d4302f76677fc0",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|KRIV|fs-affiliate|KRIV|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagKRIV",
                    "ad.pingf": "4",
                    "affiliate": "KRIV",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "KTBC | Fox-7 Austin TX | Public",
                "cid": "b2ef7a09d8d64302874b8dfc26ee1dee",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "b2ef7a09d8d64302874b8dfc26ee1dee",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|KTBC|fs-affiliate|KTBC|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagKTBC",
                    "ad.pingf": "4",
                    "affiliate": "KTBC",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "KSAZ | Fox-10 Phoenix | Public",
                "cid": "f7dad99d953a4a468239ee355b8dda93",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "f7dad99d953a4a468239ee355b8dda93",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|KSAZ|fs-affiliate|KSAZ|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagKSAZ",
                    "ad.pingf": "4",
                    "affiliate": "KSAZ",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "KTTV | Fox-11 Los Angeles CA | Public",
                "cid": "974a8c4f2e8c431a89d127ac9c57a29d",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "974a8c4f2e8c431a89d127ac9c57a29d",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|AFFILIATE CALL SIGN|fs-affiliate|AFFILIATE CALL SIGN|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagKTTVTest",
                    "ad.pingf": "4",
                    "affiliate": "KTTV",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "KTVU | Fox-2 San Francisco CA | Public",
                "cid": "fb9eee406c68408fb10f5e4baf579ad9",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "fb9eee406c68408fb10f5e4baf579ad9",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|KTVU|fs-affiliate|KTVU|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagKTVU",
                    "ad.pingf": "4",
                    "affiliate": "KTVU",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WAGA | Fox-5 Atlanta GA | Public",
                "cid": "e68a4110dfe24cbaa2f52f19061e4b83",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "e68a4110dfe24cbaa2f52f19061e4b83",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WAGA|fs-affiliate|WAGA|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagWAGA",
                    "ad.pingf": "4",
                    "affiliate": "WAGA",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WFLD | Fox-32 Chicago IL | Public",
                "cid": "99b44a26bc30487fa84a4fb38458944e",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "99b44a26bc30487fa84a4fb38458944e",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WFLD|fs-affiliate|WFLD|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagWFLD",
                    "ad.pingf": "4",
                    "affiliate": "WFLD",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WJBK | Fox-2 Detroit MI | Public",
                "cid": "84e66890e5b646bba52ee242b2eab4fd",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "84e66890e5b646bba52ee242b2eab4fd",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WJBK|fs-affiliate|WJBK|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagWJBK",
                    "ad.pingf": "4",
                    "affiliate": "WJBK",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WNYW | Fox-5 NYC NY | Public",
                "cid": "c9104b20238840d988c3f000890f7843",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "c9104b20238840d988c3f000890f7843",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WNYW|fs-affiliate|WNYW|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagWNYW",
                    "ad.pingf": "4",
                    "affiliate": "WNYW",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WOFL | Fox-35 Orlando FL | Public",
                "cid": "316e62a0ef29470dbb4c617e1de2f99d",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "316e62a0ef29470dbb4c617e1de2f99d",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WOFL|fs-affiliate|WOFL|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "WOFL",
                    "ad.pingf": "4",
                    "affiliate": "WOFL",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WOGX | Fox-51 Gainesville FL | Public",
                "cid": "9c6e2811ad394d6a8b93a60186423e57",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "9c6e2811ad394d6a8b93a60186423e57",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WOGX|fs-affiliate|WOGX|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagWOGX>",
                    "ad.pingf": "4",
                    "affiliate": "WOGX",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WTTG | Fox-5 Wash DC | Public",
                "cid": "6bd1ea18f6a14c70b76c49b72990c977",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "6bd1ea18f6a14c70b76c49b72990c977",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WTTG|fs-affiliate|WTTG|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagWTTG",
                    "ad.pingf": "4",
                    "affiliate": "WTTG",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WTVT | Fox-13 Tampa FL | Public",
                "cid": "4c6446157b9b48c891e83bee9913e944",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "4c6446157b9b48c891e83bee9913e944",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WTVT|fs-affiliate|WTVT|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagWTVT",
                    "ad.pingf": "4",
                    "affiliate": "WTVT",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            },
            {
                "channel": "WTXF | Fox-29 Philadelphia | Public",
                "cid": "7421ab1f10d34a919ff4c76f2d8cec14",
                "params": 
                {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "7421ab1f10d34a919ff4c76f2d8cec14",
                    # "up.session_kill_rate": "6000",
                    "rays": "h", #USED FOR 720P PUBLIC CHANNELS ONLY\
                    "ad": "fw_prod",
                    # "ad.breakend": "drop",
                    "ad.flags": ":slcb+sltp+qtbc+emcr+fbad+dtrd+vicb",
                    "ad.csid": "foxnow/webdesktop/live/fox",
                    "ad.prof": "516429:uplynk_foxnow_webdesktop_live",
                    "ad.kvsep": "|",
                    "ad.kv": "fnl-affiliate|WTXF|fs-affiliate|WTXF|_fw_ae|nomvpd|_fw_us_privacy|1---|_fw_did_idfa||_fw_did_google_advertising_id||_fw_did_android_id||_fw_did||_fw_nielsen_app_id||_fw_vcid2|a777b1c8-8ef2-4e08-8e93-3506fa8c804b|kuid|u3v6ytjya|_fw_seg|386123:sbu9bgphc,shpmwshty",
                    "ad.metr":"1031",
                    "ad.flex": "1",
                    "ad.breakend": "drop",
                    "v": "2",
                    "ad.cping": "1",
                    "ad._debug": "tagWTXF",
                    "ad.pingf": "4",
                    "affiliate": "WTXF",
                    "cdn": "ec",
                    "repl":"esni",
                    
                }
            }

        ],

        "nonPublicDictionary" :
        [
            {
                "channel": "KDFW | Fox-4 Dallas TX | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "e591f7887ad243b786861f04e1656069",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "e591f7887ad243b786861f04e1656069",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KDFW | Fox-4 Dallas TX | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "4fae8391d6b44298a56f84bdf0501a44",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "4fae8391d6b44298a56f84bdf0501a44",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KDFW | Fox-4 Dallas TX | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "068c8bbab26f4430a09fc55f146637e7",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "068c8bbab26f4430a09fc55f146637e7",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KDFW | Fox-4 Dallas TX | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "79c14f8359e547f38fc6d99acdbc894a",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "79c14f8359e547f38fc6d99acdbc894a",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KMSP | Fox-9 Minneapolis MN | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "a9605fc01378471c9352a745716fc21c",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "a9605fc01378471c9352a745716fc21c",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KMSP | Fox-9 Minneapolis MN | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "9d6f7748359f4cb4aab09c6515f31951",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "9d6f7748359f4cb4aab09c6515f31951",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KMSP | Fox-9 Minneapolis MN | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "877fd7599e8c432d9efc0a57327154f9",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "877fd7599e8c432d9efc0a57327154f9",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KMSP | Fox-9 Minneapolis MN | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "6cadc3e304c34ffa99885f3b6cadc9f9",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "6cadc3e304c34ffa99885f3b6cadc9f9",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KRIV | Fox-26 Houston TX | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "ed2bea70700a4e2dbf638377f888a72b",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "ed2bea70700a4e2dbf638377f888a72b",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KRIV | Fox-26 Houston TX | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "97a7179596914f9d90bea5e7a355509b",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "97a7179596914f9d90bea5e7a355509b",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KRIV | Fox-26 Houston TX | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "2accbd81c79444d59ba9de22c14fba54",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "2accbd81c79444d59ba9de22c14fba54",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KRIV | Fox-26 Houston TX | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "3d62a34405934865ace434bd64ddf571",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "3d62a34405934865ace434bd64ddf571",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTBC | Fox-7 Austin TX | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "e92d4d2e8a254f378e508ca566381f80",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "e92d4d2e8a254f378e508ca566381f80",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTBC | Fox-7 Austin TX | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "98ecf0fe9806434e87edc1388c874c42",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "98ecf0fe9806434e87edc1388c874c42",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTBC | Fox-7 Austin TX | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "ff11641ca1ce42d4bc2a4ccd43406cf8",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "ff11641ca1ce42d4bc2a4ccd43406cf8",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTBC | Fox-7 Austin TX | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "3972bb25b8ca4d65b01941327d781d78",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "3972bb25b8ca4d65b01941327d781d78",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KSAZ | Fox-10 Phoenix | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "bab0cffc51e246ee928180dd31af4237",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "bab0cffc51e246ee928180dd31af4237",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KSAZ | Fox-10 Phoenix | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "3aa9586f150847479fa0804b94f4980f",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "3aa9586f150847479fa0804b94f4980f",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KSAZ | Fox-10 Phoenix | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "17585cdbbcac49bf8638461f87ab36af",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "17585cdbbcac49bf8638461f87ab36af",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KSAZ | Fox-10 Phoenix | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "04ac5b0507c54b958bbd40974003a739",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "04ac5b0507c54b958bbd40974003a739",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTTV | Fox-11 Los Angeles CA | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "7e8e2b8e64254c66b8a540b0ad4bb9f2",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "7e8e2b8e64254c66b8a540b0ad4bb9f2",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTTV | Fox-11 Los Angeles CA | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "d2a30491adc14850acd4c66e8250d0ee",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "d2a30491adc14850acd4c66e8250d0ee",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTTV | Fox-11 Los Angeles CA | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "06c606d092644b20887e64f67d7c139c",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "06c606d092644b20887e64f67d7c139c",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTTV | Fox-11 Los Angeles CA | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "525dd01e1e2c4db2813d9e6329fa5aef",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "525dd01e1e2c4db2813d9e6329fa5aef",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },

            {
                "channel": "KTVU | Fox-2 San Francisco CA | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "fee4e2bb93f94e478d48c5b36f08fe06",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "fee4e2bb93f94e478d48c5b36f08fe06",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTVU | Fox-2 San Francisco CA | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "b23a8f89d0da405bad4b027368375e04",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "b23a8f89d0da405bad4b027368375e04",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTVU | Fox-2 San Francisco CA | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "a2b10f21c3e34a8d882c6763ade9c228",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "a2b10f21c3e34a8d882c6763ade9c228",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "KTVU | Fox-2 San Francisco CA | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "ceaff1ec617b458f9c6ab47d033cb3c1",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "ceaff1ec617b458f9c6ab47d033cb3c1",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WAGA | Fox-5 Atlanta GA | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "f2a94b1465684613b7f5416e09068ee5",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "f2a94b1465684613b7f5416e09068ee5",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WAGA | Fox-5 Atlanta GA | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "8e8a11a853c544aba04b31cca3e4f648",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "8e8a11a853c544aba04b31cca3e4f648",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WAGA | Fox-5 Atlanta GA | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "51df751f038f4d9da4f595c135068f58",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "51df751f038f4d9da4f595c135068f58",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WAGA | Fox-5 Atlanta GA | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "0547ec9cc75e4c69ace60a1da8739dcc",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "0547ec9cc75e4c69ace60a1da8739dcc",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WFLD | Fox-32 Chicago IL | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "c75920c52d4a4051bb99d6fd6afa312e",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "c75920c52d4a4051bb99d6fd6afa312e",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WFLD | Fox-32 Chicago IL | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "d276735a28fa4ad9a952f0572f5f5ff6",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "d276735a28fa4ad9a952f0572f5f5ff6",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WFLD | Fox-32 Chicago IL | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "fc45dc624ffb475487a5313e71800361",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "fc45dc624ffb475487a5313e71800361",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WFLD | Fox-32 Chicago IL | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "1a9773d032c94c9084d42a1ba37a6838",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "1a9773d032c94c9084d42a1ba37a6838",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WJBK | Fox-2 Detroit MI | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "61f8b1421d684a5ca04d450328891f0d",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "61f8b1421d684a5ca04d450328891f0d",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WJBK | Fox-2 Detroit MI | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "5c57fb286abf44e7a8f8cd9caac38b42",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "5c57fb286abf44e7a8f8cd9caac38b42",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WJBK | Fox-2 Detroit MI | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "2ae3ef81ee75465180d58d3ce24727e3",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "2ae3ef81ee75465180d58d3ce24727e3",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WJBK | Fox-2 Detroit MI | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "045ac20204214c5797f3f6431a64ad4e",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version+
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "045ac20204214c5797f3f6431a64ad4e",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WNYW | Fox-5 NYC NY | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "ffa8790995b54ce999f339df6064bf49",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "ffa8790995b54ce999f339df6064bf49",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WNYW | Fox-5 NYC NY | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "c069139f6975421c8835c13ccd2a83e9",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "c069139f6975421c8835c13ccd2a83e9",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WNYW | Fox-5 NYC NY | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "556822acf37349ce8486d9649fff2595",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "556822acf37349ce8486d9649fff2595",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WNYW | Fox-5 NYC NY | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "66e17268d0d34c128f8bd7eda02f5c04",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "66e17268d0d34c128f8bd7eda02f5c04",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WOFL | Fox-35 Orlando FL | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "5a2c57d356914d61b4301bb1dd42d3ed",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "5a2c57d356914d61b4301bb1dd42d3ed",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WOFL | Fox-35 Orlando FL | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "5abf721a97514d6b8e52b47a5cab7d66",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "5abf721a97514d6b8e52b47a5cab7d66",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WOFL | Fox-35 Orlando FL | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "1c595633e1d7437b9e76e525356d8ee1",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "1c595633e1d7437b9e76e525356d8ee1",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WOFL | Fox-35 Orlando FL | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "ba73508703074dafa3e79df8fd693e46",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "ba73508703074dafa3e79df8fd693e46",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WOGX | Fox-51 Gainesville FL | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "03e0a3b8cc85417fbb4dcc997e9e4eaa",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "03e0a3b8cc85417fbb4dcc997e9e4eaa",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WOGX | Fox-51 Gainesville FL | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "1a88cc3e34c2424583869a2be550d8d1",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "1a88cc3e34c2424583869a2be550d8d1",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WOGX | Fox-51 Gainesville FL | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "2199f6f935f64e3ca220c1cf29a5df4b",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "2199f6f935f64e3ca220c1cf29a5df4b",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WOGX | Fox-51 Gainesville FL | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "545894a6e0f246caaab23491f26d2595",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "545894a6e0f246caaab23491f26d2595",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTTG | Fox-5 Wash DC | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "63afe888981444b2b91800b43afae063",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "63afe888981444b2b91800b43afae063",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTTG | Fox-5 Wash DC | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "caa5f19f5d2041bca10a68d558638749",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "caa5f19f5d2041bca10a68d558638749",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTTG | Fox-5 Wash DC | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "d3abb6d1081045fe9e5d3cf304c34a75",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "d3abb6d1081045fe9e5d3cf304c34a75",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTTG | Fox-5 Wash DC | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "7cf5d3daadcd429c8897794073cfc752",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "7cf5d3daadcd429c8897794073cfc752",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTVT | Fox-13 Tampa FL | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "87bbc78be4ff4b70a3b3fbb5dfb4f52a",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "87bbc78be4ff4b70a3b3fbb5dfb4f52a",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTVT | Fox-13 Tampa FL | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "be12fe660c6b4952b37a7cf078dac95c",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "be12fe660c6b4952b37a7cf078dac95c",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTVT | Fox-13 Tampa FL | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "08c18a70aedc4cd5b432ed73d29b5220",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "08c18a70aedc4cd5b432ed73d29b5220",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTVT | Fox-13 Tampa FL | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "a3c4e3e0ec5e4cf7bc8137306507f024",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "a3c4e3e0ec5e4cf7bc8137306507f024",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTXF | Fox-29 Philadelphia PA | FXA - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "c3ce1870472d462e96775c035ea883df",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "c3ce1870472d462e96775c035ea883df",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTXF | Fox-29 Philadelphia PA | FXA - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "34ff5dff5805447fa3a48225dd25d327",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "34ff5dff5805447fa3a48225dd25d327",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTXF | Fox-29 Philadelphia PA | FXB - Pri",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "bf449e4971dd4eb4974973704715dee6",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "bf449e4971dd4eb4974973704715dee6",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
            {
                "channel": "WTXF | Fox-29 Philadelphia PA | FXC - Sec",
                # "key": "bvcuef+hyJ/fMSphegT6q2FeuQWjJ00hUqDyHv4F",
                "cid": "15b1e0008d9a4210b16e77bc68794ae9",
                "base_url": "https://content.uplynk.com/",
                "params": {
                    "tc": "1", # token check algorithm version
                    "exp": int(time.time()) + 1578700800, # expiry
                    "rn": str(random.randint(0, 2**32)), # random number
                    "ct": "c", #c = channel, a = asset, e = event
                    "cid": "15b1e0008d9a4210b16e77bc68794ae9",
                    "up.session_kill_rate": "6000",
                    "rays": "e", #USED FOR 720P NON-PUBLIC CHANNELS ONLY\
                    "ddp": "1"
                }
            },
        ],
    },

]
