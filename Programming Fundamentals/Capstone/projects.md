## Brute Force Calculator
This python script calculates the amount of time it would take to crack encryption keys of different sizes (bits) at different speeds (GigaFLOPS).

## HARVI Effectiveness
This script was used to analyze the HARVI scores of thousands of employees to determine the effectiveness of phishing training. Each textfile consists of a before-training score and an after-training score, respectively. The script calculates the average scores before and after training for each department to determine if there was any improvement.

## Malware Replication Speed
This script was used to calculate the speed at which malware spreads through a network. It takes the number of initially infected endpoints and the number of new infections per day to calculate how long it will be until every endpoint is infected. This is a really simple script that is purely conceptual. An actual calculator would be more robust by taking more factors into account.

## Password Checking
This script can hash and store passwords in binary, and then accept a password input that it will check against the binary file. It can also check for password policy compliance (i.e number of upper/lowercase letters and numbers). I used the recommended hashing algorithm from hashlib per NIST SP 800-132 as my attempt at compliance. I'm still proud of this one, but I know it could be improved in a number of ways and I wouldn't recommend it be used for any official password authentication.