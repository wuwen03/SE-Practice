import requests
import threading
from urllib.parse import urljoin
import main
from be.model.store import init_completed_event
from fe import conf
import logging
thread: threading.Thread = None

def run_backend():
    # rewrite this if rewrite backend
    main.be_run()


def pytest_configure(config):
    global thread
    print("frontend begin test")
    thread = threading.Thread(target=run_backend)
    thread.start()
    init_completed_event.wait()


def pytest_unconfigure(config):
    url = urljoin(conf.URL, "shutdown")
    requests.get(url)
    thread.join()
    print("frontend end test")
