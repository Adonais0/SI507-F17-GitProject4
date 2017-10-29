import sample_oauth1_code

collected_tumblr = [] # where I'll collect all the tweet data I get as I page through my results, 5 at a time
ids = []
max_id = None
my_params = {'count' : 5} # query parameters for 1st request

for i in range(5):
    if len(ids) > 0: # if we have already started the paging process
        my_params['max_id'] = min(ids) - 1
        # Twitter suggests that you take the minimum of the ids you got before, then subtract one from it, to make sure you get only ones you haven't received before. We can use the built-in min function here (could also accumulate by hand).
    # Regardless, now we need to make a request to the logged in user's timeline with the query parameters
    r = oauth.get("https://api.twitter.com/1.1/statuses/user_timeline.json",params = my_params)  # passes {'count': 5, 'max_id': whatever} ...
    # Now, append this data to a list so we can collect all the paged results
    collected_tumblr.append(r.json())
    next_five_ids = [tumblr['id'] for tumblr in r.json()]  # get the ids from the tweets we just got
    ids = ids + next_five_ids # add them to the list, and start the for loop process over again

print(ids)
print(type(ids))
# print(json.dumps(collected_tweets,indent=2))


# a super simple version of "caching"
# save the data we got back and collected in a file to check it out
fr = open("paging_nested.txt","w")
fr.write(json.dumps(collected_tumblr))
fr.close()