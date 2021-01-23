
#een HTML wordt opgebouwd door tags
class Tag:

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
       
       #werkt niet pakt weer alleen de eerste 
#        if 'img' or 'br' or 'input' in name: 
#            print("nu pakt ie alles hier")
#        else: 
 #           self.end_tag = '</{}>'.format(name)
           
 # dit werkt niet, hij pakt alleen de eerste 
 #       if name == 'input' or 'img' or 'br': 
 #           self.end_tag = '</{}>'.format(name)
 #       else: 
 #           self.end_tag = '<{}>'.format(name)
        self.contents = contents

        #misschien def end tag zoals in voorbeeld bij ledematen oppasobali 

    #tags en inhoud naar het scherm schrijven 
    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)

#in deze klasse wordt vastgelegd met welke versie van HTML gewerkt wordt 
class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML', '')
        self.end_tag = ''   # DOCTYPE heeft geen endtag


class Head(Tag):

    #plaatsen van de begintag op de juiste plaats
    def __init__(self, title=None):
        super().__init__('head', '')    #Inhoud van de head wordt apart opgebouwd
        self._head_contents = []

    #opbouwen van de inhoud
    def add_head_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._head_contents.append(new_tag)

    #laten zien van de inhoud 
    def display(self, file=None):
        for tag in self._head_contents:
            self.contents += str(tag)
        super().display(file=file)


class Body(Tag):

    #plaatsen van de begintag op de juiste plaats
    def __init__(self):
        super().__init__('body', '')   # De inhoud van de body wordt apart opgebouwd
        self._body_contents = []

    #opbouwen van de inhoud
    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    #laten zien van de inhoud 
    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
        super().display(file=file)

#alle klassen klaar nu het document opbouwen 
class HtmlDoc(object):

    #het aanmaken van nieuwe objecten, deze klasse is opgesteld uit de eerdere 
    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    #koppeling van het object en roept methode van klasse Head aan om inhoud te bouwen 
    def add_head_tag(self, name, contents):
        self._head.add_head_tag(name, contents)

    #koppeling van het object en roept methode van klasse Body aan om inhoud te bouwen 
    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    #inhoud van de pagina opbouwen 
    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

if __name__ == '__main__':
    my_page = HtmlDoc('Demo HTML Document')
    my_page.add_head_tag('title', 'Dit is de pagina van de muziekschool Sessions')
    my_page.add_tag('h1', 'Muziekschool Session')
    my_page.add_tag('h2', 'de specialist in drums en piano')
 #   my_page.add_tag('br', 'Muziekschool Session')
    my_page.add_tag('p', 'verdere informatie staat in deze paragraaf')
    my_page.add_tag('img', "foto")
    my_page.add_tag('br', "Dit kan dus niet..")
    my_page.add_tag('input', "Dit kan dus niet..")

    with open('test.html', 'w') as test_doc:
        my_page.display(test_doc)
