from selenium import webdriver
import time

class InstaBot:
    #initializer/ constructor method
    def __init__(self,username,password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(2)

    #bot function method
    def get_unfollowers(self):
        #clicking through ig to get to followers list
        self.driver.find_element_by_xpath("//a[contains(@href,'{}')]".format(self.username)).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'{}')]".format("followers")).click()
        time.sleep(1)
        followers = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'{}')]".format("following")).click()
        time.sleep(1)
        following = self._get_names()
        notFollowingBack = [user for user in following if user not in followers]
        print(notFollowingBack)

    #method to scrub respective lists for users and place them on python list
    def _get_names(self):
        #opening followers/following list
        scrollBox = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        time.sleep(1)

        #scrolling through followers/following list until reach the bottom by comparing previous height to current
        lastHeight, height = 0, 1
        while lastHeight != height:
            lastHeight = height
            time.sleep(1)
            height = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;""", scrollBox)

        #pulling every username (name) using .text into a list (names) for every username that isn't blank
        links = scrollBox.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        #closing followers list
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
        time.sleep(2)

        return names

##############################################

myBot = InstaBot("durhanicuts", "Farmerjoe2")
#!!!^Figure out how to either grant input for parameters or store parameters on a file
myBot.get_unfollowers()
