# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon


class TestWindow(xbmcgui.WindowXMLDialog):
    def __init__(self,*args,**kwargs):
        xbmcgui.WindowXMLDialog.__init__(self,*args,**kwargs)
        self.done = False

    def onInit(self):
        pass

    def onAction(self,action):
        if action == xbmcgui.ACTION_PREVIOUS_MENU or action == xbmcgui.ACTION_NAV_BACK:
            xbmc.log('CLOSE ATTEMPT')
            self.done = True
        xbmcgui.WindowXMLDialog.onAction(self,action)

    def onClick(self,controlID):
        if controlID == 300:
            xbmc.Player().play('plugin://plugin.video.youtube/play/?video_id=TAW1B9YNz5s')

w = TestWindow('script-ruuk-testing.xml',xbmcaddon.Addon().getAddonInfo('path'),'default')
w.show()
while not w.done and not xbmc.abortRequested:
    xbmc.sleep(100)

#You won't get this with latest master after you play the video, because you can't access the dialog window anymore
xbmc.log('TEST DONE')