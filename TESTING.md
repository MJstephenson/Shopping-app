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
| checkout | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/checkout/webhooks.py) | ![screenshot](documentation/pep8/pep8-checkout-webhook.png) | |
| contact | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/admin.py) | ![screenshot](documentation/pep8/pep8-contact-admin-py.png) | |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/forms.py) | ![screenshot](documentation/pep8/pep8-contact-forms-py.png) | |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/models.py) | ![screenshot](documentation/pep8/pep8-contact-models-py.png) | |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/urls.py) | ![screenshot](documentation/pep8/pep8-contact-urls-py.png) | |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/contact/views.py) | ![screenshot](documentation/pep8/pep8-contact-views-py.png) | |
|  | custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/custom_storages.py) | ![screenshot](documentation/pep8/pep8-custom-storages-py.png) | |
| home | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MJstephenson/Shopping-app/main/home/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
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

| Device | Home | Products | Contact | Details | Bag | Checkout | Success | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/home-desktop-res.png) | ![screenshot](documentation/responsiveness/products-desk-res.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-etc.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-about.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-etc.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/home-desktop-res.png) | ![screenshot](documentation/responsiveness/products-desk-res.png) | ![screenshot](documentation/responsiveness/contact-desk-res.png) | ![screenshot](documentation/responsiveness/details-desk-res.png) | ![screenshot](documentation/responsiveness/bag-desk-res.png) | ![screenshot](documentation/responsiveness/checkout-desk-res.png) | ![screenshot](documentation/responsiveness/sucess-desk-res.png) |Works as expected |



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

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |


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

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
