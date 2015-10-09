# WebMusicDownloader
I was inspired by http://iyask.me/Instant-Music-Downloader/ and created this web service.

It requires the following python modules:
- Flask
- BeautifulSoup
- Youtube-DL

Given that it was created in the space of 30 minutes there might be some bugs, my apologies in advance.

Each user is given an integer value as an ID which is stored as a cookie. Files are downloaded on the server side into directories with these values.
In a future release I will list previously downloaded files to allow users to grab them again without the delay of polliing youtube.
Another consideration for a future release is archival of old files.

If you need help getting up and running, feel free to give me a shout.

Cheers
