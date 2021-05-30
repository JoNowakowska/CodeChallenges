"""
A traveling salesman has to visit clients. He got each client's address e.g. "432 Main Long Road St. Louisville OH 43071" as a list.

The basic zipcode format usually consists of two capital letters followed by a white space and five digits. The list of clients to visit was given as a string of all addresses, each separated from the others by a comma, e.g. :

"123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432".

To ease his travel he wants to group the list by zipcode.
Task

The function travel will take two parameters r (addresses' list of all clients' as a string) and zipcode and returns a string in the following format:

zipcode:street and town,street and town,.../house number,house number,...

The street numbers must be in the same order as the streets where they belong.

If a given zipcode doesn't exist in the list of clients' addresses return "zipcode:/"
Examples

r = "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432"

travel(r, "OH 43071") --> "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"

travel(r, "NY 56432") --> "NY 56432:High Street Pollocksville/786"

travel(r, "NY 5643") --> "NY 5643:/"

Note for Elixir:

In Elixir the empty addresses' input is an empty list, not an empty string.
Note:

You can see a few addresses and zipcodes in the test cases.

source: codewars.com
"""


def travel(r, zipcode):
    # extracting addresses with zipcode of interest
    addresses_of_interest = [x for x in r.split(',') if x[-8:] == zipcode]

    # if there are no such addresses, returning the info
    if not addresses_of_interest:
        return zipcode + ":/"

    # otherwise, preparing the string which will be returned
    street_names = []
    street_nos = []
    for address in addresses_of_interest:
        # extracting street name and number from a string and adding to the lists
        address_elements = address.split(" ")
        street_names.append(" ".join(address_elements[1:-2]))
        street_nos.append(address_elements[0])

    # returning the final string
    return zipcode + ":" + ','.join(street_names) + '/' + ','.join(street_nos)


ad = "67000 Paris St. Abbeville AA 45522,88 Paris St. Abbeville AA 45511,98 Paris St. Asdfdfsdfssdbbeville AA 45522,97 Paris St. Abbeville AA 45522,1000 Paris St. Abbeville AA 45522"

print(travel(ad, "AA 45522"))


