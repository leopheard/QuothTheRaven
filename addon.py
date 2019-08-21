from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

#URL0 = "https://thefinancialreality.podomatic.com/rss2.xml"
URL1 = "https://feed.podbean.com/quoththeraven/feed.xml"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/image-logo/1811786/QTRLogo.jpg"},

        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/image-logo/1811786/QTRLogo.jpg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL1)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = mainaddon.get_soup(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items


if __name__ == '__main__':
    plugin.run()
