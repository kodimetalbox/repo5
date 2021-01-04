import plugintools
from logos import logos_bands

LIVE_SHOWS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGsqskC5RY0qt8Pk0xclK14f/"
OFFICIAL_VIDEOS = "plugin://plugin.video.youtube/playlist/PLF84630BDCCB15277/"
BEST_OF = "plugin://plugin.video.youtube/playlist/PLe7ia_jeVGd_vsqcTDyeeOHawvqoBFGbK/"

def accept1(params):
    logo=logos_bands.accept(params)

    plugintools.add_item( 
        title="Live Shows",
        url=LIVE_SHOWS,
        thumbnail=logo,folder=True )
        
    plugintools.add_item( 
        title="Official Videos",
        url=OFFICIAL_VIDEOS,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Official Best of",
        url=BEST_OF,
        thumbnail=logo, folder=True )


