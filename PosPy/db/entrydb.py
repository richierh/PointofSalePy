#!/usr/bin/python

#####################################################################
from pony import *
from pony.orm import *
from ormpony import *
import pony

"""
Code file ini berfungsi untuk membuat semua entitas databases yang dibuat 
menggunakan ERD (Entity Relational Diagram) PonyORM Tools terdata/map ke
dalam databases sqlite,mysqlite, atau yang lainnya

"""
#######################################################################

class connectdb():

    def __init__(self):
        db.bind(provider='sqlite', filename='mydatabase.sqlite', create_db=True)
       
        show(DataPersonal)
        # sql_debug digunakan untuk mengetahui proses yang terjadi selama 
        # program di jalankan
        sql_debug(True)

        """create_tables=True adalah metode untuk mempertahankan entitas
        database pada suatu table yang sudah dibuat
        """ 
        db.generate_mapping(create_tables=True)

#db = Database()
db.bind(provider='sqlite', filename='mydatabase.sqlite', create_db=True)
show(DataPersonal)
sql_debug(True)
#db.generate_mapping(False)
db.generate_mapping(create_tables=True)

#######################################################################
"""
Berisi tentang proses input data dari GUI ke databases dengan membuat
sebuah class bernama TabelForm
"""
########################################################################

class TabelForm(connectdb):
    """
    TabelForm saat database dimasukkan dari GUI ke databases
    """
    def __init__(self,*args,**kwds):
        super(TabelForm,self).__init__()
        self.dataformulir=mylist
        self.data(self.dataformulir)
        return None
  
    def data(self,a):
        return print("data sudah dimasukkan {}".format(self.dataformulir))

#mylist=["a","b","c"]
#formulir = TabelForm(mylist)