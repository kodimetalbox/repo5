import plugintools
from logos import logos_bands


CLIPS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGtfaMiug0lcFz28MhyuDshs/" 
ALBUMS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGswwL18c3AEXPMIFHL7oBUS/" 
LIVE = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGsgWZndUVrJXTLoLfwZIvar/"

def the_wizards1(params):
    logo=logos_bands.the_wizards(params)

    plugintools.add_item( 
        title="Clips",
        url=CLIPS,
        thumbnail=logo, folder=True )
		
    plugintools.add_item( 
        title="Albums",
        url=ALBUMS,
        thumbnail=logo, folder=True )
               
    plugintools.add_item( 
        title="Live",
        url=LIVE,
        thumbnail=logo, folder=True )

