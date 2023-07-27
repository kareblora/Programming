import sys
import getopt

def get_name():
    first_name = None
    last_name = None
    
    argv = sys.argv[1:]
    #print(argv)
    
    try:
        opts, args = getopt.getopt(argv, "f:l:", ["first_name=", "last_name="])
        
    except getopt.GetoptError as error:
        print(error)
        opts = []
    
    print(opts)
    print(args)
    
    
    for opt,arg in opts:
        if opt in ["-f","--first_name"]:
            first_name = arg
        elif opt in ["-l", "--last_name"]:
            last_name = arg
    
    print("First Name: {}".format(first_name))
    print("Last Name: {}".format(last_name))

get_name()


    