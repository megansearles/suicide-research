import pytumblr

ckey = '6bJgpX76yFg92HCkDfpAjphOud85kJDnwnev4mo15JNjXqHIFR'
csecret = 'W4oaRTAkWxQp9WEbneuVjtZuHtAdNc4OcVWNAmtShjdDU1eYFA'
oatoken = 'tD4CUX22oNchSQtuZgfnhSZ8glIVW8SbW3d54RAsw37MW5wYw5'
oasecret = 'zfoUIfM8mcX9rFxQeKKO8lcXCANxIA5ub4FqoKsjULEjfnG6Jx'

client = pytumblr.TumblrRestClient(
    ckey,
    csecret,
    oatoken,
    oasecret
)

print client.followers('thetinywordnerd') # This is one of my friends on tumblr and in real life, so I used her as a test.

# Note: Tumblr is not a good source for us, so I am going to abandon this.