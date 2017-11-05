import time
from browser import *
from selenium.common.exceptions import *
from mongodb1 import *

b = get_chrome_browser()


def get_yhq_yxq(url):
    yxq = []
    try:
        b.get(url)
        ele = b.find_element_by_xpath('//*[@id="mx_6"]/div/div/span[3]')
        print ele.text
        yxq = ele.text.split('-')
    except NoSuchElementException:
        print 'no yhq'
        pass
    return yxq


def update(g):
    try:
        url = g['couponShortLinkUrl']
        print url
        if len(url.strip()) == 0:
            print 'url is empty'
            delete_goods(g)
        else:
            yxq = get_yhq_yxq(url)
            if len(yxq):
                g['couponEffectiveStartTime'] = yxq[0]
                g['couponEffectiveEndTime'] = yxq[1]
                if compare_today(yxq[1]):
                    print 'yhq is guo qi'
                    delete_goods(g)
                else:
                    update_goods(g)
            else:
                print 'no yxq'
                delete_goods(g)
    except KeyError as e:
        print 'json no key:' + str(e)
        delete_goods(g)


def main():

    while True:
        goods = get_goods()

        print 'update count:'
        print goods.count()

        # no data to update
        if goods.count() == 0:
            time.sleep(5)
            continue

        for g in goods:
            # print g
            update(g)


if __name__ == '__main__':
    main()

