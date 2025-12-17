


from dotenv import load_dotenv
import os



'''
** Create a .env file and enter your paths and credentials like this: **
SECRET_FILE=H:\secrets\bcgw.env
TOOLBOX=\\somecrazyasspath\to\my\toolbox.tbx
'''


###############################################################################################################################################################
#
# Calling file paths
#
###############################################################################################################################################################


# Load the default environment
print("Test Dotenv: Loading .env file...")

# load_dotenv() (with no arguments) loads .env from the current working directory so if you run the script from a different folder it might not find it.
load_dotenv()


# Tell dotenv to get the variable SDE_FILE_PATH from the .env file and assign it to a variable
sde_path = os.getenv("SDE_FILE_PATH")

# or get a toolbox
arcpro_toolbox = os.getenv("TOOLBOX")

# Print to test
print(f"The toolbox is: {arcpro_toolbox}")


###############################################################################################################################################################
#
# Accessing Credentials
#
###############################################################################################################################################################


# Load the file path to your secrets file into a variable. At this point it is still just a path
secret_file = os.getenv("SECRET_FILE")

# A little bit of error handling
if not secret_file:
    raise RuntimeError("SECRET_FILE is not set. Check your project .env.")

# The path to the secret file is loaded into the load_dotenv function and dotenv opens the .env in that path and loads 
# the dictionary that contains the username and password into environment variables
# Different from when we called file paths that were sitting in a .env file alongside the rest of the script

load_dotenv(secret_file)

# Now you can use getenv to access to your username and password and set those to variables to be used in a database connection

db_user   = os.getenv("BCGW_USER")
db_pass   = os.getenv("BCGW_PASS")

# Print to test
print("Username is:", db_user)

print("Have DB access? :", bool(db_user and db_pass))









    