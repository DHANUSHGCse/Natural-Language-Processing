import spacy
nlp = spacy.load('en_core_web_sm')
formatpattern = input("Enter the Pattern : ")
verb = formatpattern.split(" ")[1]
def findpattern(txt):
    pattern={}
    doc = nlp(txt)
    if(len(doc)>=3):
        for i in range(len(doc)):
            x=""
            if doc[i].dep_=="ROOT" and doc[i].text == verb:
                for token in doc[i].subtree:
                    if token.dep_.startswith('nsubj'):
                        x=token.text
                    if token.dep_.endswith('obj'):
                        try:
                            pattern[x].append(token.text)
                        except:
                            pattern[x]=[]
                            pattern[x].append(token.text)
        return pattern
    return pattern
no=int(input("Enter the number of sentences : "))
texts=[]
for i in range(no):
    txt = input("Enter the text : ")
    texts.append(txt)
print("Analyzed patterns")
for i in texts:
    print("txt : "+i)
    print("pattern matched")
    pattern = findpattern(i)
    #displacy.render(nlp(i))
    for x in pattern.keys():
        for y in pattern[x]:
            print(x,verb,y)
    
