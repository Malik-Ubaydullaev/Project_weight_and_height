from read_data import read_csv_data

def get_data(data):
    """
    Get data from list.
    Gender: Change Male to 0 and Female to 1
    Weight: Place the column in the Kg view given in Pound (1 kg = 2,205 pound).
    Height: Place the column on the list in the cm view given in inches (2.54 cm = 1 inch).
    Args:
        data(list): data split row
    Returns:
        tuple: gender, weight and height

    """
    gender = []
    weight = []
    height = []
    
    # WRITE YOUR CODE HERE
    #print(data)
    #print(data[0].values())
    
    val = []
    i = 0
    while i < len(data):
        for val in data[i].values():
            if val == 'Male':
                gender.append(0)
            elif val == 'Female':
                gender.append(1)
        
        for k in data[i].keys():
            if k == 'Height':
                height.append(data[i][k])
            if k == 'Weight':
                weight.append(data[i][k])
                    
        i+=1    

    
    return gender,weight,height

data=read_csv_data('data/weight-height.csv');
get_data(data)