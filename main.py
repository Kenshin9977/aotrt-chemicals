#!/usr/bin/env python3
# coding: utf-8


def compute_value(item):
    left_value = get_single_digit("\n{} left".format(item))
    upper_value = get_single_digit("{} up".format(item))
    return left_value + upper_value


def get_single_digit(prompt):
    while True:
        try:
            answer = input("{}:> ".format(prompt))
            answer = int(answer)
            assert 0 < answer < 10
        except ValueError:
            print("\n Error '{}' is not a number\n".format(answer))
        except AssertionError:
            print("\n  The number has to be between 0 and 10\n")
        else:
            return answer


def get_positive_number(prompt):
    print()
    while True:
        try:
            answer = input("{}:> ".format(prompt));
            answer = int(answer)
            assert answer > 0
        except ValueError:
            print("\n Error '{}' is not a number\n".format(answer))
        except AssertionError:
            print("\n The number has to be greater than 0\n")
        else:
            return answer


def get_option(options, title):
    print("\n", title, "\n")
    print(*["{0:4}. {1}".format(i, c) for i, c in enumerate(options)], sep="\n")
    print()

    while True:
        try:
            answer = input(">>> ")
            answer = int(answer)
            assert -1 < answer < len(options)
        except (AssertionError, ValueError):
            print("\n Error '{}' is not a valid option\n"
                  .format(answer))
        else:
            return answer


def show_useless():
    useless_values = [
        [2, "Mixed acid"],
        [0, "Food coloring"],
        [0, "Glycerol"],
        [1, "Fat"],
        [0, "Bleach"],
        [0, "Powdered milk"],
        [0, "Pool cleaner"],
        [0, "Ice"],
        [0, "Table salt"],
        [1, "Nitrated Glycerol Solution"],
    ]

    prefixs = ["", "", "", ""]

    print("\n ================================"
          "\n|Program written by Kenshin9977|"
          "\n|  & improved by Creuilcreuil  |"
          "\n================================="
          "\n\nThe following values are useless\n",
          *["\n - {0}{1}".format(prefixs[p], v) for (p, v) in useless_values])


def main():

    def set_all_values():
        for i, (var, name, getter) in enumerate(values):
            print("\n{0} value(s) out of {1}".format(i + 1, len(values)), end="")
            # something really shady is going on here :P
            globals()[var] = getter(name)

    def set_some_values():
        def options():
            options_some = ["{0} = {1}".format(n, globals()[v])
                            for (v, n, _) in values]
            options_some[-1] += "\n"
            return options_some + ["Return to the main menu"]

        title_some = "\nChoose a value to edit"

        while True:
            result = get_option(options(), title_some)
            if result == len(values):
                return
            else:
                # hooohooo black magic :)
                var, name, getter = values[result]
                globals()[var] = getter(name)

    title = "Choisissez le produit que vous voulez obtenir"
    options = [
        "Edit one or several values",
        "Display useless values",
        "Exit\n",
        "3,4-di-nitroxy-methyl-propane",
        "Octa-hydro-2,5-nitro-3,4,7-para-zokine",
        "1,3,5 tera-nitra-phenol",
        "3-methyl-2,4-di-nitrobenzene",
    ]

    title_set = "Choose type of edit"
    options_set = [
        "Edit every values",
        "Edit specific values",
    ]

    values = [
        # [variable name, item name, getter function]
        ["phi", "Phi", get_positive_number],
        ["carburant", "Racing fuel", compute_value],
        ["insectifuge", "Repellent", compute_value],
        ["vodka", "Vodka", compute_value],
        ["bicabonate", "Baking soda", compute_value],
        ["detergent", "Detergent", compute_value],
        ["deboucheur", "Drain opener", compute_value],
        ["pieces", "Quarters", compute_value],
        ["nettoyant_vitres", "Glass cleaner", compute_value],
        ["dissolvant", "Nail polish remover", compute_value],
        ["piecette", "Pennies", compute_value],
        ["hexamine", "Hexamine", compute_value],
        ["acide_pheno", "Phenolsulfonic Acid", compute_value],
        ["phenol", "Phenol", compute_value],
        ["aldehyde_pateux", "Aldehhyde sludge", compute_value],
        ["formaldehyde", "Formaldehyde", compute_value],
        ["dinitro", "Dinitro", compute_value],
        ["huile", "Motor oil", compute_value],
        ["nettoyant_roues", "Wheel cleaner", compute_value],
        ["engrais", "Plant food", compute_value],
        ["peinture", "Paint", compute_value],
        ["vinaigre", "Vinegar", compute_value],
        ["acetaldehyde", "Acetaldehyde", compute_value],
        ["methyly", "Methylybenzene", compute_value],
    ]

    # initialize all variables to zero
    for (var, _, _) in values:
        globals()[var] = 0

    show_useless()
    print("\nPlease enter the required values")
    set_all_values()

    while True:
        answer = get_option(options, title)

        if answer == 0:
            answer_set = get_option(options_set, title_set)
            if answer_set == 0:
                set_all_values()
            elif answer_set == 1:
                set_some_values()
        elif answer == 1:
            show_useless()
        elif answer == 2:
            exit()
        elif answer == 3:
            print("\n"
                  "Quarters + Racing fuel = Formaldehyde ({})"
                  .format(pieces + carburant - phi),

                  "Pennies + Vodka = Acetaldehyde ({})"
                  .format(piecette + vodka - phi),

                  "Acetaldehyde + Formaldehyde + Detergent = Aldehyde sludge ({})"
                  .format(acetaldehyde + formaldehyde + detergent - phi),

                  "Aldehyde sludge + Nail polish remover = 3,4-di-nitroxy-methyl-propane({})"
                  .format(aldehyde_pateux + dissolvant - phi),
                  "", sep="\n")
        elif answer == 4:
            print("\n"
                  "Quarters + Racing fuel = Formaldehyde ({})"
                  .format(pieces + carburant - phi),

                  "Glass cleaner + Formaldehyde = Hexamine ({})"
                  .format(nettoyant_vitres + formaldehyde - phi),

                  "Vinegar + Plant food + Detergent + Hexamine = "
                  "Octa-hydro-2,5-nitro-3,4,7-para-zokine ({})\n"
                  .format(vinaigre + engrais + detergent + hexamine - phi),
                  "", sep="\n")
        elif answer == 5:
            print("\n"
                  "Motor oil + Wheel cleaner + Repellant = Phenol ({})"
                  .format(huile + nettoyant_roues + insectifuge - phi),

                  "Phenol + Drain opener = Phenolsulfonic acid ({})"
                  .format(phenol + deboucheur - phi),

                  "Acid Phenolsulfonic + Detergent = 1,3,5 tera-nitra-phenol ({})"
                  .format(acide_pheno + detergent - phi),
                  "", sep="\n")
        elif answer == 6:
            print("\n"
                  "Paint + Detergent + Drain opener = Methylybenzene ({})"
                  .format(peinture + detergent + deboucheur - phi),

                  "Methylybenzene + Baking soda + "
                  "Vinegar + Detergent = Dinitro ({})"
                  .format(methyly + bicabonate + vinaigre + detergent - phi),

                  "Dinitro + Racing fuel = 3-methyl-2,4-di-nitrobenzene ({})"
                  .format(dinitro + carburant - phi),
                  "", sep="\n")


if __name__ == '__main__':
    main()