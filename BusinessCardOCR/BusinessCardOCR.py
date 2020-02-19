class ContactInfo:
    email = ""      #email of the person
    name = ""       #name of the person
    number = ""     #number of the person
    data = []       #Where all the data is held from the card

    #Constructor
    def __init__(self, data):
        self.data = data

    #getEmailAddress(): A function that finds '@' in the data and makes it the email
    #Input: No required input
    #Output: self.email stored with the email of the person
    def getEmailAddress(self):
        for i in self.data:
            if '@' in i:
                self.email = i
        return self.email

    #getName(): Uses different permutations of the email to try to find the name
    #Input: No required input
    #Output: self.name stored with the name of the person
    def getName(self):
        if self.email == "":
            self.getEmailAddress()
        email = self.email.split('@')
        email = email[0]                                        #gets the part of the eamil before @
        possibleNames = [email.split('.'),email[1:],email[:-1]] #different permutation of the email
        for i in self.data:
            #lisa.haun -> if 'lisa' is in the string
            if len(possibleNames[0]) > 1:
               if possibleNames[0][0].lower() in i.lower() and not '@' in i:
                   self.name = i 
            #awilson -> if 'wilson' (without a) is in the string   
            if possibleNames[1].lower() in i.lower() and not '@' in i:
                self.name = i
            #nieberdinge -> if 'nieberding' is in the string
            if possibleNames[2].lower() in i.lower() and not '@' in i:
                self.name = i

        if self.name == "":
            self.name = "Name could not be found."

        return self.name

    #getPhoneNumber(): Finds a string with 12 or 13 numbers and makes it the phone number
    #Input: No required input
    #Output: self.number stored with the email of the person
    def getPhoneNumber(self):
        nums = ""
        for i in self.data:
            totalNums = 0
            nums = ""
            if "fax" not in i.lower():
                #goes through each character and count the amount of numbers using ascii
                for j in range(len(i)):
                    if i[j] >= '0' and i[j] <= '9':
                       nums += i[j] 
                       totalNums += 1 
                if totalNums == 10:
                    self.number = nums
                elif totalNums == 11:
                    self.number = nums[1:]
        return self.number;

#getContactInfo(): Reads the file and creates an object
#Input: document must be a valid file in the soruce directory
#Output: card which is a ContactInfo object
def getContactInfo(document):
    f = open(document,'r')
    readData=[]
    with open(document) as f:
        readData = f.read().split('\n')
    card = ContactInfo(readData)
    return card




if __name__ == '__main__':
    document = input("Please enter a document: ")
    info = getContactInfo(str(document))

    print(info.getName())
    print(info.getEmailAddress())
    print(info.getPhoneNumber())



    
    
