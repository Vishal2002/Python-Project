from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


class busticket:
    def __init__(self,source,list,passenger_name,name):
        self.name=name
        self.source=source
        self.destination=list
        self.passenger_name=passenger_name
        self.ticketlist={}
        self.fare={'Mumbai':20,'Cheenai':50,'Pune':60,'Kolkata':80}
    def displayroute(self):
        print(f"You can choose following destination : {self.name}")
        for destination in self.destination:
            print(destination)

    def createticket(self,UID,dest,no_of_passenger):
        if UID not in self.ticketlist.keys():
            self.ticketlist.update({UID:dest})
            print("Ticket created")
            print(f"Source : {self.source}")
            print(f"Destination :",dest)
            print(current_time)
            
        elif dest not in self.destination:
            print("Choose Valid Destination")
            
            
        else:
            print("Ticket not available")

    def totalfare(self,dest,no_of_passenger):
       
        price=self.fare.get(dest)
        print("Total Fare of Travel is Rs:",price*no_of_passenger)

    def cancelticket(self,UID):
        self.ticketlist.pop(UID)
        
    

if __name__=='__main__':
    Vishal=busticket('Delhi',["Mumbai","Pune","Kolkata","Chennai"],'Vishal','Sharma Travels')

    while(True):
        print('1.Make Ticket')
        print('2.Display Routelist')
        print('3.Cancel Ticket')
        user_choice=int(input())
        if user_choice==1:
            
            passenger_name=input("Enter Name :")
            no_of_passenger=int(input("Enter no of passenger :"))
            dest=input("Enter destination")
            UID=int(input("Enter Aadhar number :"))
            Vishal.createticket(UID,dest,no_of_passenger)
            Vishal.totalfare(dest,no_of_passenger)

        elif user_choice==2:
            Vishal.displayroute()
        elif user_choice==3:
            UID=int(input("Enter the UID :"))
            Vishal.cancelticket(UID)
        else:
            print("Enter correct choice ")
        
        print('Press q to quit and c to continue')

        user_choice2=""
        while(user_choice2!='q' and user_choice2!='c'):
            user_choice2=input()
            if user_choice2=='q':
                exit()
            elif user_choice2=='c':
                continue
        
