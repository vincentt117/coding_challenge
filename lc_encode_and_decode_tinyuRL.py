# 535. Encode and Decode TinyURL

# https://leetcode.com/problems/encode-and-decode-tinyurl/description/

# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

import hashlib

urlDict = {}

class Codec:
   

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # Use built in SHA encryption to create TinyURL extension that will also act as key to the value of the original URL
        urlDict[hashlib.sha1(longUrl).digest()] = longUrl
        return "http://tinyurl.com/" + hashlib.sha1(longUrl).digest()
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # Assumes the URL has been encoded previously, use the TinyURL extension as key to retrieve from the dictionary
        return urlDict[shortUrl[19:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))




# OPTIMAL: Faster than 100% of soln