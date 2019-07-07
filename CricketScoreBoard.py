#Cricket Score Board
class Cricket:
    def __init__(self):
        self.total_run=0
        self.total_ball=0

    def oneRun(self):
        self.total_run+=1
        self.total_ball+=1
        return self.info()

    def twoRun(self):
        self.total_run+=2
        self.total_ball+=1
        return self.info()

    def threeRun(self):
        self.total_run+=3
        self.total_ball+=1
        return self.info()

    def fourRun(self):
        self.total_run+=4
        self.total_ball+=1
        return self.info()

    def dot(self):
        self.total_ball+=1
        return self.info()

    def sixer(self):
        self.total_run+=6
        self.total_ball+=1
        return self.info()

    def noball(self):
        run=int(input("Enter Run:"))
        self.total_run+=run
        return self.info()

    def wide(self):
        self.total_run+=1
        return self.info()
    
    def bypass(self):
        run=int(input("Enter Run:"))
        self.total_run+=run
        return self.info()

    def info(self):
        print(f"Run:{self.total_run}  Ball:{self.total_ball}")
        return " "

if __name__=='__main__':
    Run = Cricket()
    print("1. One Run")
    print("2. Two Run")
    print("3. Three Run")
    print("4. Four Run")
    print("5. dot")
    print("6. Sixer")
    print("7. No Ball")
    print("8. Wide")
    print("9. Bypass")
    while True:
        option = int(input("\nChoose:"))
        if option==1:
            print(Run.oneRun())
        if option==2:
            print(Run.twoRun())
        if option==3:
            print(Run.threeRun())
        if option==4:
            print(Run.fourRun())
        if option==5:
            print(Run.dot())
        if option==6:
            print(Run.sixer())
        if option==7:
            print(Run.noball())
        if option==8:
            print(Run.wide()) 