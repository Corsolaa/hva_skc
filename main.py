def calculate_sq_feet_cost():
    fc_name = input("Wat is de naam van de voetbalclub?: ")

    # Een loop die altijd doorgaat totdat het een geldig getal is.
    while True:
        surface_vm = input("Wat is de oppervlakte in vierkante meter?: ")

        # Format de string zodat het een float kan zijn.
        surface_vm = surface_vm.replace(",", ".")

        # Checkecn of het een float kan zijn.
        try:
            float(surface_vm)
            is_float = True
        except ValueError:
            is_float = False

        # Checken of het getal wel echt een getal is.
        if is_float or surface_vm.isdigit():
            break
        print("Vul alsjeblieft een geldig getal in.")
    # De oppervlakte die omgerekend moet worden moet naar een float omgezet worden.
    surface_square_f = float(surface_vm) * 10.76
    print(f"De oppervlakte van {fc_name} is {surface_vm} vierkante meter. Dit is {surface_square_f} "
          f"square foot.")
    # Kosten verrekenen in euros.
    kosten = surface_square_f * 0.3

    # Euros moeten maar 2 decimalen hebben.
    print(f"De kosten zijn {round(kosten, 2)} euro.")


if __name__ == '__main__':
    calculate_sq_feet_cost()
