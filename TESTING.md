# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## Code Validation


### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| bag | bag.html | ![screenshot](documentation/validation/html/html-products-bag.png) | pass |
| checkout | checkout.html | ![screenshot](documentation/validation/html/html-checkout.png) | pass |
| checkout | checkout_success.html | ![screenshot](documentation/validation/html/checkout-success.png) | pass |
| contact | contact.html | ![screenshot](documentation/validation/html/contact-html.png) | pass |
| contact | thank_you.html | ![screenshot](documentation/validation/html/thank-you-html.png) | pass |
| home | index.html | ![screenshot](documentation/validation/html/html-home.png) | pass |
| newsletter | newsletter_confirmation.html | ![screenshot](documentation/validation/html/newsletter-confirmation-html.png) | See Bugs for this issue |
| products | edit_product.html | ![screenshot](documentation/validation/html/add-product-html.png) | pass the warning can be ignored as I require a section and no H tags for this page|
| products | product_detail.html | ![screenshot](documentation/validation/html/html-product-details.png) | pass |
| products | products.html | ![screenshot](documentation/validation/html/products-html.png) | pass |
| profiles | profile.html | ![screenshot](documentation/validation/html/profile.html.png) | pass the warning can be ignored as I require a section and no H tags for this page|

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | checkout.css | ![screenshot](documentation/validation/css/checkout-css.png) | pass |
| profiles | profile.css | ![screenshot](documentation/validation/css/profile-css.png) | pass minor warnings|
| static | base.css | ![screenshot](documentation/validation/css/base-css.png) | pass minor warnings |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | stripe_elements.js | ![screenshot](documentation/validation/js/jshint-stripe-elements.png) | pass |
| profiles | countryfield.js | ![screenshot](documentation/validation/js/jshint-countryfield.png) | pass |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/bag/admin.py) | ![screenshot](documentation/pep8/pep8-admin-py.png) | pass |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/bag/contexts.py) | ![screenshot](documentation/pep8/pep8-context-py.png) | |
| bag | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/bag/models.py) | ![screenshot](documentation/pep8/pep8-models-bag-py.png) | |
| bag | bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/pep8/pep8-bag-tools-py.png) | |
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/bag/urls.py) | ![screenshot](documentation/pep8/pep8-bag-urls-py.png) | |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/bag/views.py) | ![screenshot](documentation/pep8/pep8-bag-views-py.png) | |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/admin.py) | ![screenshot](documentation/pep8/pep8-checkout-admin-py.png) | |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/forms.py) | ![screenshot](documentation/pep8/pep8-checkout-forms-py.png) | |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/models.py) | ![screenshot](documentation/pep8/pep8-checkout-models-py.png) | |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/signals.py) | ![screenshot](documentation/pep8/pep8-checkout-signals-py.png) | |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/urls.py) | ![screenshot](documentation/pep8/pep8-checkout-urls-py.png) | |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/views.py) | ![screenshot](documentation/pep8/pep8-checkout-views-py.png) | |
| checkout | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/webhook_handler.py) | ![screenshot](documentation/pep8/pep8-checkout-webhook.png) | |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/webhooks.py) | ![screenshot](documentation/pep8/pep8-checkout-webhook.png) | |
| contact | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/admin.py) | ![screenshot](documentation/pep8/pep8-contact-admin-py.png) | |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/forms.py) | ![screenshot](documentation/pep8/pep8-contact-forms-py.png) | |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/models.py) | ![screenshot](documentation/pep8/pep8-contact-models-py.png) | |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/urls.py) | ![screenshot](documentation/pep8/pep8-contact-urls-py.png) | |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/views.py) | ![screenshot](documentation/pep8/pep8-contact-views-py.png) | |
|  | custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/custom_storages.py) | ![screenshot](documentation/pep8/pep8-custom-storages-py.png) | |
| home | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/home/admin.py) | ![screenshot](documentation/pep8/pep8-home-admin.py.png) | |
| home | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/home/models.py) | ![screenshot](documentation/pep8/pep8-home-models-py.png) | |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/home/urls.py) | ![screenshot](documentation/pep8/pep8-home-urls-py.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/home/views.py) | ![screenshot](documentation/pep8/pep8-home-views-py.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/manage.py) | ![screenshot](documentation/pep8/pep8-main-manage-py.png) | |
| newsletter | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/newsletter/admin.py) | ![screenshot](documentation/pep8/pep8-newsletter-admin-py.png) | |
| newsletter | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/newsletter/forms.py) | ![screenshot](documentation/pep8/pep8-newsletter-forms-py.png) | |
| newsletter | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/newsletter/models.py) | ![screenshot](documentation/pep8/pep8-newsletter-models-py.png) | |
| newsletter | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/newsletter/urls.py) | ![screenshot](documentation/pep8/pep8-newsletter-urls-py.png) | |
| newsletter | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/newsletter/views.py) | ![screenshot](documentation/pep8/pep8-newsletter-views-py.png) | |
| products | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/products/admin.py) | ![screenshot](documentation/pep8/pep8-products-admin-py.png) | |
| products | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/products/forms.py) | ![screenshot](documentation/pep8/pep8-products-forms-py.png) | |
| products | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/products/models.py) | ![screenshot](documentation/pep8/pep8-products-models-py.png) | |
| products | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/products/urls.py) | ![screenshot](documentation/pep8/pep8-products-urls-py.png) | |
| products | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/products/views.py) | ![screenshot](documentation/pep8/pep8-products-views-py.png) | |
| profiles | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/profiles/admin.py) | ![screenshot](documentation/pep8/pep8-profiles-admin-py.png) | |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/profiles/forms.py) | ![screenshot](documentation/pep8/pep8-profiles-forms-py.png) | |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/profiles/models.py) | ![screenshot](documentation/pep8/pep8-profiles-models-py.png) | |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/profiles/urls.py) | ![screenshot](documentation/pep8/pep8-profiles-urls-py.png) | |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/profiles/views.py) | ![screenshot](documentation/pep8/pep8-profiles-views-py.png) | |
| shopaholic | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/shopaholic/settings.py) | ![screenshot](documentation/pep8/pep8-shopaholic-settings-py.png) | |
| shopaholic | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/shopaholic/urls.py) | ![screenshot](documentation/pep8/pep8-shopaholic-urls.png) | |

