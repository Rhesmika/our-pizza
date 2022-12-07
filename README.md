# Our Pizza

Our Pizza is a local resturant who desired a wesbite where theor customers could request bookings online, and the site manager could access their bookings. Both the customer and site manager needed to be able to:
- Request new bookings
- View all their upcoming pending bookings
- View all their upcoming approved bookings
- Have the ability to edit their bookings
- Have the ability to cancel their bookings 

The Site manager also requested a way to approve pending bookings for customers. 
The website also needed to show new customers what Our Pizza is and what makes it special. 

![am-i-responsive](static/images/readme/amiresponsive-ourpizza.png)

## Design
The design of the wesbite needed to be uncomplicated but bold. This was reflected in the font and colour choices.  The actual design was created in Adobe Illustrator. 

### Mock up 
The website is intended to reflect that feel of the resturant. Friendly, welcoming, fun and fresh.

![lgoo](static/images/readme/Logo%20Deisgn.png)
![social media logo](static/images/readme/Sm%20Logo%20.png)
![favicon](static/images/readme/Favicon%20design.png)
After creating the logo for the website it was clear how the website should be a brighter to compliment the colours and the feel fo the website well. 

![design](static/images/readme/Homepage%20Design.png)
I used Adobe Illustrator to put the mock up together for this website. The layour of the page as intended to be very linier and clear.  The design allowed for a poll at the bottom of the page as well as a booking in form. The design used icons to create interest to different sections.  The tomato and pepper draw the idea to an otherwise boring area to most users. The Colours are intended to be bright but diverse. 

### Design Edits
When putting the design into practice, the poll at the bottom of the home page wasn't something I was able to include in this project. This is definately a future feature now. 

When Implimenting the bottom "book now" section, it seemed unfinished and didn't match the rest of the website. There would be a better way to impliment this feature as a pop out etc. in the future. 

## Features
When the user opens the home page, the slogan of the website will appear as if it is being written for the customer in letter by letter formation. This is a personal touch. Cheeky, personable and fun. 

### Bookings
When the user clicks the book button in the home page, they are directed to a log in page. If they aren't signed up already, there is also an option in the header to register for the website. 
When logged in, the user is shown all of their upcoming bookings which have been approved. 
![approved-bookings](static/images/readme/Upcoming%20approved.png)

If they wish to view their bookings which haven't yet been approved by the website, they have the option to click on the 'view pending bookings' button. 
![pending-bookings](static/images/readme/Pending%20Bookings%20.png)

