class student:
    stid = 19
    stnm = 'dhaval'
    
    def getdata(self):
        print("This data from the student class")

st = student()
print("Id:",st.stid)
print("Name:",st.stnm)
st.getdata()