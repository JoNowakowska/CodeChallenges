import functools


def add_host_name(name):
    def wrapper_func(func):
        def wrapped_one(*args, **kwargs):
            print(f"Hello and welcome! My name is {name}.")
            print(func(*args, **kwargs))
            print("That is all for today! Stay safe and see you soon!")

        return  wrapped_one

    return wrapper_func


@add_host_name("Joanna")
def news(city, type, info):
    return f"Now, I am going to present some {type} news about {city}! \n{info}"


CITY = "Poznan"
TYPE = "positive"
INFO = "Poznan has been doing really great during the pandemic, therefore the lockdown is over as of tomorrow, hurray!"

news(CITY, TYPE, INFO)