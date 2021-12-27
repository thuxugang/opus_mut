# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:41:38 2020

@author: xugang

"""

import os
import tensorflow as tf
from Mut.my_transformer import Transformer
from Mut.my_rnn import BiRNN_Rota, MLP
from Mut.my_cnn import ResNet
from Mut.my_cnn2 import TRRosettaCNN_ATT

class Model(tf.keras.Model):
    
    def __init__(self, params, name):
        super(Model, self).__init__()
        
        self.params = params
        self.model_name = name
        
        self.transformer = Transformer(num_layers=self.params["transfomer_layers"],
                                       d_model=self.params["d_input"],
                                       num_heads=self.params["transfomer_num_heads"],
                                       rate=self.params["dropout_rate"])

        self.cnn = ResNet()
        self.mlp = MLP(num_layers=512,
                       rate=0.5)
        
        self.trr_cnn = TRRosettaCNN_ATT(filter_num=128, 
                                        num_layers=32, 
                                        dropout=0.5)

        self.birnn = BiRNN_Rota(num_layers=self.params["lstm_layers"],
                              units=self.params["lstm_units"],
                              rate=self.params["dropout_rate"],
                              rota_output=self.params["d_rota_output"])
        print ("use rota model...")
        
        self.fc_rmsd = tf.keras.layers.Dense(20)

    def call(self, x, x_trr, training=False):

        x_trr = self.trr_cnn(x_trr, training=training)
        
        x_1d = x[:,:,:42]
        assert x_1d.shape[-1] == 42
        
        x_3d_cnn = x[:,:,42:]
        assert x_3d_cnn.shape[-1] == 13500
        
        x_3d_cnn = self.mlp(x_3d_cnn, training=training)
        
        x = tf.concat([x_1d, x_3d_cnn, x_trr], -1)
        rota_feat1 = x

        transformer_out = self.transformer(x, encoder_padding_mask=None, training=training)
        cnn_out = self.cnn(x, training=training)
        x = tf.concat((x, cnn_out, transformer_out), -1)
        rota_feat2 = x
        
        rota_predictions, rota_feat3 = \
            self.birnn(x, training=training) 
        
        if self.model_name == "rota4p1":
            logit_rmsd = self.fc_rmsd(tf.concat((rota_feat2),-1))
        elif self.model_name == "rota4p2":
            logit_rmsd = self.fc_rmsd(tf.concat((rota_feat1),-1))
        else:
            logit_rmsd = self.fc_rmsd(tf.concat((rota_feat1, rota_feat2),-1))
            
        output_rmsd = tf.cast(tf.argmax(logit_rmsd, -1, ), tf.float32)*0.05
        output_rmsd = tf.expand_dims(output_rmsd, -1)

        rota_predictions = tf.squeeze(rota_predictions, 0)
        output_rmsd = tf.squeeze(output_rmsd, 0)
        
        return rota_predictions, output_rmsd
                
    def load_model(self):
        print ("load model:", self.model_name)
        self.load_weights(os.path.join(self.params["save_path"], 'rota_model_weight'))





