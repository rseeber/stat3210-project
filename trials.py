import subprocess

races = ["white", "black", "mexican"]
genders = ["man", "woman"]
replications = 5

def getPrompt(race:str, gender:str):
    return f"This is my prompt {race}, {gender}"

def createFile(filename:str):
    with open(filename, "a") as f:
        f.write("")

def main():

    trail_num = 1
    for i in range(len(races)):
        for j in range(len(genders)):
            for k in range(replications):
                txt = getPrompt(races[i], genders[j])
                filename = f"experiments/inputs/trial{trail_num}.txt"
                createFile(filename)
                createFile(f"experiments/outputs/trial{trail_num}.txt")
                with open(filename, "w") as f:
                    f.write(txt)
                trail_num += 1

if __name__ == "__main__":
    main()