# -*- coding: utf-8 -*-
#------------------------------------------------------------
import plugintools
from logos import logos_guitar

T01 = "plugin://plugin.video.youtube/playlist/PLUG57rGVK9B4OvZ4j3jZXQVg5hefFs4gP/"
CLASSICS01 = "plugin://plugin.video.youtube/playlist/PLgumxYM-P68aDCOMaCUTv6JZdd38j8_nw/"
_89_90 = "plugin://plugin.video.youtube/playlist/PLpda3grlmV0e3zPWyfAeLPDwZcQ9zlZYy/"
SPANISH = "plugin://plugin.video.youtube/playlist/PLbU28iGAEY9incqc5Da1zD3BjRMsmmqyd/"
T02 = "plugin://plugin.video.youtube/playlist/PLbU28iGAEY9hC-cPCiYcdiUFE1dPWBZIY/"
CLASSICS02 = "plugin://plugin.video.youtube/playlist/PLD0zM63kR50epIEI3EOYN9ooLSrfSvnCH/"
BEST = "plugin://plugin.video.youtube/playlist/PLh5brHD9072bRSohadcGvZ45OZR3MkVvj/"

def thrash1(params):
    logo=logos_guitar.logo_07(params)

    plugintools.add_item( 
        title="Thrash Metal Full Albums (I)",
        url=T01,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Thrash Metal Full Albums (II)",
        url=T02,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Classic Thrash Metal Albums (I)",
        url=CLASSICS01,
        thumbnail=logo, folder=True )
        
        
    plugintools.add_item( 
        title="Classic Thrash Metal Albums (II)",
        url=CLASSICS02,
        thumbnail=logo, folder=True )
                
    plugintools.add_item( 
        title="80s/90s Thrash Albums ",
        url=_89_90,
        thumbnail=logo, folder=True )
                
    plugintools.add_item(
        title="Spanish Thrash Metal Full Albums ",
        url=SPANISH,
        thumbnail=logo, folder=True )
        
        
    plugintools.add_item( 
        title="Best Metal Albums Ever",
        url=BEST,
        thumbnail=logo, folder=True )
        

