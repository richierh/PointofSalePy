#!/usr/bin/python


class setdownup(object):
    print ("Please wait ... \n\nApplication Starting ...\n\n\nOk\n ")
    def __init__(self):
        self.downstream = [
        "128","256","384","512","1024"
        ]   
        self.upstream =["1024"]
        self.netid="enp1s0"
        
    def setnow(self):
        self.down=self.downstream[self.input_downstream-1]
        self.up = self.upstream[0]
        return self.output()

    def output(self):
        command = ("sudo wondershaper {} {} {}".format(self.netid,self.down,self.up))
        return command

    def question(self):
        self.input_downstream=input("Silahkan masukkan kecepatan download yang dikehendaki:\n\
1.128 kbps\n2.256 kbps\n3.384 kbps\n4.512 kbps\n5.1024 kbps\n\
")
        if self.input_downstream > 0 and self.input_downstream <= 5:
            self.setnow()
            return self.setnow()

l = setdownup()
print (l.question())
