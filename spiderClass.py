import requests
import re
from sys import argv
from multiprocessing.dummy import Pool as ThreadPool

class spider(object):
    def postHtml(self, url, data):
        return requests.post(url, data=data).text

    def getHtml(self, url):
        return requests.post(url).text

    def extractData(self, rePattern, Responese):
        pattern = re.compile(rePattern)
        return re.findall(pattern, Responese)

class InOutput(object):
    def read(self, filename):
        return open(filename, 'r').read().split("\n")

    def write(self, filename, list):
        with open(filename, 'w') as f:
            for line in list:
                f.write(line)
                f.write("\n")

    def outPut(self, list):
        for line in list:
            print("{}",format(line))

def crateUrl(domainList):
    return ["".format(domain) for domain in domainList]

def run(url):
    return spider.extractData('1',spider.getHtml(url))[0]

InOutput = InOutput()
spider = spider()
url = crateUrl(InOutput.read(argv[1]))
Pool = ThreadPool(int(200));results = Pool.map(run, url);Pool.close();Pool.join()
InOutput.outPut(results)