HOMEWORK WEEK 5-6
(handout for students)


TASK 1 (Agile Techniques)

Question 1
Complete definitions for Scrum related key terminology provided below.
SCRUM CEREMONIES
·        Product backlog refinement
Product owner (and other members of the team if needed) review the tasks on the backlog. This ensures that tasks in backlog remain appropriate and can be prioritised if needed. This helps prevent implementing the wrong tasks and makes sure the backlog tasks are relevant and focused.
·        Sprint planning
A meeting event that defines the tasks of the next sprint. In this meeting the team decide the tasks from the backlog to complete for the next sprint. At the end of the sprint planning the team will have a clear understanding of what is being delivered next.
·        Daily scrum.
A very brief meeting (timeboxed to 15 minutes) which usually starts at the beginning of the day. The daily scrum allows the team to briefly state what they did yesterday, what they are doing today and if there is anything blocking their work. Any issues raised can then be investigated offline.
·        Sprint review.
This is a review of the previously run sprint. In this review the team discuss what was accomplished, what tasks changed and what tasks were blocked. This then allows the team to revise the backlog ready for the next sprint.
·        Sprint retrospective
This is a team meeting where the last sprint is reviewed for what worked well and what didn’t work well. This is then used to see how the next sprint can be improved.
 
 SCRUM ROLES
·        ScrumMaster
A scrum master helps ensures the scrum approach is adopted by the team. The help ensure all scrum activities are carried out and remove barriers to the team’s progress.
·        Product Owner
Defines and manages the product backlog to achieve the required product functionality. The product owner focuses on bring value to the end user of the product and defines and updates the product goal.
·        Development Team.
A development team is a team made of professional individuals who each work on an increment task incrementing the task to “done”.
 
Question 2
 
You are leading a development team that was given a task to create a new yoga booking system.

High level description of the system is as follows:
 
·        It has a very simple interface to accept user input (bookings) and display classes information
·        All bookings, appointments, schedules etc should be stored in a SQL database.
·        There is a ‘backend’ system that should be written in Python to handle the logic and manage the data flow. 
Your team has two weeks to build a simple prototype that will be shown to the client to seek their feedback and discuss further enhancements.
 

TASK
·        Break this task into smaller stories (chunks of work) for the team to work on.
·        Assume that one person works on one task.
·        Mark tasks that can be worked on in parallel and perhaps those that need to be worked on in particular order.
 
For this task the following is the user story that has been created to fulfil the simple prototype requirement:
User story
1.	User goes to website
2.	User enters a class name in the search field
3.	Class name is retrieved through GET function (user doesn’t see)
4.	Connection to MySQL Database is used to retrieve class information (user doesn’t see)
5.	Class details is sent using POST function (user doesn’t see)
6.	Pre-loaded class details is shown on website
7.	No further interaction

In a diagram, the high-level description of the system is:

 
The blue lines and boxes represent requirements which will be initially built for the two-week requirement. The red lines and boxes represent additional functionality which will be discussed with the client after 2 weeks for suggested further enhancements.
To achieve this user story the following mini-Kanban board has been created. Where multiple tasks fall under the same order this is to indicate that the work can be carried out in parallel:
Backlog	To do (sprint 1)	Order (for sprint 1 activities)
Build resilience for peak booking times	Frontend - customer interface to search class and see results	3
Add payment service	Backend - Create database with bookings, appointments, and schedules tables	1
Add login or user verification 	Backend - Create relationships between tables	2
Build Admin app to upload yoga classes information	Backend - Create database config for python project & connect python file to MySQL database	2
	Backend - Insert database information	3
	Backend - Confirm libraries required for project	1
	Backend - Create get function from front end url 	2
	Backend – Create post function to front end url	2
	Backend – Create tests for functions	4
	Refactor and test 	5



TASK 2 (SQL)

Question 1
Design a cinema booking system.
Think how you would approach the problem and what are potential ways of solving it?

You do not need to write actual code, but describe the high-level approach:
·        Draw a list of key requirements
·        What are your main considerations?
·        What would be your common or biggest problems?
·        What components or tools would you potentially use?
·        You are welcome to draw a diagram (a very simple one) for the process flow to explain how  it is going to work. 
Process flow of cinema booking system
 

Requirements

-	Able to verify if a user is a customer or an admin user
-	The booking system is resilient if there is a high user load
-	The customer can view cinema times, book tickets and update booking
-	Admin is able view customer books and update booking information if needed

Considerations

-	If booking fails, booking needs to refresh
-	Can past bookings or past cinema times be visible?
-	If viewing cinema time or booking fails, user needs to be prompted to retry
-	If updating book fails or is completed, user needs to be informed
-	Will information be sent to the database continuously or in scheduled batches?
-	Can information be deleted? Only considered to update information. Would past cinema times be kept in database or deleted?
-	Security considerations - Can the customer have admin privileges? Can the admin see personal payment details via API? 
-	How will the cinema times be updated? Not included in high-level design
-	How long is information stored?


What would be your common or biggest problems?
-	How to manage high user load
-	How to manage data
-	Testing
What components or tools would you potentially use?
-	A payment API
-	MySQL
-	JSON, Requests library for python
-	Flask 
-	Python
-	Increase user load component
-	Unit Test tool
![image](https://user-images.githubusercontent.com/61808090/140654517-96284d1d-6bdf-4b5f-bd81-aef54fa70510.png)

