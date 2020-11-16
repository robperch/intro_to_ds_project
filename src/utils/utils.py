## MODULE WITH FUNCTIONS TO SAVE AND LOAD PICKLE, AS WELL AS OTHER USEFULL FUNCTIONS.





"------------------------------------------------------------------------------"
#############
## Imports ##
#############

import json





"------------------------------------------------------------------------------"
##############################
## Data profiling functions ##
##############################


## Pretty print a dictionary and preserving special characters
def json_dump_dict(dictionary):
    """
    Pretty print a dictionary and preserving special characters
        args:
            dictionary (dictionary): dict that will be pretty printed
        returns:
            -
    """

    print(json.dumps(dictionary, indent=4, ensure_ascii=False).encode("utf8").decode())

    return





"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
