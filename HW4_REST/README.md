# HW4 - CSC 510 Software Engineering | NCSU Spring 2019

### Task 0 :
* Sign into NCSU's GitHub, create a private repo called HW4 initialize with a README. Further, add instructor and TA as collaborators.
  * Creation of the private repositiory and addition of collaborators can be verified with the following image reflecting that a _Private_ repo named _HW4_ has been established for student with the unity id _cnaiken_ and that the instructor _nkraft2_ and TA _mrahman_ are in fact collaborators.
  ![alt text](https://github.com/carmenbentley/CSC510---SE/blob/master/HW4_REST/HW4_T0.PNG?raw=true)
### Task 1 :
* Write code to complete the following tasks using the GitHub Rest API
  * T1.1 | List all branches of an existing repo
    - **line : 7**
    - function : list_branches
    - description : This function gathers the repository name necessary to append to the url that will be passed as a parameter to a GET request to list the branches of an existing repository. Request is passed a header containing the user access_token to authenticate access to the Github account. To ensure a successful request, the status code is verified to equal _200_. If the request is successful, the function then prints the names of all the branches associated with the given repository.
    - Git API : GET /repos/:owner/:repo/branches
  * T1.2 | Create a new repo
    - **line : 35**
    - function : create_repo
    - decription : This function gathers the desired visibility, repository name, and description of the repo from the user to establish the url and data objects that will be passed as parameters to a POST request to create a new repository. Request is passed a header containing the user access_token to authenticate access to the Github account. To ensure a successful request, the status code is verified to equal _201_. If the request is successful, the function then prints the details of the new repository for the user.
    - Git API : POST /user/repos
  * T1.3 | Create an issue for an existing repo
    - **line : 80**
    - function : create_issue
    - description : This function gathers the existing repository name, desired issue title and issue description from the user to establish the url and data objects that will be passed as parameters to a POST request to create a new issue for an existing repository. Request is passed a header containing the user access_token to authenticate access to the Github account. To ensure a successful request, the status code is verified to equal _201_. If the request is successful, the function then prints the details of the new issue for the user.
    - Git API : POST /repos/:owner/:repo/issues
  * T1.4 | Add an assignee to an existing issue
    - **line : 111**
    - function : add_assignee
    - description : This function gathers the existing repository name, issue number, and desired assignee username from the user to establish the url and data objects that will be passed as parameters to a POST request to add an assignee to an existing repository issue. Before this request is processed, the function checks that the requested assignee username is valid and has the appropriate permissions to be added to this repo/issue. This is done with a GET request /repos/:owner/:repo/assignees/:assignee. If the assignee is verified then a POST request is made with the appropriate parameters to add the assignee. This request is passed a header containing the user access_token to authenticate access to the Github account. To ensure a successful request, the status code is verified to equal _201_. If the request is successful, the function then prints a message to the user that the request was made correctly and the assignee was added to the issue.
    - Git API : POST /repos/:owner/:repo/issues/:number/assignees
  * T1.5 | Edit a repo to disable issues
    - **line : 149**
    - function : edit_repo
    - description : This function gathers the existing repository name from the user to append to the url that will be passed as a parameter to a PATCH request to disable issues for that existing repository. This request is passed a header containing the user access_token to authenticate access to the Github account. The request is also passed a payload with the content of the repository name and which attribute to update. Even though the name is not being changed, the API requires it as a parameter. To ensure a successful request, the status code is verified to equal _200_. If the request is successful, the function then prints a message to the user that the request was made correctly.
    - Git API : PATCH /repos/:owner/:repo
  * T1.6 | List reactions for an issue
    - **line : 175**
    - function : list_reactions
    - description : This function gathers the existing repository name and issue number from the user to append to the url that will be passed as a parameter to a GET request to list the reactions related to that issue. This request is passed a header containing the user access_token to authenticate access to the Github account and an acceptance address for the purposes of aggreement with the development preview being tested by Github. To ensure a successful request, the status code is verified to equal _200_. If the request is successful, the function then prints the emoji names associated with each reaction to the indicated issue.
    - Git API : GET /repos/:owner/:repo/issues/:number/reactions
    
### Build & Run Instructions
To run the program HW4.py
 1) Generate an access_token at https://github.com/settings/tokens
 2) Save this token in a file named _auth.token_
 3) Place both files ( _auth.token_, _HW4.py_ ) in the same directory
 4) From the commandline, navigate to the directory where the files are located
 5) Enter the command [$ python3 HW4.py] - This will begin the program
 6) The program will then give you instructions for next actions as seen in the example below:
  ![alt text](https://github.com/carmenbentley/CSC510---SE/blob/master/HW4_REST/ProgramStartUp.PNG?raw=true)
