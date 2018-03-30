from selenium import webdriver
from time import sleep
from PIL import Image

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image.crop((x, y, x+width, y+height)).save('tel.gif')

    def navigate(self):
        self.driver.get('https://www.avito.ru/ryazan/telefony/iphone_16_gb_silver_1156788230')

        button = self.driver.find_element_by_class_name('item-phone-number')
        button.click()

        sleep(1)
        self.take_screenshot()

        image = self.driver.find_element_by_class_name('item-phone-big-number')
        location = image.location
        size = image.size

        self.crop(location, size)


def main():
    print 'start'
    b = Bot()


if __name__ == '__main__':
    main()
