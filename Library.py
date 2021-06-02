from datetime import date


class Library:
    def __init__(self):
        __memberId = ""
        __memberName = ""
        __dateOfIssue = ""

    def setNameID(self, memberId):
        self.__memberId = memberId
        self.__memberName = input("Enter Member Name: ")
        self.setDate()

    def setDate(self):
        try:
            fDate = input("Enter Date of Issue: ").split(sep="-")
            self.__dateOfIssue = date(
                int(fDate[2]), int(fDate[1]), int(fDate[0]))
        except:
            print("DateInputError: Try Again")
            self.setDate()

    def returnBook(self):
        try:
            rDate = input("Enter Date of Return: ").split(sep="-")
            dateOfReturn = date(int(rDate[2]), int(rDate[1]), int(rDate[0]))
            dateDiff = dateOfReturn - self.__dateOfIssue
            if dateDiff.days > 7:
                print("Fine: " + str(dateDiff.days*5) + "Rs")
            else:
                print("Book return sucessful!")
        # if the user try to return book without adding data
        except AttributeError:
            print("There is no Data Available")
            rBChoice = input("Do you want to Set Data (y/n): ")
            if rBChoice == "y" or rBChoice == "Y":
                self.setNameID()
            else:
                return
        # if the date is in wrong format
        except:
            print("DateInputError: Try Again")
            self.returnBook()

    def getMemberID(self):
        return self.__memberId

    def displayData(self):
        print("{:<10} {:<15} {}".format(self.__memberId,
                                        self.__memberName, self.__dateOfIssue), end=" ")
        # print(self.__memberId, self.__memberName, self.__dateOfIssue, end=" ")

# Student Class


class Student(Library):
    def __init__(self):
        _department = ""

    def setNameID(self, memberId):
        super().setNameID(memberId)
        self._department = input("Enter the Department: ")

    def displayData(self):
        super().displayData()
        print("     " + self._department)
        # print(self._department)

# Teacher Class


class Teacher(Library):
    def __init__(self):
        _designation = ""

    def setNameID(self, memberId):
        super().setNameID(memberId)
        self._designation = input("Enter the Designation: ")

    def displayData(self):
        super().displayData()
        print("     " + self._designation)


'''Check for Duplicate Member Id'''


def memberIDCheck(libraryData, memberId):
    for data in libraryData:
        if data.getMemberID() == memberId:
            return True  # memberId Existed
    return False


def mainDriver():
    # a = Library()
    # a.returnBook()
    libraryData = []
    totalMembers = 0
    memberId = 208
    while(True):
        print("Enter:")
        print("      1:Student")
        print("      2:Teacher")
        #print("      3:Display All")
        print("      4:Exit")
        choice = int(input(": "))
        if choice == 1:
            print("Enter:")
            print("      1:Input Data")
            print("      2:Display Data")
            print("      3:Return Book")
            stuChoice = int(input(": "))
            if stuChoice == 1:
                memberId = input("Enter MemberID: ")
                if len(libraryData) > 0:
                    print(memberIDCheck(libraryData, memberId))
                libraryData.append(Student())
                libraryData[totalMembers].setNameID(memberId)
                totalMembers += 1
            elif stuChoice == 2:
                memberId = input("Enter MemberId to be Searchded: ")
                if memberIDCheck(libraryData, memberId):
                    for data in libraryData:
                        if data.getMemberID() == memberId:
                            print("{:<10} {:<15} {:<15} {:<15}".format(
                                'MEMBERID', 'MEMBERNAME', 'DATEOFISSUE', 'DEPARTMENT'))
                            data.displayData()
                else:
                    print("No Data Avail")
            elif stuChoice == 3:
                memberId = input("Enter MemberId to be Return Book: ")
                if memberIDCheck(libraryData, memberId):
                    for data in libraryData:
                        if data.getMemberID() == memberId:
                            data.returnBook()
                else:
                    print("No Data Avail")

        elif choice == 2:
            print("Enter:")
            print("      1:Input Data")
            print("      2:Display Data")
            stuChoice = int(input(": "))
            if stuChoice == 1:
                memberId = input("Enter MemberID: ")
                if len(libraryData) > 0:
                    print(memberIDCheck(libraryData, memberId))
                libraryData.append(Teacher())
                libraryData[totalMembers].setNameID(memberId)
                totalMembers += 1
            elif stuChoice == 2:
                memberId = input("Enter MemberId to be Searchded: ")
                if memberIDCheck(libraryData, memberId):
                    for data in libraryData:
                        if data.getMemberID() == memberId:
                            print("{:<10} {:<15} {:<15} {:<15}".format(
                                'MEMBERID', 'MEMBERNAME', 'DATEOFISSUE', 'DESIGNATION'))
                            data.displayData()
                else:
                    print("No Data Avail")
        elif choice == 3:
            for data in libraryData:
                if data.displayData()
        elif choice == 4:
            exit()
        else:
            print("Wrong Choice!")


mainDriver()

# print ("{:<10} {:<15} {:<15} {:<15}".format('NAME', 'MEMBERID', 'DATEOFISSUE','DEPART   
                       


# echo "     _              _                                  "
# echo "    / \   _ __  ___| |__  _   _ _ __ ___   __ _ _ __   "
# echo "   / _ \ | '_ \/ __| '_ \| | | | '_ ` _ \ / _` | '_ \  "
# echo "  / ___ \| | | \__ \ | | | |_| | | | | | | (_| | | | | "
# echo " /_/   \_\_| |_|___/_| |_|\__,_|_| |_| |_|\__,_|_| |_| "
# echo "                                                       "
