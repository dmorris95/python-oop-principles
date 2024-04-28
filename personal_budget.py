#Task 1

'''class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

elec_budget = BudgetCategory("Electical", "400")
'''

#Task 2
'''
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
    
    #getters & setters
    def get_cat_name(self):
        return self.__category_name
    def get_all_budget(self):
        return self.__allocated_budget

    def set_cat_name(self, new_name):
        if new_name == "":
            print("Something must be entered for the new category name!")
        else:
            self.__category_name = new_name

    def set_all_budget(self, new_budget):
        if new_budget > 0:
            self.__allocated_budget = new_budget
        else:
            print("The budget must be a positive number!")
'''

#Task 3

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.expenses = 0
    
    #getters & setters
    def get_cat_name(self):
        return self.__category_name
    def get_all_budget(self):
        return self.__allocated_budget

    def set_cat_name(self, new_name):
        if new_name == "":
            print("Something must be entered for the new category name!")
        else:
            self.__category_name = new_name

    def set_all_budget(self, new_budget):
        if new_budget > 0:
            self.__allocated_budget = new_budget
        else:
            print("The budget must be a positive number!")

    #Add expense
    def add_expense(self, amount):
        if amount > 0:
            if (self.expenses + amount) > self.get_all_budget():
                print("Your expenses are more than your budget! Something needs to change in your expenses.")
            else:
                self.expenses += amount
        else:
            print("The expense amount must not be negative!")


    #Task 4

    #display budget information
    def display_category_information(self):
        print("Category Name:", self.get_cat_name())
        print("Allocated Budget:", self.get_all_budget())
        print("Remaining Budget after expenses:", (self.get_all_budget() - self.expenses))



elec_budget = BudgetCategory("Electical", 400)
enter_budget = BudgetCategory("Entertainment", 250)
enter_budget.set_all_budget(700)

elec_budget.add_expense(200)
enter_budget.add_expense(500)

enter_budget.display_category_information()
elec_budget.display_category_information()