## Browser Compatibility


Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Opera](https://www.opera.com/download)


I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Products | Contact | Notes |
| --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-compatability/chrome/chrome-home.png) | ![screenshot](documentation/browser-compatability/chrome/chrome-products.png) | ![screenshot](documentation/browser-compatability/chrome/chrome-contact.png) | Works as expected |
| Firefox (Developer Edition) | ![screenshot](documentation/browser-compatability/firefox/firefox-home.png) | ![screenshot](documentation/browser-compatability/firefox/firefox-products.png) | ![screenshot](documentation/browser-compatability/firefox/firefox-contact.png) | Works as expected |
| Opera | ![screenshot](documentation/browser-compatability/opera/opera-home.png) | ![screenshot](documentation/browser-compatability/opera/opera-products.png) | ![screenshot](documentation/browser-compatability/opera/opera-contact.png) | Works as Expected |


## Responsiveness


I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Products | Contact | Thanks | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/home-mob.png) | ![screenshot](documentation/responsiveness/products-mobile.png) | ![screenshot](documentation/responsiveness/mob-contact.png) | ![screenshot](documentation/responsiveness/mob-thanks.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/home-tablet.png) | ![screenshot](documentation/responsiveness/tablet-products.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/tablet-thanks.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/home-desktop-res.png) | ![screenshot](documentation/responsiveness/products-desk.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | ![screenshot](documentation/responsiveness/desktop-thanks.png) | Works as expected |



| Device | Bag | Success | Details | Email Confirmation  | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mobile-bag.png) | ![screenshot](documentation/responsiveness/mobile-success.png) | ![screenshot](documentation/responsiveness/mobile-details.png) | ![screenshot](documentation/responsiveness/mobile-conf.png) | Small issue with header cutting off body in bag|
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet-bag.png) | ![screenshot](documentation/responsiveness/tablet-success.png) | ![screenshot](documentation/responsiveness/tablet-details.png) | ![screenshot](documentation/responsiveness/tablet-conf.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/bag-desk.png) | ![screenshot](documentation/responsiveness/desktop-success.png) | ![screenshot](documentation/responsiveness/desktop-details.png) | ![screenshot](documentation/responsiveness/desktop-conf.png) | Works as expected |



