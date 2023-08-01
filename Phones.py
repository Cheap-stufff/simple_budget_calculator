class Phones:
          def __init__(self, name, price, model):
                    self.name = name
                    self.price = float(price)
                    
          def budget_check(self, budget):
                    if not isinstance(budget, (int, float)):
                              print('Invalid entry. Kindly enter number!')
                              exit()
                    
           def change(self, budget):
                    return (budget - self.price)
                    
          def buy(self, budget):
                    self.budget_check(budget)
                    
                    if budget >= self.price:
                              print(f'You can spend on a {self.name}')
                              
                              if budget == self.price:
                                        print('You have enough money for this phone')
                              else:
                                        print(f'You can buy this phone and have $ {self.change(budget)} left over')
                              exit('thanks for using the budget app!')
