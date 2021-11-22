class Fridge:
    def __init__(self, owner, nickname):
        self.nickname = nickname
        self.owner = owner
        self.__authorized_users = [owner]
        self.__contents = []

    def check_if_empty(self):
        if len(self.__contents) == 0:
            return True
        else:
            return False

    def select_item_to_delete(self):
        collection = [f"{x}[{self.__contents.index(x)}]" for x in self.__contents]
        choice = int(input(f"Chose the number of the item you want to delete: {collection} : "))
        item_to_delete = self.__contents[choice]
        print(item_to_delete)
        return item_to_delete

    def add_to_fridge(self):
        if len(self.__contents) == 5:
            print("Your fridge is full!")
        else:
            item = input("What would you like to add : ")
            self.__contents.append(item)

    def remove_from_fridge(self):
        if self.check_if_empty():
            print("This fridge is empty!")
        else:
            print("Here are the contents of the fridge")
            item_to_delete = self.select_item_to_delete()
            confirmation = int(input("Are you sure you want to delete this item? \n Yes[0], No[1], Cancel[2] : "))
            if confirmation == 0:
                self.__contents.remove(item_to_delete)
            elif confirmation == 1:
                self.remove_from_fridge()
                print("Removed")
            else:
                print("Returning back to the flow")

    def check_fridge_contents(self):
        if self.check_if_empty():
            print("This fridge is empty!")
        else:
            print(f"There are {str(len(self.__contents))} item(s) in the fridge. Here are the contents: \n")
            print(self.__contents)

