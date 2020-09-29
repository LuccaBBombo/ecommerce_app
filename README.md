# EletroHome
This is a ecommerce website that offers a varied category of products from televisions, consoles, pc's and all the accessories and equipment that you need to get started setting up your office or living room entertainment system.

## UX
We designed the website to be very intuitive and easy to use, helping people find what they are looking for in a easy and quick manner. 
Users will be able to browse through all the items in the website, sort them by various categories and have information being quickly displayed for them, such as price, ratings, reviews, everything they need in order to decide which product is the best fit for them.
We aim to make the process of finding your new console or piece of equipment quick and easy instead of it being a long and tiresome task.

### User Stories
* As a user I want to be able to browse through all the items in the website.
* As a user I want to be able to filter results of all the items in the website by categories so that I can find what I'm looking for easily.
* As a user I want to be able to easily create a profile so that I can keep track of my purchases and update my details such as delivery address and card information.
* As a user I want to be able to easily log in and log out of my profile.
* As a user I want to be able to reset my password in case I forget it.
* As a user I want to be able to quickly see information about the product I am interested in, such as price, ratings and reviews.
* As a user I want to be able to choose the quantity of the chosen item I want to purchase.
* As a user I want to easily see the items that are in my cart, as well as the full price of the items I have already selected to purchase.
* As a user I want to be able to purchase a product without having to create a profile on the website.


## Features 
* Users can buy various items of different categories and brands, choosing which one they think will be a better fit for their purposes.
* Users who don't want to create a profile can buy items and checkout as 'Guests'.
* Users can create a profile to store data on all their purchases or set default delivery information for future purchases.
* Users can update profile information such as name, phone number and delivery information for future purchases.
* Users can sort items by various categories and change the order on which items are showed.(Ex: Price Low to High, Ratings High to Low)
* Users can use the search bar to find items that they are interested in.
* Users can check items description and choose item quantity they want to add to cart.
* Users have the ability to view their cart at any time, in any page on the website.
* Users can edit their cart, change items quantity and delete items form the cart.
* Users have the ability to check their cart contents before realizing the purchase, checking items and quantity.

## Future Features
* Users have the ability for storing payment details to quicken site purchases.
* Users will be able to receive a code after making a certain amount of items to get special deals, charge free deliveries and discount percentages on items.

