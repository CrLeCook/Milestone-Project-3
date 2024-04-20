# Habitual

![Habitual](/documentation/responsive.png)

Habitual was created as my 3rd milestone project for the Code Institute's Level 5 Diploma in Web Application Development.

Link to deployed site: [Habitual](http://crlecook.pythonanywhere.com/)

- - -

## User Experience

### Project Goals

The idea for Habitual was created from a need I have myself. I personally organise my life by my phones calender. Creating events and tasks for everything so I don't forget.

I often think the app isn't very user-friendly, and it can take a few screens to even get something into the calender. This is where my idea was born. An easy to do app.

### User Stories

#### __Target Audience__

The target audience for Habitual is any one, male or female, young or old who have a need to write things down so they don't forget them.

#### __First Time Visitor Goals__

As a first time user of the site I want to be able to:

* Understand what the site is for and how to navigate the site.
* Create a task in seconds.

#### __Returning Visitor Goals__

As a returning registered user of the site I want to be able to:

* Get to where I want to be quickly.
* View, update, or delete a task.

#### __Admin User__

As an administrator for the site I want to be able to:

* Remove any content that could be offensive. (Future Implementation)

- - -

## Design

### Colour Scheme

Habitual uses soft colours around buttons to convey friendliness, but sharp colours and edges to the main writing on the homepage to convey seriousness.

### Typography

Google Fonts was used to import the chosen font for use in the site.

I have used [Kumbh Sans](https://fonts.google.com/specimen/Kumbh+Sans) across my site as the rounded edges convey the friendliness mentioned above but the sharpness of the capital letters conveys the seriousness mentioned above.

### Imagery

Being simple in nature, the website only hosts 1 image. Of a lady using a to do list. This is relevant to the website matter.

## Features

The website is comprised of 12 pages which are extended from a base template.

* Home/landing/index page
* About page
* Add To do page
* View To do's page

### Elements found on each page

* Navbar - The Navbar is displayed on all pages of the website and allows users to navigate the site with ease. The navbar is comprised of a logo, the sites name, links to navigate the site and a search bar. The navbar is mobile-device responsive and collapses into a 'hamburger' when the screen size is small enough.

### Home Page

![Home Page](/documentation/homepage.png)

### App Page/Add To do

![App page/Add To do](/documentation/app.png)

### About Page

![About Page](/documentation/about.png)

### View To do's Page

![View To do's Page](/documentation/viewtodo.png)

- - -

### Deployment

Habitual is deployed on [pythonanywhere](https://www.pythonanywhere.com), which is similar to heroku. I am using the paid account, which allows my website to connect to external websites (required so my app could reach my database)

### Future Implementations

In future implementations I would like to:

* Have user authentication. Currently every users to do's are displayed. This is complex and would involve creating a new user in the database every time someone different signs up.

### Accessibility

I have been mindful during coding to ensure that the website is as accessible friendly as possible. This has been have achieved by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Providing information for screen readers where there are icons used and no text.
* Ensuring that there is a sufficient colour contrast throughout the site.

- - -

## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python

### Database Used

[MongoDB](https://www.mongodb.com/) - Non-relational database used to store the book information.

### Frameworks Used

[Flask](https://pypi.org/project/Flask/) - A micro framework.

[Bootstrap](https://getbootstrap.com/) - version 5.2.0 - CSS Framework.

### Libraries & Packages Used

[PyMongo](https://pypi.org/project/pymongo/) - Python Driver for MongoDB.

### Programs Used

[Pip](https://pypi.org/project/pip/) - Tool for installing python packages.

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine.

[sweetalert](https://cdnjs.com/libraries/sweetalert) - For the alerts that show when creating/updating/deleting tasks.

[Git](https://git-scm.com/) - For version control.

[Github](https://github.com/) - To save and store the files for the website.

[Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

[Bootstrap Icons](https://icons.getbootstrap.com/) - Version 1.8.3 - For the iconography on the website.

[Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.

[Am I Responsive?](http://ami.responsivedesign.is/) - To show the website image on a range of devices.

- - -

## Testing

Testing was ongoing throughout the entire build. During development I made use of Google Chrome Developer Tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I have gone through each page using Google Chrome Developer Tools to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS. I have checked the HTML via direct input and also by inspecting the page source and running this through the validator.

No errors or warning were found during testing.

- - -

### Python Validator

[PythonChecker](https://www.pythonchecker.com/)

![Results of Python Checker](/documentation/pythontest.png)

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website. The mobile scores are somewhat lower than what I would like them to be so this is something that I would prioritise improving in the next implementation.

![Results of Lighthouse in Desktop](/documentation/lighthousedesktop.png)
![Results of Lighthouse in Mobile](/documentation/lighthousemobile.png)

### Full Testing

Full testing was performed on the following devices:

* PC:
  * Windows 11, 2160x1440 resolution
* Mobile Devices:
  * Samsung S23 Ultra.

  ![Mobile view](/documentation/mobile1.jpg)
  ![Mobile view 2](/documentation/mobile2.jpg)

Each device tested the site using the following browsers:

* Google Chrome
* Firefox
* Samsung Browser (mobile only)

### References

* [Checkbox found in Navbar](https://fontawesome.com/icons/square-check?f=classic&s=regular)
* [Home page image "home_page_image.svg" called "To do list"](https://undraw.co/)
* [Font](https://fonts.google.com/specimen/Kumbh+Sans)
