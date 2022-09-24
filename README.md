This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, Anyone visiting the Website should NOT add any real bank or credit card details!.

![responsive design](https://www.ledger.com/wp-content/uploads/2022/07/banner-en-last.png)

---

 # [Crypto Wallets](https://flow-matic-crypto-price-app-assetspythonapp-cs4spv.streamlitapp.com/)


The Website is designed and based on digital freedom, securing the new disruptive class of crypto assets. Crypto requires new rules. New protection. New security practices. But nothing can't be learned. Visit Crypto Wallets website for all your crypto needs. A hardware wallet is a cryptocurrency wallet which stores the user's private keys (critical piece of information used to authorise outgoing transactions on the blockchain network) in a secure hardware device. The main princible behind hardware wallets is to provide full isolation between the private keys and your easy-to-hack computer or smartphone.

<br>

---
<br>

## UX
This project is my fifth and final Milestone Project in the Code Institute's Fullstack Development program. I decided to create a website based on my passions!. Blockchain Techgnology. The E-commerce site has many features for customers and returning customers, from bowsing the latest digital wallets, to purchasing various products, also learning about Blockchain and cryptocurrency's.
___
<br>

### User Stories for Customers
<br>

| **As a customer I would like to** | **So that I can**                             |
| -------------------------------------------------- | --------------------------------------------- |
| Browse products                                    | purchase what I need                          |
| Search products                                    | find something specific                       |
| Filter products                                    | compare the offerings                         |
| Buy a product                                      | get the parts im looking for                  |
| Pay using a card                                   | complete my purchase                          |
| Create a profile                                   | save my information and review past orders    |
| See my shopping cart before paying                 | know the cost and content before the purchase |
| Update my shopping cart                            | make decisions before the purchase            |
| See details about a product                        | make an informed purchasing decision          |
| View my order history                              | be reminded of previous purchases             |
| Receive an email confirmation about my order       | have archived information about it            |
---
<br>


### User Stories for Shop Administrators
<br>

| **As an administrator I would like to**     | **So that I can**                                |
| ------------------------------------------- | ------------------------------------------------ |
| Add/Update/Remove a product                 | keep the store up to date                        |
| Add/Update/Remove a producer                | keep users informed about the latest information |
| Receive orders from customers in my mailbox | fulfill the orders                               |
---
<br>

### User Stories for Customers to Learn
<br>

| **As a returning customer I would like to** | **External links to learn provided**             |
| ------------------------------------------- | ------------------------------------------------ |
| Learn about Blockchain Technology           | Drop down learning on nav-bar                    |
| Read the latest news on cryptocurrency      | News articles provided for users                 |
| Buy and store cryptocurrency safely         | Information is provided                          |
---
<br>

## Design

The home page has a fixed nav-bar header with a search bar, as well as drop-down menus for customers to navigate through products. Account sign-up and login details are also available with shopping bag and shop now button. 

* [Home Page](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/home%20page.png?raw=true) 

## Technologies Used
<br>

- ![Visual Studio Code](https://img.shields.io/static/v1?label=VS%20Code&message=1.42.0&color=007ACC&logo=visual%20studio%20code&logoColor=ffffff)
    - [VS Code](https://code.visualstudio.com/) - Used as my code testing and editing.
- [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
    - [GitHub](https://github.com/) - Used as remote storage of my projects online.
- ![Balsamiq Wireframes](https://img.shields.io/static/v1?label=Balsamiq&message=3.5.17&color=CC0200)
    - [Balsamiq](https://balsamiq.com/) - Used to bring my wireframe sketches to life.
<br>

### Front-End Technologies
<br>

- ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- ![jQuery 3.4.1](https://img.shields.io/static/v1?label=jQuery&message=3.4.1&color=0769AD&logo=jquery&logoColor=ffffff)
    - [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- ![Stripe API](https://img.shields.io/static/v1?label=Stripe&message=API&color=008CDD&logo=stripe&logoColor=ffffff)
    - [Stripe API](https://stripe.com/docs/api?lang=python) - Used to make secured payments on *Feature Tickets*.
- ![Amazon AWS S3](https://img.shields.io/static/v1?label=Amazon%20AWS&message=S3&color=232F3E&logo=amazon%20aws)
    - [Amazon AWS S3](https://aws.amazon.com/) - Used to store *staticfiles* and *media* folders and files.
<br>

### Back-End Technologies
<br>

- ![Python](https://img.shields.io/static/v1?label=Python&message=3.6.7&color=blue&logo=python&logoColor=ffffff)
    - [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.
- ![Django](https://img.shields.io/static/v1?label=Django&message=2.2.16&color=092E20&logo=django)
    - [Django 2.2.16](https://docs.djangoproject.com/en/2.2/) - Used as my Python web framework.
- ![Heroku](https://img.shields.io/static/v1?label=Heroku&message=PaaS&color=430098&logo=heroku)
    - [Heroku](https://www.heroku.com) - Used for *"Platform as a Service"* (PaaS) for app hosting.
- ![PostgreSQL 11.4](https://img.shields.io/static/v1?label=PostgreSQL&message=11.4&color=336791&logo=postgresql)
    - [PostgreSQL 11.4](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.
___
<br>

## Testing
___
<br>
manual testing have gone into building the project.

<br>

### Validators
<br>

**HTML**
- [W3C HTML Validator](https://validator.w3.org)

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test all css code, code come back clean with no errors.

**JavaScript**
- [JShint](https://jshint.com/) was used to check the javascript code two errors did flag up as follows, ('template literal syntax' is only available in ES6 (use 'esversion: 6'). after researching how to resolve the issue a .jshinttrc file was added to the root directory with the following code {"esversion": 6} to override the issue.

- Undefined variables
 `$` (used for jQuery)

**Python**
- [PEP8 Online](http://pep8online.com/)
___
<br>

### Compatibility
___
<br>

Website was tested across 6 major browsers in both desktop and mobile configuration.

- **Chrome**
- **Edge**
- **Firefox**
- **Safari**
- **Opera**
- **Internet Explorer**
<br>
___

<br>

## Development and Deployment
___
<br>

Getting Started:
--- 
* Create a repository in [github](https://docs.github.com/en/get-started/quickstart/create-a-repo) with the desired name of your App or project.

* Once your github repository is created, click the green Gitpod [button.](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/gitpod%20button.png?raw=true) This will automatically start creating your workspace environment.

* [Gitpod](https://www.gitpod.io/) environment is used to write your code for your App then gets pushed to Github.

<br>

### Setting up a Django working environment
---

* [Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction) makes it very easy to set up your own computer so that you can start developing web applications.

    * After you’ve created and activated a virtual environment, enter the command [pip install Django](https://docs.djangoproject.com/en/1.8/topics/install/) at the shell prompt.

    * Creating a project, From the command line, cd into a directory where you’d like to store your code, then run the following command: $ django-admin startproject mysite ⬅ (name of your website/app).

    *  These files will be created in your project folder.

       * The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

       * manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in [django-admin and manage.py](https://docs.djangoproject.com/en/4.1/ref/django-admin/).

       * The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

       * mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the [official Python docs](https://docs.python.org/3/tutorial/modules.html#tut-packages).
       
       * mysite/settings.py: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/4.1/topics/settings/) will tell you all about how settings work.

       * mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/4.1/topics/http/urls/).

       * mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with [ASGI for more details](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/).

       * mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with [WSGI for more details](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/).

        * Let’s verify your Django project works. run the following commands: $ python manage.py runserver You’ve started the Django development server, a lightweight web server written purely in Python.

        Once your web application is finished deploy it to Heroku.

<br>

### Setting up Heroku environment:
---
Make sure you add a procfile to your root directory!

   * The Procfile is always a simple text file that is named [Procfile](https://devcenter.heroku.com/articles/procfile) without a file extension. For example, Procfile.txt is not valid. The Procfile must live in your app’s root directory. It does not function if placed anywhere else.

   * Once you have your [account](https://www.heroku.com/) ready, login with your credentials.

   * Click New on the top right corner and select “Create new app”.

   * Give your app a name (This will be included in the public URL for your application) and click Create app.

   * This step will take you to the dashboard of your app. Open Deploy tab and scroll to the “Deployment method” section.

   * Select GitHub as the method.

   * It will show a “Connect to GitHub” option where we can provide our GitHub repository. If you are doing it for the first time, Heroku will ask permission to access your GitHub account.

   * Here, you can search for your GitHub repository and click connect:

   * If it’s able to find and connect to the GitHub repository, the Deployment section will show up where you can select if you want Automatic Deployment (as soon as the changes are pushed to GitHub, Heroku will pick them up and deploy) or Manual Deployment.

   * Click Enable Automatic Deploys (because it’s less overhead for demo apps :) ). You can also select the GitHub branch if you need to, deploy from the master branch.       



<br>


## Credits
___
<br>

 Thanks and praises has to go to all of the below as I work through a career change, asking for help and guidance along the way is always a good starting point.

 Much like any other skill, learning how to code requires time and persistence. The difficulty will depend on the programming language itself and what kind of software you'd like to make.

  * [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template) for providing the walkthrough guided videos and code.

  * I used [YouTube](https://www.youtube.com/) for guides during my project.

  * [Unsplash](https://unsplash.com/) for unlimited free photo's.

  * [Pexels](https://www.pexels.com/) another great website for free images.

  * [Favicon](https://favicon.io/) for the website favicon.

  * My go to website is always [W3Schools](https://www.w3schools.com/)

  * [Stackoverflow](https://stackoverflow.com/) best answers to your technical question.

  * [Wiki](https://en.wikipedia.org/wiki/Main_Page) Wikipedia is a free online encyclopedia.

  * [Slack](https://slack.com/) for that extra push and always help.

  * [MDN Web Docs](https://developer.mozilla.org/en-US/) best documentation on the web.

___
<br>

Helpful Resources To Continue Learning About Blockchain
---
<br>

- [Ethereum](https://ethereum.org/) is the community-run technology powering the cryptocurrency ether (ETH) and thousands of decentralised applications.

- [Bitcoin](https://bitcoin.org/en/) uses peer-to-peer technology to operate with no central authority or banks.

- [Bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf) Satoshi Nakamoto's original paper is still recommended reading for anyone studying how Bitcoin works.

- [Solidity](https://solidity.readthedocs.io/) is an object-oriented, high-level language for implementing smart contracts. Smart contracts are programs which govern the behaviour of accounts within the Ethereum state.

- [Blockchain explorer](https://www.blockchain.com/explorer) believe that in a decade the financial system of the internet — that is, commerce that happens on the internet — will be the largest financial system in the world. And it will be powered by crypto.

- [Coinbase](https://www.coinbase.com/learn) is a distributed company; all employees operate via remote work and the company lacks a physical headquarters.

- [Truffle Suite](https://www.trufflesuite.com/) A world class development environment, testing framework and asset pipeline for blockchains using the Ethereum Virtual Machine (EVM), aiming to make life as a developer easier.

- [Ganache](https://trufflesuite.com/ganache/) Quickly fire up a personal Ethereum blockchain which you can use to run tests, execute commands, and inspect state while controlling how the chain operates.

* [Binance Academy](https://academy.binance.com/en) Your one-stop guide to all things crypto. Whether you're a rookie trying to understand mining or a veteran looking to develop a trading strategy, we've got you covered.

* [Blockchain.com Exchange APIs](https://www.blockchain.com/api) Explore the REST API documentation for detailed examples of the various functionality offered, such as receiving real-time market data, requesting balance information, and performing trades.

* [CoinMarketCap](https://coinmarketcap.com/) Since its launch in 2013, CoinMarketCap has become one of the most powerful websites in the cryptocurrency space, being one of the most visited sites in the industry and a premier source of cryptocurrency market data.

* [Coinbase](https://www.coinbase.com/) Coinbase is a distributed company; all employees operate via remote work and the company lacks a physical headquarters. It is the largest cryptocurrency exchange in the United States by trading volume.

* [Live Coin Watch](https://www.livecoinwatch.com/) Complete cryptocurrency market coverage with live coin prices, charts and crypto market cap featuring 17399 coins on 463 exchanges.

* [CoinGecko](https://www.coingecko.com/) CoinGecko is the world’s largest independent cryptocurrency data aggregator with over 13,000+ different crypto-assets tracked across more than 500+ exchanges worldwide.

* [Messari](https://messari.io/) Messari brings transparency to the crypto-economy. Messari provides crypto market intelligence products that help professionals navigate crypto/Web3.

* [UseWeb3](https://www.useweb3.xyz/) is a platform for developers to explore and learn about Web3. Whether you're a new dev getting your hands dirty for the first time, or a seasoned developer making the transition into the Web3 space.

* [Best Websites For Programmers](https://github.com/sdmg15/Best-websites-a-programmer-should-visit) you must know to get always informed to do your technologies even better and learn new things. Here is a non-exhaustive list of some sites you should visit.

___