import hashlib, time, hmac, urllib, random
import sys
import csv
from io import open
import tagConfigV3
# THIS SCRIPT IS AN EXAMPLE OF MAKING A CALL TO ONE VERIZON CMS ACCOUNT
# BOTH PUBLIC AND NON-PUBLIC URL'S ARE CREATED AS THE OUTPUT
# WITH EACH SAID CHANNEL, CONTAINING SLIGHTLY DIFFERENT QUERY STRING PARAMETERS
#Define the dictionary by VDMS CMS channel name and the channel GUID. These are the two inputs required to generate base url

publicDict = {}
fileName = "exampleOutput.csv"
with open(fileName, 'wb') as csvfile:
    fieldnames = ['Channel', 'Url', 'Account']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for a in tagConfigV3.AccountDict:
        #//////  PUBLIC DICTIONARY:
        for pd in a["publicDictionary"]:
            queryStrPublic = urllib.urlencode(dict(pd["params"]))
            owner = a["owner"]

            # VDMS will sign our playback request, appending the VDMS specific params to the signature. 
            sig = hmac.new(owner, queryStrPublic, hashlib.sha256).hexdigest()
            queryStrPublicSig = queryStrPublic + '&sig=' + sig
            # Find the channel ID for the public channels
            cidPublic =  pd["cid"]
            # # The token would then be added to a playback URL, e.g.

            publicUrl = 'https://content.uplynk.com/channel/' + cidPublic + '.m3u8'
            publicUrl = publicUrl + '?'  + queryStrPublicSig
            writer.writerow({"Channel":  pd["channel"], "Url": publicUrl, "Account": a['account'] })

            print("New output. If this works, take out the redundant 'key', 'cid'")

        #//////  NON PUBLIC DICTIONARY:
        for npd in a["nonPublicDictionary"]:
            queryStrNonPublic = urllib.urlencode(dict(npd["params"]))
            sigNonPublic = hmac.new(owner, queryStrNonPublic, hashlib.sha256).hexdigest()
            queryStrSigNonPublic = queryStrNonPublic + '&sig=' + sigNonPublic

            cidNonPublic =  npd["cid"]

            # # The token would then be added to a playback URL, e.g.
            urlNonPublic = 'https://content.uplynk.com/channel/' + cidNonPublic + '.m3u8'
            urlNonPublic = urlNonPublic + '?'  + queryStrSigNonPublic

            writer.writerow({"Channel":  npd["channel"], "Url": urlNonPublic, "Account": a['account'] })


# print ("Here we have the dict", [publicDict])


# f = open('exampleOutput.csv','wb')
# w = csv.DictWriter(f,tagConfig.AccountDict[1].keys())
# ("Printing out the keys for index 1 dict..." + " ")
# w.writerow(tagConfig.AccountDict[1].values())
# f.close()


# csv_columns = ['Public Channel Name', 'Public URL', 'account', 'Non Public Channel Name']
# csv_file = "exampleOutput.csv"

# with open('exampleOutput.csv', 'wb') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames =csv_columns)
#     writer.writeheader()
#     # writer.writerows([tagConfig.AccountDict[1]])