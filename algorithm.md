#THE ALGORITHM - HOW IT WORKS

This documentation is intended to explain and justify the design of the calculator in the software. It is intended for those with strong background knowledge of threat modelling.

The algorithm takes elements from STRIDE, CVSS, and LINDUNN GO.

Firstly, the the devices the user selects are sorted into the following five categories. A device can be in more than one category at once. If at least one device per category is added, that category is switched on for the calculations.
- Voice input devices (Cat1)
- Devices generally requiring sign-in to function (2)
- Devices communicating on the internal network (3)
- Devices communicating with external entities via the internet (4)
- Devices directly affecting home physical security (5)

The key to device categories is as follows:
- Home virtual assistant (1 2 3 4 5)
- Smart security cam (2 3 4 5)
- Smart doorbell (2 3 5)
- Smart lighting (3)
- Smart fitness aid (2 3 4)
- Smart kitchenware (3)
- Smart locks (3 4 5)
- Amazon Dash (2 3 4)
- Smart thermostat or air monitor (2 3 4 5)
- Automated 'smart home' controller* (1 2 3 4 5)
- Smart sleep tracker (2 3)
- Any other smart home devices** (1 2 3 4 5)

Obviously, these are just averages or assumptions based on what most devices of these types do. In a more developed version of the program, individual makes/models and their unique capabilities could be taken into consideration.

1* These fulfil generally the same exact functions as the virtual assistant hub and often have touchscreens as well.
2** We will have to assume these devices in the 'other' class are reasonably capable of falling into any category.

As the different devices follow differing amounts of the same threats already elucidated for the voice processing hub acting as central controller (see research paper), the same STRIDE table can be used (albeit a filtered down version by device type for relevancy) when determining the key risks.

The switched-on categories will then turn on the associated threat numbers. These numbers correlate to the STRIDE table (see paper).
- Cat 1: S(1), T(4 7), I(10 11), D(12)
- Cat 2: S(2), I(8)
- Cat 3: S(3), T(6 7), I(9), D(13 14), E(15 16)
- Cat 4: S(2), T(5), I(8 11), D(13), E(15)
- Cat 5: S(3), T(6 7), I(9), D(14), E(16)

The risk score added per STRIDE number is the average of the 3 different CVSS scores (see paper) for that threat.

Each category also has a number of POTENTIAL associated LINDUNN GO factors (again, individual devices would vary, but it is not feasible to analyse every brand and product for this project).
- Cat 1 has 11 factors: linkable user actions, linkability of retrieved data, actions identifying user, non-repudiation of sending, non-repudiation of received data, no transparency, disproportionate collection, unlawful processing, disproportionate processing, identifiability from shared data, identifiability from inbound data.
- Cat 2 has 17 factors: linkable user credentials, linkable user actions, linkable inbound data, linkable shared data, linkable stored data, linkable retrieved data, identifying credentials, actions identifying user, identifying inbound data, identifying shared data, identifying retrieved data, non-repudiation of sending, non-repudiation of storage, non-repudiation of retrieval, disproportionate collection, unlawful processing, disproportionate storage.
- Cat 3 has 4 factors: linkable credentials, linkable context, identifiable context, detectable outliers.
- Cat 4 has 10 factors: linkable inbound data, linkable shared data, linkable retrieved data, identifying shared data, identifying retrieved data, detectable outliers, disproportionate collection, unlawful processing, disproportionate processing, disproportionate storage.
- Cat5 has 4 factors: linkable user actions, linkable context, identifying context, detectable outliers.
A score is added to each risk in the category based on the number of LINDUNN GO categories flagged by the device type, multiplied by 0.5. This 0.5 was chosen as some device types have a very large amount of associated GO factors compared to others, so dividing the total by 2 reduces overly-skewed results.

Finally, the risk factors toggled by the user will also add a value to the score, based on how easy it might be for a stranger to manipulate the risk factor to form an attack. These scores go from 1 (the attacker would have a hard time utilizing this specific route though it is still possible) to 3 (relatively easy to manipulate). Obviously there is a degree of opinion to these values, but it would be very simple to change them in the code to better suit future developments in knowledge.
- R1: value 3, related STRIDEs 2 3 5 6 7 8 9 12 13 14 15 16, justification: it is incredibly easy to snoop on traffic in an unprotected network.
- R2: value 1, related STRIDEs 1 6, justification: this removes a step of complexity in gaining account access although the attacker must still manage to crack the first passcode in most cases
- R3: value 2, related STRIDEs 2 3 5 6 7 8 9 12 13 14 15 16, justification: the default passwords on many models of router can be brute forced with little effort but this depends on the victim having certain models of router
- R4: value 2, related STRIDEs 2 3 6 9 15 16, justification: weak passwords are easily bruteforced but doing this still requires significant processing power in many cases
- R5: value 1, related STRIDEs 1 4 10 12, justification: manipulating this would require an attacker to position themselves very close to the victim at an opportune moment
- R6: value 1, related STRIDEs 11, justification: there are multiple documented cases of employees hearing private conversations through this processing though obviously it depends on a malicious employee happening to hear a specific thing
- R7: value 2, related STRIDEs 1 11 12, justification: a malicious skill/app can turn on the listening mode but this requires the user to have the skill/app in the first place or for the attacker to be able to escalate privileges high enough to toggle the mic
- R8: value 3, related STRIDEs 15 16, justification: it is very easy to search for device vulnerabilities online and in many cases example attack scripts are provided
- R9: value 3, related STRIDEs 2 3 5 6 7 8 11 13 14 15 16, justification: once a malicious app is installed then an attacker has very easy access to the device they want to manipulate
- R10: value 3, related STRIDEs 2 3 5 6 7 8 9 11 13 14 15 16, justification: as above, but for devices instead of apps
- R11: value 2, related STRIDEs 1 10 11 12, justification: it would require a bad actor to be very close though many accidental bad actors manipulate this unknowingly or as a joke
- R12: value 2, related STRIDEs 9, justification: based on usage traffic patterns (even encrypted ones) an attacker can easily find out when someone is not home and use that information maliciously
- R13: value 1, related STRIDEs 11, justification: this risk relies on the third party having malicious actors within it
- R14: value 1, related STRIDEs 11, justification: this relies on a manufacturer being malicious
