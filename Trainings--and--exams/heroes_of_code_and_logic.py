def party_func(number, party):
    for n in range(number):
        hero, hp, mp = input().split()
        party[hero] = [int(hp), int(mp)]

    return party


def castspell_func(mp_needed, spell_name, hero_name, party):
    if hero_name in party:
        if party[hero_name][1] >= mp_needed:
            party[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {party[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    return party


def takedamage_func(hero_name, damage, attacker, party):
    if hero_name in party:
        if party[hero_name][0] - damage > 0:
            party[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {party[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del party[hero_name]

    return party


def recharge_func(hero_name, amount, party):
    if hero_name in party:
        if party[hero_name][1] + amount > 200:
            needed_mp = 200 - party[hero_name][1]
            party[hero_name][1] += needed_mp
            print(f"{hero_name} recharged for {needed_mp} MP!")
        else:
            party[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    return party


def heal_func(hero_name, amount, party):
    if hero_name in party:
        if party[hero_name][0] + amount > 100:
            needed_hp = 100 - party[hero_name][0]
            party[hero_name][0] += needed_hp
            print(f"{hero_name} healed for {needed_hp} HP!")
        else:
            party[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")

    return party


def print_function(party):
    print_result = ''

    for hero in party:
        print_result += f"{hero}\n  HP: {party[hero][0]}\n  MP: {party[hero][1]}\n"

    return print_result


def heroes_of_code(number):
    party = {}
    party_func(number, party)

    while True:

        command = input().split(' - ')

        if command[0] == 'End':
            print(print_function(party))
            break

        current_command = command[0]
        hero_name = command[1]

        if current_command == 'CastSpell':
            mp_needed = int(command[2])
            spell_name = command[3]
            castspell_func(mp_needed, spell_name, hero_name, party)

        elif current_command == 'TakeDamage':
            damage = int(command[2])
            attacker = command[3]
            takedamage_func(hero_name, damage, attacker, party)

        elif current_command == 'Recharge':
            amount = int(command[2])
            recharge_func(hero_name, amount, party)

        elif current_command == 'Heal':
            amount = int(command[2])
            heal_func(hero_name, amount, party)


number = int(input())
heroes_of_code(number)
