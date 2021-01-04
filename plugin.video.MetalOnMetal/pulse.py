# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google Search For This Template
# Modified: Pulse
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon
from logos import logos_guitar

addonID = 'plugin.video.MetalOnMetal'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)

xbmc.executebuiltin('Container.SetViewMode(500)')




YOUTUBE_CHANNEL_30_YEARS_OF_NUCLEAR_BLAST = "PLB4brr7vf-P4Sw27U1AsJvIevX5D7TQeW"

### BANDS
def f_accept(params):
    from bands import accept
    accept.accept1(params)

def f_acdc(params):   
    from bands import acdc
    acdc.acdc1(params)          

def f_amorphis(params):
    from bands import amorphis
    amorphis.amorphis1(params)          

def f_angelus(params):
    from bands import angelusapatrida
    angelusapatrida.angelusapatrida1(params)          
            
def f_anthrax(params):
    from bands import anthrax
    anthrax.anthrax1(params)      

def f_somascure(params):
    from bands import somascure
    somascure.somascure1(params) 
     
def f_terravore(params):
    from bands import terravore
    terravore.terravore1(params)           
     
def f_the_wizards(params):
    from bands import the_wizards
    the_wizards.the_wizards1(params) 
    
### FESTIVALS
def f_wacken(params):
    from festivals import wacken
    wacken.wacken1(params) 

def f_hellfest(params):
    from festivals import hellfest
    hellfest.hellfest1(params) 

def f_resurrection(params):
    from festivals import resurrection
    resurrection.resurrection1(params) 

   
### Record Labels   
def f_century(params):
    from record_labels import century
    century.century1(params) 
    
### Specials Playlists   
def f_best(params):
    from special_playlists import best
    best.best1(params) 

def f_spanish(params):
    from special_playlists import spanish
    spanish.spanish1(params) 
    
### YouTubeChannels  
def f_shauntrack(params):
    from youtube_channels import shauntrack
    shauntrack.shauntrack1(params)
    
def f_amusia(params):
    from youtube_channels import amusia
    amusia.amusia1(params)


### Documentaries

### Genres
def f_power(params):
    from genres import power
    power.power1(params)
    
def f_thrash(params):
    from genres import thrash
    thrash.thrash1(params)
    
### Full Albums
def f_album_power(params):
    from full_albums import power
    power.power1(params)
    
def f_album_thrash(params):
    from full_albums import thrash
    thrash.thrash1(params)    

 ###########################################################
 ################ BANDS ####################################
 ###########################################################
          
def bands(params):
    from logos import logos_bands
    ACCEPT=logos_bands.accept(params)
    ACDC=logos_bands.acdc(params)
    AMORPHIS=logos_bands.amorphis(params)
    ANGELUS=logos_bands.angelusapatrida(params)
    ANTHRAX=logos_bands.anthrax(params)
    SOMASCURE=logos_bands.somascure(params)
    THE_WIZARDS=logos_bands.the_wizards(params)
    TERRAVORE=logos_bands.terravore(params)
    plugintools.add_item(action="f_accept",title="Accept", thumbnail=ACCEPT, folder=True )  
    plugintools.add_item(action="f_acdc", title="AC/DC", thumbnail=ACDC, folder=True )  
    plugintools.add_item(action="f_amorphis", title="Amorphis", thumbnail=AMORPHIS, folder=True )  
    plugintools.add_item(action="f_angelus", title="Angelus Apatrida", thumbnail=ANGELUS, folder=True )  
    plugintools.add_item(action="f_anthrax", title="Anthrax", thumbnail=ANTHRAX, folder=True )       
    plugintools.add_item(action="f_somascure", title="Somas Cure", thumbnail=SOMASCURE, folder=True )
    plugintools.add_item(action="f_terravore", title="Terravore", thumbnail=TERRAVORE, folder=True ) 
    plugintools.add_item(action="f_the_wizards", title="The Wizards", thumbnail=THE_WIZARDS, folder=True ) 
       
 ###########################################################
 ################ FESTIVALS ################################
 ###########################################################
 
def festivals(params):
    from logos import logos_festivals
    WACKEN=logos_festivals.wacken(params)
    HELLFEST=logos_festivals.hellfest(params)
    RESURRECTION=logos_festivals.resurrection(params)
    plugintools.add_item(action="f_wacken",title="Wacken", thumbnail=WACKEN, folder=True )  
    plugintools.add_item(action="f_hellfest",title="Hellfest", thumbnail=HELLFEST, folder=True )  
    plugintools.add_item(action="f_resurrection",title="Resurrection Fest", thumbnail=RESURRECTION, folder=True )  


 ###########################################################
 ################ RECORD LABELS ############################
 ###########################################################

