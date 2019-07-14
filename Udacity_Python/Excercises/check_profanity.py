import urllib
def read_txt():
    quotes = open(r"/Users/archananagaraja/Desktop/AN_Personal/Udacity_Python/movies_quotes.txt")
    content_of_the_file = quotes.read()
    #print(content_of_the_file)
    check_profanity(content_of_the_file)
    quotes.close()

def check_profanity(text_to_check):
   # print(text_to_check)
    connection = urllib.urlopen("https://www.purgomalum.com/service/xml?text="+text_to_check)
    contents_of_url = connection.read()
    print(contents_of_url)
    connection.close()
    if "****" in contents_of_url:
        print("profanity alert")
    else:
        print("The file is a clean document with no curse words")  
read_txt()




