import plugintools
from logos import logos_festivals

FROM_HOME_2020 = "plugin://plugin.video.youtube/playlist/PLxYfFQmDVUbMRrtPDGNVmz61tIU1iOY_2/"
ARTE_CONCERT = "plugin://plugin.video.youtube/playlist/PL66OD4JjS_2PQTMDC3jP1iZJx30dG2Eia/"
BEST_FULL_SHOWS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGuo96p2C832lP5SQyZPQGAM/"

def hellfest1(params):
    logo=logos_festivals.hellfest(params)
     
    plugintools.add_item( 
        title="Hellfest from home - 2020",
        url=FROM_HOME_2020,
        thumbnail=logo, folder=True ) 
    plugintools.add_item( 
        title="Arte Concert",
        url=ARTE_CONCERT,
        thumbnail=logo, folder=True ) 
    plugintools.add_item( 
        title="Best Full Shows",
        url=BEST_FULL_SHOWS,
        thumbnail=logo, folder=True ) 


  
