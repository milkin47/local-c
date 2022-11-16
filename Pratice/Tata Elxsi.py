list = [1,1,1,2,3,5,5]

count = {}

for i in list:
    if i in count:
        count[i] = count[i] + 1
        #print(count[i])
    else:
        count[i] = 1
        #print(count[i])
print(count)

# *** Settinng ***
# import
# *** Testcase***
#     LOgin into the page
#     validating the login page
#
# *** Keyword ***
# Login into the page:
#     Open browser
