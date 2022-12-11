# import requests #동기적 코드ㅔㅑㅔ
# import aiohttp
import requests
import asyncio
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor 



def fetcher(params):
    session = params[0]
    url = params[1] 
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://naver.com",
            "https://google.com",
            # "https://instagram.com",
    ] * 50

    executor = ThreadPoolExecutor(max_workers=20)#최대 스레드의 개수

    with requests.Session() as session:
        # result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        # print(result)
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))
        print(results)



if __name__ == "__main__":

    start = time.time()
    # asyncio.run(main())
    main()
    end = time.time()

    print(end - start)