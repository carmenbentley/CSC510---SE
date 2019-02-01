from collections import defaultdict
import json
import requests

# --------------------------------------------------------------------------------------------------------------------------------------Task 1.1
# Lists the branches of an existing repository from GitHub
def list_branches( username, url, header ):

    # Title of Function/Task
    print( "\n\tTask 1 : List all Branches of an Existing Repository" )
    
    # Gather repo from user for which he/she wishes to list the branches
    repo = input( ( "\n\t\tPlease enter the repo belonging to '{}'\n\t\tfor which you would like to retrieve the branches : ").format( username ) )
    
    # Append appropriate URL depending on Github type
    url = url + "repos/" + username + "/" + repo + "/branches"

    # Make request
    r = requests.get( url, headers= header )

    # Print Results
    print( "\n\t\tReturn Code => {}".format( r ) )
    if r.status_code == 200 :
        json_Object = r.json()
        print( "\n\t\tNumber of branches in '{}' : {}".format( repo, len( json_Object ) ) )
        count = 1
        for x in range( len( json_Object ) ):
            print( "\t\t\tBranch #{} : {}".format( count,json_Object[ x ][ 'name' ] ) )
            count = count + 1
    else :
        print( "\n\t\tUnable to process the request *** BAD RETURN CODE ***" )
    
# --------------------------------------------------------------------------------------------------------------------------------------Task 1.2
# Creates a new private/public repository on GitHub
def create_repo( username, url, header ):

    # Title of Function/Task
    print( "\n\tTask 2 : Create a New Repository" )
    
    # Append appropriately to URL
    url = url + "user/repos"
    
    # Determine visibility of the repository
    print( "\n\t\tSet the visibility of your repo:" )
    print( "\t\t\tEnter 1 : Private Repository" )
    print( "\t\t\tEnter 2 : Public Repository" )
    visibility = 0
    private = True
    while True :
        visibility = int( input( "\n\t\tEnter your selection : " ) )
        if visibility > 0 and visibility < 3 :
            break;
        else : 
            print( "\t\t*** Invalid selection --> '{}' Must selection numbers 1 - 2 inclusive. ***\n".format( selection ) )
    if visibility != 1:
        private = False
    
    # Gather repo name and description
    repoName = input( "\n\t\tPlease enter the name of your new repository : " )
    repoDescription = input( "\t\tPlease enter a short description for your new repository : " )
    
    # Setup data param
    data = { 'name': repoName, 'private': private, 'description': repoDescription }
    
    # Make request
    r = requests.post( url, data= json.dumps( data ), headers= header )
    
    # Print Results
    print( "\n\t\tReturn Code => {}".format( r ) )
    if r.status_code == 201 :
        print( "\n\t\tNew Repository Created with the following attributes: " )
        print( "\t\t\tName        : {}".format( repoName ) )
        print( "\t\t\tVisibility  : Privacy is set to '{}'".format( private ) )
        print( "\t\t\tDescription : {}".format( repoDescription ) )
    else :
        print( "\n\t\tUnable to process the request *** BAD RETURN CODE ***" )
    
# --------------------------------------------------------------------------------------------------------------------------------------Task 1.3
# Creates a new issue in a repository on GitHub
def create_issue( username, url, header ):

    # Title of Function/Task
    print( "\n\tTask 3 : Create an Issue for and Existing Repisting Repository" )
    
    # Gather repo name, issue title, and issue body
    repo = input( "\n\t\tPlease enter the name of the repository for which you would like to create an issue : " )
    title = input( "\t\tPlease enter the title of your issue : " )
    body = input( "\t\tPlease enter a brief description of your issue : " )
    
    # Append appropriately to URL
    url = url + "repos/" + username + "/" + repo + "/issues"
    print(url)
    
    # Setup data param
    data = { 'title': title, 'body': body }
    
    # Make request
    r = requests.post( url, data= json.dumps( data ), headers= header )
    
    # Print Results
    print( "\n\t\tReturn Code => {}".format( r ) )
    if r.status_code == 201 :
        print( "\n\t\tNew Issue Created  in your Repo '{}' with the following attributes".format( repo ) )
        print( "\t\t\tTitle : {}".format( title ) )
        print( "\t\t\tbody  : {}".format( body ) )
    else :
        print( "\n\t\tUnable to process the request *** BAD RETURN CODE ***" )
    
# --------------------------------------------------------------------------------------------------------------------------------------Task 1.4
# Adds an assignee to a repository on GitHub
def add_assignee( username, url, header ):

    # Title of Function/Task
    print( "\n\tTask 4 : Add an Assignee to an Existing Issue" )
    
    # Gather repo name, issue number, and username of assignee
    repo = input( "\n\t\tPlease enter the name of the repository for which you would like to add an assignee : " )
    number = input( "\t\tPlease enter the identification number of the issue you would like to add an assignee : " )
    assignee = input( "\t\tPlease enter assignee name : " )
    
    # Check that user can be added as an assignee
    checkURL = url + "repos/" + username + "/" + repo + "/assignees/" + assignee
    r = requests.get( checkURL, headers= header )
    
    if r.status_code != 404 :
        # Username is valid and able to be added as an assignee to the requested issue/repo
        
        # Append appropriately to URL
        requestURL = url + "repos/" + username + "/" + repo + "/issues/" + str( number ) + "/assignees"
        
        # Setup data param
        data = { 'assignees': assignee }

        # Make add request
        r = requests.post( requestURL, data= json.dumps( data ), headers= header )
        
        # Print Results
        print( "\n\t\tReturn Code => {}".format( r ) )
        if r.status_code == 201 :
            print( "\n\t\t'{}' was added as an assignee to your issue. ".format( assignee ) )
        else :
            print( "\n\t\tUnable to process the request *** BAD RETURN CODE ***" )
    else :
        # Username is invalid or does not have permission to be added to this issue/repo
        print( "\n\t\t'{}' is either (1) not a valid username or\n\t\t(2)'{}' does not have permission to be assigned to this issue.".format( assignee, assignee ) )

