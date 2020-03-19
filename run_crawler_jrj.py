from Crawler.crawler_jrj import WebCrawlFromjrj

if __name__ == '__main__':
    web_crawl_obj = WebCrawlFromjrj("2000-01-01","2020-03-17",100,ThreadsNum=40,IP="localhost",PORT=27017,\
        dbName="Jrj_Stock",collectionName="jrj_news_company")
    web_crawl_obj.coroutine_run()  #web_crawl_obj.single_run() #web_crawl_obj.multi_threads_run()
