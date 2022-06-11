
welcome = "Hello welcome to Mas ABAP\n\n"
control = "You can control me by sending these commands:\n\n"


# Command Introduce
introduce = "*Introduce : *\n"
i1 = "/abap - Programming Language SAP\n"
i2 = "/alv - Report\n"
i3 = "/bapi - Functional Module\n\n"


# Command Create
create = "*Create :* \n"
c1 = "/alvcreate - Create ALV Report\n\n"

# Command contact
contact = "*Contact : *\n"
h1 = "/contactus"

start = welcome + control + introduce + i1 + i2 + i3 + create + c1 + contact + h1

# Text Intrpduce
getTextABAP = open("text/introduce/introduce_abap.txt", "r")
whatIsABAP = ""
for text in getTextABAP:
    whatIsABAP = whatIsABAP + text

getTextAlv = open("text/introduce/introduce_alv.txt", "r")
whatIsALV = ""
for text in getTextAlv:
    whatIsALV = whatIsALV + text

getTextBAPI = open("text/introduce/introduce_bapi.txt", "r")
whatIsBAPI = ""
for text in getTextBAPI:
    whatIsBAPI = whatIsBAPI + text


# Text Create ALV
# =====================================================================
# Fieldcat
# =====================================================================
getTextCreateALV = open("text/create/alv/fieldcat.txt","r")
textCreateALV = ""
for text in getTextCreateALV:
    textCreateALV = textCreateALV + text

getTextCreateALVNote = open("text/create/alv/fieldcat_note.txt","r")
textCreateALVNote = ""
for text in getTextCreateALVNote:
    textCreateALVNote = textCreateALVNote + text
# =====================================================================
# Fieldcat
# =====================================================================

# =====================================================================
# Layout
# =====================================================================
getTextCreateLayout = open("text/create/alv/layout.txt","r")
textCreateLayout = ""
for text in getTextCreateLayout:
    textCreateLayout = textCreateLayout + text

getTextCreateLayoutNote = open("text/create/alv/layout_note.txt","r")
textCreateLayoutNote = ""
for text in getTextCreateLayoutNote:
    textCreateLayoutNote = textCreateLayoutNote + text
# =====================================================================
# Layout
# =====================================================================

# =====================================================================
# TOP
# =====================================================================
getTextCreateTOPALV = open("text/create/alv/top_include_alv.txt","r")
textCreateTOPALV = ""
for text in getTextCreateTOPALV:
    textCreateTOPALV = textCreateTOPALV + text
# =====================================================================
# TOP
# =====================================================================