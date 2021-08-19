import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import pipeline_pb2

def read_config(PIPELINE_CONFIG):
  pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
  with tf.io.gfile.GFile(PIPELINE_CONFIG, "r") as f:
    proto_str = f.read()
    text_format.Merge(proto_str, pipeline_config)
  return pipeline_config

def write_config(PIPELINE_CONFIG, pipeline_config):
    config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
    with tf.io.gfile.GFile(PIPELINE_CONFIG, "wb") as f:                                                                                                                                                                                                                       
        f.write(config_text)