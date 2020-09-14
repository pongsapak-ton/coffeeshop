def showspec(water,milk,coffee,money,cups):
            print("The coffee machine has : ")
            print(water," of water ")
            print(milk," of milk")
            print(coffee," of coffee beans")
            print(cups," of disposable cups")
            print(money," of money")






def buys(water, milk, coffee, money, cups):
           print("What do you want to buy  1- espresso, 2 - latte, 3 - cappuccino :")
           cof = int(input(":"))
           if cof == 1:
               print("----Espresso----")
               water -= 250
               coffee -= 16
               money += 4
               cups -= 1

           elif cof == 2:
               print("----Latte----")
               water -= 350
               milk -= 75
               coffee -= 20
               money += 7

           elif cof == 3:
               print("----Cappucino----")
               water -= 200
               milk -= 100
               coffee -= 12
               money += 6
           showspec(water, milk, coffee, money, cups)



def fills(water,milk,coffee,cups):
           print("Write how many ml of water do you  want to add : ")
           water+= int(input(":"))
           print("Write how many ml of milk do you  want to add : ")
           milk += int(input(":"))
           print("Write how many grams of coffee beans  do you  want to add : ")
           coffee += int(input(":"))
           print("Write  how many disposable cups of coffee do you  want to add : ")
           cups += int(input(":"))
           showspec(water, milk, coffee, money, cups)


def take(water, milk, coffee, money, cups):
           money -=int(input("I gave you $ :"))
           showspec(water, milk, coffee, money, cups)
           return money





if __name__ == '__main__':
      water = 400
      milk = 540
      coffee = 120
      cups = 9
      money  = 150
      showspec(water,milk,coffee,money,cups)
      print("Write action (buy, fill ,take)")
      ac = str(input(":"))
      if ac == 'buy':buys(water, milk, coffee, money, cups)
      if ac == 'fill':fills(water,milk,coffee,cups)
      if ac == 'take':take(water, milk, coffee, money, cups)






