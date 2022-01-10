# Selenium


## Selenium
The Selenium folder contains code to scrap the CoCoRaHS website and obtain hail events for a given province.
This website is built using the Microsoft ASP.NET framework.

Normally, we can scrap a website using the standard requests and BeautifulSoup package. In this case however, we will need to simulate an actual browsing session to press buttons and click on a number of options.

A good place to start understanding Selenium is this [post](https://techrando.com/2020/08/09/how-to-web-scrape-a-asp-net-web-form-using-selenium-in-python/) by kperry2215 at techrando.com and Selenium's [documentation](https://selenium-python.readthedocs.io/getting-started.html).

### set-up
- Install Selenium in the environment
`pip install selenium`
- Get a web driver like [GeckoDriver](https://github.com/mozilla/geckodriver/releases) or ChromeDriver [[1]](https://chromedriver.chromium.org/home) [[2]](https://sites.google.com/a/chromium.org/chromedriver/getting-started) and [add to path](https://www.kenst.com/2015/03/including-the-chromedriver-location-in-macos-system-path/). The script here uses the web driver for Chrome.
