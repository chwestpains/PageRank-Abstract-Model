class Websites:
    def __init__(self, webpageName):
        self.webpageName = webpageName
        self.pageRank = 0
        self.dampingFactor = 0.85
        self.outbound_links = 0
        self.inbound_links = 0
        self.inboundWebsites = []
        self.outboundWebsites = []

    def set_initial_pageRank(self):
        self.pageRank = 1

    def update_pageRank(self):
        PRCn = self.get_outbound() + self.get_inbound()
        PRTn = self.get_inbound()
        if PRTn > 0:
            self.pageRank = (1-self.dampingFactor) + (PRTn / PRCn)
        else:
            pass

    def get_external_webName(self, website):
        return website.webpageName

    def get_internal_webName(self):
        return self.webpageName

    def get_webName(self):
        return self.webpageName

    def get_inbound(self):
        return self.inbound_links

    def get_outbound(self):
        return self.outbound_links

    def set_outboundWebsites(self, website_link):
        self.outboundWebsites.append(website_link.get_external_webName(website_link))
        self.set_outbound()
        website_link.update_pageRank()
        ownwebsite = self.get_webName()
        website_link.set_inboundWebsites(ownwebsite)

    def get_outboundWebsites(self):
        return self.outboundWebsites

    def get_inboundWebsites(self):
        return self.inboundWebsites
    
    def set_inboundWebsites(self, webobject):
        self.inboundWebsites.append(webobject)
        self.set_inbound()
        

    
    def set_inbound(self):
        self.inbound_links += 1

    def set_outbound(self):
        self.outbound_links += 1



page1 = Websites("BBC News")
page1.set_initial_pageRank()

page2 = Websites("Isaac Computer Science")
page2.set_initial_pageRank()

page3 = Websites("Spotify Web Player")
page3.set_initial_pageRank()

page4 = Websites("Twitter")
page4.set_initial_pageRank()

page5 = Websites("Google")
page5.set_initial_pageRank()

page6 = Websites("Youtube")
page6.set_initial_pageRank()

page7 = Websites("Facebook")
page7.set_initial_pageRank()

page8 = Websites("Amazon")
page8.set_initial_pageRank()

page9 = Websites("Netflix")
page9.set_initial_pageRank()

page4.set_outboundWebsites(page1)
page2.set_outboundWebsites(page1)
page1.update_pageRank()
page1.set_outboundWebsites(page4)
page1.update_pageRank()
page6.set_outboundWebsites(page5)
print(page5.pageRank)

