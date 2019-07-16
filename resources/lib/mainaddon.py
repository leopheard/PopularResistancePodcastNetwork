import requests
import re
from bs4 import BeautifulSoup

URL1 = "https://clearingthefogradioshow.libsyn.com/rss"
URL2 = "https://archive.wpfwfm.org/getrss.php?id=voiceswdiocoop"
URL3 = "http://commoncensored.libsyn.com/rss"
URL4 = "https://blackagendaradio.podbean.com/feed.xml"
URL5 = "https://moderaterebels.libsyn.com/rss"
URL6 = "https://actout.libsyn.com/page/1/size/1600"
URL7 = "http://drugpositive.org/rss"

def get_soup1(url1):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup1)
    return soup1

get_soup1("https://clearingthefogradioshow.libsyn.com/rss")

def get_soup2(url2):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup2)
    return soup2

get_soup2("https://archive.wpfwfm.org/getrss.php?id=voiceswdiocoop")

def get_soup3(url3):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup3)
    return soup3

get_soup3("http://commoncensored.libsyn.com/rss")

def get_soup4(url4):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup4)
    return soup4

get_soup4("https://blackagendaradio.podbean.com/feed.xml")

def get_soup5(url5):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url5)
    soup5 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup5)
    return soup5

get_soup5("https://moderaterebels.libsyn.com/rss")

def get_soup6(url6):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url6)
    soup6 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup6)
    return soup6

get_soup6("https://actout.libsyn.com/page/1/size/1600")

def get_soup7(url7):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url7)
    soup7 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup7)
    return soup7

get_soup7("http://drugpositive.org/rss")



def get_playable_podcast1(soup1):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup1.find_all('item'):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
                'desc': desc,
                'thumbnail': thumbnail,
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items

def get_playable_podcast2(soup2):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup2.find_all('item'):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "http://confessor.wpfwfm.org/pix/voiceswithvision_it_94.jpg",
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast2(playable_podcast2):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_playable_podcast3(soup3):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup3.find_all('item'):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail,
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast3(playable_podcast3):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items



def get_playable_podcast4(soup4):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup4.find_all('item'):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://pbcdn1.podbean.com/imglogo/image-logo/277790/BlackAgendaRadio_AlbumArt.jpg",
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast4(playable_podcast4):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast4:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_playable_podcast5(soup5):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup5.find_all('item'):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail,
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast5(playable_podcast5):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items



def get_playable_podcast6(soup6):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup6.find_all('body'):
        
        try:        
            link = content.find('li')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('div', {'class': 'libsyn-item-body'})
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://secureimg.stitcher.com/feedimagesplain328/164080.jpg",
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast6(playable_podcast6):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast6:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_playable_podcast7(soup7):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup7.find_all('item'):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail,
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast7(playable_podcast7):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast7:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items