def recordlabels(params):
    from logos import logos_labels
    CENTURY=logos_labels.century(params)
    plugintools.add_item(action="f_century",title="Century Media Records", thumbnail=CENTURY, folder=True )  

 ###########################################################
 ################ SPECIAL PLAYLISTS ########################
 ###########################################################
 
def specialplaylists(params):
    logo=logos_guitar.logo_04(params)
    plugintools.add_item(action="f_best",title="Best Metal Playlists", thumbnail=logo, folder=True )
    plugintools.add_item(action="f_spanish",title="Spanish Metal Playlists", thumbnail=logo, folder=True )  
      
 ###########################################################
 ################ YOUTUBE CHANNELS #########################
 ###########################################################
 
def youtubechannels(params):
    from logos import logos_youtube_channels
    SHAUNTRACK=logos_youtube_channels.shauntrack(params)
    plugintools.add_item(action="f_shauntrack",title="Shaun Track", thumbnail=SHAUNTRACK, folder=True )  
    AMUSIA=logos_youtube_channels.amusia(params)
    plugintools.add_item(action="f_amusia",title="El canal de Amusia", thumbnail=AMUSIA, folder=True )  
      
 ###########################################################
 ################ DOCUMENTARIES ############################
 ###########################################################
 
def documentaries(params):
    from logos import logos_documentaries
    GIBSONTV=logos_documentaries.gibsontv(params)
    ICONS  = "plugin://plugin.video.youtube/playlist/PL7qLGYJiRJ1hr5qFhq3xFlyNNO1iQPjQU/"
    plugintools.add_item( 
        title="Icons - Gibson TV",
        url=ICONS,
        thumbnail=GIBSONTV, folder=True )  

 ###########################################################
 ################ METAL GENRES #############################
 ###########################################################
 
def genres(params):
    logo=logos_guitar.logo_07(params)
    plugintools.add_item(action="f_power",title="Power", thumbnail=logo, folder=True )  
    plugintools.add_item(action="f_thrash",title="Thrash", thumbnail=logo, folder=True )       
 

 ###########################################################
 ################ FULL ALBUMS ##############################
 ###########################################################
 
def full_albums(params):
    logo=logos_guitar.logo_08(params)
    plugintools.add_item(action="f_album_power",title="Power", thumbnail=logo, folder=True )  
    plugintools.add_item(action="f_album_thrash",title="Thrash", thumbnail=logo, folder=True ) 
          
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()
    
    
    
####### Añadir:  documentales 
# Main menu
def main_list(params):
    #from logos import logos_guitar
    logo_01=logos_guitar.logo_01(params)
    logo_02=logos_guitar.logo_02(params)
    logo_03=logos_guitar.logo_03(params)
    logo_04=logos_guitar.logo_04(params)
    logo_05=logos_guitar.logo_05(params)
    logo_06=logos_guitar.logo_06(params)
    logo_07=logos_guitar.logo_07(params)
    logo_08=logos_guitar.logo_08(params)
    logo_09=logos_guitar.logo_09(params)
    logo_10=logos_guitar.logo_10(params)
    logo_11=logos_guitar.logo_11(params)
    logo_12=logos_guitar.logo_12(params)
    logo_13=logos_guitar.logo_13(params)
    
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        action="bands", 
        title="Bands",
        thumbnail=logo_01,
        folder=True )  
          
    plugintools.add_item( 
        action="festivals", 
        title="Festivals",
        thumbnail=logo_02,
        folder=True ) 


    plugintools.add_item( 
        action="recordlabels", 
        title="Record Labels",
        thumbnail=logo_03,
        folder=True ) 

    plugintools.add_item( 
        action="specialplaylists", 
        #action="recordlabels",
        title="Special Playlists",
        thumbnail=logo_04,
        folder=True ) 
        
    plugintools.add_item( 
        action="youtubechannels", 
        title="YouTube Channels",
        thumbnail=logo_05,
        folder=True )
        

    plugintools.add_item( 
        action="documentaries", 
        title="Documentaries",
        thumbnail=logo_06,
        folder=True )
        
    plugintools.add_item( 
        action="genres", 
        title="Videos by Metal Genres",
        thumbnail=logo_07,
        folder=True )
        
        
    plugintools.add_item( 
        action="full_albums", 
        title="Full Albums",
        thumbnail=logo_08,
        folder=True )
run()
