import pytest
from TestCases.Event import Event
from Responseassertion.Assert import JmespathAssert
import threading
import logging
import time

class TestCIC(Event):

    def setUp(self):
        Event.setUp(self)
        self.JmespathAssert=JmespathAssert()

    def session_cic(self,url):
        url=url
        response=self.req.getResp(url)
        time.sleep(5)
        self.JmespathAssert.assertEqual(response.status_code,200)
        print(threading.current_thread().name)
        print('sunny1')

    def session_cic_sessionid(self):
        url='https://cn.bing.com/'
        response=self.req.getResp(url)
        time.sleep(1)
        self.JmespathAssert.assertEqual(response.status_code,200)

    def test_multple_run(self):
        log=logging.getLogger('test_multple_run')
        log.debug ('testit')
        print('testitby sunny ')
        urls=['https://www.baidu.com/','https://cn.bing.com/']
        self.threads=[]
        for url in urls:
            
            self.threads.append( threading.Thread(target=self.session_cic,name=url,args=(url,)))
        for thread in self.threads:   
            thread.start()
        for thread in self.threads:   
            thread.join()
            print (threading.current_thread().name)
            print ('sunny2')

    # def test_1(self):
    #     log = logging.getLogger('test_1')
    #     time.sleep(1)
    #     print('after 1 sec')
    #     time.sleep(1)
    #     log.debug('after 2 sec')
    #     time.sleep(1)
    #     log.debug('after 3 sec')
    #     assert 1, 'should pass'