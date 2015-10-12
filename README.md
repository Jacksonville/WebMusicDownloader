# WebMusicDownloader
I was inspired by [Instant Music Downloader] (http://iyask.me/Instant-Music-Downloader/) and created this web service.
View a demo [here] (http://music.jagnet.biz)

It requires the following python modules:
- [Flask] (http://flask.pocoo.org/)
- [BeautifulSoup] (http://www.crummy.com/software/BeautifulSoup/)
- [Youtube-DL] (https://rg3.github.io/youtube-dl/)

I made use of the following incredible resources on the web side of things:
- [Noty] (http://ned.im/noty/)
- [Bootstrap] (http://getbootstrap.com/)
- [Jquery] (https://jquery.com/)

Given that it was created in the space of 30 minutes there might be some bugs, my apologies in advance.

Each user is given an integer value as an ID which is stored as a cookie. Files are downloaded on the server side into directories with these values.
Previously downloaded files are available to quickly download without having to poll youtube.
Files are not currently archived/removed so disk space could be consumed in a busy environment.

If you need help getting up and running, feel free to give me a shout.

Cheers
