import os

def create_directories(PROJECT_NAME, CUSTOM_MODEL_NAME):
  
  # project environment set-up
  paths = {
    # directories
    WORKSPACE_PATH: os.path.join('TensorFlow', 'workspace'),
    PROJECT_PATH: os.path.join(WORKSPACE_PATH, PROJECT_NAME),
    APIMODEL_PATH: os.path.join('TensorFlow','models'),
    PROTOC_PATH: os.path.join('TensorFlow', 'prerequisites', 'protoc'),
    SCRIPTS_PATH: os.path.join('TensorFlow', 'scripts'),
    ANNOTATIONS_PATH: os.path.join(PROJECT_PATH, 'annotations'),
   
    # model information
    PRETRAINED_MODEL_PATH: os.path.join(PROJECT_PATH, 'pre-trained-models'),
    LABELMAP: os.path.join(PROJECT_PATH, 'annotations', 'label_map.pbtxt'),
    CHECKPOINT_PATH: os.path.join(PROJECT_PATH, 'models', CUSTOM_MODEL_NAME),
    PIPELINE_CONFIG: os.path.join(PROJECT_PATH, 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    EXPORT_PATH: os.path.join(PROJECT_PATH, 'exported_models')
  }
 
  try:
    for path in paths.values():
      os.makedirs(path, exist_ok=True)

    print("Successfully created environment directories")
    return paths

  except:
    print("Error creating the environment directories")
