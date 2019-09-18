# Copyright (C) 2019 baalajimaestro
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Save all denials line by line to denials.txt in the same folder as code
# Fixes are saved to fixes.txt

import re
with open("denials.txt") as denfile:
    data=denfile.read()
data=data.split("\n")
data.remove(data[-1])
with open("fixes.txt","w") as fixfile:
    for i in data:
        test=re.search("{",i)
        test2=re.search("}",i)
        se_context=i[test.span()[0]:test2.span()[0]+1]
        test=re.search("scontext",i)
        scontext=i[(test.span()[0]):].split(":")[2]
        test=re.search("tcontext",i)
        tcontext=i[(test.span()[0]):].split(":")[2]
        test=re.search("tclass",i)
        tclass=i[(test.span()[0]):].split("=")[1].split(" ")[0]
        fix="allow "
        fix+=scontext
        fix+=" "
        fix+=tcontext
        fix+=":"
        fix+=tclass
        fix+=" "
        fix+=se_context
        fix+=";"
        fix+="\n"
        fixfile.write(fix)
