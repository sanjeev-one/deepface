
#Import libraries
import os
import concurrent.futures
from re import search
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable





def worker_thread(search_key):
    image_scraper = GoogleImageScraper(
        webdriver_path, 
        image_path, 
        search_key, 
        number_of_images, 
        headless, 
        min_resolution, 
        max_resolution, 
        max_missed)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, keep_filenames)

    #Release resources
    del image_scraper

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))


    search_keys = [
    "Tushar Gupta",
    "Sarthak Srinivas",
    "Wael Abid",
    "Vaibhav Chhajed",
    "Adib Shakib",
    "Arnav Aghav",
    "Charlene Wang",
    "Devica Verma",
    "Dominic Damoah",
    "Eric Wang",
    "Harsh Varshney",
    "Haya Elmizwghi",
    "John Joseph",
    "Kanan Mehdizade",
    "Kyiana Williams",
    "Luke Blommesteyn",
    "Mukul Garg",
    "Paras Savnani",
    "Phani Munipalli",
    "Punn Kam",
    "Rohan Deshpande",
    "Sai Vuppalapati",
    "Saurav Bhattacharya",
    "Shahab Mousavi",
    "Sivarasu Subbaiyan",
    "Will Blair",
    "Xavier Verdu",
    "Ventura",
    "Abhay Paroha",
    "Albert Lai",
    "Amit Bihari",
    "Ana Han",
    "Ankit Virmani",
    "Arpit Chaudhary",
    "Arpita Goyal",
    "Atharva Amdekar",
    "Cat Wu",
    "David Okao",
    "Eli Reinhardt",
    "Gautam Madaan",
    "HarshaVardhan Mudumba Venkata",
    "Hassan Peer",
    "Jatin Gupta",
    "Josh",
    "Keerti Bishnoi",
    "Khushpreet Sohi",
    "Kumar Abhirup",
    "Lia Tian",
    "Mac Klinkachorn",
    "Mark Rachapoom",
    "Marvin von Hagen",
    "Muthhukumar Malaiiyyappan",
    "Navdeep Malik",
    "Nemo Shi",
    "Nick Goodson",
    "Perrin Myerson",
    "Philipp Zagar",
    "Pierre Arys",
    "Prakhar Agarwal",
    "Preetham Vemasani",
    "Priyanka Pande",
    "Raakesh Premkumar",
    "Rajat Goel",
    "Rugved Hattekar",
    "Saarth Shah",
    "Sahil Dhansinghani",
    "Sai Srinivas Somarouthu",
    "Sandeep R",
    "Sandesh Manik",
    "Sheikh Srijon",
    "Sid Bendre",
    "Siddhant Raman",
    "Sudomarith Chin (zero2sudo)",
    "Tejaswi Agarwal",
    "Tinah Hong",
    "Tunay Gur",
    "Tushar Dogra",
    "Vamshi Enabothala",
    "Vamsi Krishna Cheekatimalla",
    "Vineet Sood",
    "William Hou",
    "Yatharth Agarwal",
    "Zhuyuan He",
    "Shah",
    "Ansh Mehra",
    "Girri Palaniyapan",
    "Krish",
    "Krishna",
    "Sai Tarun K",
    "Sriram"
]

   
    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    #search_keys = list(set(["cat","t-shirt"]))
    print(search_keys[:5])
    #Parameters
    number_of_images = 3                # Desired number of images
    headless = True                     # True = No Chrome GUI
    min_resolution = (0, 0)             # Minimum desired image resolution
    max_resolution = (9999, 9999)       # Maximum desired image resolution
    max_missed = 10                     # Max number of failed images before exit
    number_of_workers = 40               # Number of "workers" used
    keep_filenames = False              # Keep original URL image filenames

    #Run each search_key in a separate thread
    #Automatically waits for all threads to finish
    #Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)
