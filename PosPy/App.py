#!/usr/bin/python
"""This code is the starting python Apps to running"""

import frame.main as begin

class Begin(begin.MyApp):
    """Kode ini adalah program utama untuk menjalankan aplikasi"""
    def __init__(self, *args, **kwds):
        """Kode ini adalah program utama untuk menjalankan aplikasi"""
        super(Begin, self).__init__(*args, **kwds)
        self.app = self.MyApp()
Begin()
