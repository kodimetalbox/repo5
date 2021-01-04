import plugintools
from logos import logos_bands


CLIPS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGvySVZ9nPUdcnix9JRSx-Rg/" 
ALBUMS = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGv8pfvS28MLhReklB1soJKw/" 
LIVE = "plugin://plugin.video.youtube/playlist/PLxdXmWB9WeXbxydcjidCAdxC1k2gYe5He/"

def terravore1(params):
    logo=logos_bands.terravore(params)

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

