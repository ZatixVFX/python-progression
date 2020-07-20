# Junaid Salie Class 2
import datetime


class UserCar:
    def __init__(self, make, id, distance_driven, tank_size, kilometers_per_tank, year_model, base_price):
        self.make = make
        self.id = id
        self.distance_driven = distance_driven
        self.tank_size = tank_size
        self.kilometers_per_tank = kilometers_per_tank
        self.year_model = year_model
        self.base_price = base_price

    def get_id(self):
        self.id = int(input("Enter an ID: "))

    def get_make(self):
        self.make = str(input("Enter car make: "))

    def __str__(self):  # returns car properties used in menu
        for t in cars:
            if (self.make and self.id) == (t["make"] and t["id"]):
                return "\n ID: %s \n Make: %s \n Distance driven: %skm \n Tank size: %s \n Kilometers per tank: %sL \n " \
                       "Year model: %s \n Base price: R%s" % (
                           t['id'], t['make'], t['distance_driven'], t['tank_size'], t['kilometers_per_tank'],
                           t['year_model'],
                           t['base_price'])

    def return_fuel_usage(self):  # Function to return fuel usage for Volkswagen, Mercedes or Toyota used in Menu
        for dict_car in cars:
            # From Volkswagen Class
            volkswagen_answer = Volkswagen(self.make, self.id, year_model=dict_car['year_model'],
                                           distance_driven=None,
                                           tank_size=dict_car['tank_size'],
                                           kilometers_per_tank=dict_car['kilometers_per_tank'],
                                           base_price=dict_car['base_price'])
            # From Mercedes Class
            mercedes_answer = Mercedes(self.make, self.id, year_model=dict_car['year_model'], distance_driven=None,
                                       tank_size=dict_car['tank_size'],
                                       kilometers_per_tank=dict_car['kilometers_per_tank'],
                                       base_price=dict_car['base_price'])
            # From Toyota Class
            toyota_answer = Toyota(self.make, self.id, year_model=dict_car['year_model'], distance_driven=None,
                                   tank_size=dict_car['tank_size'],
                                   kilometers_per_tank=dict_car['kilometers_per_tank'],
                                   base_price=dict_car['base_price'])
            # if id and make equals to the id and make from car list return Volkswagen fuel usage
            if (self.make and self.id) == (dict_car["make"] and dict_car["id"]):
                return str(volkswagen_answer.calculate_fuel_usage())
            # elif id and make equals to the id and make from car list return Mercedes fuel usage
            elif (self.make and self.id) == (dict_car["make"] and dict_car["id"]):
                return str(mercedes_answer.calculate_fuel_usage())
            # elif id and make equals to the id and make from car list return Toyota fuel usage
            elif (self.make and self.id) == (dict_car["make"] and dict_car["id"]):
                return str(toyota_answer.calculate_fuel_usage())

    # Function to return resell value for Volkswagen, Mercedes or Toyota used in Menu
    def return_resell_value(self):
        for dict_car in cars:
            # From Volkswagen Class
            volkswagen_answer = Volkswagen(self.make, self.id, year_model=dict_car['year_model'],
                                           distance_driven=None,
                                           tank_size=dict_car['tank_size'],
                                           kilometers_per_tank=dict_car['kilometers_per_tank'],
                                           base_price=dict_car['base_price'])
            # From Mercedes Class
            mercedes_answer = Mercedes(self.make, self.id, year_model=dict_car['year_model'], distance_driven=None,
                                       tank_size=dict_car['tank_size'],
                                       kilometers_per_tank=dict_car['kilometers_per_tank'],
                                       base_price=dict_car['base_price'])
            # From Toyota Class
            toyota_answer = Toyota(self.make, self.id, year_model=dict_car['year_model'], distance_driven=None,
                                   tank_size=dict_car['tank_size'],
                                   kilometers_per_tank=dict_car['kilometers_per_tank'],
                                   base_price=dict_car['base_price'])
            # if id and make equals to the id and make from car list return Volkswagen resell value
            if (self.make and self.id) == (dict_car["make"] and dict_car["id"]):
                return str(volkswagen_answer.calculate_resell_value())
            # elif id and make equals to the id and make from car list return Mercedes resell value
            elif (self.make and self.id) == (dict_car["make"] and dict_car["id"]):
                return str(mercedes_answer.calculate_resell_value())
            # elif id and make equals to the id and make from car list return Toyota resell value
            elif (self.make and self.id) == (dict_car["make"] and dict_car["id"]):
                return str(toyota_answer.calculate_resell_value())


