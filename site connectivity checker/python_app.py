#import urllib
#use urllib.request to get the data from the url
#write a function that takes a url
#returns a response


import urllib.request as urllib

def main(url):
    print("Checking connectivity ")
    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("the responde code was: ", response.getcode())

print("this is a connectivity checker program")
input_url = "www.gmail.com"
main(input_url)
