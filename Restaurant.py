from Fridge import Fridge as fr


class Restaurant:
    def __init__(self, owner):
        self.owner = owner
        self.__owned_fridges = []

    def edit_fridge(self):
        print(f"Select a fridge to edit or hit [c] to cancel:")
        """create list comprehension to show fridge nickname and index"""
        choice = input()
        if choice == 'c':
            return
        else:
            selected_fridge = self.__owned_fridges[int(choice)]
            print("What would you like to do?: \n Add Item[0] Remove Item[1] View Contents[2] Cancel[3]")
            action = int(input())
            if action == 0:
                selected_fridge.add_to_fridge()
            elif action == 1:
                selected_fridge.remove_from_fridge()
            elif action == 2:
                selected_fridge.check_fridge_contents()
            else:
                return

    def add_fridge(self):
        self.__owned_fridges.append(fr(self.owner))

    def remove_fridge(self):
        pass

    def show_all_fridges(self):
        for fridge in self.__owned_fridges:
            print(f"Fridge[{self.__owned_fridges.index(fridge)}] contents:")
            fridge.check_fridge_contents()



