class Course:
    def __init__(self,cname,cid):
        self._cname = cname
        self._cid = cid

    def getCname(self):
        return self._cname
    def getCid(self):
        return self._cid
    
    def courseInfo(self):
        print(f"The name of the course: {self._cname}")
        print(f"The course id: {self._cid}")
