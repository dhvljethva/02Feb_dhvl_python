class Studentinfo:
    stid:int
    stnm: str

    def getdata(self):
        self.stid=input("Enter an Id:")
        self.stnm=input("Enter a NAME:")

    def printdata(self):
        print("Id:",self.stid)
        print("Name;",self.stnm)
         
st=Studentinfo()
st.getdata()
st.printdata()         