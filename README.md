# No(Co)vid - 19 screening system
### Computer Innovation Engineering (4th Year) - King Mongkut's Institute of Technology Ladkrabang (KMITL)

## About the project
We came up with this project in an attempt to improve the current Covid-19 screening system in Thailand. Despite having multiple Covid-19 screening system located in front of many restaurants and facilities, there are still more cases emerging.

The common screening systems that can be found in Thailand include:
* Temperature checking using face recognition and infrared sensor
* Temperature checking using only the infrared sensor

There is also a **Check-In** system called **Thai-Chana(ไทยชนะ)**. However, many people **intentionally** ignore the system because it is not required to be done before entering the building or public facilities such as restaurants and malls.

We saw the possible improvement that could be done to the current system, and that is why we chose to do this project as the capstone project.

## How is it different from the current Covid-19 screening system?

We realized that by only checking the temperature of a person could not ensure the safety of the community. Therefore, we decided to add more layers of screening checkpoints into the system. The system consists of two main checkpoints which are:
* First checkpoint: QR Code scanning
* Second checkpoint: Correctness of how you wear your mask and temperature checking

We plan to build a web application where the **user** will be **required** to input their information into the form. The information will include:
* First Name
* Last Name
* Contact
* Number of doses of Covid-19 vaccines received
* Vaccine 1 Name
* Vaccine *n* Name

After the user filled and submitted the form. Our backend will use the data to generate a QR Code based on the data the user provided. The QR will then be sent back to the user to use for the first checkpoint in the screening system.

After the user has passed the first checkpoint, the second checkpoint will check for the correctness of how that user wears their mask and also their temperature. The correctness is referred to:
* No mask under the nose
* No mask under the chin
* Only the correct way of wearing your mask will be granted entry

The users are required to pass both first and second checkpoint to be granted entry to the building or facility. 

## Monitoring the safety of the facility

*More information will be added*






