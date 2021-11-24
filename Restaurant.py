from Fridge import Fridge as fr


class Restaurant:
    def __init__(self, owner, password):
        self.__password = password
        self.owner = owner
        self.__owned_fridges = []

    def user_choice(self):
        print(f"Select a fridge to edit or hit [c] to cancel:")
        fridges = [f"{fridge.nickname}[{self.__owned_fridges.index(fridge)}]" for fridge in self.__owned_fridges]
        user_selection = input(fridges)
        return user_selection

    def edit_fridge(self):
        choice = self.user_choice()
        if choice.lower() == 'c':
            return
        else:
            selected_fridge = self.__owned_fridges[int(choice)]
            print("What would you like to do:\n Add Item[0] Remove Item[1] View Contents[2] Remove Fridge[3] Cancel[4]")
            action = int(input())
            if action == 0:
                selected_fridge.add_to_fridge()
            elif action == 1:
                selected_fridge.remove_from_fridge()
            elif action == 2:
                selected_fridge.check_fridge_contents()
            elif action == 3:
                self.remove_fridge(selected_fridge)
            else:
                return

    def add_fridge(self):
        nickname = input("What would you like to name the fridge: ")
        self.__owned_fridges.append(fr(self.owner, nickname))
        print("Fridge added!")

    def remove_fridge(self, choice):
        if choice.check_if_empty():
            self.__owned_fridges.remove(choice)
            print("Fridge removed!")
        else:
            print("Fridge not empty!")
            option = input("Would you like to discard all items to remove fridge? (y/n)")
            if option.lower() == 'n':
                self.edit_fridge()
            else:
                self.__owned_fridges.remove(choice)
                print("Items discarded and Fridge removed!")

    def show_all_fridges(self):
        for fridge in self.__owned_fridges:
            fridge.check_fridge_contents()

    # Will utilize this code for when complete application has been finished
    def validate_password(self, pw):
        if pw == self.__password:
            return True
        else:
            return False


