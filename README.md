This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, Anyone visiting the Website should NOT add any real bank or credit card details!.

![responsive design](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/home%20page.png?raw=true)

---

 # [Crypto Wallets](https://crypto-hardware-wallets.herokuapp.com/)


The Website is designed and based on digital freedom, securing the new disruptive class of crypto assets. Crypto requires new rules. New protection. New security practices. But nothing can't be learned. Visit Crypto Wallets website for all your crypto needs. A hardware wallet is a cryptocurrency wallet which stores the user's private keys (critical piece of information used to authorise outgoing transactions on the blockchain network) in a secure hardware device. The main principle behind hardware wallets is to provide full isolation between the private keys and your easy-to-hack computer or smartphone.

<br>

---

## UX
This project is my fifth and final Milestone Project in the Code Institute's Full-stack Development program. I decided to create a website based on my passions!. Blockchain Technology. The E-commerce site has many features for customers and returning customers, from browsing the latest digital wallets, to purchasing various products, also learning about Blockchain and cryptocurrency's.
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
| Receive orders from customers in my mailbox | fulfil the orders                                |
---
<br>

### User Stories for Customers to Learn
<br>

| **As a returning customer I would like to** | **External links to learn provided**             |
| ------------------------------------------- | ------------------------------------------------ |
| Learn about Blockchain Technology           | Drop down learning on nav-bar                    |
| Read the latest news on cryptocurrency      | News articles provided for users                 |
| Buy and store cryptocurrency safely         | Information is provided                          |

### User Stories Errors 

* If a user 

    * [puts in the same email to register, user already exists will show and they will have to sign in.](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/user%20already%20exists%20.png?raw=true) 

    * [user name too familiar will apply, and a different one will have to be added instead.](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/username%20too%20familiar.png?raw=true)

    * [password too common, users will have to add a stronger password.](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/password%20too%20common.png?raw=true)

    * [password too short must contain at least 8 characters, users will be advbised to create a longer password.](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/password%20too%20short.png?raw=true)

    * [if a user adds a incorrect bank card, your card number is invalid will advice users to add a correct card.](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/card%20is%20invalid.png?raw=true)

More products will be added at a later date, latest ( Storage ) devices. 

Features to add will be a Blog page with new information regarding Blockchain Technology.

---

