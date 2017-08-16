#!/usr/bin/python
"""Kode ini adalah program utama untuk menjalankan aplikasi"""

import frame.main as begin

class Begin(begin.MyApp):

    """Kode ini adalah program utama untuk menjalankan aplikasi"""

    def __init__(self, *args, **kwds):
        """Kode ini adalah program utama untuk menjalankan aplikasi"""
        super(Begin, self).__init__(*args, **kwds)
        self.app = self.StartApp()
        self.Loop()

Begin()
