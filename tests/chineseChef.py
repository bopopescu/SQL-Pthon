from Chef import Chef
#inside the parantheses thaty mean sinherite all from that class
#meaining this chef can use every function in its parent class of Chef
class ChineseChef(Chef):

    def makes_fried_rice(self):
        print("Chef makes fried rice")

    def make_special_dish(self):
        print("The chef makes orange chicken")