# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  1 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FUtama
###########################################################################

class FUtama ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SOFTWARE", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 500,400 ) )
	#	self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
	#	self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.p_main = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
	#	self.p_main.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
	#	self.p_main.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.statictext = wx.StaticText( self.p_main, wx.ID_ANY, u"MODEL TAMPILAN APLIKASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext.Wrap( -1 )
		self.statictext.SetFont( wx.Font(24 , wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
	#	self.statictext.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
	#	self.statictext.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer3.Add( self.statictext, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer2 = wx.FlexGridSizer( 5, 0, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.AddGrowableRow( 0 )
		fgSizer2.AddGrowableRow( 1 )
		fgSizer2.AddGrowableRow( 2 )
		fgSizer2.AddGrowableRow( 3 )
		fgSizer2.AddGrowableRow( 4 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.btnsale = wx.Button( self.p_main, wx.ID_ANY, u"Penjualan", wx.DefaultPosition, wx.DefaultSize, 0 )
	#	self.btnsale.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
	#	self.btnsale.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		fgSizer2.Add( self.btnsale, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.btnset = wx.Button( self.p_main, wx.ID_ANY, u"Pengaturan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btnset, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnbuy = wx.Button( self.p_main, wx.ID_ANY, u"Pembelian", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btnbuy, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnreport = wx.Button( self.p_main, wx.ID_ANY, u"Laporan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btnreport, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnhelp = wx.Button( self.p_main, wx.ID_ANY, u"Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btnhelp, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer28.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		self.mainBitmap = wx.StaticBitmap( self.p_main, wx.ID_ANY, wx.Bitmap( u"/home/pmc/Projects/PointofSalePy/PosPy/frame/icons/store.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
	#	self.mainBitmap.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
	#	self.mainBitmap.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer28.Add( self.mainBitmap, 3, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		
		self.p_main.SetSizer( bSizer3 )
		self.p_main.Layout()
		bSizer3.Fit( self.p_main )
		bSizer1.Add( self.p_main, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0|wx.TAB_TRAVERSAL|wx.WANTS_CHARS )
		self.m_menu2 = wx.Menu()
		self.m_submenu = wx.Menu()

		self.menuitemsave=wx.MenuItem(self.m_menu2,wx.ID_ANY,u"Save",wx.EmptyString,wx.ITEM_NORMAL)
		self.menuitemexit=wx.MenuItem(self.m_menu2,wx.ID_ANY,u"Exit",wx.EmptyString,wx.ITEM_NORMAL)
	
		self.menuitemsavepdf = wx.MenuItem(self.m_menu2,wx.ID_ANY,u"Pdf",wx.EmptyString,wx.ITEM_NORMAL)
		self.m_submenu.Append(self.menuitemsavepdf)

		self.m_menu2.Append(self.menuitemsave)

		self.m_menu2.AppendSubMenu(self.m_submenu,"Save As ..")
		self.m_menu2.Bind(wx.EVT_MENU,self.Onclickexit,self.menuitemexit)
		self.m_menu2.AppendSeparator()
		self.m_menu2.Append(self.menuitemexit)
		self.m_menubar2.Append( self.m_menu2, u"&Berkas" ) 
		
		self.m_menu5 = wx.Menu()
		self.menuitemsale = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Penjualan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.menuitemsale )
		
		self.menuitembuy = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Pembelian", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.menuitembuy )
		
		self.m_menu5.AppendSeparator()
		
		self.menuitemreport = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"Laporan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.menuitemreport )
		
		self.m_menubar2.Append( self.m_menu5, u"&Tampilan" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Data", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItem2 )
		
		self.m_menubar2.Append( self.m_menu3, u"&Pengaturan" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_menubar2.Append( self.m_menu4, u"&Bantuan" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FUtamaOnClose )
		self.btnsale.Bind( wx.EVT_BUTTON, self.btnsaleOnButtonClick )
		self.btnset.Bind( wx.EVT_BUTTON, self.btnsetOnButtonClick )
		self.btnbuy.Bind( wx.EVT_BUTTON, self.btnbuyOnButtonClick )
		self.btnreport.Bind( wx.EVT_BUTTON, self.btnreportOnButtonClick )
		self.btnhelp.Bind( wx.EVT_BUTTON, self.btnhelpOnButtonClick )
		self.m_menubar2.Bind( wx.EVT_CHAR, self.m_menubar2OnChar )
		self.Bind( wx.EVT_MENU, self.menuitemsaleOnMenuSelection, id = self.menuitemsale.GetId() )
		self.Bind( wx.EVT_MENU, self.mitembuyOnMenuSelection, id = self.menuitembuy.GetId() )
		self.Bind( wx.EVT_MENU, self.menuitemreportOnMenuSelection, id = self.menuitemreport.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem2OnMenuSelection, id = self.m_menuItem2.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FUtamaOnClose( self, event ):
		event.Skip()
	
	def btnsaleOnButtonClick( self, event ):
		event.Skip()
	
	def btnsetOnButtonClick( self, event ):
		event.Skip()
	
	def btnbuyOnButtonClick( self, event ):
		event.Skip()
	
	def btnreportOnButtonClick( self, event ):
		event.Skip()
	
	def btnhelpOnButtonClick( self, event ):
		event.Skip()
	
	def m_menubar2OnChar( self, event ):
		event.Skip()
	
	def menuitemsaleOnMenuSelection( self, event ):
		event.Skip()
	
	def mitembuyOnMenuSelection( self, event ):
		event.Skip()
	
	def menuitemreportOnMenuSelection( self, event ):
		event.Skip()
	
	def m_menuItem2OnMenuSelection( self, event ):
		event.Skip()
	
	def Onclickexit(self,event):
		print ("hello")
		self.Close()
		event.Skip()
