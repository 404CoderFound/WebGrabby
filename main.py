from pywebcopy import save_website
from pywebcopy import save_webpage
print("""
 _       __     __    ______           __    __         
| |     / /__  / /_  / ____/________ _/ /_  / /_  __  __
| | /| / / _ \/ __ \/ / __/ ___/ __ `/ __ \/ __ \/ / / /
| |/ |/ /  __/ /_/ / /_/ / /  / /_/ / /_/ / /_/ / /_/ / 
|__/|__/\___/_.___/\____/_/   \__,_/_.___/_.___/\__, /  
                                               /____/   """)


input1 = input("Do u want a single page or a full copy? (single, full (full not recommended could overload the target server) ): ")
if input1 == "single":
  input_url = input("what webpage do u want to copy? (ex. https://youtube.com/): ")
  input_folder = input("Where do u wanna store this scan? ")
  input_project_name = input("What do u want the project name to be? ")
  open_in_browser = input("Do u want the website opening in browser when its done? (True or False): ")
  save_webpage(
      url=input_url,
      project_folder=input_folder,
      project_name=input_project_name,
      bypass_robots=True,
      debug=True,
      open_in_browser=open_in_browser,
      delay=None,
      threaded=False,
  )


if input1 == "full":
  input_url = input("what webpage do u want to copy? (ex. https://youtube.com/): ")
  input_folder = input("Where do u wanna store this scan? ")
  input_project_name = input("What do u want the project name to be? ")
  open_in_browser = input("Do u want the website opening in browser when its done? (True or False): ")
  save_website(
  url=input_url,
  project_folder=input_folder,
  project_name=input_project_name,
  bypass_robots=True,
  debug=True,
  open_in_browser=open_in_browser,
  delay=None,
  threaded=False,
  )



