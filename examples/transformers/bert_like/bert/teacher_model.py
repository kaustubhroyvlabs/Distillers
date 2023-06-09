#%%
from __init__ import *
from transformers import BertConfig, BertModel
from configparser import ConfigParser

parser = ConfigParser()
parser.read('teacher_config.cfg')

config = {}
config['num_hidden_layers'] = int(parser['TEACHER_CONFIG']['num_hidden_layers'])
config['num_attention_heads'] = int(parser['TEACHER_CONFIG']['num_attention_heads'])
config['hidden_size'] = int(parser['TEACHER_CONFIG']['hidden_size'])
config['intermediate_size'] = int(parser['TEACHER_CONFIG']['intermediate_size'])

TEACHER_CONFIG = BertConfig(**config)
# %%
class TeacherModel(BertModel):
    def __init__(self, config) -> None:
        super().__init__()
        self.bert = BertModel(config)
        
    def forward(self, input):
        return self.bert(**input, output_attentions=True, output_hidden_states=True)

TEACHER_MODEL = TeacherModel(TEACHER_CONFIG)