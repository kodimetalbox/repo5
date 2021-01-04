import plugintools
from logos import logos_bands


LIVE70 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVQ_4kbSQ2qP7Kh-BfpWZEzE/"
LIVE80 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVSSPAtSnfc7FR9A9M3mJQHt/"
LIVE90 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVS5qi1DdTW1Mi3Yizqqn5gk/"
LIVE2000= "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVQfLBqmbxjsYJG3j_B3TkCp/"

VIDEOS70 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVT3EgqkKI8BCRFMcBfKihHt/"
VIDEOS80 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVQMR8ocCtX02ZMDEb13Q840/"
VIDEOS90 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVRXR1AdmqItdcX4dfqIQAxs/"
VIDEOS2000 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVQjZ5b4r_28Wb9EhrEYNH2U/"

MOST_REQUEST = "plugin://plugin.video.youtube/playlist/PL4FDF40C9C9FEF425/"
OFFICIAL_GREATEST_HITS = "plugin://plugin.video.youtube/playlist/PLQlc99hV-nkGWDaG-gJxwOfqp8jxyHaaQ/"
FAMILY_JEWELS = "plugin://plugin.video.youtube/playlist/PLkxUTH8fpHnf4SdpjqUsAUtDuv0DQGR-a/"

HIGHWAY_TO_HELL   = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVRQ9AOtjH3sgAlwRP80yWGe/"
BACK_IN_BLACK = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVQixI3AkXu862cZHi5XMev1/"

PARIS_79 = "plugin://plugin.video.youtube/playlist/PLKBTqDbSIw1PB3ZidZi_kma7XtxNhQf1L/"
DONINGTON_91 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVS00s8iX8zxaCyE54BN6h9W/"
NO_BULL_MADRID_96  = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVRon479P35zRg3Gw0mcMJFS/"
STIFF_UPPER_LIP_01 = "plugin://plugin.video.youtube/playlist/PLlbmqKJOeu-zu6Dp91NpOFbZXoNSDvM8y/"
CIRCUS_KRONE_03 = "plugin://plugin.video.youtube/playlist/PLibldNdnTlYTNXNI_s8awnuvcXDWvhGe_/"
RIVER_PLATE_09 = "plugin://plugin.video.youtube/playlist/PLx1MDbsLNfVTiAIYbfgqg_8mCPAjvBxeV/"

LIVE_SHOWS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGvlGz9LEsoAelTAswFts2gG/"


def acdc1(params):
    logo=logos_bands.acdc(params)
    
    plugintools.add_item( 
        title="Live Clips 70s",
        url=LIVE70,
        thumbnail=logo, folder=True )   
        
    plugintools.add_item( 
        title="Live Clips 80s",
        url=LIVE80,
        thumbnail=logo, folder=True )         
    
    plugintools.add_item( 
        title="Live Clips 90s",
        url=LIVE90,
        thumbnail=logo, folder=True )        

    plugintools.add_item( 
        title="Live Clips 2000s",
        url=LIVE2000,
        thumbnail=logo, folder=True )

    plugintools.add_item( 
        title="Videos 70s",
        url=VIDEOS70,
        thumbnail=logo, folder=True ) 
 
    plugintools.add_item( 
        title="Videos 80s",
        url=VIDEOS80,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        title="Videos 90s",
        url=VIDEOS90,
        thumbnail=logo, folder=True )  
 
    plugintools.add_item( 
        title="Videos 2000s",
        url=VIDEOS2000,
        thumbnail=logo, folder=True )  

    plugintools.add_item( 
        title="Most Request",
        url=MOST_REQUEST,
        thumbnail=logo, folder=True )    
   
    plugintools.add_item( 
        title="Official Greatest Hits",
        url=OFFICIAL_GREATEST_HITS,
        thumbnail=logo, folder=True )            
        
    plugintools.add_item( 
        title="Family Jewels",
        url=FAMILY_JEWELS,
        thumbnail=logo, folder=True )                          
        
    plugintools.add_item( 
        title="Highway to Hell",
        url=HIGHWAY_TO_HELL,
        thumbnail=logo, folder=True ) 
          
    plugintools.add_item( 
        title="Back in Black Videos",
        url=BACK_IN_BLACK,
        thumbnail=logo, folder=True )   
 
    plugintools.add_item( 
        title="Live Paris 79",
        url=PARIS_79,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        title="Live Donington 91",
        url=DONINGTON_91,
        thumbnail=logo, folder=True )   
        
    plugintools.add_item( 
        title="No Bull - Live Madrid 96",
        url=NO_BULL_MADRID_96,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        title="Stiff Upeer Lip - Live Munchen 01",
        url=STIFF_UPPER_LIP_01,
        thumbnail=logo, folder=True )  

    plugintools.add_item( 
        title="Live at the Circus Krone - Munchen 2003",
        url=CIRCUS_KRONE_03,
        thumbnail=logo, folder=True ) 
   
    plugintools.add_item( 
        title="Live River Plate 2009",
        url=RIVER_PLATE_09,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        title="Live Shows",
        url=LIVE_SHOWS,
        thumbnail=logo, folder=True ) 
