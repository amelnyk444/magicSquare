import random
import os

class magicSquare:


    def __init__(self,n=4):
        
        self.dimension = n
        self.magicConst = (n*(n*n + 1))/2
        self._matrix =  [[0] * (n+1) for i in range(n+1)]
        self.reservedInd = []


    def _createCoordForMatrix(self):
        #User can see NxN matrix with numbers for each row and column
        self._matrix[0][0] = " "
        for i in range(1,self.dimension + 1):
            self._matrix[0][i] = i
            self._matrix[i][0] = i
    

    def _canBeInserted(self,element, rowVal, colVal):

         if element < 1:
             return False

         if [rowVal, colVal] in self.reservedInd:
             return False

         for i in range(1,self.dimension+1):
             for j in range(1,self.dimension+1):
                 if element == self._matrix[i][j]:
                     return False

         sum = element
         for i in range(1,self.dimension+1):
             sum += self._matrix[rowVal][i]
             if sum > self.magicConst:
                 return False
         
         sum = element
         for i in range(1,self.dimension+1):
             sum += self._matrix[i][colVal]
             if sum > self.magicConst:
                 return False

         if (rowVal == colVal) or (rowVal == self.dimension+1 - colVal):
            sum = element
            for i in range(self.dimension):
                sum += self._matrix[i+1][i+1]
                if sum > self.magicConst:
                    return False
         
            sum = element
            for i in range(self.dimension, 0, -1):
                sum += self._matrix[i][i]
                if sum > self.magicConst:
                    return False

         self.reservedInd.append([rowVal, colVal])
         return True


    def _createChallenge(self):
        #This function makes start conditions by generating start N elements
        self._matrix =  [[0] * (self.dimension+1) for i in range(self.dimension+1)]
        self._createCoordForMatrix()
        self.reservedInd = []
        counter = 0
        while counter <= self.dimension:
            rowVal = random.randint(1,self.dimension)
            colVal = random.randint(1,self.dimension)
            element = random.randint(1,self.magicConst//2)
            if(self._canBeInserted(element,rowVal,colVal) and self._matrix[rowVal][colVal]==0):
                self._matrix[rowVal][colVal] = element
                counter += 1


    def _printMatrix(self):

        for i in range(len(self._matrix)):
            print()
            for j in range(len(self._matrix[i])):
                print(self._matrix[i][j], end=' ')
                
        
    def getInstructions(self):

         print("Hi, player\nDo you know the rules of the game? (Y/N): ")
         userInp = input()
         if userInp.lower() == "n":
              print("Rules: \n a magic square is a  n*n square grid (where  n is the number of cells on each side)\n filled with distinct positive integers in the range  1,2,...,n^2\n such that each cell contains a different integer and the sum of the integers\n in each row, column and diagonal is equal. The sum is called the magic constant or magic sum of the magic square.\n")
         elif userInp.lower() == "y":
             print("Let`s go\n")


    def _checkIntegerInput(self):
        #Error prevention
        try:
            inp = int(input())
        except ValueError:
            print("Incorrect input, try again: ")
            return self.checkIntegerInput()
        else:
            return inp


    def _checkRangeInput(self):
        #Error prevention
        try:
            inp = int(input())
            self._matrix[inp][inp]
        except ValueError:
            print("Incorrect input, try again: ")
            return self.checkIntegerInput()
        except IndexError:
            print("This square has a smaller dimension, try again: ")
            return self.checkRangeInput()
        else:
            return inp

           
    def userInput(self,instructions=True):

        if True==instructions:
            self.getInstructions()

        print("\nInput the dimension of the square: ")
        self.dimension = self.checkIntegerInput()
        os.system('cls')

        self.createChallenge()
        self.printMatrix()

        counter = self.dimension
        while(counter <= self.dimension*self.dimension):

            print("\nInput row number: ")
            rowNumb = self.checkRangeInput()
            print("\nInput column number: ")
            columnNumb = self.checkRangeInput()
            print("\nInput element: ")
            element = self.checkIntegerInput()
            
            if(True==self._canBeInserted(element,rowNumb,columnNumb)):
                self._matrix[rowNumb][columnNumb] = element
                os.system('cls')
                self.printMatrix()
                counter += 1
            else:
                print("You can't insert this item here\n")

        print("Great! Try again?(Y/N)\n")
        if "y" == input().lower():
            os.system('cls')
            self.userInput(False)
        else:
            print("Bye\n")
        