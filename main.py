
mass = int(input('Введите свой вес'))
height = int(input('Введите свой рост'))
steps = int(input('Введите количсетво пройденных шагов'))
time = int(input('Введите время активности'))


def countSteps (mass, height, steps):
    step_distance = height / 4 + 0.37
    distance = step_distance * steps
    speed = distance / time

    energySpend = 0.035 * mass + ((speed**2)/height) * 0.029 * mass
    if distance <= 2000:
        support_text = print("Ты можешь больше!")
    elif 2000 < distance <= 4000:
        support_text = print("У тебя не плохо получается!")
    elif distance >= 4000:
        support_text = print("Отличный результат!")
    return energySpend, distance


print(f"Калории и шаги:{countSteps(mass, height, steps)}")
