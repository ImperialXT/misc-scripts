# misc-scripts
A collection of random scripts I've written that are probably of use to no one but me

## critrole.py
I watch Critical Role but since timezones are not in my favour and I don't really like twitch overall and much prefer to watch them on my local machine via plex or similar. I wrote a script to automatically download episodes after they air and give them semi useful names. Script is run via cron. Needs cookies.txt due to a bug in youtube-dl with auth and twitch getting redirects, haven't tested in a month or so to see if it's still an issue.

## critrole-yt.py
Similar to the above script but does youtube via their channel instead as the filesizes are a lot nicer 2gb vs 12gb. This does mean you have to wait until Tuesday for the episode but in my situation I'm still way behind so it doesn't effect me in that regard. Could probably put size restrictions in place with twitch somehow..
