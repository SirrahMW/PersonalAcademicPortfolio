# Personal Repository
This repository functions as an easy way for me to prove some of my knowledge and abilities to potential employers. A majority of the content is prior coursework from my time at Columbia Basin College, where I graduated with my BAS in Cyber Security. Any other relevant projects, professional or personal, will get added over time. The link for this repo should be included on my résumé upon application.

## Database Design
This is the result of a group project for Database Design class in which we designed a database for an imaginary company as if they were our client. We were given a scope of requirements that the imaginary client provided. We then went through the following process:
1. Created an Entity Relationship Diagram (ERD) from the requirements provided to us.
2. Mapped a Relational Schema using the ERD and then normalized the data to the 3rd normal form.
3. Created the tables and relations in SQL via Microsoft Access to match the normalized schema.
4. Added forms, reports, and queries including a Navigation Form.
5. Finalized by adding test data to ensure functionality.

## Programming Fundamentals
The content of this folder should act as proof of my foundational knowledge of the Python programming language. I still consider myself a novice, but I feel confident that I have the tools and knowledge at my disposal to use Python however is needed.

### Capstone
My Cyber Security capstone class required lab work in which we would be given an objective (Usually a calculation or functionality) which we had to complete using a scripting language of our choosing (I picked Python). Here are short descriptions of each:

#### Brute Force Calculator
This python script calculates the amount of time it would take to crack encryption keys of different sizes (bits) at different speeds (GigaFLOPS).

#### HARVI Effectiveness
This script was used to analyze the HARVI scores of thousands of employees to determine the effectiveness of phishing training. Each textfile consists of a before-training score and an after-training score, respectively. The script calculates the average scores before and after training for each department to determine if there was any improvement.

#### Malware Replication Speed
This script was used to calculate the speed at which malware spreads through a network. It takes the number of initially infected endpoints and the number of new infections per day to calculate how long it will be until every endpoint is infected. This is a really simple script that is purely conceptual. An actual calculator would be more robust by taking more factors into account.

#### Password Checking
This script can hash and store passwords in binary, and then accept a password input that it will check against the binary file. It can also check for password policy compliance (i.e number of upper/lowercase letters and numbers). I used the recommended hashing algorithm from hashlib per NIST SP 800-132 as my attempt at compliance. I'm still proud of this one, but I know it could be improved in a number of ways and I wouldn't recommend it be used for any official password authentication.

### Etc.
These files are examples of various python functionalities such as:

- Class Inheritence
- File Input/Output
- GUI Generation
- Recursive Functions

As well as some extra credit assignments from Programming Fundamentals II.

### Exam
This was the Final Exam of Programming Fundamentals II. I was given 90 minutes to create this program that uses a hierarchy of related objects and inherited methods and properties. The objective was to create a program that could create an Author object that could contain what books were written and details about the Author. Because of the limited time frame, this program is very barebones with limited required input and limited input validation. However it met the rubric of the assignment listed below:

- Appropriate data types
- Constructors initialize private members from data passed on object instantiation
- Inheritance is used
- The program logic is good/logical
- Accessors for private primitive variables
- Testing of BookAuthor instantiation and print of data from all 3 objects

