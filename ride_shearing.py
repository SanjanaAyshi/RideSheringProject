from abc import ABC, abstractmethod
#company main settings
class rideShearing:
    def __init__(self,companyName):
        self.companyName=companyName
        self.riders=[]
        self.drivers=[]
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_drivers(self,driver):
        self.drivers.append(driver)
    def __repr__(self):
        return f"{self.companyName} has {self.riders}"

#user ability
class user(ABC):
    def __init__(self,user_name,user_email,nid):
        self.user_name=user_name
        self.user_email=user_email
        self.nid=nid
    @abstractmethod
    def display_profile(self):
        return NotImplemented

#driver information
class driver(user):
    def __init__(self, user_name,user_email, nid,current_location) -> None:
        super().__init__(user_name,user_email, nid)
        self.current_location = current_location
    
    def display_profile(self):
        print(f"Driver:{self.user_name} Email:{self.user_email}")

#rider information
class rider(user):
    def __init__(self,user_name,user_email,nid,current_location):
        self.current_ride=None #currently the rider is free
        super().__init__(user_name,user_email,nid)
        self.current_location=current_location
    def display_profile(self):
        print(f"Rider: {self.user_name} who's email is {self.user_email}")
    def rider_request(self,Pathaw,destination):
        print("Looking for it.....")
        if not self.current_location:
            obtain= rider_matching(Pathaw.drivers) #pathaw er driver der current location er sathe match kore
            receive=obtain.has_driver(self,destination)
            print("Your result: ", receive)
            self.current_location=receive
            return True
        else:
            return False
    
#ride ordering
class ride:
    def __init__(self,start_location,end_location):
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
    def start_ride(self):
        pass
    def end_ride(self):
        pass
    def __repr__(self):
        return f"The journey started from {self.start_location} to {self.end_location}.Enjoy!!"

# rider matching 
class rider_matching(ride):
    def __init__(self,drivers):
        self.drivers=drivers
    
    def has_driver(self,rider,destination):
        if len(self.drivers)> 0: #driver er length jodi 0 theke besi hoi tahole accept korbe 
            ride=ride(ride.current_location,destination)
            return ride
        else:
            return f"Sorry no Ride Found for {self.end_location}"
    
# giving info

Pathaw= rideShearing("Pathaw") #company info

Anis=driver("Anis mama", "anis@gmail.com",12245,"Pagol der Pabna") # driver info

Kudus=rider("Kuddus miya","kudus@gmail.com",22457,"chapabas der chapay") #Rider info

#passing info 
Pathaw.add_drivers(Anis)
Pathaw.add_rider(Kudus)

#checking ride request
if Kudus.rider_request(Pathaw,"Dhaka"):
    print("Got you ride")
else:
    print("Can't find any ride")






 
 
            
   