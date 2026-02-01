from reportlab.pdfgen import canvas
text="""Who is most susceptible to cyber threats?
Similar to how humans or animals are more exposed to danger when they are vulnerable, software programs, hardware, and business processes with weak or flawed systems are most susceptible to cyber attacks. A robust cybersecurity architecture includes tools such as antivirus software, private networks, and secure file-sharing solutions, and vigorous employee training and access management to protect against social engineering cyber attacks such as phishing.

Although public and private sectors share the same need to protect critical data, those working in government need extra layers of security. Government employees in the US and many other countries worldwide must pass security clearance in order to qualify for certain jobs.

9 cybersecurity best practices
Conducting a cybersecurity audit on your business to assess your current situation may be helpful. What security measures are already in place? Are all employees aware of potential security risks and threats, and how to protect against them? Are all of the company’s networks and data protected with several layers of security?

The following nine cybersecurity tips can help mitigate system and network vulnerabilities that expose organizations to security breaches and ransomware attacks.

1. Implement a people-first cybersecurity strategy.
A people-centric cybersecurity strategy focuses on equipping employees with the education they need to be able to recognize potential threats. This can include recognizing suspicious activity, such as a sudden uptick in traffic to a specific web page. Or, avoid malicious software by avoiding suspicious links.

If your team is new to cybersecurity, check out and share this cybersecurity glossary and FAQ page. You can also consider enrolling in the following free course offered by the University of Maryland, Cybersecurity for Everyone"""

c=canvas.Canvas("text.pdf")
y=800

for line in text.split("\n"):
    c.drawString(50,y,line)
    y=y-20
    c.save()

