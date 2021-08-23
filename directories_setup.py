import os

def create_directories(PROJECT_NAME, CUSTOM_MODEL_NAME):
  
  # project environment set-up
  paths = {
    # directories
    'WORKSPACE_PATH': os.path.join('TensorFlow', 'workspace'),
    'PROJECT_PATH': os.path.join('TensorFlow', 'workspace', PROJECT_NAME),
    'APIMODEL_PATH': os.path.join('TensorFlow', 'models'),
    'PROTOC_PATH': os.path.join('TensorFlow', 'prerequisites', 'protoc'),
    'SCRIPTS_PATH': os.path.join('TensorFlow', 'scripts'),
    'ANNOTATIONS_PATH': os.path.join('TensorFlow', 'workspace', PROJECT_NAME, 'annotations'),
   
    # model information
    'PRETRAINED_MODEL_PATH': os.path.join('TensorFlow', 'workspace', PROJECT_NAME, 'pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('TensorFlow', 'workspace', PROJECT_NAME, 'models', CUSTOM_MODEL_NAME),
    'EXPORT_PATH': os.path.join('TensorFlow', 'workspace', PROJECT_NAME, 'exported_models')
  }
  
  files = {
    'PIPELINE_CONFIG': os.path.join('TensorFlow', 'workspace', PROJECT_NAME, 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'LABELMAP': os.path.join('TensorFlow', 'workspace', PROJECT_NAME, 'annotations', 'label_map.pbtxt'),
    'TRAIN_SCRIPT': os.path.join('TensorFlow', 'models', 'research', 'object_detection', 'model_main_tf2.py'),
    'EXPORT_SCRIPT': os.path.join('TensorFlow', 'models', 'research', 'object_detection', 'exporter_main_v2.py'),
    'CHECKPOINT': os.path.join('TensorFlow', 'workspace', PROJECT_NAME, 'models', CUSTOM_MODEL_NAME, 'checkpoint')
  }
 
  try:
    for path in paths.values():
      os.makedirs(path, exist_ok=True)

    print("Successfully created environment directories")
    return paths, files

  except:
    print("Error creating the environment directories")
