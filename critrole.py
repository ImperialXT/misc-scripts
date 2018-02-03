import feedparser
import youtube_dl

feedUrl = 'https://twitchrss.appspot.com/vod/geekandsundry'

d = feedparser.parse(feedUrl)

class MyLogger(object):
      def debug(self, msg):
            pass

      def warning(self, msg):
            pass

      def error(self, msg):
            print(msg)

def my_hook(h):
      if h['status'] == 'finished':
            print('Done downloading: ' + h['filename'])
            print('Final Size: ' + h['downloaded_bytes'])

for post in d.entries:
      if "REBROADCAST" not in post.title and "Critical Role: Campaign 2" in post.title:
            ydl_opts = {
                        'cookiefile': '/data/cookies.txt',
                        'outtmpl': '/data/critical role/campaign 2/'+ post.title.replace(' #GNSLive', '').replace(':', ' -') + '.%(ext)s',
                        'progress_hooks': [my_hook],
                        'logger': MyLogger(),
                        'download_archive': '/home/download/.imperialxt/youtube_dl_download_archive',
                        }
            print('Downloading: ' + post.title + " - " + post.link)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                  ydl.download([post.link])
