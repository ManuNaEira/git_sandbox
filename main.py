"""
Created on Apr 2023
@author: Alice
@mail to: alice@com
Brief:

"""
import argparse
import logging

def main(args):
    """ Main function
    Args:
        args (namespace): Command line arguments. Fields:
    """
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%H:%M:%S', level=logging.getLevelName(args.v))
    

if __name__ == "__main__":
    # Handle command line arguments with argparse
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", help="Logging verbose as per the Python Logging "
        "module. Default: %(default)s", default='INFO',
        choices=list(logging._levelToName.values())[:-1])
    
    args = parser.parse_args()
    # Launch main function if arguments passed are ok
    main(args)