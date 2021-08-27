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
        
def modify_config(PIPELINE_CONFIG, labels, TRAIN_BATCH_SIZE, paths, files):
  pipeline_config = read_config(PIPELINE_CONFIG)

  # pipeline configuration settings
  pipeline_config.model.ssd.num_classes = len(labels)
  pipeline_config.train_config.batch_size = TRAIN_BATCH_SIZE
  pipeline_config.eval_config.batch_size = 1
  pipeline_config.train_config.fine_tune_checkpoint = os.path.join(paths['PRETRAINED_MODEL_PATH'], PRETRAINED_MODEL_NAME, 'checkpoint', 'ckpt-0')
  pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
  pipeline_config.train_input_reader.label_map_path= files['LABELMAP']
  pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [os.path.join(paths['ANNOTATIONS_PATH'], 'train.record')]
  pipeline_config.eval_input_reader[0].label_map_path = files['LABELMAP']
  pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [os.path.join(paths['ANNOTATIONS_PATH'], 'test.record')]

  write_config(PIPELINE_CONFIG, pipeline_config)
