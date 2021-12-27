# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:41:38 2020

@author: xugang

"""
import os

def triResname(AA):
    if(len(AA) == 3):
        return AA
    else:
        if(AA == "G"):
            return "GLY"
        elif(AA == "A"):
            return "ALA"
        elif(AA == "S"):
            return "SER"
        elif(AA == "C"):
            return "CYS"
        elif(AA == "V"):
            return "VAL"
        elif(AA == "I"):
            return "ILE"
        elif(AA == "L"):
            return "LEU"
        elif(AA == "T"):
            return "THR"
        elif(AA == "R"):
            return "ARG"
        elif(AA == "K"):
            return "LYS"
        elif(AA == "D"):
            return "ASP"
        elif(AA == "E"):
            return "GLU"
        elif(AA == "N"):
            return "ASN"
        elif(AA == "Q"):
            return "GLN"
        elif(AA == "M"):
            return "MET"
        elif(AA == "H"):
            return "HIS"
        elif(AA == "P"):
            return "PRO"
        elif(AA == "F"):
            return "PHE"
        elif(AA == "Y"):
            return "TYR"
        elif(AA == "W"):
            return "TRP"
        else:
            print ("ResidueInfo.triResname() false" + AA)
            
def mutPDB(filename, ori, resid, mut):
    f = open(filename,'r')
    atomsDatas = []
    for line in f.readlines():   
        if (line == "" or line == "\n" or line[:3] == "TER"):
            break
        else:
            if (line[:4] == 'ATOM' or line[:6] == 'HETATM'):

                name1 = line[11:16].strip()
                
                res_id = line[22:27].strip()
                if res_id == resid:

                    resname = line[16:20]
                    assert resname.strip() == ori
                    resname_mut = resname[0] + mut
                    line = line[:16] + resname_mut + line[20:]
                    
                if(name1 in ["N","CA","C","O"]):
                    atomsDatas.append(line.strip())
    f.close()
    return atomsDatas

def cleanPDB(filename):
    f = open(filename,'r')
    atomsDatas = []
    for line in f.readlines():   
        if (line == "" or line == "\n" or line[:3] == "TER"):
            break
        else:
            if (line[:4] == 'ATOM' or line[:6] == 'HETATM'):

                name1 = line[11:16].strip()
                    
                if(name1 in ["N","CA","C","O"]):
                    atomsDatas.append(line.strip())
    f.close()
    return atomsDatas

native_filepath = "./3phv.pdb"
output_path = "./"

filename = native_filepath.strip().split('/')[-1].split('.')[0]

atomsData = cleanPDB(os.path.join(output_path, filename+'.pdb')) 
f = open(os.path.join(output_path, filename + ".native_bb"), 'w')
for i in atomsData:
    f.writelines(i + "\n")
f.close()

mutations = ["P9Y", "V82I", "V82G", "I84N", "L90R"]

for mutation in mutations:
    
    ori = triResname(mutation[0])
    resid = mutation[1:-1]
    mut = triResname(mutation[-1])
    
    atomsData = mutPDB(native_filepath, ori, resid, mut) 
    f = open(os.path.join(output_path, filename + "_" + mutation + ".bb"), 'w')
    for i in atomsData:
        f.writelines(i + "\n")
    f.close()