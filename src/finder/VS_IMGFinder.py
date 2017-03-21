import os
from appium import webdriver
from finder.template_finder import TemplateFinder
from finder.template_matcher import TemplateMatcher
from finder.cv2img import CV2Img

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ROOT_DIR, "resources")


def IMG_PATH(name):
    return os.path.join(RESOURCES_DIR, name)

def find(target_path, source_path=None, driver=None,METHOD=None):
    #autoScreenshotCount = 0
    #driver.driver.save_screenshot(IMG_PATH("autoScreenshot" + str(autoScreenshotCount) + ".png"))
     source = CV2Img()
     source.load_file(IMG_PATH(source_path), 0)
     #source.load_file(IMG_PATH("autoScreenshot" + str(autoScreenshotCount) + ".png"), 0)
     target = CV2Img()
     target.load_file(IMG_PATH(target_path), 0)
     finder = TemplateFinder(source)
     results = finder.find_all(target, 0.9)
     #autoScreenshotCount + 1
     for item in results:
         result = source.crop(item)
         coordinate_x, coordinate_y = source.coordinate(item)
         return coordinate_x, coordinate_y


def imageExist(target_path, source_path=None, driver=None, METHOD=None):
    source = CV2Img()
    source.load_file(IMG_PATH(source_path), 0)
    target = CV2Img()
    target.load_file(IMG_PATH(target_path), 0)

    finder = TemplateFinder(source)
    results = finder.find_all(target, 0.9)

    for item in results:
        result = source.crop(item)
        coordinate_x, coordinate_y = source.coordinate(item)
        if (source.coordinate(item) == None):
            return False
        else:
            return True
"""
class ImageFinder():
    def find(target_path, source_path=None, driver=None,METHOD=None):
        #autoScreenshotCount = 0
        #driver.driver.save_screenshot(IMG_PATH("autoScreenshot" + str(autoScreenshotCount) + ".png"))


        source = CV2Img()
        source.load_file(IMG_PATH(source_path), 0)
        #source.load_file(IMG_PATH("autoScreenshot" + str(autoScreenshotCount) + ".png"), 0)
        target = CV2Img()
        target.load_file(IMG_PATH(target_path), 0)



        finder = TemplateFinder(source)
        results = finder.find_all(target, 0.9)

        #autoScreenshotCount + 1

        for item in results:
            result = source.crop(item)
            coordinate_x, coordinate_y = source.coordinate(item)
            return coordinate_x, coordinate_y


    def assertExist(target_path, source_path=None, driver=None,METHOD=None):

        source = CV2Img()
        source.load_file(IMG_PATH(source_path), 0)
        target = CV2Img()
        target.load_file(IMG_PATH(target_path), 0)

        finder = TemplateFinder(source)
        results = finder.find_all(target, 0.9)

        for item in results:
            result = source.crop(item)
            coordinate_x, coordinate_y = source.coordinate(item)
        if (source.coordinate(item)!=None):
            return False
        else:
            return True
"""
