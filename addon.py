from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

URL1 = "https://clearingthefogradioshow.libsyn.com/rss"
URL2 = "https://archive.wpfwfm.org/getrss.php?id=voiceswdiocoop"
URL3 = "http://commoncensored.libsyn.com/rss"
URL4 = "https://blackagendaradio.podbean.com/feed.xml"
URL5 = "https://moderaterebels.libsyn.com/rss"
URL6 = "https://actout.libsyn.com/rss"
URL7 = "http://drugpositive.org/rss"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/6/2/3/e/623e3618da36f78a/FOG_Radio_logo_final_392x283.jpg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('all_episodes2'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/voices-vision2.jpg"},
 {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('all_episodes3'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/9/7/a/9/97a99a0a0f9947c5/common-FINAL.jpg"},
 {
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('all_episodes4'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/black-agenda2.jpg"},
 {
            'label': plugin.get_string(30005), 
            'path': plugin.url_for('all_episodes5'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/09/screen-shot-2018-09-25-at-1.34.39-pm.png"},
 {
            'label': plugin.get_string(30006), 
            'path': plugin.url_for('all_episodes6'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/act-out.jpg"},
 {
            'label': plugin.get_string(30007), 
            'path': plugin.url_for('all_episodes7'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/09/drugpostive_podcast_logo_sm.jpg"},
    ]

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup1 = mainaddon.get_soup1(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/all_episodes2/')
def all_episodes2():
    """
    contains playable podcasts listed as just-in
    """
    soup2 = mainaddon.get_soup2(URL2)
    
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    
    items = mainaddon.compile_playable_podcast2(playable_podcast2)

    return items

@plugin.route('/all_episodes3/')
def all_episodes3():
    """
    contains playable podcasts listed as just-in
    """
    soup3 = mainaddon.get_soup3(URL3)
    
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast3)

    return items

@plugin.route('/all_episodes4/')
def all_episodes4():
    """
    contains playable podcasts listed as just-in
    """
    soup4 = mainaddon.get_soup4(URL4)
    
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    
    items = mainaddon.compile_playable_podcast4(playable_podcast4)

    return items

@plugin.route('/all_episodes5/')
def all_episodes5():
    """
    contains playable podcasts listed as just-in
    """
    soup5 = mainaddon.get_soup5(URL5)
    
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast5)

    return items

@plugin.route('/all_episodes6/')
def all_episodes6():
    """
    contains playable podcasts listed as just-in
    """
    soup6 = mainaddon.get_soup6(URL6)
    
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast6)

    return items

@plugin.route('/all_episodes7/')
def all_episodes7():
    """
    contains playable podcasts listed as just-in
    """
    soup7 = mainaddon.get_soup7(URL7)
    
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    
    items = mainaddon.compile_playable_podcast7(playable_podcast7)

    return items

if __name__ == '__main__':
    plugin.run()