## Technologies Used
* [Python](https://www.python.org/)
    * The project uses Python.
* [JQuery](https://jquery.com/)
    * The project uses JQuery to simplify DOM manipulation.
* [JavaScript](https://www.javascript.com/)
    * Used to make the webpage dynamic and interactive by implementing custom client-side scripts.
* [Bootstrap](https://getbootstrap.com/)
    * The project uses Bootstrap to allow for maximum responsiveness on various screen sizes and quick customization.
* [Font Awesome](https://fontawesome.com/)
    * The project uses Font Awesome to be able to use Font Awesome Icons Library.
* [Django](https://www.djangoproject.com/)
    * The project uses Django to build a webiste with a rapid and clean design.

### Testing
* The HTML and CSS files were tested by using the W3C Mark Validator Service by direct input of the files on the validator.
* The Python file was tested by direct input at the (extendsclass.com) file validator.
* The JavaScript files were tested using JSLint by direct input of the files on the validator.
* To test the responsiveness of the website in phones, tablets, and desktops screens, I was used the Chrome Developer Tools, verifying how the site reacted in different screen sizes and that it would not interfere with UX.
1. Profile page
    1. Click the Profile icon.
    1. Select the register account if you don't have one and verify that you receive an email to confirm you email address.
    1. After that click the link and see if you are taken to the confirm username and login into your account.
    1. If you already have an account, click 'login', enter details and see if you receive a message saying that you have been successfully signed in.
    1. If you are signed in, click the logout link and receivea messagesaying that you have successfully been logged out.
    1. Click the Profile icon, click My Profile and see if you are taken to profile page, where you can update your default delivery details and see orders history.
    1. Try using the Update Delivery Information form by filling it out and pressing the 'Update' button, checking to see if the information has been updated successfully.
2. Products page
    1. Enter a search querie in the searchbar, verifying that there are item that match the search and if they aren't any, that the user is properly informed.
    1. Choose a item category and see if the category name that was chosen and the items that are part of it are correctly displayed.
    1. Select the sort button and choose a sorting method seeing that the items in display are correctly updated.
    1. Click the 'View item' button or item name, verifying that you are taken to the correct item details page.
3. Products Information Page
    1. Choose a quantity of the item and click the 'Add to cart' button, checking to see if the message of confirmation appears showing the item name and quantity that have been added to the cart.
    1. Click the 'Go back to shopping' link to go back to the 'all products' page.
4. Cart page
    1. Click the cart icon.
    1. See if the items and quantity are correctly displayed on the page.
    1. Try and edit a item quantity by clicking the 'Edit' button, verifying that the 'Success' message is displayed, informing that the cart was successfully updated.
    1. Try and delete a item by clicking the 'Delete' button, verifying that the 'Success' message is displayed, informing that the cart was successfully updated.
    1. Click on the 'Procced to Checkout' button, being taken to the checkout view. 
5. Checkout page
    1. Click the 'Procced to checkout' button on the cart page.
    1. Check to see if you are taken to the checkout page, with cart information on the item being displayed and the card details form.
    1. Insert incorrect details on the cart, verifying that an error message appears informing the user.
    1. Try to submit payment without filling the delivery form correctly and get a message informing the user of what went wrong.
    1. Insert correct details on the cart, verifying that an success message appears informing the user on the number of their order and showing the email that was used to send the order confirmaton.
### Admin access only
6. Add item page
    1. Press the product managment link in the profile dropdown and verify that you are taken to the add item page.
    1. Fill the item add form, testing leaving required fields empty to verify the admin is showed a message warning that there are fields missing.
    1. Fill the form correctly, pressing the 'add' item button and verify that you are taken to the items detail page and receive a message confirming that the item was successfully added.
7. Edit item page
    1. Press the 'Edit' link on the 'all products' view or on the product detail view, checking that you are taken to the edit product page and the form is populated with all the information that were already filled.
    1. Fill the item edit form, testing leaving required fields empty to verify the admin is showed a message warning that there are fields missing.
    1. Fill the form correctly, pressing the 'edit' item button and verify that you are taken to the items detail page and receive a message confirming that the item was successfully updated.
8. Delete item 
    1. Go to the 'all products' view, click the 'Delete' button and verifiy that you receivea message saying the item was successfully deleted and are taken to the 'all products' page.
    1. Go to the any product detail view, click the 'Delete' button and verifiy that you receivea message saying the item was successfully deleted and are taken to the 'all products' page.
### Deployment
* To locally run the code, verify that all the items listed inside the "requirements.txt" file have been installed..
* Before running the project, make sure you set all the environmental variables correctly so that you can use all the sites functionalities properly.
* Use the console command 'python3 manage.py makemigrations --dry-run' to see all the migrations that need to be made.
* Use the console command 'python3 manage.py makemigrations' to realize those migrations.
* Use the console command 'python3 manage.py migrate --plan' to see if everything is okay with the created classes.
* Use the console command 'python3 manage.py migrate' to migrate the classes.
* After those steps have been taken, you do not need to install any new inputs to make the project run.
* Finally type the command 'python3 manage.py runserver' to get the website running.
* If you want you can set an alias for the command 'python3 manage.py runserver' to make is easier to run the project.

### Credits
* All the items images and description were taken from CurrysPcWorld website [Currys PC World](https://www.currys.ie/ieen/index.html).
### Acknowledgement
* Special thanks to all the team from Code Institute on helping me on this project, tutors, mentors and also the students on the Slack community.

