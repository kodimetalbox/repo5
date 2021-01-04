import plugintools
from logos import logos_bands

OFFICIAL_VIDEOS = "plugin://plugin.video.youtube/playlist/PLBCkm4VYo_DgzDg5O2-8UxgzZ6iVC_iza/"
LIVE = "plugin://plugin.video.youtube/playlist/PLBCkm4VYo_Dhy8W6G55jyzMOwDX1HwRMh/"
LIVESHOWS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGsGUAwjHr2Wj2kuhAby8mSS/"
def amorphis1(params):
    logo=logos_bands.amorphis(params)

    plugintools.add_item( 
        title="Official Videos",
        url=OFFICIAL_VIDEOS,
        thumbnail=logo, folder=True )  
        
    plugintools.add_item( 
        title="Live Shows 1",
        url=LIVE,
        thumbnail=logo, folder=True )  

    plugintools.add_item( 
        title="Live Shows 2",
        url=LIVESHOWS,
        thumbnail=logo, folder=True )  