# car calculations for fuel usage and resell value
class Volkswagen(UserCar):
    def calculate_fuel_usage(self):
        for fuel_usage in cars:
            if (self.make and self.id) == (fuel_usage["make"] and fuel_usage["id"]):
                fuel_usage_answer = str(self.kilometers_per_tank // self.tank_size)
                return "Fuel usage: " + fuel_usage_answer + "L"

    def calculate_resell_value(self):
        for resell_value in cars:
            if (self.make and self.id) == (resell_value["make"] and resell_value["id"]):
                age = datetime.datetime.now().year - self.year_model
                if age < 20:
                    younger_answer = str(self.base_price * 0.9 * age)
                    return "Resell value: R" + younger_answer
                elif age >= 20:
                    older_or_same_age_answer = str(self.base_price * 0.9 * age + 20000)
                    return "Resell value: R" + older_or_same_age_answer


class Mercedes(UserCar):
    def calculate_fuel_usage(self):
        for fuel_usage in cars:
            if (self.make and self.id) == (fuel_usage["make"] and fuel_usage["id"]):
                fuel_usage_answer = str(self.kilometers_per_tank // self.tank_size)
                return "Fuel usage: " + fuel_usage_answer + "L"

    def calculate_resell_value(self):
        for resell_value in cars:
            if (self.make and self.id) == (resell_value["make"] and resell_value["id"]):
                age = datetime.datetime.now().year - self.year_model
                if age < 20:
                    younger_answer = str(self.base_price * 0.9 * age)
                    return "Resell value: R" + younger_answer
                elif age >= 20:
                    older_or_same_age_answer = str(self.base_price * 0.9 * age + 20000)
                    return "Resell value: R" + older_or_same_age_answer


class Toyota(UserCar):
    def calculate_fuel_usage(self):
        for fuel_usage in cars:
            if (self.make and self.id) == (fuel_usage["make"] and fuel_usage["id"]):
                fuel_usage_answer = str(self.kilometers_per_tank // self.tank_size)
                return "Fuel usage: " + fuel_usage_answer + "L"

    def calculate_resell_value(self):
        for resell_value in cars:
            if (self.make and self.id) == (resell_value["make"] and resell_value["id"]):
                age = datetime.datetime.now().year - self.year_model
                if age < 20:
                    younger_answer = str(self.base_price * 0.9 * age)
                    return "Resell value: R" + younger_answer
                elif age >= 20:
                    older_or_same_age_answer = str(self.base_price * 0.9 * age + 20000)
                    return "Resell value: R" + older_or_same_age_answer


# Exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


cars = [{'id': 1, 'year_model': 1995, 'distance_driven': 240000, 'base_price': 200000, 'tank_size': 30,
         'kilometers_per_tank': 100, 'make': 'Volkswagen'},
        {'id': 2, 'year_model': 2010, 'distance_driven': 10000, 'base_price': 300000, 'tank_size': 20,
         'kilometers_per_tank': 120, 'make': 'Volkswagen'},
        {'id': 3, 'year_model': 2017, 'distance_driven': 300000, 'base_price': 900000, 'tank_size': 15,
         'kilometers_per_tank': 80, 'make': 'Volkswagen'},
        {'id': 4, 'year_model': 1982, 'distance_driven': 560000, 'base_price': 50000, 'tank_size': 25,
         'kilometers_per_tank': 150, 'make': 'Mercedes'},
        {'id': 5, 'year_model': 2012, 'distance_driven': 30000, 'base_price': 500000, 'tank_size': 20,
         'kilometers_per_tank': 90, 'make': 'Mercedes'},
        {'id': 6, 'year_model': 2019, 'distance_driven': 10000, 'base_price': 1000000, 'tank_size': 15,
         'kilometers_per_tank': 100, 'make': 'Mercedes'},
        {'id': 7, 'year_model': 2000, 'distance_driven': 600000, 'base_price': 250000, 'tank_size': 25,
         'kilometers_per_tank': 200, 'make': 'Toyota'},
        {'id': 8, 'year_model': 2015, 'distance_driven': 30000, 'base_price': 350000, 'tank_size': 20,
         'kilometers_per_tank': 100, 'make': 'Toyota'},
        {'id': 9, 'year_model': 2018, 'distance_driven': 2000, 'base_price': 800000, 'tank_size': 25,
         'kilometers_per_tank': 200, 'make': 'Toyota'}]


# Main Menu
def main_menu():
    global user_choice, menu_2, user_input
    try:
        print(str("""Select an option:
                        1. Select a car based on their ID 
                        2. Display all of the cars
                        3. Exit program"""))
        user_choice = int(input("Choose an option: "))
        if user_choice == 2:
            for t in cars:
                print("ID:", t['id'], "   ", "Make:", t['make'])  # Display ID corresponding to make
            main_menu()  # Return back to main menu

        elif user_choice == 3:
            print("Exiting program .....")
            exit()  # Exit program
        # if user's choice is more than 3 raise ValueTooLargeError
        elif user_choice > 3:
            raise ValueTooLargeError
        # if user's choice is less then 1 raise ValueTooSmallError
        elif user_choice < 1:
            raise ValueTooSmallError
    except ValueError:
        # exception message if user types string instead of integers
        print("Type Number(integer) not letter/s(string/s)")
        main_menu()
    except ValueTooSmallError:
        print("Invalid option, try again")  # Message when Value is too small
        main_menu()  # Return back to main menu
    except ValueTooLargeError:
        print("Invalid option, try again")  # Message when value is too high
        main_menu()  # Return back to main menu
    for result in cars:
        """Enter car make and ID, result get's the distance driven, tank size, kilometers per tank, year model, 
        base price in cars list corresponding to car make and ID 
        """
        user_input = UserCar(make=result['make'], id=result['id'],
                             distance_driven=result['distance_driven'],
                             # program runs in this specific order
                             tank_size=result['tank_size'], kilometers_per_tank=result['kilometers_per_tank'],
                             year_model=result['year_model'], base_price=result['base_price'])
        user_input.get_make()
        user_input.get_id()
        break  # break once user has entered car make and ID
    # Menu 2
    while True:
        try:
            if user_choice == 1:  # if choice equal to 1 it takes the user to menu 2 once car make and ID has been given
                menu_2 = str("""Select what option you want for your car:
                                     1. Show car properties
                                     2. Show fuel usage
                                     3. Show resell value
                                     4. Go back to Main menu
                                     5. Exit Program""")
                print(menu_2)
                user_choice_2 = int(input("Choose an option: "))
                # if user chooses option 1, it prints car properties corresponding with given car make and ID
                if user_choice_2 == 1:
                    car_properties = user_input.__str__()
                    print("Car properties: ", car_properties)
                    # elif user chooses option 2, to print fuel usage corresponding with given car make and ID
                elif user_choice_2 == 2:
                    fuel_usage = user_input.return_fuel_usage()
                    print(fuel_usage)
                # elif user chooses option 3, to print resell value corresponding with given car make and ID
                elif user_choice_2 == 3:
                    resell_value = user_input.return_resell_value()
                    print(resell_value)
                # elif user chooses option 4 to go back to main then returns to main menu
                elif user_choice_2 == 4:
                    return main_menu()
                # elif user chooses option 5 to exit program then exit's program
                elif user_choice_2 == 5:
                    print("Exiting program .....")
                    exit()  # Exit program
                # elif user's choice is more than 3 raise ValueTooLargeError
                elif user_choice_2 > 5:
                    raise ValueTooLargeError
                # elif user's choice is less then 1 raise ValueTooSmallError
                elif user_choice_2 < 1:
                    raise ValueTooSmallError
        except ValueError:
            # exception message if user types string instead of integers
            print("Type Number(integer) not letter/s(string/s)")
        except ValueTooSmallError:
            print("Invalid option, try again")  # Message when Value is too small
        except ValueTooLargeError:
            print("Invalid option, try again")  # Message when value is too high


main_menu()
