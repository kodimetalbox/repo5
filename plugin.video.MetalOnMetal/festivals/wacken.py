import plugintools
from logos import logos_festivals

WACKEN_2020 = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGtgW7lbAJ-P_zitY3JJQScx/"
W3_SONGS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGtlB4ugCq9cNCLnAD2JSkix/"
ALL_LIVE_SHOWS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC3pLnvPFudbDoBEReM3xcRw/"
BEST_FULL_SHOWS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGuxXN0Wo9nRes7rYPtfRLqN/"
BLACK_METAL_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC0_wDTyJ_UWJKZOvBdN4fXt/"
DEATH_METAL_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC1vKSeAX1xa7vfe3l1BD3Ks/"
GRINDCORE_EXTREME_METAL_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC2KEypK4oYX9_pNuVMamUVI/"
HEAVY_ROCK_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC3ET6JyUgbW6R5Yp8BReNFd/"
MEDIAVAL_METAL_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC2iNfBOXBwUpy1XWnRSJuYv/"
MELODIC_DEATH_METAL_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC2-vQ9ORH8LHgkTa36odnBu/"
METAL_ICONS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC2aXVVsXN4xDbM2Nx-tZVcl/"
PAGAN_VIKING_METAL_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC09sP2au8177_PpZag8e0jt/"
ROCK_ICONS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC3_H1e978hugznB6S7ItZ8Q/"
SYMPHONIC_METAL_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC001OWeN4j4o-UmdK7SBiwP/"
THRASH_METAL_BANDS = "plugin://plugin.video.youtube/playlist/PLPfPNs01OQC1W-iGG0wy0Oo3W4ihaZZAi/"

def wacken1(params):
    logo=logos_festivals.wacken(params)
     
    plugintools.add_item( 
        #action="", 
        title="Wacken World Wide 2020",
        url=WACKEN_2020,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Wacken All Live Shows",
        url=ALL_LIVE_SHOWS,
        thumbnail=logo, folder=True ) 		

    plugintools.add_item( 
        #action="", 
        title="Wacken Best Full Shows",
        url=BEST_FULL_SHOWS,
        thumbnail=logo, folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Wacken - 3 Songs",
        url=W3_SONGS,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Wacken Rock Icons",
        url=ROCK_ICONS,
        thumbnail=logo, folder=True )         
 
    plugintools.add_item( 
        #action="", 
        title="Wacken Metal Icons",
        url=ROCK_ICONS,
        thumbnail=logo, folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Wacken Heavy Rock Bands",
        url=HEAVY_ROCK_BANDS,
        thumbnail=logo, folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Wacken Thrash Metal Bands",
        url=THRASH_METAL_BANDS,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Wacken Symphonic Metal Bands",
        url=SYMPHONIC_METAL_BANDS,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Wacken Death Metal Bands",
        url=DEATH_METAL_BANDS,
        thumbnail=logo, folder=True ) 		

    plugintools.add_item( 
        #action="", 
        title="Wacken Melodic Death Metal Bands",
        url=MELODIC_DEATH_METAL_BANDS,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Wacken Black Metal Bands",
        url=BLACK_METAL_BANDS,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Wacken Grindcore and Extreme Metal Bands",
        url=GRINDCORE_EXTREME_METAL_BANDS,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Wacken Pagan and Viking Metal Bands",
        url=PAGAN_VIKING_METAL_BANDS,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Wacken Mediaval Metal Bands",
        url=MEDIAVAL_METAL_BANDS,
        thumbnail=logo,
        folder=True )
