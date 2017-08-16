#!/usr/bin/python

import os
#$import wx.dataview
import wx

class CToolbar(wx.Frame):

    def __init__(self,*args,**kwds):
        super(CToolbar,self).__init__(None)



"""
check this
"""
class CDataViewListCtrl( wx.ListCtrl ):
    
    def __init__( self, *args,**kwds):
        super (CDataViewListCtrl,self).__init__(*args,**kwds)
       
        mycolumns=["A","B","C","D","E"]
        mywidth=[50,250,300,200,200]
        heading = list(mycolumns)
        print (len(mycolumns))
        l = [self.InsertColumn(i,heading=(str(heading[i])),width=mywidth[i]) for i in range(len(mycolumns))]

class CStaticBitmap(wx.StaticBitmap,wx.Bitmap):
    """
    kode file Tempat naruh gambar icons
    """
    def __init__(self,*args,**kwds):
        super(CStaticBitmap,self).__init__(*args,**kwds)        
        self.Bitmap=wx.Bitmap(os.path.realpath("PosPy/frame/icons/store.png"),wx.BITMAP_TYPE_ANY)
      
        """disini sudah bisa """
        return None
    
    def __repr__(self):
        return "this is my functions"


