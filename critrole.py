import feedparser
import youtube_dl
import pprint
import re
import sys


class MyLogger(object):
      def debug(self, msg):
            pass

      def warning(self, msg):
            pass

      def error(self, msg):
            print(msg)

def parse_critrole_title(title):
      match = re.match(r".*Critical Role:? (Campaign (\d+):?),?,? Ep(isode)? ?(\d+).*", title, flags=re.I)

      campaign, episode = None, None

      if match:
            campaign = "1"
            if match.group(2):
                  campaign = match.group(2)
            episode = int(match.group(4))

      return (campaign, episode)

def format_critrole_title(campaign, episode):
    """format a critical role episode title into either a short or long
    format
    """
    campaign_str = ""
    ep_str = ""
    if campaign:
            campaign_str = "Campaign {}".format(campaign)
    if episode:
            ep_str = "Episode {}".format(episode)

    return " ".join([campaign_str, ep_str])

def my_hook(h):
      if h['status'] == 'finished':
            pprint.pprint(h)
            print('Done downloading: ' + h['filename'])
            print('Final Size: ' + str(h['total_bytes']))

def download(title, url):
            campaign, episode = parse_critrole_title(title)
            if campaign and episode:
                ep_title = format_critrole_title(campaign,episode)
                actual_title = "Critical Role " + ep_title

                ydl_opts = {
                            'cookiefile': '/data/cookies.txt',
                            'outtmpl': '/data/critical role/campaign 2/'+ actual_title + '.%(ext)s',
                            'progress_hooks': [my_hook],
                            'logger': MyLogger(),
                            'download_archive': '/home/download/.imperialxt/youtube_dl_download_archive',
                            }
                print('Downloading: ' + actual_title + " - " + url)
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                      ydl.download([url])
            else:
                print('Skipping: ' + title + " - " + url)
def main():
    feedUrl = 'https://twitchrss.appspot.com/vod/criticalrole'

    d = feedparser.parse(feedUrl)

    for post in d.entries:
          if "REBROADCAST" not in post.title:
            try:
                download(post.title, post.link)
            except Exception as e:
                print(e)
                download(post.title, post.link)
            except KeyboardInterrupt:
                sys.exit()

if __name__ == '__main__':
    main()
