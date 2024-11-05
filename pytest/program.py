

def one():

    return 13


def two(x = 2, y = 3):

    return x * y


def three():

    data = {
        "band_6ghz" : {
            "clients" : []
            }
        }

    return data


if __name__ == '__main__':

    print("Run main")
    a = one()
    b = two()
    c = three()

    print(a, b, c)