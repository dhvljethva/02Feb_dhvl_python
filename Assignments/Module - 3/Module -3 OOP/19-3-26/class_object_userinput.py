class studentdata:
    stid = int
    stnm = str

    def getdata(self):
        self.stid=input("enter a id:")
        self.stnm=input("enter a name")

    def printdata(self):
        print("ID",self.stid)
        print("name",self.stnm)

st=studentdata()
st.getdata()
st.printdata()