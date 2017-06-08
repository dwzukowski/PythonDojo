import datetime
class Call(object):
    def __init__(self, name, number, reason):
        self.callid = 0
        self.callerName = name
        self.callerNumber = number
        self.callTime = 0
        self.callReason = reason
    def displayCallDetails(self):
        print "Call id:",self.callid, "\nName:",self.callerName, "\nNumber:",self.callerNumber, "\nTime:",self.callTime, "\nReason:",self.callReason

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
        self.centerid = 100
    def add(self,caller):
        caller.callid= self.centerid
        caller.callTime= datetime.datetime
        self.centerid+=1
        self.calls.append(caller)
        self.queue+=1
        #print "added call"
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    def info(self):
        print "There are currently",self.queue,"callers in the queue.\n"
        for caller in range(0,len(self.calls)):
            self.calls[caller].displayCallDetails()


caller1=Call("Timbo Jones", "412-555-8675", "complaint")
#call1.displayCallDetails()
center1=CallCenter()
center1.add(caller1)
#center1.calls[0].displayCallDetails()
#center1.remove()
#print center1.calls
center1.info()