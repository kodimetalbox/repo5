import plugintools
from logos import logos_bands

OFFICIAL = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGvMA3l5yxO__qZVbkQLBqIM/" 
LIVE_SHOWS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGvLvSsyKdjl2PUqVNrThLEQ/" 
NONOFFICIAL = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGv0-FLOu957BUNlPRk4HjPX/" 

def angelusapatrida1(params):
    logo=logos_bands.angelusapatrida(params)
    
    plugintools.add_item( 
        title="Official Videos",
        url=OFFICIAL,
        thumbnail=logo, folder=True )
               
    plugintools.add_item( 
        title="Live Shows",
        url=LIVE_SHOWS,
        thumbnail=logo, folder=True )
		

    plugintools.add_item( 
        title="No Official Videos",
        url=NONOFFICIAL,
        thumbnail=logo, folder=True )

