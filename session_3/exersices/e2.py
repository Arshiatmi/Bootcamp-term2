"""
برنامه ای بنویسید که ریشه های معادله درجه دو را بدست آورد.
"""


def delta(a, b, c):
    target_delta = (b ** 2) - 4 * a * c
    return target_delta


def calculate_roots(a, b, c):
    delta_number = delta(a, b, c)
    if delta_number > 0:
        print("Two Roots Found !")
        return (-b-(delta_number**0.5)/2*a), (-b+(delta_number**0.5)/2*a)
    elif delta_number == 0:
        print("One Root Found !")
        return (-b/2*a)
    else:
        print("There Is No Root For This Problem :(")
        return None


if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    response = calculate_roots(a, b, c)
    print(response)
