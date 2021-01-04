import plugintools
from logos import logos_bands


CLIPS = "plugin://plugin.video.youtube/playlist/PL00jwbCsmYLdt8lK7rqUUZn7hzd-Pa8fD/" 
CLIPS2 = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGv0A2lJoGqs7B8rvwKSxIXG/" 
LIVE = "plugin://plugin.video.youtube/playlist/PLGuhlLazJwGtklxRQWZaPJPgQVCEfmKrl/"

def somascure1(params):
    logo=logos_bands.somascure(params)

    plugintools.add_item( 
        title="Videos Oficiales",
        url=CLIPS,
        thumbnail=logo, folder=True )
		
    plugintools.add_item( 
        title="Videos",
        url=CLIPS2,
        thumbnail=logo, folder=True )
               
    plugintools.add_item( 
        title="Live",
        url=LIVE,
        thumbnail=logo, folder=True )

