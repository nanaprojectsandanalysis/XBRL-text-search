XBRL US API document text search (in-progress)
===========================================

***This code is still in progress and has been a little tough to tackle, so any suggestion is appreciated***

**Author:** *nanaprojectsandanalysis*

# Overview and motivation
XBRL is a eXtensible Business Reporting Language, XBRL US is a non-profit community improving U. S. reporting through a free, open standard. The code aims to request and save information on organizations with subsidiaries. The similar code was used to retrieve data from another database, however for the further research necessary for my thesis topic, this code has been started. 

# What is the code doing right now?
The code should extract all the documents containing text '21.1' The 21.1 refers to the Exhibit 21.1 of 10-K annual company reports containing list of subsidiaries of US companies. 
The endpoints and other request information is here: [text] (https://xbrlus.github.io/xbrl-api/#/oauth2/tokenUrl)
You can generate client_id and client_secret after logging-in (not using e-mail SSO) in here: [text](https://xbrl.us/home/use/xbrl-api/access-token/)
**However,** I was not able to overcome the limitation of getting at least 10 documents with only the text search parameter. For now, the request does provide the information on the text search **ONY** when including *report.id*. 

# What should this code do?
The code should generate the list of document links, company cik or document dts.id, links to Exhibits 21.1, and subsidiary list.

# What do I want to add to the code eventually?
I want to the add the loop which is able to recursively generate over the limit that is allowed for the non-Member clients of XBRL.

# What are the redundant/unneccessary code line?
I left in code lines and ideations in case they might be necessary. I apologize for a non-optimized code, this is due to me not having a a solid base of coding education, and picking up from non-linear college courses, tutorials and Stack Overflow forums. 