| Device | Checkout | Edit/add | | | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mob-checkout.png) | ![screenshot](documentation/responsiveness/mobile-manage.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/tablet-manage.png) | | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/desktop-checkout.png) |  |  | Works as expected |


## Lighthouse Audit


I've tested my deployed project using the Lighthouse Audit tool to check for any major issues on the major pages in the app that would be in the main user journey. some of the poor lighthouse scores are produced by a poor server load time, depreciated API's, 3rd party cookies etc which I would look to delve into if I had more time on the project.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/light-home-mob.png) | ![screenshot](documentation/lighthouse/light-home-desk.png) | Some warnings about minifying css and javascript witha cache policy required |
| Products | ![screenshot](documentation/lighthouse/light-product-mob.png) | ![screenshot](documentation/lighthouse/light-product-desk.png) | Some minor warnings |
| Contact | ![screenshot](documentation/lighthouse/light-contact-mob.png) | ![screenshot](documentation/lighthouse/light-contact-desk.png) | Some minor warnings |
| Bag | ![screenshot](documentation/lighthouse/light-bag-mob.png) | ![screenshot](documentation/lighthouse/light-bag-desk.png) | Some minor warnings |
| Checkout | ![screenshot](documentation/lighthouse/checkout-success-light-mob.png) | ![screenshot](documentation/lighthouse/checkout-success-light-mob.png) | Some minor warnings |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Subscribe feature redirects user to confirmation page and sends email to user| Tested the feature by doing inputting my email | The feature behaved as expected, and it sent me the email. The same email cannot be inputted again and a message is shown to the user to inform them of this | Test concluded and passed | ![screenshot](documentation/readme_images/features/email-confirmation.png) |
| Contact Us | | | | | |
| | Feature is expected to send the form details to the backend when the user fills the form and clicks/presses the submit button. The user is then redirected to a thank you page | Tested the feature by doing filling in the form. Form cannot be sent if fields not filed in and inputs must conform to max lengths | The feature behaved as expected, and it did sent the message to the backend | Test concluded and passed | ![screenshot](documentation/testing_images/back-form.png) |
| Search | | | | | |
| |Search feature is expected to searchthe products and redirect to products with matching text | Tested the feature by using the search bar for red wine | The feature behaved as expected, and it did show red wine products. If there is no match then the user is redirected to a no search results page | Test concluded and passed | ![screenshot](documentation/testing_images/red-wine-search.png) |


| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on All Products link in navbar | Redirection to products page | Pass | |
| | Click on Price link in navbar | Redirection to products page sorted low to high | Pass | |
| | Click on Rating link in navbar | Redirection to products page sorted high to low | Pass | |
| | Click on Type link in navbar | Redirection to products page sorted to product types | Pass | |
| | Click on All products link in navbar | Redirection to products page all products show | Pass | |
| | Click on lager in navbar | Lager products show | Pass | |
| | Click on bitter in navbar | Bitter products show | Pass | |
| | Click on red link in navbar | red wine products show | Pass | |
| | Click on white link in navbar | white wines show | Pass | |
| | Click on vodka link in navbar | rose wines show | Pass | |
| | Click on whiskey link in navbar | whiskey products show | Pass | |
| | Click on rum link in navbar | rum products show | Pass | |
| | Click on gin link in navbar | gin products show | Pass | |
| | Click on new arrivals link in navbar | new arrivals show | Pass | |
| | Click on deals link in navbar | deas show | Pass | |
| | Click on clearance link in navbar | clearence products show | Pass | |
| | Click on all specials link in navbar | all products show | Fail | |
| | Click on Home contact us | Redirection to contact page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Products | | | | |
| | sort dropdown | sorts all products depending on selection | Pass | |
| | superuser CRUD functionality edit/delete | works as expected deletes or redirects to edit page | Pass | |
| | superuser CRUD functionality edit/delete shows toast | works as expected  | Pass | |
| | number of items displayed | works as expected  | Pass | |
| | superuser can edit all details and image for a product then clicks update | updates and image is changed | Pass | |
| Product Details | | | | |
| | Ratings | Ratings show | Pass | |
| | product details | All details show | Pass | |
| | price | price shows | Pass | |
| | add more products and add to bag| products are added | Pass | |
| | sucess toast shows on add to bag click | free delivery shows/hides based on £ in bag | Pass | |
| | toast link on click | Redirection to checkout | Pass | |
| Register | | | | |
| | Click on sign up button after correctly filling in fields | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| | register toast | toast appears as expected | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page and shows logout toast | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User can edit their details | Pass | |
| | Previous orders should show | past orders should show | Fail | Past orders should show in the users history |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| Shopping Bag | | | | |
| | Bag products | all products selected show in bag | Pass | |
| | Add quantity | works as expected | Pass | |
| | Remove products | works as expected | Pass | |
| | Keep Shopping button on click | works as expected redirects to all products | Pass | |
| Checkout | | | | |
| | Fill in form and stripe payment | proceeds to confirmation page | Pass | |
| | Enter invalid data | tooltips are shown | Pass | |
| | Save details tickbox | does not save data | Fail | Customer details should save but they dont|
| Confirmation page | | | | |
| | Invoice shows all details/data from purchase | Pass | |
| | Toast for confirmation shows| works as expected | Pass | |
| Shopping Bag Icon Price | | | | |
| | Basket totals icon | basket icon updates price accordingly | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| Superuser | | | | |
|| superuser clicks link to product management | redirects to add product page | Pass | |
|| superuser fills out product form and adds image | product is added | Pass | |
|| superuser attempts to incorrectly fill out form | all tooltips display as appropriate & page wont proceed | Pass | |
| Special Offers | | | | |
|| superuser clicks tickbox to make a product clearence/deal/new.  | Text appears on image as expected and product appears when special offers type is selected in navbar. | Pass | |
|| superuser clicks 2-3 tickboxes | 3 special offer text boxes appear on images | Fail | All 3 offers overlap |


## User Story Testing


| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to be able to add/delete alcoholic drinks to my basket, so that I can checkout with the correct basket | ![screenshot](documentation/user-stories/add-delete.png) |
| As a new site user, I would like to search all products, a product type or special offers, so that I can narrow down my choices | ![screenshot](documentation/user-stories/searchproducts.png) |
| As a new site user, I would like to be able to sort my results , so that I can sort by A-Z, Z-A, rating, type etc | ![screenshot](documentation/user-stories/sort-user.png) |
| As a new site user, I would like to see new arrivals, clearence and deals, so that I can make an informed choice on my purchases | ![screenshot](documentation/user-stories/offers.png) |
| As a new site user, I would like to be able to create an account, so that I can login, logout and see my purchases | ![screenshot](documentation/user-stories/register-user.png) |
| As a new site user, I would like to be able to pay by credit or debit card in the app, so that I can quickly make a purchase | ![screenshot](documentation/user-stories/credit-card.png) |
| As a new site user, I would like to be able to see what goes into my basket via a notification so that I can see what I am purchasing | ![screenshot](documentation/user-stories/add-toast.png) |
| As a new site user, I would like to be able to see a confirmation of what I have purchased once I have checked out so I can see what I have purchased | ![screenshot](documentation/user-stories/check-conf.png) |
| As a new site user, I would like to be able to contact the company via a contact form should I have any issues, so I can get help if required | ![screenshot](documentation/user-stories/contact-form-user.png) |
| As a new site user, I would like to be able to sign up to a email newsletter, so that I can keep up to date with news and offers | ![screenshot](documentation/user-stories/sign-up.png) |
| As a new site user, I would like to be able to see a rating for each item, so I get to know how good it is | ![screenshot](documentation/user-stories/rating.png) |
| As a returning site user, I would like to see my past purchases, so that I can make the same purchase | ![screenshot](documentation/user-stories/past.png) |
| As a returning site user, I would like to be able to log in to my account, so that I can make a purchase | ![screenshot](documentation/user-stories/register-user.png) |
| As a returning site user, I would like to see what new offers are available, so that I can consider a purchase | ![screenshot](documentation/user-stories/clearance.png) |
| As a site administrator, I should be able to log in and log out as a superuser, so that I can make admin changes that normal users cannot on the frontend| ![screenshot](documentation/user-stories/prod-management.png) |
| As a site administrator, I should be able to edit/delete products with CRUD functionality on the front end, so that I can adjust prices/details etc etc | ![screenshot](documentation/user-stories/edit-delete-front.png) |
| As a site administrator, I should be able to view all customer orders, so that I can manage order processing and fullfillment | ![screenshot](documentation/user-stories/orders.png) |
| As a site administrator, I should be able to see that payments have been processed with a time and date, so that I can ensure they are delivered | ![screenshot](documentation/user-stories/paid-back.png) |
|As a site administrator, I should be able to manage user accounts and passwords, so that I can remove/add or change accounts or passwords | ![screenshot](documentation/user-stories/accounts.png) |
| As a site administrator, I should be able to see who has filled in a form, so that I can respond accordingly and edit or delete/add customer details | ![screenshot](documentation/user-stories/contact-form-back.png) |
| As a site administrator, I should be able to see who has filled in a form, so that I can respond to them accordingly | ![screenshot](documentation/user-stories/contact-form-back.png) |


## Unfixed Bugs


- When validating the html for the newsletter confirmation I get the error of Error: Element style not allowed as child of element body in this context.. To attempt to fix it I remove the styles from the html just like I did with the same error for the thank you page. I add the styles to main.css and the thank you page finds the css classes and implements them, centering the text in the screen, but the confirmation page doesn't and the styles are not applied. I have put the styles back inline in the html file until I can look into what is causing this issue. 

    ![screenshot](documentation/bugs/html-bug.png)
    ![screenshot](documentation/bugs/confirmation-html.png)
    ![screenshot](documentation/bugs/confirmation-bug.png)
    ![screenshot](documentation/bugs/subscribe-fine.png)

- Attempted fix: I have tried reseting the server and tracing the issue back with the inspect tools. This will require further investigation to get this validation fixed.

- When you fill in the subscribe to newsletter and get redirected to the confirmation page - all is ok. But when you click the logo and navigate back to the homepage an error toast appears. I believe this is due to the app believing that you are attempting to put in the same email address even though it does not show in the subscribe input field when you click on subscribe again.

     ![screenshot](documentation/bugs/bug-toast-subscribe.png)
    
- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/validation/html/add-product-html.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

- When validating code for html an unknown change in the code that I have made means that the special offers nav link broke and it now shows all the products, rather than all the special offeres.

    ![screenshot](documentation/bugs/bug-offers.png)

    - Attempted fix: I have looked through changes in github but I cannot currently identify what code has been changed to address this issue and put it back to how it was previous to the validation. This will require extra time on the project to rescue this feature.