# --------------------------------------------------------------------------------------------------------------------------------------Task 1.5
# Edits the contents of a repository on GitHub to disable issues
def edit_repo( username, url, header ):

    # Title of Function/Task
    print( "\n\tTask 5 : Edit a Repository to Disable Issues" )
    
    # Gather name of repo
    repo = input( "\n\t\tPlease enter the name of the Repository you would like to enable projects : " )

    # Append appropriately to URL
    requestURL = url + "repos/" + username + "/" + repo

    # Setup data param
    data = { 'has_issues': 'false', 'name': repo } # Must include name as a parameter per API

    # Make request
    r = requests.patch( requestURL, data= json.dumps(data), headers= header )
    
    # Print Results
    print( "\n\t\tReturn Code => {}".format( r ) )
    if r.status_code == 200 :
        print( "\n\t\t'{}' was udpated to disable issues. ".format( repo ) )
    else :
        print( "\n\t\tUnable to process the request *** BAD RETURN CODE ***" )

# --------------------------------------------------------------------------------------------------------------------------------------Task 1.6
# Lists the reactions for an issue of a repository on GitHub
def list_reactions( username, url, header ):

    # Title of Function/Task
    print( "\n\tTask 6 : List Reactions for an issue" )
    
    # Gather repo name and issue number
    repo = input( "\n\t\tPlease enter the repo for which you would like to list issue reations : " )
    number = input( "\t\tPlease enter the identification number of the issue you would like to list reactions : " )
    
    # Append appropriately to URL
    url = url + "repos/" + username + "/" + repo + "/issues/" + str( number ) + "/reactions"
    
    # Append header to contain the necessary API acceptance header for the developer preview
    header[ 'Accept' ] = 'application/vnd.github.squirrel-girl-preview+json'
    
    # Make request
    r = requests.get( url, headers= header )

    # Print Results
    print( "\n\t\tReturn Code => {}".format( r ) )
    if r.status_code == 200 :
        json_Object = r.json()
        print( "\n\t\tNumber of reactions to Repo:{} Issue #{} : {}".format( repo, number, len( json_Object ) ) )
        count = 1
        for x in range( len( json_Object ) ):
            print( "\t\t\tReaction #{} : {}".format( count,json_Object[ x ][ 'content' ] ) )
            count = count + 1
    else :
        print( "\n\t\tUnable to process the request *** BAD RETURN CODE ***" )
        
# --------------------------------------------------------------------------------------------------------------------------------------MAIN
# Main entry of program. Asks for user input to call appropriate function/action.
def main( args ):
    # Program Notes for user
    print( "\n\tCSC-510 Software Engineering | Homework 4 - REST\n" )
    print( "\tNOTE: Authentication Token should be saved in file named\n\t'auth.token' and placed in the same directory as 'HW4.py'" )
    print( "\tThis will be used to authenticate access to your GitHub account." )
    
    print( "\n\tSelect the appropriate Hub Type:" )
    print( "\t\tEnter 1 : github.com" )
    print( "\t\tEnter 2 : github.ncsu.edu\n" )
    
    # Determine user's github type for URL generation
    hubType = 0
    while True :
        hubType = int( input( "\tEnter your selection : " ) )
        if hubType > 0 and hubType < 3 :
            break;
        else : 
            print( "\t*** Invalid selection --> '{}'. Must be '1' or '2' ***\n".format( hubType ) )

    # Gather user's username for the GitHub account for URL generation
    username = ''
    url = ''
    if hubType == 1:
        username = input( "\n\tPlease enter your GitHub 'username' (eg.: cnaiken) : " )
        #URL for normal Github account
        url = "https://api.github.com/"
    elif hubType == 2:
        username = input( "\n\tPlease enter your GitHub Enterprise 'username' (eg.: cnaiken) : " )
        url = "https://github.ncsu.edu/api/v3/"
        
    #Read in user authentication token for session
    f = open("auth.token","r")
    header = {'Authorization': 'token ' + f.readline()}
    f.close()

    while True :
        print( "\n\tSelect from the following user tasks :")
        print( "\t\tEnter 1 : List all brances of an existing repo." )
        print( "\t\tEnter 2 : Create a new repo." )
        print( "\t\tEnter 3 : Create an issue for an existing repo." )
        print( "\t\tEnter 4 : Add an assignee to an existing issue." )
        print( "\t\tEnter 5 : Edit a repo to disable issues." )
        print( "\t\tEnter 6 : List reactions from an issue." )
        print( "\t\tEnter 7 : To EXIT\n")
        
        selection = 0
        while True :
            selection = int( input( "\tEnter your selection : " ) )
            if selection > 0 and selection < 8 :
                break;
            else : 
                print( "\t*** Invalid selection --> '{}' Must selection numbers 1 - 7 inclusive. ***\n".format( selection ) )
                
        if selection is 7 :
            print( '\n' )
            return 0
        elif selection is 1 :
            list_branches( username, url, header )
        elif selection is 2 :
            create_repo( username, url, header )
        elif selection is 3 :
            create_issue( username, url, header )
        elif selection is 4 :
            add_assignee( username, url, header )
        elif selection is 5 :
            edit_repo( username, url, header )
        elif selection is 6 :
            list_reactions( username, url, header )

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
