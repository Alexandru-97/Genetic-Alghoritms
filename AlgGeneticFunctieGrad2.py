import random



def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
    return key1

def log2n(n):
    return 1 + log2n(n / 2) if (n > 1) else 0

def fitnessFunction(num):
    sol = 0 - abs(num*num) + num + 2
    return (sol)

def crossoverFunc(ch1, ch2, cut):
    return ch1[:cut] + ch2[cut:]



with open ('output.txt', 'w') as f:
    population = 20
    lowerBound = -1
    upperBound = 2
    a = -1
    b = 1
    c = 2
    precision = 8
    crossover = 0.3
    mutation = 0.12
    steps = 100

    maxNum = float('-inf')
    maxIndex = -1
    maxChromosome = 0
    maxValue = 0
    currentPopulation = []
    chromosomes = []
    chromosomeLength = log2n((upperBound-lowerBound)*10**precision)


    for i in range (population):
        binValue = rand_key(chromosomeLength)
        aux = int(binValue, 2)
        val = aux * ((upperBound - lowerBound) / (2 ** chromosomeLength - chromosomeLength)) + lowerBound
        rounded = round(val, precision)
        currentPopulation.append(rounded)
        chromosomes.append(binValue)


    f.write("Populatia initiala\n\n")
    for i in range(population):
        f.write(str(i+1) + ": " + str(chromosomes[i]) + ", x = " + str(currentPopulation[i]) + ", f = " + str(fitnessFunction(currentPopulation[i])) + '\n')

    f.write('\n\n')
    for x in range(steps):

        fitness = []
        fitnessSum = 0
        for el in currentPopulation:
            val = fitnessFunction(el)
            fitness.append(val)
            fitnessSum += val


        probabilities = []

        if x==0:
            f.write("Probabilitati selectie\n\n")
        for i in range(population):
            probability = fitness[i] / fitnessSum
            probabilities.append(probability)
            if x == 0:
                f.write("Probabilitate cromozom ")
                f.write(str(i+1) + ": ")
                f.write(str(probability) + '\n')

        if x==0:
            f.write("\n\n")

        print(probabilities)
        probabilities.sort()

        if x == 0:
            f.write("Intervalele de probabilitate sunt:" + '\n')
            f.write('0 ')

        currentProbability = 0
        probabilityIntervals = []

        for i in range(population-1):
            currentProbability += probabilities[i]
            probabilityIntervals.append(currentProbability)
            if x == 0:
                f.write(str(currentProbability) + " ")

        probabilityIntervals.append(1)

        if x == 0:
            f.write('1'+ '\n')

        aux = [0 for i in range(population)]
        aux2 = [0 for i in range(population)]
        for i in range(population):
            uniform = random.uniform(0,1)
            if x == 0:
                f.write("u = " + str(uniform) + " ")
            for j in range(population):
                if probabilityIntervals[j] > uniform:
                    aux[i] = chromosomes[j]
                    aux2[i] = currentPopulation[j]
                    if x == 0:
                        f.write("Cromozomul ")
                        f.write(str(j+1))
                        f.write(" a fost ales")
                        break
            if x==0:
                f.write("\n")

        for i in range(population):
            chromosomes[i] = aux[i]
            currentPopulation[i] = aux2[i]

        if x == 0:
            f.write("\nDupa selectie\n")
            for i in range(population):                                                                                                                                          
                f.write(str(i+1) + ": " + str(chromosomes[i]) + ", x = " + str(currentPopulation[i]) + ", f = " + str(fitnessFunction(currentPopulation[i])) + '\n')
            f.write('\n\n')
            
        if x == 0:
            f.write("Probabilitate de incrucisare: ")
            f.write(str(crossover) + '\n\n')
        crossoverParticipants = []

        for i in range(population):
            uniform = random.uniform(0, 1)
            if x ==0:
                f.write("u = " + str(uniform))
            if uniform < crossover:
                crossoverParticipants.append(i)
                if x == 0:
                    f.write(" Cromozomul ")
                    f.write(str(i+1))
                    f.write(" participa")
            if x == 0:
                f.write('\n')

        if x==0:
            f.write('\n\n')
        if len(crossoverParticipants) % 2 != 0 :
            if len(crossoverParticipants) == 1:
                if x == 0:
                    f.write("Cromozomul" + str(crossoverParticipants[0]) + "e singurul participant")
            else:
                rand1 = random.choice(crossoverParticipants)
                crossoverParticipants.remove(rand1)
                rand2 = random.choice(crossoverParticipants)
                crossoverParticipants.remove(rand2)
                rand3 = random.choice(crossoverParticipants)
                crossoverParticipants.remove(rand3)
                cut = random.randint(0, chromosomeLength)
                sol1 = crossoverFunc(chromosomes[rand1], chromosomes[rand2], cut)
                if x == 0:
                    f.write("Crossover intre cromozomul " + str(rand1+1) + " si cromozomul " + str(rand2+1) + " taietura " + str(cut) + "\n")
                    f.write(str(chromosomes[rand1]) + " " + str(chromosomes[rand2]) + '\n')
                    f.write("Rezultat: " + str(sol1) +"\n")
                cut = random.randint(0, chromosomeLength)
                sol2 = crossoverFunc(chromosomes[rand2], chromosomes[rand3], cut)
                if x == 0:
                    f.write("Crossover intre cromozomul " + str(rand2+1) + " si cromozomul " + str(rand3+1) + " taietura " + str(cut) + "\n")
                    f.write(str(chromosomes[rand2]) + " " + str(chromosomes[rand3]) + '\n')
                    f.write("Rezultat:" + str(sol2)+ "\n")
                cut = random.randint(0, chromosomeLength)
                sol3 = crossoverFunc(chromosomes[rand3], chromosomes[rand1], cut)
                if x == 0:
                    f.write("Crossover intre cromozomul " + str(rand3+1) + " si cromozomul " + str(rand1+1) + " taietura " + str(cut) + "\n")
                    f.write(str(chromosomes[rand3]) + " " + str(chromosomes[rand1]) + '\n')
                    f.write("Rezultat: " + str(sol3)+ "\n")
                chromosomes[rand1] = sol1
                chromosomes[rand2] = sol2
                chromosomes[rand3] = sol3


        while crossoverParticipants:
            if len(crossoverParticipants) == 1:
                break
            else:
                rand1 = random.choice(crossoverParticipants)
                crossoverParticipants.remove(rand1)
                rand2 = random.choice(crossoverParticipants)
                crossoverParticipants.remove(rand2)
                cut = random.randint(0, chromosomeLength)
                cut2 = random.randint(0, chromosomeLength)
                sol = crossoverFunc(chromosomes[rand1], chromosomes[rand2], cut)
                sol2 = crossoverFunc(chromosomes[rand2], chromosomes[rand1], cut2)
                if x==0:
                    f.write("Crossover intre cromozomul " + str(rand1+1) + " si cromozomul " + str(rand2+1) + " taietura " + str(cut)+ "\n")
                    f.write(str(chromosomes[rand1]) + " " + str(chromosomes[rand2]) + '\n')
                chromosomes[rand1] = sol
                chromosomes[rand2] = sol2
                if x == 0:
                    f.write("Rezultat: " + str(sol) + " " + str(sol2)+ "\n")

        for i in range(population):
            aux = int(chromosomes[i], 2)
            val = aux * ((upperBound - lowerBound) / (2 ** chromosomeLength - chromosomeLength)) + lowerBound
            rounded = round(val, precision)
            currentPopulation[i] = rounded
        if x == 0:
            f.write('\n')
            f.write("Dupa crossover: \n")
            for i in range(population):
                f.write(str(i+1) + ": " + str(chromosomes[i]) + ", x = " + str(currentPopulation[i]) + ", f = " + str(fitnessFunction(currentPopulation[i])) + '\n')

        if x ==0:
            f.write('\n')
            f.write("Probabilitatea de mutatie pentru fiecare cromozom: " + str(mutation) + '\n')
        ok = 0
        for i in range(population):
            uniform = random.uniform(0, 1)
            if uniform <= mutation:
                randVar = random.randint(0, chromosomeLength-1)
                if x == 0:
                    f.write("Se modifica gena " + str(randVar+1) + " a cromozomului " + str(i+1) + '\n')
                if randVar == chromosomeLength:
                    if chromosomes[i][randVar] == '0':
                        chromosomes[i] = chromosomes[:-1] + '1'
                    else:
                        chromosomes[i] = chromosomes[:-1] + '0'
                else:
                    if chromosomes[i][randVar] == '0':
                        chromosomes[i] = chromosomes[i][:randVar] + '1' + chromosomes[i][(randVar+1):]
                    else:
                        chromosomes[i] = chromosomes[i][:randVar] + '0' + chromosomes[i][(randVar+1):]
                ok = 1

        if ok == 0 and x==0:
            f.write("Nu a fost modificat niciun cromozom.")
        elif x == 0:
            f.write("\nDupa mutatie\n")

        for i in range(population):
            aux = int(chromosomes[i], 2)
            val = aux * ((upperBound - lowerBound) / (2 ** chromosomeLength - chromosomeLength)) + lowerBound
            rounded = round(val, precision)
            currentPopulation[i] = rounded
            fitness[i] = fitnessFunction(rounded)
            if x == 0:
                f.write(str(i+1) + ": " + str(chromosomes[i]) + ", x = " + str(currentPopulation[i]) + ", f = " + str(fitnessFunction(currentPopulation[i])) + '\n')
        else:
            if maxNum > min(fitness):
                randVar = random.randint(0, population-1)
                currentPopulation[randVar] = maxValue
                chromosomes[randVar] = maxChromosome
                fitness[randVar] = maxNum
        maxNum = max(fitness)
        maxIndex = fitness.index(maxNum)
        maxValue = currentPopulation[maxIndex]
        maxChromosome = chromosomes[maxIndex]
        if x==0:
            f.write("\nEvolutia maximului(" + str(steps) +" de repetari):\n\n")
        f.write(str(maxNum) + "\n")