The user has the ability to edit and cancel their bookings. 
![booking-options](static/images/readme//booking%20Options%20.png)

If the customer edits their booking, this updates their booking to pending meaning that resturant will need to re-approve their booking. This was an important feature to create as it wouldn't be good for a customer to edit their booking from 2 people to 10 people without the resturant being aware. 
![edit-booking](static/images/readme/Editbooking.png)

The customer also has the option cancel their booking which will remove their booking completely. 
![cancel-booking](static/images/readme/cancel%20booking.png)

### Admin Portal
The admin portal can be found in the footer of the website and can only be accessed as the superuser. If the user isnt' currently logged in at all, they will be directed to the log in page. If they are currently logged in as another user, they will be directed to their own booking page.
![admin-portal-link](static/images/readme/adminportal%20link.png)

The admin portal is design to be a place where all upcoming bookings can be views in upcoming order. The table shows all the relevant details for the booking and if it is approved or pending. If the booking is pending, the 'approve' button appears. 
![admin-portal-table](static/images/readme/Admin%20portal%20.png)

If the admin decides to update the booking, the booking remains as its bookings statues. ie. if the booking was already approved, it remains approved. If it was pending, it remains pending.

### Future Features
- Polls to interact with the user on the home page
- Social media feed to feature on the contact page 
- Option for customers to leave reviews / rank their experience. 

## Testing

The website and all links/ features have been tested on both mobile and laptop. On laptop, the browser was Chrome, on movile, the browser was Safari.
Media queries created were suitable for each screen size and didn't negatively affect the ratio of images etc. 

### HTML:
The wesbites pages were run through the W3C Validator. Minor errors were picked up and and corrected simply. Now shows no errors.
![html-validator](static/images/readme/HTML%20validator.png)

### CSS:
The created CSS was run through the Jigsaw CSS Validator. Minor errors were picked up and and corrected simply.Now shows no errors. 
![css-validator](static/images/readme/css%20validator%20.png)


### Javascript:
The Javascript was run through the PJ Hint Validator. 15 warnings appeared all related to irrelevant features.
![js-validator](static/images/readme/JS%20Validator.png)


### Lighthouse
When initially run through the lighthouse report, the images for mobile were too large. Smaller image version were then implimented for smaller screen sizes.  These were amended and scores are now positive.
![lighthouse](static/images/readme/lighthouse.png)

### Manual Testing 
New Account: 
Expected: As a user, I want to register to the website to have access to bookings
Test: Register a new account without a password, without a name, with incorrect matching passwords
Outcome: user si redirected to register page and all options are still available to be filled in

Login:
Expected: As a user i ecxpect to be able to log in to have acess to bookings
Test: log in as user
Outcome: log in was sucessful, directed to the bookings page

Logout :
Expected: As a user i expect to be able to logout from the website
Test: log out from website 
Outcome: direct to a 'are you sure page and once confirmed, redirected to the homepage and can no longer see bookings. 

View bookings: 
Expected: as a logged in user and amin, I expect to see my requested bookings
Test: create bookings as a user, approve some as superuser and review as user. 
Outcome: Bokings are found on correct pages, Approved on one page, pending bookings are on the pending page

Create Bookings:
Expected: As a logged in user and admin, I expect to make create a booking with referece, date, time and party.
Test: all / individual fields left empty. 
Outcome: form does not submit without all fields being completed. 

Edit Booking:
Expected: As a logged in user, I expect to edit all fields of my booking and the booking to revert to pending
Test: incomplete all / individual field left empty
Outcome: form does not submit without all fields being completed.  Completed edit booking is then seen on pending page.

Delete Bookings:
Expected: As a logged in user and admin, I expect to delete a speicific booking
Test: Select the delete button and confirm deletion
Outcome: Booking is no longer seen on user view or on back end 

Edit Booking - Admin:
Expected: As a logged in admin, I expect to edit all fields of my booking and the booking remain at the same booking status
Test: edit both pending and approved bookings
Outcome: Both types of bookings remaing their status

Admin portal Access:
Expected: As the admin, i expect to be the only one who can see the admin portal
Test: request access to admin portal as anothe user and as someone not logged in at all
Outcome: direct to the bookings page if logged in, or the log in page if not logged in. 

Admin Portal View:
Expected: As the admin, I expect to view all upcoming bookings from all users
Test: create bookings from other users
Outcome: bookings appear in the table

Approve Booking button:
Expected: As the admin, I expect to see the approve button if a booking is pending
Test: create a user booking which automates to pending
Outcome: Button appears

Approve Booking:
Expected: As the admin, I expect when i click the approve button, the booking status is updated to approved and the approve button is removed
Test: click approve button 
Outcome: booking is updated as approved and the button disapears

## Deployment
 The site was deployed to Heroku. The steps to deploy are as follows: 

- Create Heroku App
- Link the Github repositary and connect to main
- Add the Postgres
- Add config Vars: CLoudinary, Secret Key & Elephant SQL
- Add these values to the env.py file in Github Repositary
- Update Repositary Settings file 
- Deploy app in Heroku


The live link can be found here - https://our-pizza.herokuapp.com/

# Issues
My major issue came when I was deploying the final app. All the HTMl content carried over along with the Javascript, however the CSS and images weren't visible. 
With help from Tutor assistance it was noted that as the css and images were in the cloudinary api, django didn't transfer them over correctly. After manually runnning collect static, this then created version issues and no images were holding the right URL. 
To resolve this, all images were re-uploaded directly to the cloudinary and the URL for each cloudinary image was then pasted into the css where relevant. 

# Credits

Scroll Tutorial: 
https://www.youtube.com/watch?v=SJVCvnKM_lI&t=396s

Icons: 
Tomato = https://www.flaticon.com/free-icon/tomato_819856?term=tomato&page=1&position=6&page=1&position=6&related_id=819856&origin=search
Pepper = https://www.flaticon.com/free-icon/bell-pepper_883661?term=pepper&page=1&position=49&page=1&position=49&related_id=883661&origin=search

Limit view to superuser:
https://stackoverflow.com/questions/15998140/how-to-limit-a-view-to-superuser-only

Tutor Assistance pointed me in the direction of this page / Website
https://ccbv.co.uk/projects/Django/1.9/django.contrib.auth.mixins/UserPassesTestMixin/#handle_no_permission

Hero Image: 
https://unsplash.com/photos/frTrM7Gdkho

Gallery Images:
Dough = https://unsplash.com/photos/h8cHw0Zv5GI
Oven = https://unsplash.com/photos/e8ULlZbWu0I
Resturant = https://unsplash.com/photos/ogtpG5pCwrE