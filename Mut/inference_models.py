# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:41:38 2020

@author: xugang

"""

from Mut.my_model import Model

#============================Parameters====================================
params = {}
params["d_input"] = 41 + 1 + 128 + 512
params["1d_input"] = 41 + 1
params["d_rota_output"] = 8
params["dropout_rate"] = 0.25
  
#parameters of transfomer model
params["transfomer_layers"] = 2
params["transfomer_num_heads"] = 1

#parameters of birnn model
params["lstm_layers"] = 4
params["lstm_units"] = 1024

#============================Models====================================

model_rota1 = Model(params=params, name="rota4p1")
model_rota1.params["save_path"] = "./Mut/models/1"
model_rota1.load_model()  

model_rota2 = Model(params=params, name="rota4p1")
model_rota2.params["save_path"] = "./Mut/models/2"
model_rota2.load_model()  

model_rota3 = Model(params=params, name="rota4p2")
model_rota3.params["save_path"] = "./Mut/models/3"
model_rota3.load_model()  

model_rota4 = Model(params=params, name="rota4p2")
model_rota4.params["save_path"] = "./Mut/models/4"
model_rota4.load_model()  

model_rota5 = Model(params=params, name="rota4p3")
model_rota5.params["save_path"] = "./Mut/models/5"
model_rota5.load_model()  

def test_infer_step(x, x_trr):
    
    rota_predictions = []
    rmsd_predictions = []
    
    rota_prediction, rmsd_prediction = model_rota1(x, x_trr, training=False)        
    rota_predictions.append(rota_prediction)
    rmsd_predictions.append(rmsd_prediction)

    rota_prediction, rmsd_prediction = model_rota2(x, x_trr, training=False)        
    rota_predictions.append(rota_prediction)
    rmsd_predictions.append(rmsd_prediction)

    rota_prediction, rmsd_prediction = model_rota3(x, x_trr, training=False)        
    rota_predictions.append(rota_prediction)
    rmsd_predictions.append(rmsd_prediction)

    rota_prediction, rmsd_prediction = model_rota4(x, x_trr, training=False)        
    rota_predictions.append(rota_prediction)
    rmsd_predictions.append(rmsd_prediction)

    rota_prediction, rmsd_prediction = model_rota5(x, x_trr, training=False)        
    rota_predictions.append(rota_prediction)
    rmsd_predictions.append(rmsd_prediction)

    return rota_predictions, rmsd_predictions