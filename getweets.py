import csv
import twitter
api = twitter.Api(
    consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='')

hashtags_to_track = [
    "@jimmyjairala",
    "@cedeno_marth",
    "@jorgevillacrese",
    "@CynthiaViteri6",
    "@GinoCornejoM",
    "@BermudezBronson",
    "@balerioestacio",
    "@cgcassanello",
    "@inca_jose",
    "@EduardoArgudoG",
    "@fcojimenez21",
    "@patobuendia23",
    "@jaimelomas74",
    "@Simon_BolivarEC",
    "@edgarsalazar_51",
    "@jaimenebotsaadi"
]

stream = api.GetStreamFilter(track=hashtags_to_track)

with open('tweets.csv', 'a+') as csv_file:
    csv_writer = csv.writer(csv_file)
    for line in stream:
        # Signal that the line represents a tweet
        tweet = twitter.Status.NewFromJsonDict(line)
        print(tweet.id)
        jimmyjairala = cedeno_marth = jorgevillacrese = CynthiaViteri6 = GinoCornejoM = BermudezBronson = balerioestacio = inca_jose = EduardoArgudoG = fcojimenez21 = patobuendia23 = jaimelomas74 = Simon_BolivarEC = edgarsalazar_51 = jaimenebotsaadi = False
        for user in tweet.user_mentions:
            if user.screen_name.lower() == 'jimmyjairala':
                jimmyjairala = True
            if user.screen_name.lower() == 'cedeno_marth':
                cedeno_marth = True
            if user.screen_name.lower() == 'jorgevillacrese':
                jorgevillacrese = True
            if user.screen_name.lower() == 'cynthiaviteri6':
                CynthiaViteri6 = True
            if user.screen_name.lower() == 'ginocornejom':
                GinoCornejoM = True
            if user.screen_name.lower() == 'bermudezbronson':
                BermudezBronson = True
            if user.screen_name.lower() == 'balerioestacio':
                balerioestacio = True
            if user.screen_name.lower() == 'inca_jose':
                inca_jose = True
            if user.screen_name.lower() == 'eduardoargudog':
                EduardoArgudoG = True
            if user.screen_name.lower() == 'fcojimenez21':
                fcojimenez21 = True
            if user.screen_name.lower() == 'patobuendia23':
                patobuendia23 = True
            if user.screen_name.lower() == 'jaimelomas74':
                jaimelomas74 = True
            if user.screen_name.lower() == 'simon_bolivarec':
                Simon_BolivarEC = True
            if user.screen_name.lower() == 'edgarsalazar_51':
                edgarsalazar_51 = True
            if user.screen_name.lower() == 'jaimenebotsaadi':
                jaimenebotsaadi = True
            
        if(tweet.hashtags):
            hashtags = ' '.join(list(map(lambda x: x.text, tweet.hashtags)))
        else:
            hashtags = ''
        if(tweet.truncated):
            text = tweet.full_text
        else:
            text = tweet.text
        if(tweet.in_reply_to_status_id):
            replay = True
        else:
            replay = False
        row = [tweet.id,  tweet.created_at, tweet.user.screen_name, tweet.user.name, 
                tweet.user.created_at, tweet.user.followers_count, tweet.user.friends_count, tweet.user.statuses_count,
                tweet.user.geo_enabled, tweet.user.lang,
                tweet.source, tweet.lang, 
                text, hashtags, replay,
                jimmyjairala, cedeno_marth, jorgevillacrese, CynthiaViteri6, GinoCornejoM, BermudezBronson, balerioestacio, inca_jose, EduardoArgudoG, fcojimenez21, patobuendia23, jaimelomas74, Simon_BolivarEC, edgarsalazar_51, jaimenebotsaadi
                 ]
        csv_writer.writerow(row)
    
