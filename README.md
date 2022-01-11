# MovieScreenings

<h2>Introduction</h2>
<p>This was my final project in Tero Karvinen's course "Python Web Service from Idea to Production" in Summer 2021.</p>
<p>My idea for the project was a "Movie Screening Service", a platform where users can make announcements of their own movie screening events.</p>
<p>The service can be used with or without account: the user only needs an account if they want to add their own movie screenings</p>
<p>Each post contains the details of the movie screening: 
<li>Title, Director, Release Year, Cast, Length, Synopsis</li>
<li>Screening date, Screening Time, Screening Address</li>
<li>Host's Name, Email and Phone Number</li>
<h2>Example of the Service</h2>
<h5> THE MOVIE IN THE EXAMPLE IS FOR DEMONSTRATION ONLY --> SHIN GODZILLA BELONGS TO TOHO.CO, LTD. </h5>
<br>
<img src="https://github.com/hffriman/MovieScreenings/blob/master/MovieScreenings-image.png">
<h2>Different Pages</h2>
<h3>This service has following pages:</h3>
<p><b>Home</b>: Shows the introduction of this project</p>
<p><b>Now Showing</b>: Shows all the current screenings. If the user wants to add, edit or delete screenings, they must be logged in</p>
<p><b>Add Screening</b>: A function only available for users logged in. A page where the user can add a new movie screening.
<p><b>Log In</b>: A Log-In page for users. If they are logged in, there will be Log-Out button instead of Log-In. The email of the user is also shown.</p>
<p><b>Register</b>: A registration page for new users. The registration fails, if the user's email address already has an account in the service. If the registration is successful, the user will be redirected to Log-In page</p>
<h2>How to Improve</h2>
<p>If I decide to continue evolving this project, I would try to do the following improvements:</p>
<li>I would create a better user authentication: during registration, the user would have to write their password twice, and they would receive verification mail in order to complete the process</li>
<li>I would create more specific rights to the user accounts: they would have access ONLY TO THEIR OWN movie screenings instead of being able to delete and edit other user's posts.</li>
<li>I would create a reservation system: instead of having to contact the host by mail or phone, the user could just reserve their seats on this web service only.</li>

<h2>Licence</h2>
<p>GNU General Public License</p>
