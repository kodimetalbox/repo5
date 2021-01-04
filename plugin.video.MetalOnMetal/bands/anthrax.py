import plugintools
from logos import logos_bands

ANNIVERSARY = "plugin://plugin.video.youtube/playlist/PLFdcG9gTDhXxde_Dm4iG4djHA7BAcl9qJ/" 
LIVE_SHOWS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGvoKFw5_qfcvr_Omoxix1cY/" 
VIDEOS = "plugin://plugin.video.youtube/playlist/PLFdcG9gTDhXy3V5W9XojnCO340WJEouaV/"
VIDEOS2 = "plugin://plugin.video.youtube/playlist/PLamrICcWG5Qfj9ykKcMAVIrYXiwhv5X1H/"

def anthrax1(params):
    logo=logos_bands.anthrax(params)

    plugintools.add_item( 
        title="Live Shows",
        url=LIVE_SHOWS,
        thumbnail=logo, folder=True )
		
    plugintools.add_item( 
        title="Official Music Videos",
        url=VIDEOS,
        thumbnail=logo, folder=True )

    plugintools.add_item( 
        title="XXXV Anniversary",
        url=ANNIVERSARY,
        thumbnail=logo, folder=True )
               
    plugintools.add_item( 
        title="Music Videos 1984-2017",
        url=VIDEOS2,
        thumbnail=logo, folder=True )