## Data Schema

 * [Dbdiagram.io](https://dbdiagram.io/home) is a free online database diagraming tool for developers and data analysts. It uses a code-based user interface, and you can create up to 10 diagrams for free.
 [screen shot]()

 ## User story boards

 * User stories provide a way to simply and plainly describe user action and intent when interacting with a system (typically a user interface). In considering both the steps a user takes, and their motivations, in a narrative form we aim to empathize with our users while delivering a product or service.

 * here are the user stories I created with Github. 
 * [Story board 1](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/phase%201%20user%20story%20board.png?raw=true) 
 * [Story board 2](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/phase%202%20user%20story%20board.png?raw=true)
---

## Design

The home page has a fixed nav-bar header with a search bar, as well as drop-down menus for customers to navigate through products. Account sign-up and login details are also available with shopping bag and shop now button. 

* [Home Page](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/home%20page.png?raw=true)

* [Search Bar](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/search%20bar.png?raw=true)

* [All Products](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/all%20products.png?raw=true)

* [Wallets](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/wallets.png?raw=true)

* [Learning](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/learn.png?raw=true)

* [Login Register](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/login%20register.png?raw=true)

* [Bag](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/check%20out%20bag.png?raw=true)

* [Order Products](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/order%20product.png?raw=true)

* [Shopping Bag](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/bag.png?raw=true)

* [Card Details](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/card%20details.png?raw=true)

* [Thank You For Your Order](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/thank%20you%20for%20your%20order.png?raw=true)
* [Order Confirmation Number](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/order%20number%20confirmation.png?raw=true)
___

## Stripe 

Payments on the website I used [Stripe](https://stripe.com/gb).

* What does Stripe actually do? <br>
As a payment processor, Stripe allows business owners to accept payments from credit and debit cards and processes those payments. Using Stripe, businesses can also accept payments from mobile wallets and buy now, pay later services.

* [Simulate payments to test your integration.](https://stripe.com/docs/testing) <br>
To confirm that your integration works correctly, simulate transactions without moving any money, using special values in [test mode](https://stripe.com/docs/keys#test-live-modes).

* [Test bank card number](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/test%20bank%20card.png?raw=true) Please DO NOT! use any real bank cards as previously mentioned, use the numbers provided from [Stripe](https://stripe.com/docs/payments/without-card-authentication) for testing payments.

* [Stripe payment success](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/stripe%20payment%201.png?raw=true)

* [Payment method](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/stripe%20payment%202.png?raw=true)

* [Payment processed](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/stripe%20payment%20successful.png?raw=true)
<br>

When testing stripe payments the links and images above should tell you that everything is working as it should be, if for any reasons you are getting any errors have a look at these links. [Help Guides](https://stripe.com/docs)

---

## [Balsamiq Wireframes](https://balsamiq.com/)

The designs you received are called wireframes (sometimes called wires, mockups, or mocks).

A wireframe is a schematic, a blueprint, useful to help you're and your programmers and designers think and communicate about the structure of the software or website your building.

[Home Page](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/crypto%20wallet%20home.png?raw=true)

[Checkout Bag](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/crypto%20wallets%20checkout.png?raw=true)

[Order Complete](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/crypto%20wallet%20order%20complete.png?raw=true)

[Subscribe](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/subcribe%20wireframes.png?raw=true)

---

## [Mailchimp](https://mailchimp.com/en-gb/?currency=GBP)

* Mailchimp was added to the footer of each page, for customers and users to [subscribe](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/mailchimp%20contacts.png?raw=true) to.

    What is mailchimp!
    * marketing automation platform designed and developed for businesses using email to reach out to their target markets. It is an all-in-one tool where you can manage your mailing lists, create custom email templates, and nurture and automate your entire marketing campaigns. Enterprises looking to leverage email marketing need a tool, such as Mailchimp, to run their campaigns like a well-oiled machine.


--- 

## [Facebook Mockup Page](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/facebook%20mockup.png?raw=true) 

* SEO is not limited too websites; it also applies to your Facebook pages. You can consider a facebook page as a web page only and SEO principles can be applied here to maximise reach, attract followers, and advance businesses by increasing organic visibility and ranking.

### [What is a Facebook pixel?](https://en.wikipedia.org/wiki/Conversion_tracking)

* The Facebook pixel is a piece of code that you place on your website. It collects data that helps you track conversions from Facebook ads, optimise ads, build targeted audiences for future ads and remarket to people who have already taken some kind of action on your website.

---

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
    - [Amazon AWS S3](https://aws.amazon.com/) - Used to store *static-files* and *media* folders and files.
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

## Testing

<br>
manual testing have gone into building the project.

<br>

### Validators
<br>

**HTML**
- [W3C HTML Validator](https://validator.w3.org) further testing with html checker needs done as it seems some errors were flagging up Django code {% %}

- Element li not allowed as child of element nav in this context. 

- Mailchimp signup embedded code has also flagged up a few errors.

- A meta element with an http-equiv attribute whose value is X-UA-Compatible. 
  * Either X-UA-Compatible is not "standard" HTML (FSVO "standard" that involves appearing on a publicly editable wiki page referenced by the specification) or the Validator isn't up to date with the current status of that wiki.

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test all css code, code come back clean with no errors.

**JavaScript**
- [JShint](https://jshint.com/) was used to check the javascript code two errors did flag up as follows, ('template literal syntax' is only available in ES6 (use 'esversion: 6'). after researching how to resolve the issue a .jshinttrc file was added to the root directory with the following code {"esversion": 6} to override the issue.

- Undefined variables
 `$` (used for jQuery)

**Python**
- [PEP8 Online](http://pep8online.com/)

In the command line interface the following input was added, (python3 -m flake8) to bring up files with errors. Most errors were ( E501 line too long (81 > 79 characters) at this point in time I didn’t want to adjust my code incase I added more issues.

'django.test.TestCase' imported but unused on various files.

More testing will be done at a leter date, to remove any errors. 
___

**Email Issues** 

* Issue with sending emails was discovered just before submission was due, all step were taking from the video guide tutorials during the build process, Ive contacted various tutors and students to resolve my issue.

From Slack the below article

* FYI: for those dealing with password reset and google blocking django from sending emails:
It seems that Django and Google's "Allow Less Secure Apps" setting don't play together nicely anymore, and it's been like this for a while.
What can you do instead: use an App Password.
How?

1: turn off less secure apps

2: turn on two-factor authentication

3: click on app passwords (this will appear right below where you turned on the two-factor auth)

4: set up your new app password

5: put it in your env/config vars instead of your normal password

**Email sending fixed**

* The reason my Emails weren’t sending on the sign up page is because in Heroku I still had development=true in my config vars, I deleted the config vars and the issue is now resolved.

**[TempMail](https://temp-mail.org/en/) was used for dummy email addresses.**

 * Disposable email - is a free email service that allows to receive email at a temporary address that self-destructed after a certain time elapses. It is also known by names like : tempmail, 10minutemail, 10minmail, throwaway email, fake-mail , fake email generator, burner mail or trash-mail.

___

## [404 Page Not Found Error Page:](https://github.com/Flow-matic/crypto-hardware-wallet/blob/main/media/404%20error%20page.png?raw=true)

  * This error shows when a user types a URL into the browser which does not exist within the app's domain.
---

**Config Vars**

* Whilst working on my project I accidentally pushed my convig vars to github, realised after. I deleted it from Heroku and created a new config vars. I spoke to a Code Institute tutor who guided me on this issue. And recommend I mention it in my readme.md file to say it has been corrected.
___

### Compatibility

<br>

Website was tested across various browsers in both desktop and mobile configuration.

- **Chrome**
- **Safari**
- **Internet Explorer**

- **Apple iphone xr, 12,**
- **Android Pixel 5, Galaxy s20**
___

## Development and Deployment

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
___

### AWS 

Amazon web services was used to store the static files for this project.

Amazon S3 or Amazon Simple Storage Service is a service offered by Amazon Web Services that provides object storage through a web service interface. Amazon S3 uses the same scalable storage infrastructure that Amazon.com uses to run its e-commerce network.

[Step by Step guides for setting up a AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)
___

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

  * [Font Awesome](https://fontawesome.com/) is the Internet's icon library and toolkit, used by millions of designers, developers, and content creators.

___

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