def create_label_map(file, labels):

    try:
        with open(file, 'w') as f:
            for label in labels:
                f.write('item { \n')
                f.write('\tname:\'{}\'\n'.format(label['name']))
                f.write('\tid:{}\n'.format(label['id']))
                f.write('}\n')
        
        print("Label map successfully created")
    
    except:
        print("Error creating the label map")
