from colorama import Fore
import secrets


def main():
    values = list(range(1, 20)) + [None, 1, 1, 2, 3, 5, 8]

    for v in values:
        try:
            print(Fore.YELLOW + f"Calling sketchy_method with {v}...", flush=True)
            sketchy_method(v)
        except BrokenPipeError:
            print(Fore.LIGHTRED_EX + f" **** Network error, check our wifi.")
        except ArithmeticError:
            print(Fore.LIGHTRED_EX + f" **** Cannot compute with {v}!")
        except Exception as e:
            print(Fore.LIGHTRED_EX + f" **** Error: {type(e).__name__} ==> {str(e)}")
        # finally:
        #     print("Finally!")


def sketchy_method(value: int):

    if not value:
        raise ValueError(f"{value} is not valid.")
    elif value % 6 == 0:
        raise ArithmeticError()
    elif secrets.SystemRandom().randint(1, 10) == 3:
        raise BrokenPipeError("Bad network!")

    print("sketchy_method() actually worked!")


if __name__ == '__main__':
    main()
