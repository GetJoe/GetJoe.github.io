import requests
from sys import argv
from bs4 import BeautifulSoup

states = ["US-AL", "US-AK", "US-AZ", "US-AR", "US-CA", "US-CO", "US-CT", "US-DC", "US-DE", "US-FL", "US-GA", 
          "US-HI", "US-ID", "US-IL", "US-IN", "US-IA", "US-KS", "US-KY", "US-LA", "US-ME", "US-MD", 
          "US-MA", "US-MI", "US-MN", "US-MS", "US-MO", "US-MT", "US-NE", "US-NV", "US-NH", "US-NJ", 
          "US-NM", "US-NY", "US-NC", "US-ND", "US-OH", "US-OK", "US-OR", "US-PA", "US-RI", "US-SC", 
          "US-SD", "US-TN", "US-TX", "US-UT", "US-VT", "US-VA", "US-WA", "US-WV", "US-WI", "US-WY"]

"""
states = ["US-GA", "US-KS", "US-MO"] 
"""


#regardless of job searched or location, url will always have same structure
#adding in tokens to make compiling the query string easier
#Needs to use a long advancedsearch so we ensure we only get jobs in the state we specify and not jobs from nearby states as well
standardURL = "https://www.indeed.com/jobs?as_and=JOBTITLE&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=0&l=LOCATION&fromage=any&limit=10&sort=&psf=advsrch&from=advancedsearch"



#Use all the query strings to scrape the indeed website and match each state with the total number of jobs
#IN: an empty totalJobsDictionary that will store the result & a dictionary for each    
def obtainTotalJobs(totalJobsDictionary, queryDictionary):
    for x in queryDictionary:
        #obtain query string from queryDictionary for each state and perform a GET request to indeed server
        result = requests.get(queryDictionary[x])
        print(result.status_code)
        
        #get the pagesource and create a BeautifulSoup datastructure
        soup = BeautifulSoup(result.content, 'html.parser')
        
        #Indeed stores the total number of jobs from a query in a div with id searchCountPages
        #This div is always of the form "Page 1 of x Jobs" where x is the total number of jobs for that query
        #Because its a string seperated by spaces we can split it and easily extract the total jobs
        
        totalJobsDiv = soup.find_all(id="searchCountPages")
        
        #if the state has 0 jobs we have to account for the fact that the div is empty
        if not totalJobsDiv:
            totalJobsDictionary[x] = 0
        else:  
            totalJobsArray = totalJobsDiv[0].text.split()
            #indeed uses a ',' when numbers exceed 1,000 so we have to account for that.
            totalJobs = totalJobsArray[3].replace(',', '')
            
            #after the total amount of jobs for that state has been isolated, pair it with the state in a dictionary
            totalJobsDictionary[x] = int(totalJobs)
        
    return totalJobsDictionary
    
#Scrape the Indeed.com jobsite to get an idea of how many of requested job is in each state
#IN: Desired Job to Search
#OUT: Dictionary mapping each state to the total number of jobs in that state
def scrapeIndeed(jobTitleSearch):
    jobTitle = jobTitleSearch
    jobTitleQuery = jobTitle.replace(' ', '+')

    #create a dictionary to store each state with their respective query string
    queryDictionary = {}
    createFinalQuery(queryDictionary, jobTitleQuery)
    
    #create a second dictionary that stores each state with the total amount of specified job in that state
    #specified job was obtained earlier by user input
    #total number of jobs will be obtained by querying indeed's server with the compiled query string
    totalJobsDictionary = {}
    obtainTotalJobs(totalJobsDictionary, queryDictionary)
    return totalJobsDictionary
    
def createFinalQuery(queryDictionary, jobTitleQuery): 
    #loop through all the states and create the final query string by adding in the state abbreviation
    #then pair each state abbreviation with its query string
    urlWithJobTitle = standardURL.replace("JOBTITLE", jobTitleQuery)
    for i in range(len(states)):
        completedURL = urlWithJobTitle.replace("LOCATION", states[i][3:])
        queryDictionary[states[i]] = completedURL
        
    return queryDictionary

#if __name__ == '__main__':
    #scrapeIndeed('Park Ranger')

