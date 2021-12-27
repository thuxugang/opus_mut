# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:41:48 2016

@author: XuGang
"""

import os
import numpy as np

if __name__ == "__main__":
    
    pdb_lists = []
    f = open(r'./bb_list', 'r')
    for i in f.readlines():
        pdb_lists.append(i.strip().split('/')[-1].split('.')[0])
    f.close()
    print (len(pdb_lists))
    
    ori_name = "3phv"
    fasta_len = 99
    predict_path = "./predictions"
    for filename in pdb_lists:
    
        print (filename)
        
        results_native = []
        count = 0
        f = open(os.path.join(predict_path, ori_name + ".mut"))
        for i in f.readlines():
            if i[0] == '#': continue
        
            key = i.strip().split()[1]
            x1_4 = i.strip().split()[2:6]
            assert len(x1_4) == 4
            rmsd = i.strip().split()[6]
            results_native.append([key, [float(j) for j in x1_4], float(rmsd)])
            count += 1
        f.close()      
        assert count == fasta_len
       
        results_predict = []
        count = 0
        f = open(os.path.join(predict_path, filename + ".mut"))
        for i in f.readlines():
            if i[0] == '#': continue
            
            key = i.strip().split()[1]
            x1_4 = i.strip().split()[2:6]
            assert len(x1_4) == 4
            rmsd = i.strip().split()[6]
            results_predict.append([key, [float(j) for j in x1_4], float(rmsd)])
            count += 1
        f.close()      
        assert count == fasta_len
        
        assert len(results_native) == len(results_predict)
        
        change_rmsds = []
        changes = []
        ress = []
        for item_n, item_p in zip(results_native, results_predict):
            
            ress.append(item_p[0])
            
            if item_n[0] != item_p[0]: 
                changes.append(0)
                change_rmsds.append(item_p[2]-item_n[2])
                continue
        
            x1_4_n = item_n[1]
            x1_4_p = item_p[1]
            
            x1_4_n = [i for i in x1_4_n if i != 182]
            x1_4_p = [i for i in x1_4_p if i != 182]
            assert len(x1_4_n) == len(x1_4_p)
            
            rmsd_n = item_n[2]
            rmsd_p = item_p[2]
            change_rmsd = np.abs(rmsd_n-rmsd_p)
            change_rmsds.append(change_rmsd)
            
            x1_4_n = np.array(x1_4_n)
            x1_4_p = np.array(x1_4_p)
            
            diff = x1_4_n - x1_4_p
            diff[np.where(diff<-180)] += 360
            diff[np.where(diff>180)] -= 360
            mae = np.abs(diff)        
            
            if len(x1_4_n) == 0:
                change = 0
            else:
                change = np.mean(mae)
            changes.append(change)
                
        output_path = os.path.join(predict_path, filename+".changes")
        f = open(output_path, 'w')
        f.write("#\tRES\tDi\tRMSD\n")
        for idx, (res_name, change, rmsd) in enumerate(zip(ress, changes, change_rmsds)):
            f.write('%i\t%s\t%3.2f\t%3.2f\n'%(idx+1, res_name, change, rmsd))
        f.close()
        
    f = open(os.path.join(predict_path, ori_name + ".changes"))
    fasta = ""
    for i in f.readlines():
        if i[0] == "#": continue
        resid, resname = i.strip().split()[:2]
        fasta += resname
    f.close()
    assert len(fasta) == fasta_len
    print (fasta, len(fasta))

    for filename in pdb_lists:
        if filename == "3phv": continue
    
        position = filename.split("_")[-1][1:-1]
        mut = filename.split("_")[-1][-1]
        
        count = 0
        all_changes = 0
        f = open(os.path.join("./predictions", filename + ".changes"))
        for i in f.readlines():
            if i[0] == "#": continue
            count += 1
            resid, resname, di = i.strip().split()[:3]
            assert resid == str(count)
            if resid == position:
                assert mut == resname
            if not int(resid) in [25, 26, 27]: continue
        
            diff = float(di)
            
            # if diff < 1:
            #     diff = 0
            # elif diff < 5:
            #     diff = 1
            # elif diff < 10:
            #     diff = 2
            # elif diff < 20:
            #     diff = 3
            # else:
            #     diff = 4
            
            all_changes += diff
        f.close()
        print (filename, filename.split("_")[-1], all_changes)
