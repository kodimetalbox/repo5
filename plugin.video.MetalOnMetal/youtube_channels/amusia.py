# -*- coding: utf-8 -*-
#------------------------------------------------------------
import plugintools
from logos import logos_youtube_channels

_2020  = "plugin://plugin.video.youtube/playlist/PLe_OWxpTcSPRG84VNwKXB2Iq4PRX77l95/"
CLASICOS  = "plugin://plugin.video.youtube/playlist/PLgyUYejNPEs2pL_5qiAEe1V5hIw7rlUjy/"

def amusia1(params):
    logo=logos_youtube_channels.amusia(params)

    plugintools.add_item( 
        title="Vídeos 2020",
        url=_2020,
        thumbnail=logo, folder=True )  
       
    plugintools.add_item( 
        title="Comentarios álbumes clásicos",
        url=CLASICOS,
        thumbnail=logo, folder=True )
        

        

